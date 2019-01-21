# West Cork Vegetables

For my Data Centric Development project I will be creating a resource for vegetable gardeners in West Cork, Ireland, where I live.

There are many great organic vegetable growers in West Cork, some who operate on a commercial basis selling in farmers' markets or to independent shops or to restaurants or supermarkets; some who grow primarily for their own use and for their families' but sell of excess to the local wholefood shop for example; and others who grow purely for their own households and for the wonderful satisfaction in growing their own food, the feeling of vibrant life energy that comes from crunching into a freshly-dug carrot, the exuberant mouth-feel of a ripe cherry tomato lightly plucked from its cane.

So I would like to begin collating a database of vegetables that people grow in West Cork, which can be augmented by contributions from any West Cork vegetable gardeners.

For each vegetable grown, the database will store its common names, its Linnaean name, its category (leafy, root, bulb etc.), its ideal soil type (clay, sandy, loamy etc.) and moisture content (wet, dry, medium), time to sow indoors, time to plant out, time to sow outdoors, comments, tips, lists of suppliers and photographs.

Users will be able to click to display lists of vegetables filtered by different properties, e.g. "All vegetables that you sow before April in clay soil".

Registered users will be automatically approved as editors and as such will be able to edit records and add new records.   Only the database administrator will be able to delete records.

## UX
 
### User stories

- Taidhgh, new to vegetable gardening, has some time off work in April and would like to know what he can plant straightaway and get a quick crop from.

He should be able to see a list of all vegetables in the database together with a well-signposted hierarchical drop-down menu allowing him to filter his request by the above criteria and so show just the records which meet the criteria.

- Siobhan, just finished an intensive horticulture course, has just moved to West Cork with the intention of starting a business growing vegetables for restaurants.   She wants to see what other people are growing, generally get a feel of the West Cork organic growing scene, and in particular find out who's supplying good-quality seed garlic.

She should be able to display a list of all suppliers of garlic listed, i.e. a view which presents the contents of the "suppliers" field of the "garlic" record in an easily readable form

## Features

The app will be coded in Python using Flask and a MongoDB instance hosted at mLab, and deployed to Heroku.

There should be a standard view for a list of records of any length, and a different view for a single record.   Only in the single record view will the photograph and comments be displayed, for instance.   There will be a third view for lists of single fields, which we will call the field view.

## Development

I have started by beginning this README and by instantiating a database at mLab called wc-veg.   I have created two collections, "categories" and "vegetables".   I have created a single record in each collection.

I am sure that as I develop the app many ideas will occur to me for features to implement, and I will evaluate all such ideas according to their estimated usefulness and ease of implementation, allowing the app to take shape "organically".

At some point I will then consider critically whether it fulfils the original concept, whether it satisfies the project requirements, whether any functionality ought to be removed or changed and whether any new functionality is needed.

I will now continue by setting up the Python/Flask scaffolding for a database app and get basic "Hello World" functionality working. 

## Setup

Created directory west-cork-veg and cded into it, did a git init, linked with remote Github repo and pushed to it.

`$ python3 -m venv venv` failed.
```
17:16 /west-cork-veg: 2024$ python3 --version
Python 3.6.7
17:16 /west-cork-veg: 2025$ sudo pip3 install virtualenv
[sudo] password for john: 
The directory '/home/john/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/john/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting virtualenv
  Downloading https://files.pythonhosted.org/packages/6a/d1/e0d142ce7b8a5c76adbfad01d853bca84c7c0240e35577498e20bc2ade7d/virtualenv-16.2.0-py2.py3-none-any.whl (1.9MB)
    100% |████████████████████████████████| 1.9MB 204kB/s 
Requirement already satisfied: setuptools>=18.0.0 in /home/john/.local/lib/python3.6/site-packages (from virtualenv)
Installing collected packages: virtualenv
Successfully installed virtualenv-16.2.0
17:21 /west-cork-veg: 2026$ python3 -m venv venv
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/media/john/sys2/web18/code-institute/milestone-projects/project-4/west-cork-veg/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']

17:21 /west-cork-veg: 2027$ sudo pip3 install python3-venv
The directory '/home/john/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/john/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting python3-venv
  Could not find a version that satisfies the requirement python3-venv (from versions: )
No matching distribution found for python3-venv
17:22 /west-cork-veg: 2028$ sudo apt install python3-venv
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  python3.6-venv
The following NEW packages will be installed:
  python3-venv python3.6-venv
0 upgraded, 2 newly installed, 0 to remove and 36 not upgraded.
Need to get 7,392 B of archives.
After this operation, 44.0 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 python3.6-venv amd64 3.6.7-1~18.04 [6,184 B]
Get:2 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 python3-venv amd64 3.6.7-1~18.04 [1,208 B]
Fetched 7,392 B in 1s (12.3 kB/s)       
Selecting previously unselected package python3.6-venv.
(Reading database ... 220557 files and directories currently installed.)
Preparing to unpack .../python3.6-venv_3.6.7-1~18.04_amd64.deb ...
Unpacking python3.6-venv (3.6.7-1~18.04) ...
Selecting previously unselected package python3-venv.
Preparing to unpack .../python3-venv_3.6.7-1~18.04_amd64.deb ...
Unpacking python3-venv (3.6.7-1~18.04) ...
Setting up python3.6-venv (3.6.7-1~18.04) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Setting up python3-venv (3.6.7-1~18.04) ...
17:22 /west-cork-veg: 2029$ ll
total 56K
drwxrwxr-x 4 john john 4.0K Jan 21 17:15 ./
drwxrwxr-x 3 john john 4.0K Jan 21 14:34 ../
drwxrwxr-x 8 john john 4.0K Jan 21 16:04 .git/
-rw-rw-r-- 1 john john  35K Jan 21 16:01 LICENSE
-rw-rw-r-- 1 john john 3.8K Jan 21 16:02 README.md
drwxrwxr-x 5 john john 4.0K Jan 21 17:15 venv/
17:22 /west-cork-veg: 2030$ ll venv
total 24K
drwxrwxr-x 5 john john 4.0K Jan 21 17:15 ./
drwxrwxr-x 4 john john 4.0K Jan 21 17:15 ../
drwxrwxr-x 2 john john 4.0K Jan 21 17:15 bin/
drwxrwxr-x 2 john john 4.0K Jan 21 17:15 include/
drwxrwxr-x 3 john john 4.0K Jan 21 17:15 lib/
lrwxrwxrwx 1 john john    3 Jan 21 17:15 lib64 -> lib/
-rw-rw-r-- 1 john john   69 Jan 21 17:21 pyvenv.cfg
17:23 /west-cork-veg: 2031$ python3 -m venv venv
17:23 /west-cork-veg: 2032$17:23 /west-cork-veg: 2032$ source venv/bin/activate
(venv) 17:26 /west-cork-veg: 2033$ pip3 install flask
Collecting flask
  Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
    100% |████████████████████████████████| 92kB 225kB/s 
Collecting itsdangerous>=0.24 (from flask)
  Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.14 (from flask)
  Downloading https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
    100% |████████████████████████████████| 327kB 168kB/s 
Collecting click>=5.1 (from flask)
  Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
    100% |████████████████████████████████| 81kB 247kB/s 
Collecting Jinja2>=2.10 (from flask)
  Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl (126kB)
    100% |████████████████████████████████| 133kB 245kB/s 
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10->flask)
  Downloading https://files.pythonhosted.org/packages/08/04/f2191b50fb7f0712f03f064b71d8b4605190f2178ba02e975a87f7b89a0d/MarkupSafe-1.1.0-cp36-cp36m-manylinux1_x86_64.whl
Installing collected packages: itsdangerous, Werkzeug, click, MarkupSafe, Jinja2, flask
Successfully installed Jinja2-2.10 MarkupSafe-1.1.0 Werkzeug-0.14.1 click-7.0 flask-1.0.2 itsdangerous-1.1.0
(venv) 17:28 /west-cork-veg: 2034$ 

```
Created app.py and single "/" route.   "Hello World" functionality achieved successfully.

app.py
```
import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello Star Cluster"

if __name__ == "__main__":
	app.run(host = os.environ.get('IP', "0.0.0.0"),
            port = int(os.environ.get('PORT', "5000")),
            debug = True)
```

Created Heroku app:

```
(venv) 17:57 /west-cork-veg: 2049$ heroku create wcveg
Creating ⬢ wcveg... done
https://wcveg.herokuapp.com/ | https://git.heroku.com/wcveg.git
(venv) 17:58 /west-cork-veg: 2050$ git push -u heroku master 
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 14.36 KiB | 1.79 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote:  !     No default language could be detected for this app.
remote: 			HINT: This occurs when Heroku cannot detect the buildpack to use for this application automatically.
remote: 			See https://devcenter.heroku.com/articles/buildpacks
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to wcveg.
remote: 
To https://git.heroku.com/wcveg.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/wcveg.git'
(venv) 18:04 /west-cork-veg: 2052$ 
 
```

