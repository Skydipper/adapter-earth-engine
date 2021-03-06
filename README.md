# Google Earth Engine Adapter Microservice

This repository implements the Google Earth Engine Adapter services that are available in the Skydipper API.

## Quick Overview

### Create a GEE Dataset

To create a new GEE dataset it's necessary to execute the following request.

Important:
- the connectorType value has to be "rest"
- the provider value has to be "gee"

```
POST: /dataset -> payload:
{
	"dataset": {
		"application": [<application-name>],
		"name": <dataset-name>,
		"connectorType": "rest",
		"provider": "gee",
		"tableName": <table-name>
	}
}
```

### Example (copy&paste)

```
POST: https://api.skydipper.com/dataset -> payload:
{
	"dataset": {
		"application": ["skydipper"],
		"name": "Data about whatever",
		"connectorType": "rest",
		"provider": "gee",
		"tableName": "ft:1qpKIcYQMBsXLA9RLWCaV9D0Hus2cMQHhI-ViKHo"
	}
}
```

Once the dataset has been saved (a few seconds after the creation) you can start doing queries to GEE.

### Fields

This endpoint returns the available fields in the dataset

```
GET: /fields/:dataset
```

Example (copy&paste)

```
GET: https://api.skydipper.com/fields/68353d61-0f47-4836-9699-72e008cd9f5f
```

### Query

This endpoint returns the execution of the SQL query (sql queryParam is required)

```
GET: /query/:dataset?sql=<slq_query>
```

Example (copy&paste)

```
GET: https://api.skydipper.com/query/68353d61-0f47-4836-9699-72e008cd9f5f?sql=select * from ft:1qpKIcYQMBsXLA9RLWCaV9D0Hus2cMQHhI-ViKHo where width > 100
```

### Download

Download the data in json format (csv coming soon)

```
GET: /download/:dataset?sql=<slq_query>
```

Example (copy&paste)

```
GET: https://api.skydipper.com/download/68353d61-0f47-4836-9699-72e008cd9f5f?sql=select * from ft:1qpKIcYQMBsXLA9RLWCaV9D0Hus2cMQHhI-ViKHo where width > 100
```


## Tests

As this microservice relies on Google Earth Engine, tests require a valid `storage.json` or equivalent file. 
At the time of this writing, actual tests use mock calls, so the real credential are only needed because Google's 
library actually validates the credentials on startup. 

Before you run the tests, be sure to install the necessary development libraries, using `pip install -r requirements_dev.txt`.

Actual test execution is done by running the `pytest` executable on the root of the project.  
