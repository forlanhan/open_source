$(function () {
    ////文库采集趋势图
    var char1 =  $('#wenku-chart-display').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: ''
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            //categories: list_to_string(wenku_x)
            categories: wenku_x
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        tooltip: {
            enabled: true,
            formatter: function() {
                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'°C';
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: true
            }
        },
        series: [{
            name: '文库采集趋势图',
            data: wenku_y
        }],
        credits: {
            enabled: false
        }
    });
//////////////////////////////////////////////////////////
    var char2 =  $('#scholar-chart-display').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: ''
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: scholar_x
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        tooltip: {
            enabled: true,
            formatter: function() {
                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'°C';
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: true
            }
        },
        series: [{
            name: '学术采集趋势图',
            data: scholar_y
        }],
        credits: {
            enabled: false
        }
    });
//////////////////////////////////////////////////////////
    var char3 =  $('#baike-chart-display').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: ''
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: ['04-03', '04-04', '04-05', '04-06']
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        tooltip: {
            enabled: true,
            formatter: function() {
                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'°C';
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: true
            }
        },
        series: [{
            name: '百科采集趋势图',
            data: [3.9, 4.2, 5.7, 8.5]
        }],
        credits: {
            enabled: false
        }
    });
//////////////////////////////////////////////////////////
    var char4 =  $('#homepage-chart-display').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: ''
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: ['04-03', '04-04', '04-05', '04-06']
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        tooltip: {
            enabled: true,
            formatter: function() {
                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'°C';
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: true
            }
        },
        series: [{
            name: '主页采集趋势图',
            data: [3.9, 4.2, 5.7, 8.5]
        }],
        credits: {
            enabled: false
        }
    });
//////////////////////////////////////////////////////////
    var char5 =  $('#anwang-chart-display').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: ''
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: ['04-03', '04-04', '04-05', '04-06']
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        tooltip: {
            enabled: true,
            formatter: function() {
                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'°C';
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: true
            }
        },
        series: [{
            name: '暗网采集趋势图',
            data: [3.9, 4.2, 5.7, 8.5]
        }],
        credits: {
            enabled: false
        }
    });
//////////////////////////////////////////////////////////
});

