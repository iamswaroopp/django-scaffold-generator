#!/usr/bin/env bash

if [ -z "$2" ]; then
  exec_dir=$(dirname "$0")
else
  exec_dir=$2
fi

formatter() {
  echo "Running formatter in Directory $exec_dir"

  # Autoflake
  autoflake --expand-star-imports --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables --recursive --in-place $exec_dir

  #Isort
  isort --atomic --force-single-line-imports --force-sort-within-sections --order-by-type --apply --recursive --quiet --jobs 4 --line-width 119 $exec_dir

  #Yapf
  yapf --parallel --recursive --in-place $exec_dir --style ./.style.yapf
}

clean() {
  find $exec_dir | grep -E "(__pycache__|\\.pyc|\\.pyo$)" | xargs rm -rf
}

check_for_warnings() {
  pylint --rcfile=$exec_dir/.pylintrc --output-format=colorized crawlers crawlersmods
}

$1
