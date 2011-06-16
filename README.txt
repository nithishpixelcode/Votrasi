Future work
=============

    * Google sitemap 
    * Blog
    * Page navagation
    * Admin Thumbnail
    * Flicker API
    * Contact Us From

Requirements
==============

The Project  requires Python 2.7 and Django 1.2 and depends on the following
packages:
	
	* Python Imaging Library (http://www.pythonware.com/products/pil/)
	* South (http://south.aeracode.org/)

Installation
==============

1. Clone the read-only repo

     git clone git@github.com:abhipixelcode/Votrasi.git

2. Install the dependencies via PIP.  

     



4. You'll notice that the settings file Django's using in that script,
   settings file exist in the root dir.  This settings file
   containing the shared settings you'll need to run the code.

   You should Create the Database , use the follwing steps 
	* mysql -u root -p
	* Then when you are in mysql shell, run the command: create database votrasi;
	* mysql -u root -p votrasi < db.sql
	* exit

   



5. Run the server and head over to the admin.

     http://localhost:8000/admin/




