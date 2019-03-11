# West Cork Vegetables

This web application has been designed and built by me, John Lynch, to satisfy the requirements for the "Data Centric Development" project of the Code Institute Full-Stack Software Development course I am currently pursuing.   It is intended to be a community resource for vegetable gardeners in West Cork, Ireland, where I live, and I hope to continue to develop it going forward.

There are many great organic vegetable growers in West Cork, some who operate on a commercial basis selling in farmers' markets or to independent shops or to restaurants or supermarkets; some who grow primarily for their own use and for their families' but sell of excess to the local wholefood shop for example; and others who grow purely for their own households and for the wonderful satisfaction in growing their own food, the feeling of vibrant life energy that comes from crunching into a freshly-dug carrot, the exuberant mouth-feel of a ripe cherry tomato lightly plucked from its cane.

## Specification / Design

I would like to begin collating information to build a database of vegetables that can be grown in West Cork, which can be augmented by contributions from any West Cork vegetable gardeners; or even non-West Cork gardeners!

For each vegetable grown, the database will store its common names, its Linnaean name, its category (leafy, root, bulb etc.), information, comments, growing tips, cooking tips and photographs.   Once sufficient content has been gathered, it will also show its ideal soil type (clay, sandy, loamy etc.) and moisture content (wet, dry, medium), time to sow indoors, time to plant out, time to sow outdoors, lists of suppliers.   I shall be open to feature requests from users!

Logging in will bring the user to a list of all vegetables in the database, with buttons to show, edit or delete them and links that can be clicked to sort or filter the list:  users will be able to click to sort the list by category, genus, common name or creator, and display lists of vegetables filtered by different properties, e.g. "All fruiting vegetables" or "All Alliums".

Clicking "Show" for a vegetable will cause a detailed view to be displayed. with a photograph.   Registered users will be able to upload photographs for a new entry, to add to an existing entry or replace an existing image.

### The project specification states:

> Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a 
> username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)

In accordance with this, the user will be allowed to register just by logging in with a username.   The list of users will just be stored in memory so will not persist over a server reboot.   Registered users will be automatically approved as editors and as such will have full CRUD permissions.   Unregistered users will not be able to update or delete records.

I like to trust people but accept that if this becomes a real web app rather than, as it is now, a project for a course, I'll have to introduce a proper user registration and authorisation scheme.

The vegetables will be stored as documents in a non-relational MongoDB database hosted with mLab.   The app will be hosted with Heroku.


## UX
 
### User stories

- Taidhgh, new to vegetable gardening, has some time off work in April so wants to browse, look at the pictures, read the wisdom of others and get an idea what he can plant straightaway and get a quick crop from.

The app should make it easy and intuitive to be able to see a list of all vegetables in the database together with a detailed view of any individual vegetable, with useful information and good photographs.

- Siobhan, just finished an intensive horticulture course, has just moved to West Cork with the intention of starting a business growing vegetables for restaurants.   She wants to see what other people are growing, generally get a feel of the West Cork organic growing scene, and in particular find out who's supplying good-quality seed garlic.

She should enjoy browsing and reading the comments, and if she clicks "Show" against the garlic entry she ought to be able to see lots of useful information about growing garlic in West Cork, and hopefully a list of all suppliers too.

- Dave, an experienced West Cork organic vegetable grower, just wants to share his knowledge by editing and adding to the entries to augment the database with handy tips and ideas for less experienced gardeners.

It should be a painless exercise to edit or add to the existing content.

### UI

I conceived the design in my head and made a couple of sketches on paper (scans below), then let the design evolve as I developed the app and introduced features step by step.

![](static/images/wcveg-design-00.jpg)
![](static/images/wcveg-design-01.jpg)

I tried to give the site a natural feel with browns and greens and a background of green leafy vegetables.

### Features

- Upon login, or subsequent to clicking "Browse Veg" the user sees displayed a table of all the vegetables in the database.

- All pages feature a navigation bar at the top, with links to browse the vegetables, see useful links, or login / logout.  The user can click "About" for an overview of the site, or "Links" for a list of useful links.   For registered users there is also a link to add a vegetable to the database.

- For each vegetable in the list the common name, genus, species and category are shown, and the username of the entry's creator, together with buttons to show a detailed view, and for registered users buttons to edit or delete the vegetable.   The delete option features a modal confirmation dialogue to mitigate the chances of an inadvertant deletion.

- For registered users there is also a well placed "Add Vegetable" link at the top of the list in addition to the one in the navbar.

- As well as information about the site, the "About" page displays live up-to-date statistics about the database and brief details regarding its development.

- The forms to add and edit vegetable entries have sensible defaults for which fields are required and which are not editable, and for exampe allow only alphabetic characters in common names, genera and species.

- When editing or adding a vegetable, the user has the option of uploading a photograph, which will be saved and displayed in the detailed view.

### Features Left to Implement

- Multiple photos for each vegetable.

- More fields, for properties like soil type, recommended acidity (pH value), time to sow (outside / inside), time to plant out, time to harvest, nutrient needs, tips and tricks, together with the ability to sort and filter by these fields.

- A blog page where expert gardeners can share their ideas about organic vegetable growing in West Cork.

- Proper, secure user registration and authorisation.

- Any features subsequently requested if thought to be useful and feasible.

- Augmented and improved content.

- Persistence of user-uploaded images (see the section "Interesting Bugs" below in this README.)

- As the site grows, with more entries, maybe I will create fields for planting time, harvest time, nutrient requirements, soil type etc..   This will depend on what users want and what feels appropriate and useful to me.

- The project is open-source so I am open tto pull requests.

## Technologies Used

I developed the app on my local machine, coding in Sublime Text 3 using Emmet, and running a standard Bash terminal in Ubuntu 18.   My default browser is Chrome 70/71 but from time to time I also check how the app appears in Firefox Developer Edition, and on tablet browsers.

The app is coded in Python 3, using Flask and a MongoDB instance hosted at mLab.   It is deployed to Heroku.

It uses Jinja templates for the views and PyMongo for database access.   The vegetables are stored as one collection in the database, one document per vegetable.   The categories are stored as another collection.   References to users are stored in an array in memory.   Uploaded images are saved to the `images` directory and named `&lt;vegetable name&gt;.jpg` or `&lt;vegetable name&gt`;.png, so we can find them without having to index them.   Going forward, ancilliary images will be allowed, and this will be handled by the addition of a numerical suffix preceding the file extension.

The views are styled with Materialize.   Having developed the first three projects with raw CSS in order to learn it better, I decided to try using a CSS framework, and after watching a few tutorials I found that Materialize seemed easier and more intuitive to me than Bootstrap.   I played with it a little then incorporated it to make it the foundation of the site's styling.   Materialize uses a little jQuery, other than that I use no Javascript.   All the logic is implemented in Python.

In quest of learning all the plumbing and wiring necessary for such an app, I have made much use of a number of websites, particularly

- [Stack Overflow][0]
- [tutorialspoint][1]
- [Materialize][2]
- [The Hitchhiker’s Guide to Python][3]
- [Explore Flask][4]
- [Flask / Pocoo][5]
- [Miguel Grinberg's blog][6]
- [Python Tips][7]

## Testing

The app has been manually tested extensively throughout the development process, and when bugs have been found I have either fixed them or noted them down for later fixing.

Each time I introduce a new feature, change something or fix a bug, I have attempted to break the app if possible.

As this has been only my second proper Flask app (and first with database), a number of issues were significant during the development process, and required me to use the above websites to help me find the correct syntax.   Examples:  getting file paths right in constructing URIs, e.g. for saving the images; keeping track of users; interrogating and updating the database; constraining and validating form input.

Extensive testing was required, and accessing pages from different starting points, registered and unregistered, was important.

I tested mobile responsiveness in Chrome Dev Tools and on my Android tablet and Android phone.

### Interesting Bugs

I have had an issue with user uploads of images to my Heroku server.
At first, and for a short time, an uploaded image is displayed correctly, but after an hour it seems to have disappeared.

Details below.

Steps to reproduce the issue:

1. Log in with a username of > 4 letters. You are taken to veg.html, a table of all the veg.
2. Click "Add a vegetable".   You are taken to addveg.html.
3. Fill in common name, genus and species fields (letters only).
4. Click "Upload a Photo". Select a (small) photo and click OK.
5. Click "Add to database".   The photo should upload, then you will be redirected back to the listing.
6. Click "Show" against the name of the vegetable you added.   You should see the image you uploaded.
7. Go back to the listing, wait a minute, then click "Show" again.   You should still see the image.
8. Wait an hour and try again.   

Expected state and behaviour:

1. The image is uploaded to the static/images folder when you click "Add to database"
2. It is downloaded and displayed correctly by any browser displaying showveg.html.
3. It remains stored in the static/images folder on the server, and will be displayed at any time by any browser which requests the showveg.html page.

Actual state and behaviour:

1. & 2. The above expected behaviour seems to work for a few minutes after uploading.
3. After an hour the image is not displayed as expected.

#### Notes:

If I log into my Heroku server with 'heroku run bash' and I cd into the static/images folder, I only see the image files I have pushed to the server via git.   I don't see any user-uploaded files.   In particular I don't see the file I just uploaded, even when my browser is correctly displaying it.

#### Cause:

I've discovered that user-uploaded images will disappear because the Heroku filesystem is ephemeral - that means that any changes to the filesystem whilst the dyno is running only last until that dyno is shut down or restarted.

#### Solution:

I looked into storing the images elsewhere in the Cloud, e.g. using S3 or GCP.   I scanned through the documentation for getting these up and running and implemented in Python/Flask, and judged that it would take some time to get all the configuration right.   

The other option I considered was base-64-encoding the images and storing them in the database as strings.   Investigation revealed that Python has a `base64` module which provides precisely the methods necessary to do base 64 encoding and decoding.

A couple of tests showed that the resultant file sizes were only about 10% bigger and the encoding (using `b64encode()`) and decoding (using `b64decode()`) seemed to happen in a fraction of a second for a 500kB file.

More tests showed that the data gets stored as `<binarydata>` in the database and needs to be decoded not with `b64decode()` but with the  the built-in `str.decode()` method.

I also save the mimetype as a three-character string (`"png"` or `"jpg"`) in the database so I can use it in the `src` property of the `<img>` tag in `showveg.html` when it needs to be displayed to the user.

This solution works fine, except that it seems to slow down the application, in the sense that pages are slow to load.   This slowdown seems to happen also on pages where no encoding or decoding takes place, which seems strange.   At the time of writing I have not yet debugged this slowdown, and this permanent starage solution remains in git branch `base64test`, not merged into the `master` branch.

#### Update:

Following communication with a Code Institute tutor, in which she said

>  "It's absolutely fine to stick with Heroku and document the ephemerality of it's filesystem. The assessor will be much more
> interested in how you've set up and queried your database and in the code you've written to run your project (rather than the
> limitations of heroku)."

I have decided to deploy the master branch for my project submission, i.e. the one which stores user-uploaded images in the ephemeral Heroku file system.
The alternative, in git branch `base64test` in the Github repo, shows the code I have used to base64-encode the images and save them as bytestrings in the MongoDB database.   

## Deployment

The app is deployed to Heroku and can be accessed at [West Cork Veg][8].

Version control is implememnted in git, and I have pushed the project directory to Github at [West Cork Veg Github repo][9], as well as pushing to Heroku.   I have largely used 'micro-commits' with detailed commit messages, as (apart from its being considered good practice) it means I can look back at the log when implementing future similar projects in order to learn from my mistakes and hopefully obviate issues.  

The database is hosted at [mLab][10].

For production, the app's `debug` attribute is set to False, and the secret data, i.e the `app.secret_key` and the database connection string encoding the password in plain text, are stored as environment variables at Heroku and accessed through the `os.getenv()` method.

## Acknowledgements

Small bits of code have been copied from elsewhere, such as Materialize markup, and the Python function `allowed_file(filename)`.   The latter is acknowledged in a copmment above the function.

All vegetable images are either my own or I have been let use them by friends without restrictions or the necessity of attribution.

Thanks to all the open-source community and all the community-minded developers whose sharing of their knowledge and understanding has enabled me to comprehend the necessary concepts to be able to build this app.   And also to all those who have contributed to making a dev's life a bit easier by building frameworks such as Flask and Materialize.

[0]: https://stackoverflow.com/
[1]: https://www.tutorialspoint.com/flask
[2]: https://materializecss.com
[3]: https://docs.python-guide.org/
[4]: http://exploreflask.com/en/latest/
[5]: http://flask.pocoo.org/
[6]: https://blog.miguelgrinberg.com/category/Flask
[7]: http://book.pythontips.com/en/latest/
[8]: https://wcveg.herokuapp.com/
[9]: https://github.com/teraspora/wc-veg
[10]: https://mlab.com/