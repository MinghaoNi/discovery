# API Reference

[API Reference from IBM](https://www.ibm.com/watson/developercloud/discovery/api/v1/)

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


**RESPONSE**

