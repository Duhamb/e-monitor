if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.callback_filters = {
    get_all_filters: function (trigger, country, bearer, base_url){
        const request = new XMLHttpRequest();
        request.open('GET', base_url + '/api/rappi-cube-back/cauth/filters/' + country + '/all', false);
        request.setRequestHeader('authorization', bearer);
        request.send();
        if (request.status==401) {
            window.location.href = "https://cube.rappi.com/login";
        }
        const response = JSON.parse(request.response);
        // TODO: Change this to an array of the keys of the response
        const filter_names = ['vertical', 'city_name', 'microzone', 'store_microzone', 'polygon_size', 'store', 'brand', 'store_type', 'kam_name', 'value_bucket', 'orders_bucket', 'flawless_bucket', 'service_type', 'delivery_type'];
        const all_filters = [];
        var i = 0;
        for (name of filter_names) {
            all_filters.push([]);
            for (const key of response[name]) {
                all_filters[i].push({'label': key, 'value': key})
            }
            i++;
        }
        document.getElementById("sidebar-loader").style.display = "none";
        document.getElementById("sidebar-loader-div").style['z-index'] = 0;
        return all_filters;
    },
    start_loading: function (country, bearer){
        document.getElementById("sidebar-loader").style.display = "block";
        document.getElementById("sidebar-loader-div").style['z-index'] = 1031;
        return ['loading']
    }
}
