(function () {
    'use strict';
    $(document).ready(function () {

        function hideIfAlreadyOnModal(button) {
            const currentModal = button.closest('.modal');
            if (currentModal) {
                currentModal.modal('hide');
            }
        }

        $('#commonModal').on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget); // Button that triggered the modal
            var title = button.data('target-title'); // Extract info from data-* attributes
            var url = button.data('target-url');
            hideIfAlreadyOnModal(button);
            // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
            // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
            $(this).find('.modal-title').text(title);
            $(this).find('.modal-body-content').load(url);
        }).on('shown.bs.modal', function (event){
            $(this).find('.modal-body-content').removeClass('d-none');
            $(this).find('.modal-body-loading').addClass('d-none');
        }).on('hidden.bs.modal', function (event){
            $(this).find('.modal-body-loading').removeClass('d-none');
            $(this).find('.modal-body-content').addClass('d-none');
             $(this).find('.modal-body-content').empty();
        });

    });
})();



