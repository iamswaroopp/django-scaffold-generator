import logging
import pathlib
from pathlib import Path
import random
import shutil
import string

LOGGER = logging.getLogger(__name__)


class FileTransaction:

    @staticmethod
    def _generate_transaction_id(len=4):
        return ''.join(random.choice(string.ascii_letters) for i in range(len))

    def __init__(self):
        self._reset()
        self._transaction_status = False
        self._transaction_id = self._generate_transaction_id()

    def __enter__(self):
        self.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not isinstance(exc_val, Exception):
            self.commit()
        self.close()

    def __del__(self):
        self.rollback()

    def _reset(self):
        self.original_file_path_to_transaction_file_path = {}

    def begin(self):
        if self._transaction_status:
            self.rollback()  # Rollback if already in a transaction
        self._transaction_status = True
        self._transaction_id = self._generate_transaction_id()

    def close(self):
        self._transaction_status = False
        self.rollback()

    def commit(self):
        if not all(Path(path).exists() for path in self.original_file_path_to_transaction_file_path.values()):
            LOGGER.error('Transaction files missing. Rolling back Transaction')
            self.rollback()
        for original_file_path, transaction_file_path in self.original_file_path_to_transaction_file_path.items():
            shutil.move(transaction_file_path, original_file_path)
        self._reset()

    def rollback(self):
        for path in self.original_file_path_to_transaction_file_path.values():
            try:
                Path(path).unlink()
            except FileNotFoundError:
                pass
        self._reset()

    def open(self, path, *args, default_file_content='', **kwargs):
        if not self._transaction_status:
            raise ValueError('Transaction not initialized.')
        original_path = pathlib.Path(path)
        if original_path not in self.original_file_path_to_transaction_file_path:
            transaction_file_path = pathlib.Path(str(original_path.absolute()) + '.' + self._transaction_id)
            try:
                shutil.copy2(original_path, transaction_file_path)
            except FileNotFoundError:
                with open(transaction_file_path, 'w') as f:
                    f.write(default_file_content)
            self.original_file_path_to_transaction_file_path[original_path] = transaction_file_path
        return self.original_file_path_to_transaction_file_path[original_path].open(*args, **kwargs)
