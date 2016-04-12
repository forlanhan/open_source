$(function () {
    var wenku = $('#wenku').highcharts({
        title: {
            text: '',
            x: -20 //center
        },
        subtitle: {
            text: '',
            x: -20
        },
        xAxis: {
            categories: wenkucaiji_date_list
        },
        yAxis: {
            title: {
                text: ''
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: '个'
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            borderWidth: 0
        },
        series: [{
            name: '文库数据采集',
            data: wenkucaiji_data_list
        }, {
            name: '保密检查告警',
            data: secret_check_alert_data
        }, {
            name: '已保密检查',
            data: secret_check_data
        },{
            name: '已隐写检查',
            data: yx_check_data
        },{
            name: '隐写检查告警',
            data: yx_check_alert_data
        }

        ],
         credits: {
            enabled: false
        }
    });
    /////////////////
     var schoolar =  $('#schoolar').highcharts({
        title: {
            text: '',
            x: -20 //center
        },
        subtitle: {
            text: '',
            x: -20
        },
        xAxis: {
            categories: wanfang_date
        },
        yAxis: {
            title: {
                text: ''
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: '个'
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: true
            }
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            borderWidth: 0
        },
        series: [{
            name: '万方数据采集',
            data: wanfang_data
        }

        ],
         credits: {
            enabled: false
        }
    });
});
