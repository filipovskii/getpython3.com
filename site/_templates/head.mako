<!-- use the less files directly while developing styles -->

<!--
<link rel="stylesheet/less" type="less" href="media/less/base.less" media="screen, projection" />
<script type="text/javascript" src="media/js/less.min.js"></script>
-->

<!-- Once the stylesheets are compiled, use the resulting css file instead! -->
<link rel="stylesheet" type="text/css" href="media/css/base.css" media="screen, projection" />
<link rel="stylesheet" type="text/css" href="media/css/codemirror.css" media="screen, projection" />
<link rel="stylesheet" type="text/css" href="media/css/default.css" media="screen, projection" />

<script type="text/javascript" src="media/js/jquery-1.7.1.min.js"></script>
<script type="text/javascript" src="media/js/bootstrap-scrollspy.js"></script>
<script type="text/javascript" src="media/js/codemirror.js"></script>
<script type="text/javascript" src="media/js/python.js"></script>

<!-- google analytics right up in this piece son. -->
<script type="text/javascript">

    (function($){
        $('#topbar').scrollSpy();
    })(jQuery);

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-25994146-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

    
  (function($) {
      $(document).ready(function () {
          var viewer = CodeMirror($("div#code-viewer")[0], {
            readOnly: true
          });
          var editor = CodeMirror($("div#code-editor")[0], {
            value: "print 1",
            mode: "python",
            onChange: function (e, props) {
                console.log(e.getValue())
                $.ajax("http://localhost:8080/convert", {
                    dataType: "jsonp",
                    data: {code: e.getValue()},
                    success: function (result) {
                        if (result.error !== undefined) {
                            viewer.setValue("# " + result.error);
                        } else {
                            viewer.setValue(result['py3']);
                        }
                    }
                });
            }
          });
          
          viewer.setValue("print(1)")
        });

    
  })(jQuery)
</script>
