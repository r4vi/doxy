Doxy: A Google Docs (Spreadsheet) Proxy
============


      .----------------.  .----------------.  .----------------.  .----------------. 
     | .--------------. || .--------------. || .--------------. || .--------------. |
     | |  ________    | || |     ____     | || |  ____  ____  | || |  ____  ____  | |
     | | |_   ___ `.  | || |   .'    `.   | || | |_  _||_  _| | || | |_  _||_  _| | |
     | |   | |   `. \ | || |  /  .--.  \  | || |   \ \  / /   | || |   \ \  / /   | |
     | |   | |    | | | || |  | |    | |  | || |    > `' <    | || |    \ \/ /    | |
     | |  _| |___.' / | || |  \  `--'  /  | || |  _/ /'`\ \_  | || |    _|  |_    | |
     | | |________.'  | || |   `.____.'   | || | |____||____| | || |   |______|   | |
     | |              | || |              | || |              | || |              | |
     | '--------------' || '--------------' || '--------------' || '--------------' |
      '----------------'  '----------------'  '----------------'  '----------------' 
 
 


What is this?
-------------

Because the JSON that Google provides from Google Spreadsheets is utterly useless, I built this during a hackathon.


Usage
-------
* First of all, create a Google Spreadsheet add your headers to row 1 and freeze it. 
* Add your data in the rows below. 
* Then **File > Publish to web** 
* Copy the KEY from the Google Docs URL
* Visit the URL at which doxy is running: ````mydoxy.herokuapp.com```` then add the KEY to the end of it ````http://mydoxy.herokuapp.com/KEY/````.
* Enjoy sexy JSON.

Example
--------

Before (from Google Docs):
```json
{
   "version":"1.0",
   "encoding":"UTF-8",
   "feed":{
      "xmlns":"http://www.w3.org/2005/Atom",
      "xmlns$openSearch":"http://a9.com/-/spec/opensearchrss/1.0/",
      "xmlns$gsx":"http://schemas.google.com/spreadsheets/2006/extended",
      "id":{
         "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values"
      },
      "updated":{
         "$t":"2006-11-30T05:44:34.623Z"
      },
      "category":[
         {
            "scheme":"http://schemas.google.com/spreadsheets/2006",
            "term":"http://schemas.google.com/spreadsheets/2006#list"
         }
      ],
      "title":{
         "type":"text",
         "$t":"Sheet1"
      },
      "link":[
         {
            "rel":"alternate",
            "type":"text/html",
            "href":"https://spreadsheets.google.com/pub?key\u003do13394135408524254648.240766968415752635"
         },
         {
            "rel":"http://schemas.google.com/g/2005#feed",
            "type":"application/atom+xml",
            "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values"
         },
         {
            "rel":"self",
            "type":"application/atom+xml",
            "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values?alt\u003djson-in-script"
         }
      ],
      "author":[
         {
            "name":{
               "$t":"lblackmagicwoman"
            },
            "email":{
               "$t":"lblackmagicwoman@gmail.com"
            }
         }
      ],
      "openSearch$totalResults":{
         "$t":"8"
      },
      "openSearch$startIndex":{
         "$t":"1"
      },
      "entry":[
         {
            "id":{
               "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/cokwr"
            },
            "updated":{
               "$t":"2006-11-30T05:44:34.623Z"
            },
            "category":[
               {
                  "scheme":"http://schemas.google.com/spreadsheets/2006",
                  "term":"http://schemas.google.com/spreadsheets/2006#list"
               }
            ],
            "title":{
               "type":"text",
               "$t":"Bingley"
            },
            "content":{
               "type":"text",
               "$t":"hours: 10, items: 2, ipm: 0.003333333333333"
            },
            "link":[
               {
                  "rel":"self",
                  "type":"application/atom+xml",
                  "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/cokwr"
               }
            ],
            "gsx$name":{
               "$t":"Bingley"
            },
            "gsx$hours":{
               "$t":"10"
            },
            "gsx$items":{
               "$t":"2"
            },
            "gsx$ipm":{
               "$t":"0.003333333333333"
            }
         },
         {
            "id":{
               "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/cpzh4"
            },
            "updated":{
               "$t":"2006-11-30T05:44:34.623Z"
            },
            "category":[
               {
                  "scheme":"http://schemas.google.com/spreadsheets/2006",
                  "term":"http://schemas.google.com/spreadsheets/2006#list"
               }
            ],
            "title":{
               "type":"text",
               "$t":"Captain Carter"
            },
            "content":{
               "type":"text",
               "$t":"hours: 200, items: 75360, ipm: 6.28"
            },
            "link":[
               {
                  "rel":"self",
                  "type":"application/atom+xml",
                  "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/cpzh4"
               }
            ],
            "gsx$name":{
               "$t":"Captain Carter"
            },
            "gsx$hours":{
               "$t":"200"
            },
            "gsx$items":{
               "$t":"75360"
            },
            "gsx$ipm":{
               "$t":"6.28"
            }
         },
         {
            "id":{
               "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/cre1l"
            },
            "updated":{
               "$t":"2006-11-30T05:44:34.623Z"
            },
            "category":[
               {
                  "scheme":"http://schemas.google.com/spreadsheets/2006",
                  "term":"http://schemas.google.com/spreadsheets/2006#list"
               }
            ],
            "title":{
               "type":"text",
               "$t":"Dawson"
            },
            "content":{
               "type":"text",
               "$t":"hours: 200, items: 100000, ipm: 8.33333333333333"
            },
            "link":[
               {
                  "rel":"self",
                  "type":"application/atom+xml",
                  "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/cre1l"
               }
            ],
            "gsx$name":{
               "$t":"Dawson"
            },
            "gsx$hours":{
               "$t":"200"
            },
            "gsx$items":{
               "$t":"100000"
            },
            "gsx$ipm":{
               "$t":"8.33333333333333"
            }
         },
         {
            "id":{
               "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/chk2m"
            },
            "updated":{
               "$t":"2006-11-30T05:44:34.623Z"
            },
            "category":[
               {
                  "scheme":"http://schemas.google.com/spreadsheets/2006",
                  "term":"http://schemas.google.com/spreadsheets/2006#list"
               }
            ],
            "title":{
               "type":"text",
               "$t":"Colonel Forster"
            },
            "content":{
               "type":"text",
               "$t":"hours: 40, items: 40, ipm: 0.016666666666667"
            },
            "link":[
               {
                  "rel":"self",
                  "type":"application/atom+xml",
                  "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/chk2m"
               }
            ],
            "gsx$name":{
               "$t":"Colonel Forster"
            },
            "gsx$hours":{
               "$t":"40"
            },
            "gsx$items":{
               "$t":"40"
            },
            "gsx$ipm":{
               "$t":"0.016666666666667"
            }
         },
         {
            "id":{
               "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/ciyn3"
            },
            "updated":{
               "$t":"2006-11-30T05:44:34.623Z"
            },
            "category":[
               {
                  "scheme":"http://schemas.google.com/spreadsheets/2006",
                  "term":"http://schemas.google.com/spreadsheets/2006#list"
               }
            ],
            "title":{
               "type":"text",
               "$t":"William Goulding"
            },
            "content":{
               "type":"text",
               "$t":"hours: 100, items: 25842, ipm: 4.307"
            },
            "link":[
               {
                  "rel":"self",
                  "type":"application/atom+xml",
                  "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/ciyn3"
               }
            ],
            "gsx$name":{
               "$t":"William Goulding"
            },
            "gsx$hours":{
               "$t":"100"
            },
            "gsx$items":{
               "$t":"25842"
            },
            "gsx$ipm":{
               "$t":"4.307"
            }
         },
         {
            "id":{
               "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/ckd7g"
            },
            "updated":{
               "$t":"2006-11-30T05:44:34.623Z"
            },
            "category":[
               {
                  "scheme":"http://schemas.google.com/spreadsheets/2006",
                  "term":"http://schemas.google.com/spreadsheets/2006#list"
               }
            ],
            "title":{
               "type":"text",
               "$t":"Lady Lucas"
            },
            "content":{
               "type":"text",
               "$t":"hours: 100, items: 25670, ipm: 4.27833333333333"
            },
            "link":[
               {
                  "rel":"self",
                  "type":"application/atom+xml",
                  "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/ckd7g"
               }
            ],
            "gsx$name":{
               "$t":"Lady Lucas"
            },
            "gsx$hours":{
               "$t":"100"
            },
            "gsx$items":{
               "$t":"25670"
            },
            "gsx$ipm":{
               "$t":"4.27833333333333"
            }
         },
         {
            "id":{
               "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/clrrx"
            },
            "updated":{
               "$t":"2006-11-30T05:44:34.623Z"
            },
            "category":[
               {
                  "scheme":"http://schemas.google.com/spreadsheets/2006",
                  "term":"http://schemas.google.com/spreadsheets/2006#list"
               }
            ],
            "title":{
               "type":"text",
               "$t":"Sir William"
            },
            "content":{
               "type":"text",
               "$t":"hours: 190, items: 98765, ipm: 8.66359649122807"
            },
            "link":[
               {
                  "rel":"self",
                  "type":"application/atom+xml",
                  "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/clrrx"
               }
            ],
            "gsx$name":{
               "$t":"Sir William"
            },
            "gsx$hours":{
               "$t":"190"
            },
            "gsx$items":{
               "$t":"98765"
            },
            "gsx$ipm":{
               "$t":"8.66359649122807"
            }
         },
         {
            "id":{
               "$t":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/cyevm"
            },
            "updated":{
               "$t":"2006-11-30T05:44:34.623Z"
            },
            "category":[
               {
                  "scheme":"http://schemas.google.com/spreadsheets/2006",
                  "term":"http://schemas.google.com/spreadsheets/2006#list"
               }
            ],
            "title":{
               "type":"text",
               "$t":"Charlotte"
            },
            "content":{
               "type":"text",
               "$t":"hours: 60, items: 18000, ipm: 5"
            },
            "link":[
               {
                  "rel":"self",
                  "type":"application/atom+xml",
                  "href":"https://spreadsheets.google.com/feeds/list/o13394135408524254648.240766968415752635/od6/public/values/cyevm"
               }
            ],
            "gsx$name":{
               "$t":"Charlotte"
            },
            "gsx$hours":{
               "$t":"60"
            },
            "gsx$items":{
               "$t":"18000"
            },
            "gsx$ipm":{
               "$t":"5"
            }
         }
      ]
   }
}

```

After (using Doxy):
```json
[
  {
    "IPM":"0.003333333333333",
    "Name":"Bingley",
    "Hours":"10",
    "Items":"2"
  },
  {
    "IPM":"6.28",
    "Name":"Captain Carter",
    "Hours":"200",
    "Items":"75360"
  },
  {
    "IPM":"8.33333333333333",
    "Name":"Dawson",
    "Hours":"200",
    "Items":"100000"
  },
  {
    "IPM":"0.016666666666667",
    "Name":"Colonel Forster",
    "Hours":"40",
    "Items":"40"
  },
  {
    "IPM":"4.307",
    "Name":"William Goulding",
    "Hours":"100",
    "Items":"25842"
  },
  {
    "IPM":"4.27833333333333",
    "Name":"Lady Lucas",
    "Hours":"100",
    "Items":"25670"
  },
  {
    "IPM":"8.66359649122807",
    "Name":"Sir William",
    "Hours":"190",
    "Items":"98765"
  },
  {
    "IPM":"5",
    "Name":"Charlotte",
    "Hours":"60",
    "Items":"18000"
  }
]
```


Instructions
------------

First, you'll need to clone the repo.

    $ git clone git@github.com:r4vi/doxy.git
    $ cd doxy

Second, let's download `pip`, `virtualenv`, `foreman`, and the [`heroku`
Ruby gem](http://devcenter.heroku.com/articles/using-the-cli).

    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ sudo gem install foreman heroku

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate


Installing Packages
--------------------

### Gevent

To use `gevent`, we'll need to install `libevent` for the
`gevent` production server. If you're operating on a Linux OS, you can
`apt-get install libevent-dev`. If you're using Mac OS X, consider
installing the [homebrew](http://mxcl.github.com/homebrew/) package
manager, and run the following command:

    $ brew install libevent

If you're using Mac OS X, you can also install `libevent` through [a DMG
available on Rudix](http://rudix.org/packages-jkl.html#libevent).


### Without Gevent

If you'd rather use `gunicorn` without `gevent`, you just need to edit
the `Procfile` and `requirements.txt`.

First, edit the `Procfile` to look the following:

    web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app

Second, remove `gevent` from the `requirements.txt` file.

### pip

Then, let's get the requirements installed in your isolated test
environment.

    $ pip install -r requirements.txt


Running Your Application
------------------------

Now, you can run the application locally.

    $ foreman start

You can also specify what port you'd prefer to use.

    $ foreman start -p 5555


Deploying
---------

If you haven't [signed up for Heroku](https://api.heroku.com/signup), go
ahead and do that. You should then be able to [add your SSH key to
Heroku](http://devcenter.heroku.com/articles/quickstart), and also
`heroku login` from the commandline.

Now, to upload your application, you'll first need to do the
following -- and obviously change `app_name` to the name of your
application:

    $ heroku create app_name -s cedar

And, then you can push your application up to Heroku.

    $ git push heroku master
    $ heroku scale web=1

Finally, we can make sure the application is up and running.

    $ heroku ps

Now, we can view the application in our web browser.

    $ heroku open

And, to deactivate `virtualenv` (once you've finished coding), you
simply run the following command:

    $ deactivate



Reactivating the Virtual Environment
------------------------------------

If you haven't worked with `virtualenv` before, you'll need to
reactivate the environment everytime you close or reload your terminal.

    $ source env/bin/activate

If you don't reactivate the environment, then you'll probably receive a
screen full of errors when trying to run the application locally.


Adding Requirements
-------------------

In the course of creating your application, you may find yourself
installing various Python modules with `pip` -- in which case you'll
need to update the `requirements.txt` file. One way that this can be
done is with `pip freeze`.

    $ pip freeze > requirements.txt


Custom Domains
--------------

If your account is verified -- and your credit card is on file -- you
can also easily add a custom domain to your application.

    $ heroku addons:add custom_domains
    $ heroku domains:add www.mydomainname.com

You can add a [naked domain
name](http://devcenter.heroku.com/articles/custom-domains), too.

    $ heroku domains:add mydomainname.com

Lastly, add the following A records to your DNS management tool.

    75.101.163.44
    75.101.145.87
    174.129.212.2
