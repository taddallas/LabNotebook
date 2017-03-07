---
layout: page
title: Github Activity
---


<script type="text/javascript" src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="FeedEk.js"></script>



<div id="divRss"></div>




<script type='text/javascript'> 

$('#divRss').FeedEk({
    FeedUrl : 'http://jquery-plugins.net/rss',
    MaxCount : 5,
    ShowDesc : true,
    ShowPubDate:true,
    DescCharacterLimit:100,
    TitleLinkTarget:'_blank'
  });

</script>









