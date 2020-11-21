if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.callback_categories = {
    get_categories: function (metric, bearer, country, base_url){
        const options = [];
        if (['Cancellations', 'Defects', 'Delays'].includes(metric)) {
            const request = new XMLHttpRequest();
            request.open('GET', base_url + '/api/rappi-cube-back/cauth/filters/' + country + '/' + metric.toLowerCase().slice(0, -1) + '_category', false);
            request.setRequestHeader('authorization', bearer);
            request.send();
            if (request.status==401) {
                window.location.href = "https://cube.rappi.com/login";
            }
            for (const key of JSON.parse(request.response).filters) {
                options.push(
                    {
                        'label': key.split('_').join(' ').replace(/\w\S*/g,function(txt){return (txt.length<=3) ? txt.toUpperCase() : txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();}),
                        'value': key
                    }
                )
             }
        };
        var radio_options = [];
        var radio_value = '';
        if (['GMV', 'AOV', 'Orders', 'Sales', 'Tickets', 'E2E Time', 'Stockouts', '', null].includes(metric)) {
            radio_options = [
                {'label':'Rate (%)', 'value': 'rate', 'disabled': true},
                {'label':'Contribution (p.p.)', 'value':'contribution', 'disabled': true},
                {'label':'Contribution (%)', 'value':'contribution_100', 'disabled': false},
                {'label':'Absolute', 'value': 'absolute', 'disabled': false}
            ];
            radio_value = 'absolute';
        } else if (['Markdown %'].includes(metric)) {
            radio_options = [
                {'label':'Rate (%)', 'value': 'rate', 'disabled': false},
                {'label':'Contribution (p.p.)', 'value':'contribution', 'disabled': true},
                {'label':'Contribution (%)', 'value':'contribution_100', 'disabled': false},
                {'label':'Absolute', 'value': 'absolute', 'disabled': true}
            ];
            radio_value = 'rate';
        } else {
            radio_options = [
                {'label':'Rate (%)', 'value': 'rate', 'disabled': false},
                {'label':'Contribution (p.p.)', 'value':'contribution', 'disabled': false},
                {'label':'Contribution (%)', 'value':'contribution_100', 'disabled': false},
                {'label':'Absolute', 'value': 'absolute', 'disabled': false}
            ];
            radio_value = 'rate';            
        }
        return [
            radio_options,
            radio_value,
            (options.length==0) ? {'display': 'none'} : {'display': 'flex'},
            options,
            null
        ]
    },
    get_subcategories: function (category, bearer, metric, country, base_url){
        const options = []
        if (['Cancellations','Defects'].includes(metric) && category != null) {
            const request = new XMLHttpRequest();
            request.open('GET', base_url + '/api/rappi-cube-back/cauth/' + metric.toLowerCase().slice(0, -1) + '/' + country + '/' + category, false);
            request.setRequestHeader('authorization', bearer);
            request.send();
            if (request.status==401) {
                window.location.href = "https://cube.rappi.com/login";
            }
            console.log(request.response);
            for (const key of JSON.parse(request.response).filters) {
                options.push(
                    {
                        'label': key.split('_').join(' ').replace(/\w\S*/g,function(txt){return (txt.length<=3) ? txt.toUpperCase() : txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();}),
                        'value': key
                    }
                )
            }
        }
        // console.log(options);
        return [
            (options.length==0) ? {'display': 'none'} : {'display': 'flex'},
            options,
            null
        ]
    },
}