if (!window.dash_clientside) { window.dash_clientside = {}; }
window.dash_clientside.callback_navigation = {
    clear_filters: function(button_clicks) {
        return [
            'GMV', // metric
            null, // verticals
            null, // weekdays
            null, // value_buckets
            null, // orders_buckets
            null, // flawless_buckets
            null, // service_types
            null, // delivery_types
        ]
    },
    reset_datepicker: function(button_clicks) {
        var ending = new Date();
        var monday_offset = (ending.getDay() + 6) % 7; // Mon=0, Tue=1,..., Sun=6
        // ending.setDate(ending.getDate() - monday_offset);
        var beginning = new Date(ending);
        beginning.setDate(beginning.getDate() - 28);
        var minimum = new Date(ending);
        minimum.setDate(minimum.getDate() - 60);
        return [
            beginning.toISOString().substring(0, 10), // start date
            ending.toISOString().substring(0, 10), // end_date
            minimum.toISOString().substring(0, 10), // min_date_allowed
            ending.toISOString().substring(0, 10), // max_date_allowed
        ]
    },
    clear_geography_store_filters: function(button_clicks, country) {
        return [
            null, // cities
            null, // microzones
            null, // store_microzones
            null, // polygon_sizes
            null, // brands
            null, // stores
            null, // store_types
            null, // kams
        ]
    },
    update_x_color_options: function(metric) {
        const options = [
            { 'label':'Aggregated Hours',  'value':'agg_hour' },
            { 'label': 'Hours',            'value': 'calendar_hour' },
            { 'label': 'Days',             'value': 'calendar_date' },
            { 'label': 'Weeks',            'value': 'calendar_week' },
            { 'label': 'Weekdays',         'value': 'day_of_week' },
            { 'label': 'Verticals',        'value': 'vertical' },
            { 'label': 'Value Buckets',    'value': 'value_bucket' },
            { 'label': 'Orders Buckets',   'value': 'orders_bucket' },
            { 'label': 'Flawless Buckets', 'value': 'flawless_bucket' },
            { 'label': 'Cities',           'value': 'city_name' },
            { 'label': 'User Microzones',  'value': 'microzone' },
            { 'label': 'Store Microzones', 'value': 'store_microzone' },
            { 'label': 'Polygon Sizes',    'value': 'polygon_size' },
            { 'label': 'Brands',           'value': 'brand' },
            { 'label': 'Stores',           'value': 'store' },
            { 'label': 'Store Types',      'value': 'store_type' },
            { 'label': 'KAMs',             'value': 'kam_name' },
            { 'label': 'Service Types',    'value': 'service_type' },
            { 'label': 'Delivery Types',   'value': 'delivery_type' }
        ];
        if (metric == 'Cancellations') {
            options.push({ 'label': 'Cancellation Categories',    'value': 'cancellation_category' });
            options.push({ 'label': 'Cancellation Subcategories', 'value': 'cancellation_subcategory' });
        }
        else if (metric == 'Defects') {
            options.push({ 'label': 'Defect Categories',    'value': 'defect_category' });
            options.push({ 'label': 'Defect Subcategories', 'value': 'defect_subcategory' });
        }
        else if (metric == 'Delays') {
            options.push({ 'label': 'Delay Categories', 'value': 'delay_category' });
        }
        // else {
        //     options.push({ 'label': 'Cancellation Categories',    'value': 'cancellation_category' });
        //     options.push({ 'label': 'Cancellation Subcategories', 'value': 'cancellation_subcategory' });
        //     options.push({ 'label': 'Defect Categories',          'value': 'defect_category' });
        //     options.push({ 'label': 'Defect Subcategories',       'value': 'defect_subcategory' });
        //     options.push({ 'label': 'Delay Categories',           'value': 'delay_category' });
        // }
        return [
            options,
            'calendar_week',
            options,
            null
        ]
    }
}