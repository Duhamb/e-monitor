if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.callback_data = {
    get_data: function (
        trigger,
        country, 
        vertical, 
        metric, 
        use_rate, 
        category, 
        subcategory, 
        var_x, 
        var_color, 
        time_window_start, 
        time_window_end, 
        day_of_week, 
        value_bucket,
        orders_bucket, 
        flawless_bucket, 
        city_name, 
        microzone, 
        store_microzone, 
        polygon_size, 
        brand, 
        store, 
        store_type, 
        kam_name, 
        service_type, 
        delivery_type,
        bearer,
        base_url
    ){
        const column2name = {
            'order_id':'Order ID',
            'gmv':'GMV',
            'markdown':'Markdown',
            'agg_hour':'Aggregated Hours',
            'calendar_hour':'Hour',
            'calendar_date':'Day',
            'calendar_week':'Week',
            'day_of_week':'Weekday',
            'delivery_type':'Delivery Type',
            'city_name':'City',
            'microzone':'User Microzone',
            'polygon_size':'Polygon Size',
            'cancelled':'Cancelled',
            'cancellation_category':'Cancellation Category',
            'cancellation_subcategory':'Cancellation Subcategory',
            'store':'Store',
            'brand':'Brand',
            'service_type':'Service Type',
            'vertical':'Vertical',
            'store_type':'Store Type',
            'kam_name':'KAM',
            'store_microzone':'Store Microzone',
            'delay_category':'Delay Category',
            'defect_category':'Defect Category',
            'defect_subcategory':'Defect Subcategory',
            'value_bucket':'Value Bucket',
            'flawless_bucket':'Flawless Bucket',
            'orders_bucket':'Orders Bucket',
        }
        const payload = {
            country: (country != null) ? country : 'br',
            vertical: (vertical != null) ? vertical : [],
            metric: (metric != null) ? metric : 'GMV',
            use_rate: (use_rate != null) ? use_rate : 'rate',
            category: (category != null) ? [category] : [],
            subcategory: (subcategory != null) ? [subcategory] : [],
            var_x: (var_x != null) ? var_x : 'calendar_week',
            var_color: (var_color != var_x) ? var_color : null,
            time_window_start: time_window_start.substring(0, 10),
            time_window_end: time_window_end.substring(0, 10),
            day_of_week: (day_of_week != null) ? day_of_week : [],
            value_bucket: (value_bucket != null) ? value_bucket : [],
            orders_bucket: (orders_bucket != null) ? orders_bucket : [],
            flawless_bucket: (flawless_bucket != null) ? flawless_bucket : [],
            city_name: (city_name != null) ? city_name : [],
            microzone: (microzone != null) ? microzone : [],
            store_microzone: (store_microzone != null) ? store_microzone : [],
            polygon_size: (polygon_size != null) ? polygon_size : [],
            brand: (brand != null) ? brand : [],
            store: (store != null) ? store : [],
            store_type: (store_type != null) ? store_type : [],
            kam_name: (kam_name != null) ? kam_name : [],
            service_type: (service_type != null) ? service_type : [],
            delivery_type: (delivery_type != null) ? delivery_type : []
        }
        const request = new XMLHttpRequest();
        request.open('POST', base_url + '/api/rappi-cube-back/cauth/data', false);
        request.setRequestHeader('authorization', bearer);
        request.setRequestHeader('Content-type', 'application/json')
        request.send(JSON.stringify(payload));
        response = JSON.parse(request.response);
        if (request.status==401) {
            window.location.href = "https://cube.rappi.com/login";
        }
        columns = [];
        for (const key of response.data.columns) {
            columns.push({
                name: key,
                id: key,
                type: 'numeric',
            });
        }
        if (payload.var_color != null) {
            columns.unshift({
                name: column2name[var_color],
                id: var_color,
                type: 'numeric',
            })
        }
        return [
            (response.data != null) ? JSON.stringify(response.data) : '[]',
            columns,
            response.table,
            {'symbol': ['R$']},
            base_url + '/api/rappi-cube-back/cauth/download_table?filters=' + encodeURIComponent(JSON.stringify(payload)),
            base_url + '/api/rappi-cube-back/cauth/download?filters=' + encodeURIComponent(JSON.stringify(payload)),
        ]
    },
    start_loading: function (
        country, 
        vertical, 
        metric, 
        use_rate, 
        category, 
        subcategory, 
        var_x, 
        var_color, 
        time_window_start, 
        time_window_end, 
        day_of_week, 
        value_bucket,
        orders_bucket, 
        flawless_bucket, 
        city_name, 
        microzone, 
        store_microzone, 
        polygon_size, 
        brand, 
        store, 
        store_type, 
        kam_name, 
        service_type, 
        delivery_type,
        bearer
    ){
        //enable loading
        document.getElementById("chart-loader").style.display = "block";
        document.getElementById("chart-loader-div").style['z-index'] = 1031;
        return ['loading']
    }
}