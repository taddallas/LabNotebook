---
layout: page
title: Github Activity
---


<!-- <iframe allowtransparency="true" frameborder="2" scrolling="no" seamless="seamless" src="https://colmdoyle.github.io/gh-activity/gh-activity.html?user=taddallas&type=user" width="500" height="700"></iframe>-->

<script type="text/javascript">

function feedwind_show_widget_iframe(params, html) {
    params['rssmikle_frame_width'] = params['rssmikle_frame_width'] ? params['rssmikle_frame_width'] : 180;
    params['rssmikle_frame_height'] = params['rssmikle_frame_height'] ? params['rssmikle_frame_height'] : 500;

    var iframe_width = params['rssmikle_frame_width'];
    var iframe_height = params['rssmikle_frame_height'];

    if (params['rssmikle_border'] != 'off' && !params['rssmikle_css_url']) {
        iframe_width = iframe_width.match(/^\d+%$/) ? iframe_width : parseInt(params['rssmikle_frame_width']) + 2;
        iframe_height = iframe_height.match(/^\d+%$/) ? iframe_height : parseInt(params['rssmikle_frame_height']) + 2;
    }

    if (params['responsive'] == 'on') {
        iframe_width = '100%';
    }

    var scroll_flag = params['rssmikle_item_description_tag'] == 'on_scrollbar' ? 'auto' : 'no';
    scroll_flag = params['autoscroll'] == 'on' ? 'no' : scroll_flag;

    var iframe_height_attr = ' height="' + iframe_height + '" ';
    var iframe_id_attr = '';
    if ('frame_height_by_article' in params && parseInt(params['frame_height_by_article']) != 'NaN' && parseInt(params['frame_height_by_article']) > 0 ) {
      var date = new Date();
      var iframe_id = 'feedwind_' + Math.floor(Math.random()*1000) + date.getTime();
      params['iframe_id'] = iframe_id;
      iframe_id_attr = ' id="' + iframe_id + '" ';
      iframe_height_attr = '';

      function receiveSize(e) {
        if (e.origin === "http://feed.mikle.com" || e.origin === "https://feed.mikle.com") {
          var datas = e.data.split('|');
          if (document.getElementById(datas[0])) {
            document.getElementById(datas[0]).style.height = datas[1];
          }
        }
      }
      if (window.addEventListener) {
        window.addEventListener("message", receiveSize, false);
      } else if (window.attachEvent) {
        window.attachEvent("onmessage", receiveSize, false);
      }
    }

    var url = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'feed.mikle.com/widget/?';
    for (var key in params) {
        if (params[key]) {
            url += key + '=' + encodeURIComponent(params[key]) + '&';
        }
    }

    var iframe = '<iframe ' + iframe_id_attr + iframe_height_attr + ' width="' + iframe_width + '" src="' + url + '" scrolling="' + scroll_flag
        + '" name="rssmikle_frame" marginwidth="0" marginheight="0" vspace="0" hspace="0" frameborder="0"></iframe>';

    if (html) {
        return iframe;
    } else {
        document.write(iframe);
        if (('iframe_id' in params) && (document.getElementById(params['iframe_id']))) {
            document.getElementById(params['iframe_id']).contentWindow.location.href = url;
        }
    }
}

(function(){
    var a = window;
    if (a.rssmikle_url && typeof(a.rssmikle_url) == 'string') {
        old_snippet();
    }
    
    function undef_to_nullstr(v) {
        return (v ? v : '');
    }
    
    function old_snippet() {
        var params = {
            rssmikle_url: undef_to_nullstr(a.rssmikle_url),
            rssmikle_frame_width: undef_to_nullstr(a.rssmikle_frame_width),
            rssmikle_frame_height: undef_to_nullstr(a.rssmikle_frame_height),
            rssmikle_target: undef_to_nullstr(a.rssmikle_target),
            rssmikle_font: undef_to_nullstr(a.rssmikle_font),
            rssmikle_font_size: undef_to_nullstr(a.rssmikle_font_size),
            rssmikle_border: undef_to_nullstr(a.rssmikle_border),
            responsive: undef_to_nullstr(a.responsive),
            rssmikle_css_url: (a.rssmikle_css_url == 'http://' ? '' : undef_to_nullstr(a.rssmikle_css_url)),
            text_align: undef_to_nullstr(a.text_align),
            corner: undef_to_nullstr(a.corner),
            autoscroll: undef_to_nullstr(a.autoscroll),
            scrolldirection: undef_to_nullstr(a.scrolldirection),
            scrollstep: undef_to_nullstr(a.scrollstep),
            mcspeed: undef_to_nullstr(a.mcspeed),
            sort: undef_to_nullstr(a.sort),
            rssmikle_title: undef_to_nullstr(a.rssmikle_title),
            rssmikle_title_sentence: undef_to_nullstr(a.rssmikle_title_sentence),
            rssmikle_title_link: (a.rssmikle_title_link == 'http://' ? '' : undef_to_nullstr(a.rssmikle_title_link)),
            rssmikle_title_bgcolor: undef_to_nullstr(a.rssmikle_title_bgcolor),
            rssmikle_title_color: undef_to_nullstr(a.rssmikle_title_color),
            rssmikle_title_bgimage: (a.rssmikle_title_bgimage == 'http://' ? '' : undef_to_nullstr(a.rssmikle_title_bgimage)),
            rssmikle_item_bgcolor: undef_to_nullstr(a.rssmikle_item_bgcolor),
            rssmikle_item_bgimage: (a.rssmikle_item_bgimage == 'http://' ? '' : undef_to_nullstr(a.rssmikle_item_bgimage)),
            rssmikle_item_title_length: undef_to_nullstr(a.rssmikle_item_title_length),
            rssmikle_item_title_color: undef_to_nullstr(a.rssmikle_item_title_color),
            rssmikle_item_border_bottom: undef_to_nullstr(a.rssmikle_item_border_bottom),
            rssmikle_item_description: undef_to_nullstr(a.rssmikle_item_description),
            rssmikle_item_description_length: undef_to_nullstr(a.rssmikle_item_description_length),
            rssmikle_item_description_color: undef_to_nullstr(a.rssmikle_item_description_color),
            rssmikle_item_date: undef_to_nullstr(a.rssmikle_item_date),
            rssmikle_timezone: undef_to_nullstr(a.rssmikle_timezone),
            datetime_format: undef_to_nullstr(a.datetime_format),
            rssmikle_item_description_tag: undef_to_nullstr(a.rssmikle_item_description_tag),
            rssmikle_item_description_image_scaling: undef_to_nullstr(a.rssmikle_item_description_image_scaling),
            rssmikle_item_podcast: undef_to_nullstr(a.rssmikle_item_podcast)
        };
    
        feedwind_show_widget_iframe(params);
        
        a.rssmikle_url = '';
        a.rssmikle_frame_width = '';
        a.rssmikle_frame_height = '';
        a.rssmikle_target = '';
        a.rssmikle_font = '';
        a.rssmikle_font_size = '';
        a.rssmikle_border = '';
        a.responsive = '';
        a.rssmikle_css_url = '';
        a.text_align = '';
        a.corner = '';
        a.scrollbar = '';
        a.autoscroll = '';
        a.scrolldirection = '';
        a.scrollstep = '';
        a.mcspeed = '';
        a.sort = '';
        a.rssmikle_title = '';
        a.rssmikle_title_sentence = '';
        a.rssmikle_title_link = '';
        a.rssmikle_title_bgcolor = '';
        a.rssmikle_title_color = '';
        a.rssmikle_title_bgimage = '';
        a.rssmikle_item_bgcolor = '';
        a.rssmikle_item_bgimage = '';
        a.rssmikle_item_title_length = '';
        a.rssmikle_item_title_color = '';
        a.rssmikle_item_border_bottom = '';
        a.rssmikle_item_description = '';
        a.rssmikle_item_description_length = '';
        a.rssmikle_item_description_color = '';
        a.rssmikle_item_date = '';
        a.rssmikle_timezone = '';
        a.datetime_format = '';
        a.rssmikle_item_description_tag = '';
        a.rssmikle_item_description_image_scaling = '';
        a.rssmikle_item_podcast = '';
    }
})()
</script>




<script type="text/javascript">(function() {var params = {rssmikle_url: "https://github.com/taddallas.atom",rssmikle_frame_width: "800",rssmikle_frame_height: "800",frame_height_by_article: "0",rssmikle_target: "_blank",rssmikle_font: "Helvetica, sans-serif",rssmikle_font_size: "12",rssmikle_border: "off",responsive: "on",rssmikle_css_url: "",text_align: "left",text_align2: "left",corner: "off",scrollbar: "on",autoscroll: "off",scrolldirection: "up",scrollstep: "5",mcspeed: "10",sort: "Off",rssmikle_title: "on",rssmikle_title_sentence: "",rssmikle_title_link: "",rssmikle_title_bgcolor: "#000000",rssmikle_title_color: "#e0e8ff",rssmikle_title_bgimage: "",rssmikle_item_bgcolor: "#85f7a0",rssmikle_item_bgimage: "",rssmikle_item_title_length: "55",rssmikle_item_title_color: "#0066FF",rssmikle_item_border_bottom: "on",rssmikle_item_description: "off",item_link: "on",rssmikle_item_description_length: "150",rssmikle_item_description_color: "#e8e8e8",rssmikle_item_date: "gl1",rssmikle_timezone: "Etc/GMT",datetime_format: "%b %e, %Y %l:%M %p",item_description_style: "html",item_thumbnail: "full",item_thumbnail_selection: "auto",article_num: "15",rssmikle_item_podcast: "off",keyword_inc: "",keyword_exc: ""};feedwind_show_widget_iframe(params);})();</script><div style="font-size:10px; text-align:center; width:600px;">
</div>
