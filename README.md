# Add Training Data into Discovery

[Tutorial: Migrating from Retrieve and Rank](https://console.bluemix.net/docs/services/discovery/migrate-rnr-tut.html#adding-training-data-into-discovery)

# API Reference

**API Reference from IBM**

https://www.ibm.com/watson/developercloud/discovery/api/v1/)

**Python Module**

https://pypi.python.org/pypi/watson-developer-cloud

## Environments

### list environments

> GET /v1/environments
**REQUEST**

```bash
curl -u "{username}":"{password}" "https://gateway.watsonplatform.net/discovery/api/v1/environments?version=2017-09-01"
```
**RESPONSE**

```json
{
  "environments" : [ {
    "environment_id" : "system",
    "name" : "Watson System Environment",
    "description" : "Shared system data sources",
    "read_only" : true
  }, {
    "environment_id" : "af3e2cb0-4fee-419a-933c-256a0d473266",
    "name" : "byod",
    "description" : "",
    "created" : "2017-10-13T05:27:43.493Z",
    "updated" : "2017-10-13T05:27:43.493Z",
    "read_only" : false
  } ]
}
```

## Configurations

### list configurations

> GET /v1/environments/{environment_id}/configurations

**REQUEST**

```bash
curl -u "{username}":"{password}" "https://gateway.watsonplatform.net/discovery/api/v1/environments/{environment_id}/configurations?version=2017-09-01"
```

**RESPONSE**

```json
{
  "configurations": [
    {
      "configuration_id": "b8b3a927-b9de-4e03-85e9-0df98ca44342",
      "name": "Default Configuration",
      "description": "The configuration used by default when creating a new collection without specifying a configuration_id.",
      "created": "2017-10-13T05:27:43.537Z",
      "updated": "2017-10-13T05:27:43.537Z"
    },
    {
      "configuration_id": "551a3bcf-d043-49fe-924b-bf5d86a67820",
      "name": "Japanese-csv",
      "description": null,
      "created": "2017-10-13T05:28:33.170Z",
      "updated": "2017-10-13T05:35:57.496Z"
    }
  ]
}
```

## Collections

### list collections

> GET /v1/environments/{environment_id}/collections

**REQUEST**

```bash
curl -u "{username}":"{password}" "https://gateway.watsonplatform.net/discovery/api/v1/environments/{environment_id}/collections?version=2017-09-01"
```

**RESPONSE**

```json
{
  "collections" : [ {
    "collection_id" : "6072d7a3-91cb-4bbb-b6eb-597916af93c4",
    "name" : "japanese-collection",
    "configuration_id" : "551a3bcf-d043-49fe-924b-bf5d86a67820",
    "language" : "ja",
    "status" : "active",
    "description" : "",
    "created" : "2017-10-13T05:28:04.516Z",
    "updated" : "2017-10-13T05:28:33.988Z"
  } ]
}
```

### list collection details

> GET /v1/environments/{environment\_id}/collections/{collection_id}

**REQUEST**

```bash
curl -u "{username}":"{password}" "https://gateway.watsonplatform.net/discovery/api/v1/environments/{environment_id}/collections/{collection_id}?version=2017-09-01"
```

**RESPONSE**

```json
{
  "collection_id" : "6072d7a3-91cb-4bbb-b6eb-597916af93c4",
  "name" : "japanese-collection",
  "configuration_id" : "551a3bcf-d043-49fe-924b-bf5d86a67820",
  "language" : "ja",
  "status" : "active",
  "description" : "",
  "created" : "2017-10-13T05:28:04.516Z",
  "updated" : "2017-10-13T05:28:33.988Z",
  "document_counts" : {
    "available" : 2,
    "processing" : 0,
    "failed" : 1
  },
  "disk_usage" : {
    "used_bytes" : 19515156
  },
  "training_status" : {
    "data_updated" : "",
    "total_examples" : 0,
    "sufficient_label_diversity" : false,
    "processing" : false,
    "minimum_examples_added" : false,
    "successfully_trained" : "",
    "available" : false,
    "notices" : 0,
    "minimum_queries_added" : false
  }
}
```

## Documents

### list document details

> GET /v1/environments/{environment\_id}/collections/{collection\_id}/documents/{document_id}

**The document ids only can get from tooling by "View data schema", no API?!**

**REQUEST**

```bash
curl -u "{username}":"{password}" "https://gateway.watsonplatform.net/discovery/api/v1/environments/{environment_id}/collections/{collection_id}/documents/{document_id}?version=2017-09-01"
```

**RESPONSE**

```json
{
  "document_id": "84667fd2b7c9be9ee62f84fd904a9cc5",
  "notices": [
    {
      "notice_id": "index_failed_cluster_unavailable",
      "created": "2017-10-13T06:03:26.316Z",
      "document_id": "84667fd2b7c9be9ee62f84fd904a9cc5",
      "severity": "error",
      "step": "indexing",
      "description": "Failed to index document because cluster was not available."
    }
  ],
  "status": "available with notices",
  "status_description": "Document is successfully ingested and indexed, but with some warnings",
  "filename": "20160719-RR_index.html20171013-6-rl4jel.html",
  "file_type": "html",
  "sha1": "cfd437fe788259a25debc85edf5ea18a14b6704c"
}
```

### delete a document

> DELETE /v1/environments/{environment\_id}/collections/{collection\_id}/documents/{document_id}

**REQUEST**

```bash
curl -X DELETE -u "{username}":"{password}" "https://gateway.watsonplatform.net/discovery/api/v1/environments/{environment_id}/collections/{collection_id}/documents/{document_id}?version=2017-09-01"
```

**RESPONSE**

```json
{
  "document_id": "84667fd2b7c9be9ee62f84fd904a9cc5",
  "status": "deleted"
}
```

