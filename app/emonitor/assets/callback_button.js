if (!window.dash_clientside) { window.dash_clientside = {}; }
window.dash_clientside.callback_button = {
    download_table: function(button_clicks, url, bearer) {
        if (button_clicks > 0) {
            const request = new XMLHttpRequest();
            request.open('GET', url, false);
            request.setRequestHeader('authorization', bearer);
            request.send();

            console.log(request);

            var hiddenElement = document.createElement('a');
            hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(request.response);
            hiddenElement.target = '_blank';
            hiddenElement.download = 'table_data.csv';
            hiddenElement.click();            
        }
        return [
            ''
        ]
    },
}