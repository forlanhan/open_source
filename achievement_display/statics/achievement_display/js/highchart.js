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
            categories: date_no_hour
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
             formatter: function() {
                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'个';
            }
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            borderWidth: 0
        },
        //plotOptions: {
        //    line: {
        //        dataLabels: {
        //            enabled: true
        //        },
        //        enableMouseTracking: false
        //    }
        //},
        credits:{
          enabled:false
        },
        series: [{
            name: '文库采集数据',
            data: wenku_caiji_data
        }, {
            name: '保密检查告警',
            data: secret_check_alert
        }, {
            name: '已保密检查',
            data: secret_check
        }, {
            name: '隐写检查告警',
            data: yx_check_alert
        }, {
            name: '已隐写检查',
            data: yx_check
        }]
    });
    //////////
      var schoolar = $('#schoolar').highcharts({
        title: {
            text: '',
            x: -20 //center
        },
        subtitle: {
            text: '',
            x: -20
        },
        xAxis: {
            categories: date_no_hour_schoolar
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
             formatter: function() {
                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'个';
            }
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            borderWidth: 0
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: true
            }
        },
        credits:{
          enabled:false
        },
        series: [{
            name: '学术采集数据',
            data: wanfang
        }]
    });
});
