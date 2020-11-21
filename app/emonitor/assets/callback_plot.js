if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.callback_plot = {
    create_plot: function (
        data_cache,
        chart_type,
        country,
        metric,
        category,
        subcategory,
        var_x,
        var_color,
        use_rate
    ) {
        // converters
        const column2name = {
            'order_id':'Order ID',
            'gmv':'GMV',
            'markdown':'Markdown',
            'agg_hour':'Aggregated Hour',
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
        // create local functions
        function select_template(metric, use_rate, country) {
            const currency_symbol = {
                'ar':'$',
                'br':'R$',
                'cl':'$',
                'co':'$',
                'mx':'$',
                'pe':'S/.',
                'uy':'$U',
                'ec':'$',
                'cr':'₡'
            };
            if (['rate', 'contribution_100'].includes(use_rate) || ['Markdown %'].includes(metric)) {
                return '%{y:,.2%}'
            } else if (['contribution'].includes(use_rate)) {
                return '%{y:,.2f}p.p.'
            } else if (['GMV', 'AOV'].includes(metric)) {
                // return currency_symbol[country] + '%{y:,.3s}' // change currency
                return 'US$' + '%{y:,.3s}' // change currency
            } else {
                return '%{y:,.3s}'
            }
        };
        function generate_title(metric, category, subcategory, var_x, var_color, use_rate) {
            // const has_color = var_color != null && var_color != var_x;
            const rate2title = {
                'rate': 'Rate (%)',
                'absolute': 'Absolute',
                'contribution_100': 'Contribution (%)',
                'contribution': 'Contribution (p.p.)'
            }
            var category_title = '';
            var subcategory_title = '';
            var var_color_title = '';
            if (subcategory != null) {
                subcategory_title = [', ', subcategory.split('_').join(' ').replace(/\w\S*/g,function(txt){return (txt.length<=3) ? txt.toUpperCase() : txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();})].join('');
            }
            if (category != null) {
                category_title = [' (', category.split('_').join(' ').replace(/\w\S*/g,function(txt){return (txt.length<=3) ? txt.toUpperCase() : txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();}), subcategory_title, ')'].join('');
            }
            if (var_color != null) {
                var_color_title = [' & ', var_color].join('');
            }
            return [
                '<b>',
                metric,
                category_title,
                ' x ',
                var_x,
                var_color_title,
                ' - ',
                rate2title[use_rate],
                // ')',
                '</b>'
            ].join('')
        };
        function title_case(category, var_color) {
            return (String(var_color).includes('ategory')) ? // if the group is a category, it should be displayed in title case
                    category.split('_').join(' ').replace(/\w\S*/g,function(txt){return (txt.length<=3) ? txt.toUpperCase() : txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();}) : 
                    category
        };
        const cache = JSON.parse(data_cache);
        const Figure = {'data': [], 'layout': {}};
        const columns = [];
        // truncate x axis labels
        for (obj of cache.columns) {
            columns.push(obj.substring(0, 25));
        }
        // define text template format.
        const texttemplate = select_template(metric, use_rate, country);
        var i = 0; // since we are iterating over two objects at once, we need a iterator. And theres no better name for iterators!
        // add data to chart
        for (obj of cache.index) {
            const label = title_case(obj, var_color);
            Figure.data.push({
                'type': (['group', 'stack'].includes(chart_type)) ? 'bar' : 'scatter', // chart type
                'x': columns, // x axis
                'y': (use_rate == 'contribution') ? cache.data[i].map(function(x) { return x * 100; }) : cache.data[i], // y axis
                'name': label.substring(0, 25), // colors name (truncated for a less squishy experience)
                'texttemplate': texttemplate, // text template format
                'textposition': chart_type=='stack' ? 'inside' : 'outside',
                'hoverinfo': 'text',
                'hovertemplate': [
                        (var_color != null) ? label : '',
                        (var_color != null) ? '<br>' : '',
                        column2name[var_x],
                        ': %{x}<br>',
                        metric,
                        ': ',
                        texttemplate,
                        '<extra></extra>'
                    ].join(''),
                'cliponaxis': false
            });
            i++;
        }
        // prettify chart :)
        Figure.layout['title'] = {
            'text': generate_title(metric, category, subcategory, column2name[var_x], column2name[var_color], use_rate),
            'x': .5,
            'y': .95,
            'xanchor': 'center',
            'yanchor': 'top'
        };
        Figure.layout['titlefont'] = {
            'size': 24
        };
        Figure.layout['xaxis'] = {
            'title': column2name[var_x],
            'tickvals': (chart_type == 'lines' || columns.length < 10) ? null : columns,
            'type': 'category',
            'automargin': true,
        };
        Figure.layout['yaxis'] = {
            'title': metric,
            'tickformat': (['rate', 'contribution_100'].includes(use_rate) || ['Markdown %'].includes(metric)) ? '.1%' : (['contribution'].includes(use_rate) ? '.1f' : ',d'),
            'automargin': true
        };
        Figure.layout['uniformtext'] = {
            'mode': 'hide',
            'minsize': 8
        };
        Figure.layout['template'] = 'plotly_white';
        if (['stack'].includes(chart_type)) {Figure.layout['barmode'] = 'stack'} // change grouped bars to stacked bars, if needed
        // Figure.layout['hovertemplate'] = var_x + ': %{x}<br>' + metric + ': ' + texttemplate;
        Figure.layout['hovermode'] = 'closest'; // set default hover mode to data under the mouse, not the whole X bin
        // disable loading
        document.getElementById("chart-loader").style.display = "none";
        document.getElementById("chart-loader-div").style['z-index'] = -1;
        return [
            Figure
        ]
    }
}
