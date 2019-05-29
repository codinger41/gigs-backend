
Gigs backend
================================

This project was built with Graphene, Flask and MongoEngine.

Getting started
---------------

First you'll need to get the source of the project. Do this by cloning the repository:

```bash
git clone git@github.com:leksyib/gigs-backend.git
cd gigs-backend
```

It is good idea (but not required) to create a virtual environment
for this project. We'll do this using
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
to keep things simple,
but you may also find something like
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
to be useful:

```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```

- Make a `.env` file, fill it with details from the `.env.sample` file.

Now the following command will setup the database, and start the server:

```bash
python app.py

```


Now head on over to
[http://127.0.0.1:5000/graphql](http://127.0.0.1:5000/graphql)
and run some queries!
