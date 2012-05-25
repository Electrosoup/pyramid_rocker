Pyramid Rocker
==============

Pyramid Rocker allows you to change static the Javascript and CSS files of you Pyramid application from within chrome DevTools on the fly. No need to be constantly moving from
Devtools to your text editor.

Requirements
============

Nikita Vasilyev's Chrome Plugin `Chrome Devtools Autosave <https://github.com/NV/chrome-devtools-autosave>`_

Pyramid Rocker plugin for Pyramid

Installation
============

Install pyramid rocker (using Mr. Developer or whatever) and in your development.ini file
add the following line.

``pyramid.includes = pyramid_rocker``


Install the Chrome Plugin folowing the Nikita's instructions, but there is no need to install the server that he has written, just the plugin, we will be using Pyramid directly.

In the plugins settings select 'options' for the Dev Tools Extension and Add a Rule:

Resource ``(leave this empty)``
Post To  ``http://thepyramidapp:andport/__rocker_update``

for example

``http://127.0.0.1:6543:/__rocker_update``


In chrome devtools you can now edit your CSS and Javascript and click on the page for it to be saved into Pyramid.

This is a proof of concept, Still need to tidy up and write some tests before I upload to PyPi.

But Enjoy.

Mr. J