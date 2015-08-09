
This is a blank open lab notebook, ready to be filled with your great science. Below, I'll guide you through what you need to do to get it up and running. 



## File structure

The general file structure may seem intimidating, but I assure you it's pretty straight-forward. Below, I provide a general idea about the purpose of each folder


### _layouts

Contains the `html` layouts that determine where your content goes. You most likely won't have to touch these, unless you want your lab notebook to exist as your personal site (`you.github.io`) instead of as a project page, which is how I've set this one up. Here's [more information](http://jekyllrb.com/docs/github-pages/) about the changes you'll need to make if you want the open labnotebook to be your personal website, and not a page thereof.


### _includes

Similar to _layouts, _includes will contain `html` templates for the header and the sidebar of the website. I typically put anything "preamble-ly" into the `head.html` file, like links to fonts, or custom `css` files. 



### public

This folder contains all the `css` files for your open labnotebook. These control the styling, including color, font, etc. The only files you will most likely need to change are `hyde.css` and `lanyon.css`. These are two variations or themes to the blog, which can be viewed [here](https://github.com/poole/lanyon). It is pretty easy to switch between themes.  


### _knitr

This folder is designed to contain any posts which you want to embed `R` code chunks in. The file format is R markdown, which is discussed [here](http://rmarkdown.rstudio.com/) and [here](http://kbroman.org/knitr_knutshell/pages/Rmarkdown.html), and lots of other places. It's pretty useful. Posts contained in this folder need to first be `knit` into markdown (`.Rmd` to `.md`), which you can do (currently manually, though this is clunky) with the `render_post.R` function that lives in the `_knitr` folder. You hand the function the file name (when you are in the `_knitr` folder as your working directory), and it will put the resulting markdown output into your `_posts` folder.


### _posts

This is where you will spend the majority of your time. Each post is an entry in your open lab notebook, and must be formatted with date, and post name (e.g. `2015-8-1-Post-Name.md`). Within this folder, you can have a folder called `_drafts`, which are those posts that just aren't ready for the big time. 


### _config.yml

The config file is pretty important, but you shouldn't have to edit much of it. Just a couple of lines under the `Setup` heading. All those entries are pretty clear; `paginate` refers to how many posts to show on a page, and the base `url` is currently set to be `/sampleNotebook`, but will need to be changed to your repository name, before you push this to Github. Information on setting up your Github account, and an introduction to the version control platform can be found [here](https://guides.github.com/activities/hello-world/)


## Creating pages

Pages live in the home directory of your notebook, and are written as simple markdown documents. In fact, the only difference between a page and a post apart from directory location, is the `yaml` header. The header of a post specifies that the layout (from the `_layouts` folder) is that of a post, while the layout for a page is `layout: page`. Pretty simple, right?

There are a lot of other bells and whistles that could be added, but my goal was just to offer a nice and simple open lab notebook template that is accessible to a broad range of folks. That being said, feel free to contribute functionality or to make some project aspects clearer by forking or filing an issue on the [Github page](https://github.com/taddallas/LabNotebook/tree/sampleNotebook). 



Tad











