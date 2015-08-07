---
layout: post
title: Example post
author: tad
tags:
- How-to
---


This document will serve as both a template for blog post structure, and as a "how-to" for Drake lab members wanting to contribute blog posts. 

## The problem I had to solve
<div class="message">
  Insert problem here. Markdown syntax won't work in here, since it's treating it like html. Here, the problem I'm solving is figuring out how to contribute a post to the blog. 
</div>



## Why this is a problem (not trivial)

This is a non-trivial problem, since all members of the Drake lab should be able to contribute blog posts if they choose. In our case, we're using Jekyll, and hosting the project on Github. `DrakeLab` is an organization, and you can ask permission to join the organization once you sign up for GitHub. For a tutorial on how to use GitHub generally, look [here](http://github.com/taddallas/githubTutorial). Clone the [repository](http://github.com/DrakeLab/DrakeLab.github.io), and get ready to contribute.


## Why this is generic

This is a problem encountered by anyone wanting to post on our blog, but also is applicable to other folks wanting to use Jekyll and R markdown to generate blog posts. 


## What I did

The [repository](http://github.com/DrakeLab/DrakeLab.github.io) has a bunch of folders. The only ones that you'll really need to worry about are `_knitr` and `tags`. You will write your posts as `.Rmd` files, and name them with the date (e.g., `2015-2-14-Valentines-Day.Rmd' would be a romantic post). The part after the date is just to provide a brief bit about what the post is about.

Posts have a yaml heading that needs to be used. 


{% highlight r %}
---
layout: post 
title: Example post
author: tad
tags:
- How-to
--- 
{% endhighlight %}

Above provides the details. `layout` will always be "post". Provide your post title. If you are posting for the first time, chat with me about getting yourself listed as an author, or you can edit the `_data/authors.yaml` file with your information. Tags work in the following way. They'll easy to use, but for every new tag you use, you'll have to create a folder in the `tags` folder with the tag name, and a file called `index.html` containing a simple 2 line yaml stating what your tag name is and specifying the `layout` as "tagpage". I know it's silly, but whatever. It works for now. 

Proceed to write your awesome blog post, complete with reproducible and dynamically inserted plots and such. Below, I make a quick plot of an interaction matrix using the `metacom` package. 


{% highlight r %}
	library(metacom)
	Imagine(matrix(rbinom(400,1,0.4), ncol=20,nrow=20))
{% endhighlight %}

![center](/../figs/2015-1-11-example-post/unnamed-chunk-2-1.png) 

Feel free to mix a bit of `html` in with your markdown if you're feeling frisky. Below, I use the `img` html tag to include a picture of a Turkish van cat. 

<img src="http://upload.wikimedia.org/wikipedia/commons/2/22/Turkish_Van_Cat.jpg" height="300"> Cat. </img>

Here's the annoying part. Once you finish your post, you'll have to convert it to an `md` file and put it in the `_posts` directory. I've semi-automated this process using some code from [this helpful post](http://www.jonzelner.net/jekyll/knitr/r/2014/07/02/autogen-knitr/). All you'll need to do is source `_knitr/render_post.R` in an R instance. That will convert all `Rmd` posts to `md` and move them to the `_posts` folder and any figures created into the `figs` folder. Once that's done, you can push your changes. If you find it annoying or too time-consuming to rebuild all posts from `Rmd` to `md`, you can just open the `render_post.R` file and run the `KnitPost` function on a single post instead of all posts. Easy.

 If you'd like to view your post locally, you'll need to set up Jekyll on your machine. Pretty easy to set up, and if you have Ruby gems installed. 


{% highlight r %}
gem install jekyll
cd USERNAME.github.com 
jekyll serve
{% endhighlight %}

After this, use your browser to check out [http://localhost:4000/](http://localhost:4000/) where the blog will be locally live. 

Okay. So you've written a blog post, sandboxed it on your local machine and are ready for it to go live. Simply `add`, `commit`, and `push` your changes to the [repository](http://github.com/DrakeLab/DrakeLab.github.io), and your set. 


{% highlight r %}
cd USERNAME.github.com
git add .
git commit -m "SOME HELPFUL MESSAGE"
git push origin master
{% endhighlight %}
Enter in your `username` and `password` and you have just created a beautiful blog post full of reproducible code. 



## How you can do it, too

I just told you how to do it, silly. For fun, I've also added in some `Font-Awesome` capabilities, so you have access to a [beautiful library of icons](http://fortawesome.github.io/Font-Awesome/icons/) which are really easy to input. 

For instance, let's say I want to make a tree icon. Simple.


{% highlight r %}
<i class="fa fa-tree"> </i>
{% endhighlight %}

<i class="fa fa-tree"> </i>

Let's say I want the tree to be like 2,3,4,or 5x larger.


{% highlight r %}
<i class="fa fa-tree fa-2x"> </i>
<i class="fa fa-tree fa-3x"> </i>
<i class="fa fa-tree fa-4x"> </i>
<i class="fa fa-tree fa-5x"> </i>
{% endhighlight %}

<i class="fa fa-tree fa-2x"> </i>
<i class="fa fa-tree fa-3x"> </i>
<i class="fa fa-tree fa-4x"> </i>
<i class="fa fa-tree fa-5x"> </i>

What if I want the tree to be green?


{% highlight r %}
<i class="fa fa-tree" style="color:green"> </i>
{% endhighlight %}
<i class="fa fa-tree" style="color:green"> </i>

Thanks for reading. I hope you decide to contribute to this blog, and that other folks find this blog useful. 

<i class="fa fa-heart" style="color:pink"> </i>




