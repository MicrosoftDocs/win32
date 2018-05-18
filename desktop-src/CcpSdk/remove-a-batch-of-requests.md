---
Description: 'Deletes a batch of SOA requests that you previously sent.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1139E3C1-D109-4742-97B7-B563533810D6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Delete Requests
---

# Delete Requests

Deletes a batch of SOA requests that you previously sent.

## Request

You can specify the Delete Requests request as follows.



| Method                      | Request URI                                                                                                               |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| POST (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHpc/*HPC\_cluster\_name*/session/*session\_identifier*/batch/*batch\_name*/Purge |
| POST (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHpc/session/*session\_identifier*/batch/*batch\_name*/Purge                      |



 

For sessions that are managed by the Azure HPC Scheduler, the head node name should have a format of *Azure\_service\_name*.cloudapp.net.

To get the name to use for the HPC cluster, use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version | Required if the request does not contain the api-version header. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/> |



 

### Request Headers

The following table describes required and optional request headers.



| Request Header | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version    | Required if the request does not include the api-version URI parameter. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with SP3, use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value specified in this header overrides the value specified in the api-version URI parameter if both are specified.<br/> |
| CONTENT-TYPE   | Indicates the type of content that the request contains.<br/>                                                                                                                                                                                                                                                                                                                                                                                        |
| Content-Length | Required. Indicates the length of the request body. Specify 0 for this request.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| Accept         | Optional. Specifies the type of content accepted in the response. Specify application/json to get a response body that is an object represented as text in JavaScript Object Notation (JSON), or specify application/xml to get a response body that is formatted as XML. The default value is application/xml.<br/>                                                                                                                                 |



 

### Request Body

None.

## Response

The response includes an HTTP status code and a set of response headers.

### Status Code

A successful operation returns status code 200 (OK).

If the request includes neither the api-version URI parameter nor the api-version header, the operation returns status code 400 (Bad Request).

For more information about status codes, see [HttpStatusCode](https://msdn.microsoft.com/library/system.net.httpstatuscode.aspx).

The error response will be contained in a descriptive XML response (Note: Values will vary based on the error):


```XML
<HpcWebServiceFault xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
  <Code>267386880</Code>
  <Message>Error message text.</Message>
  <Values i:nil="true" xmlns:a="http://schemas.datacontract.org/2004/07/System.Collections.Generic"/>
</HpcWebServiceFault>
```



### Response Headers

The response for this operation includes the following standard HTTP headers:

-   Content-Length

-   Date

-   Pack

All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

None.

## Remarks

This operation is supported only for sessions that are managed by the Azure HPC Scheduler.

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP3, or a later version of HPC Pack.<br/> |



 

 




