# D-SNAP Rules
[![CircleCI](https://circleci.com/gh/18F/dsnap_rules.svg?style=svg)](https://circleci.com/gh/18F/dsnap_rules)

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.

## Development

### Installation

Install project dependencies using:
```
pipenv install
```
Once the dependencies have been installed, you can run the rest of the commands by dropping into a virtual environment shell by running `pipenv shell`, or by preceding each command with a `pipenv run`.

### Testing

Run tests using:
```
pytest
```

### Deployment

The project has been set up for continuous integration and deployment through CirclCI and cloud.gov. The cloud.gov spaces, URLs and deployment triggers are:

| Space | URL | Deployment trigger |
|-------|-----|--------------------|
| dev   | https://dsnap-rules-dev.app.cloud.gov | Any push to a branch other than `master`|
| staging   | https://dsnap-rules-staging.app.cloud.gov | Any push to `master`|
| prod   | https://dsnap-rules.app.cloud.gov | Any tag push with a tag that begins with 'v'|
| demo   | https://dsnap-rules-demo.app.cloud.gov | Any tag push with a tag that begins with 'v'|

#### Testing the demo application
A demo version of the application has been deployed in cloud.gov and is available at https://dsnap-rules-demo.app.cloud.gov.

The `examples` directory has examples for eligible, ineligible and invalid payloads.

Submit examples from the directory `examples`. E.g.,
```
curl -X POST -d @examples/eligible_request.json https://dsnap-rules-demo.app.cloud.gov
```

In addition, there is a quick-and-dirty [form](https://dsnap-rules-demo.app.cloud.gov) that can be used to test the application.

### Running locally
Create a local PostgreSQL database. Set the environment variable DATABASE_URL to point to this database, e.g.:
```
export DATABASE_URL=postgresql:///dsnap
```
If this variable is not set, it defaults to `postgresql:///dsnap` in development/local environments.

Migrate the database, if necessary, using:
```
python manage.py migrate
```
Load fixture data for disasters, using:
```
python manage.py loaddata dsnap_rules/fixtures/disaster.json
```
Alternatively, data can be loaded using the Django admin app, described below.

Start the app using:
```
python manage.py runserver
```

This will make the application available at `http://localhost:8000`, by default. To change the port and other settings, see https://docs.djangoproject.com/en/2.1/ref/django-admin/#runserver.

## Admin app
To use the admin app, create admin users using:
```
python manage.py createsuperuser
```
Access the admin app at {deployment_url}/admin and authenticate using the admin userid and password created.

## Endpoints

| URL         | Verb     | Description
|-------------|----------|--------------------|
| /           | POST     | The main rules service endpoint for submitting requests and executing the rules |
| /           | GET      | Quick and dirty form for demo purposes |
| /disasters  | GET      | Returns the active disasters, i.e., those with registration periods that span today's date |
| /admin      | GET/POST | Django Admin interface for CRUD operations on disasters |
