(function () {
    'use strict';

    const dom = `
    <'row'<'col-lg-6 text-left'B><'col-lg-6 text-right'f>> 
    <'row'<'col'tr>> 
    <'row'<'col-lg-5 text-left'i><'col-lg-7 text-right'p>>
    `
    $(document).ready(function () {
        $('.datatable').each(function (index, value) {
            $(this).dataTable({
                dom: dom,
                responsive: true,
                deferRender: true,
                colReorder: true,
                fixedColumns: true,
                stateSave: true,
                pageLength: 10,
                buttons: [
                    'copy',
                    {
                        extend: 'csv',
                        text: 'Export',

                    }, 'pageLength', {
                        extend: 'colvis',
                        columns: ':not(.noVis)',
                        text: 'Columns',
                    }
                ]
            });

        });

    });
})();
