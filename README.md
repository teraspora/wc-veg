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
Created requirements.txt with
`$ pip3 freeze --local > requirements.txt`

Then push worked, dependencies installed etc.:

```
$ git push -u heroku master 
Counting objects: 11, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (10/10), done.
Writing objects: 100% (11/11), 17.84 KiB | 1.78 MiB/s, done.
Total 11 (delta 1), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-3.6.7
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting atomicwrites==1.2.1 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/3a/9a/9d878f8d885706e2530402de6417141129a943802c084238914fa6798d97/atomicwrites-1.2.1-py2.py3-none-any.whl
remote:        Collecting attrs==18.2.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/3a/e1/5f9023cc983f1a628a8c2fd051ad19e76ff7b142a0faf329336f9a62a514/attrs-18.2.0-py2.py3-none-any.whl
remote:        Collecting click==6.7 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl (71kB)
remote:        Collecting cycler==0.10.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
remote:        Collecting Django==1.11 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 5))
remote:          Downloading https://files.pythonhosted.org/packages/47/a6/078ebcbd49b19e22fd560a2348cfc5cec9e5dcfe3c4fad8e64c9865135bb/Django-1.11-py2.py3-none-any.whl (6.9MB)
remote:        Collecting Flask==1.0.2 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 6))
remote:          Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
remote:        Collecting itsdangerous==0.24 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 7))
remote:          Downloading https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz (46kB)
remote:        Collecting Jinja2==2.10 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 8))
remote:          Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl (126kB)
remote:        Collecting kiwisolver==1.0.1 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 9))
remote:          Downloading https://files.pythonhosted.org/packages/69/a7/88719d132b18300b4369fbffa741841cfd36d1e637e1990f27929945b538/kiwisolver-1.0.1-cp36-cp36m-manylinux1_x86_64.whl (949kB)
remote:        Collecting MarkupSafe==1.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 10))
remote:          Downloading https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz
remote:        Collecting matplotlib==3.0.1 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 11))
remote:          Downloading https://files.pythonhosted.org/packages/1e/f8/4aba1144dad8c67db060049d1a8bc740ad9fa35288d21b82bb85de69ff15/matplotlib-3.0.1-cp36-cp36m-manylinux1_x86_64.whl (12.9MB)
remote:        Collecting more-itertools==5.0.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 12))
remote:          Downloading https://files.pythonhosted.org/packages/a4/a6/42f17d065bda1fac255db13afc94c93dbfb64393eae37c749b4cb0752fc7/more_itertools-5.0.0-py3-none-any.whl (52kB)
remote:        Collecting numpy==1.15.4 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 13))
remote:          Downloading https://files.pythonhosted.org/packages/ff/7f/9d804d2348471c67a7d8b5f84f9bc59fd1cefa148986f2b74552f8573555/numpy-1.15.4-cp36-cp36m-manylinux1_x86_64.whl (13.9MB)
remote:        Collecting pandas==0.23.3 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 14))
remote:          Downloading https://files.pythonhosted.org/packages/f4/cb/a801eaf624e36fffaa6cf1f4597a1e4b0742c200ed928e689c58fb3cb811/pandas-0.23.3-cp36-cp36m-manylinux1_x86_64.whl (8.9MB)
remote:        Collecting pluggy==0.8.1 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 15))
remote:          Downloading https://files.pythonhosted.org/packages/2d/60/f58d9e8197f911f9405bf7e02227b43a2acc2c2f1a8cbb1be5ecf6bfd0b8/pluggy-0.8.1-py2.py3-none-any.whl
remote:        Collecting py==1.7.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 16))
remote:          Downloading https://files.pythonhosted.org/packages/3e/c7/3da685ef117d42ac8d71af525208759742dd235f8094221fdaafcd3dba8f/py-1.7.0-py2.py3-none-any.whl (83kB)
remote:        Collecting pyparsing==2.3.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 17))
remote:          Downloading https://files.pythonhosted.org/packages/71/e8/6777f6624681c8b9701a8a0a5654f3eb56919a01a78e12bf3c73f5a3c714/pyparsing-2.3.0-py2.py3-none-any.whl (59kB)
remote:        Collecting pytest==4.1.1 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 18))
remote:          Downloading https://files.pythonhosted.org/packages/9e/bf/2974be45c498a0ebc2708bfada25d5d1874ab3315a4e76ce7d38e29724fa/pytest-4.1.1-py2.py3-none-any.whl (216kB)
remote:        Collecting python-dateutil==2.7.5 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 19))
remote:          Downloading https://files.pythonhosted.org/packages/74/68/d87d9b36af36f44254a8d512cbfc48369103a3b9e474be9bdfe536abfc45/python_dateutil-2.7.5-py2.py3-none-any.whl (225kB)
remote:        Collecting pytz==2018.5 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 20))
remote:          Downloading https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl (510kB)
remote:        Collecting scipy==1.1.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 21))
remote:          Downloading https://files.pythonhosted.org/packages/a8/0b/f163da98d3a01b3e0ef1cab8dd2123c34aee2bafbb1c5bffa354cc8a1730/scipy-1.1.0-cp36-cp36m-manylinux1_x86_64.whl (31.2MB)
remote:        Collecting six==1.12.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 22))
remote:          Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
remote:        Collecting virtualenv==16.2.0 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 23))
remote:          Downloading https://files.pythonhosted.org/packages/6a/d1/e0d142ce7b8a5c76adbfad01d853bca84c7c0240e35577498e20bc2ade7d/virtualenv-16.2.0-py2.py3-none-any.whl (1.9MB)
remote:        Collecting Werkzeug==0.14.1 (from -r /tmp/build_a46e1bb81b709b5381ceed35947f3f2d/requirements.txt (line 24))
remote:          Downloading https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
remote:        Installing collected packages: atomicwrites, attrs, click, six, cycler, pytz, Django, MarkupSafe, Jinja2, Werkzeug, itsdangerous, Flask, kiwisolver, pyparsing, numpy, python-dateutil, matplotlib, more-itertools, pandas, pluggy, py, pytest, scipy, virtualenv
remote:          Running setup.py install for MarkupSafe: started
remote:            Running setup.py install for MarkupSafe: finished with status 'done'
remote:          Running setup.py install for itsdangerous: started
remote:            Running setup.py install for itsdangerous: finished with status 'done'
remote:        Successfully installed Django-1.11 Flask-1.0.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 atomicwrites-1.2.1 attrs-18.2.0 click-6.7 cycler-0.10.0 itsdangerous-0.24 kiwisolver-1.0.1 matplotlib-3.0.1 more-itertools-5.0.0 numpy-1.15.4 pandas-0.23.3 pluggy-0.8.1 py-1.7.0 pyparsing-2.3.0 pytest-4.1.1 python-dateutil-2.7.5 pytz-2018.5 scipy-1.1.0 six-1.12.0 virtualenv-16.2.0
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> (none)
remote: 
remote: -----> Compressing...
remote:        Done: 127.6M
remote: -----> Launching...
remote:        Released v3
remote:        https://wcveg.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/wcveg.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'heroku'.
(venv) 18:09 /west-cork-veg: 2057$ 
```

Added Procfile with
`$ echo 'web: python3 app.py' > Procfile`
	[NOTE: you MUST have a SPACE after the COLON!]

```(venv) 18:14 /west-cork-veg: 2063$ heroku ps:scale web=1
Scaling dynos... done, now running web at 1:Free
(venv) 18:19 /west-cork-veg: 2064$ 
```

Set IP (0.0.0.0) and PORT (5000) in Heroku dashboard.
Clicked "Open App" and my Hello World page was displayed by the browser.

