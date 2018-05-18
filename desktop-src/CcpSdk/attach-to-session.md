---
Description: 'Connects to an existing SOA session.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '36E7EA7D-7EB7-4D3E-87DA-04819894316A'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Attach to Session
---

# Attach to Session

Connects to an existing SOA session.

## Request

You can specify the Attach Session request as follows.



| Method                     | Request URI                                                                                            |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| GET (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHpc/*HPC\_cluster\_name*/Session/*session\_identifier*/Attach |
| GET (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHpc/Session/*session\_identifier*/Attach                      |



 

For sessions that are managed by the Azure HPC Scheduler, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for the HPC cluster, use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| durable     | Required. Specifies whether the session is a durable session or an interactive session. True indicates that the session is a durable session. False indicates that the session is an interactive session. When connecting to sessions that are managed by the Azure HPC Scheduler, specify false, because durable sessions are not supported for the Azure HPC Scheduler.<br/>                                                        |
| api-version | Required if the request does not contain the api-version header. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/> |



 

### Request Headers

The following table describes required and optional request headers.



| Request Header | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version    | Required if the request does not include the api-version URI parameter. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with SP3, use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value specified in this header overrides the value specified in the api-version URI parameter if both are specified.<br/> |
| Accept         | Optional. Specifies the type of content accepted in the response. Specify application/json to get a response body that is an object represented as text in JavaScript Object Notation (JSON), or specify application/xml to get a response body that is formatted as XML. The default value is application/xml.<br/>                                                                                                                                 |



 

### Request Body

None.

## Response

The response includes an HTTP status code, a set of response headers, and a response body.

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

-   Transfer-Encoding

-   Content-Type

-   Date

-   Server

All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The response body is an object specified as JSON text if the value of the Accept request header was application/json. This text has the following format: {"BrokerNode":*node\_name*,"Id":*session\_identifier*,"IsDurable":\[true\|false\],"MaxMessageSize":*size*,"ServiceOperationTimeout":*duration*,"ServiceVersion":*version*}

The response body is formatted as XML if the value of the Accept request header was application/xml. This text has the following format:

``` syntax
<WebSessionInfo xmlns="http://hpc.microsoft.com/" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
    <BrokerNode>node_name</BrokerNode>
    <Id>session_identifier</Id>
    <IsDurable>[true|false]</IsDurable>
    <MaxMessageSize>size</MaxMessageSize>
    <ServiceOperationTimeout>duration</ServiceOperationTimeout>
    <ServiceVersion xmlns:a="http://schemas.datacontract.org/2004/07/System"/>version</ServiceVersion>
</WebSessionInfo>
```

The following table describes each of the items in the response string.



| Item                   | Description                                                                                                                                                                                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BrokerNode             | The name of the broker node for the session. For sessions that are managed by the Azure HPC Scheduler, this name has a format of *Windows\_Azure\_service\_name*.cloudapp.net.<br/>                                                                             |
| Id                     | The session identifier for the session.<br/>                                                                                                                                                                                                                    |
| IsDurable              | A value that indicates whether the session is a durable session or an interactive session. True indicates a durable session. False indicates an interactive session. For sessions that are managed by the Azure HPC Scheduler, this value is always false.<br/> |
| MaxMessageSize         | The maximum size in bytes of a SOA request or SOA response message for the session.<br/>                                                                                                                                                                        |
| SeviceOperationTimeout | The amount of time in milliseconds that the SOA service tries to perform operations before timing out.<br/>                                                                                                                                                     |
| ServiceVersion         | The version of the service to which the session connected. A value of null indicates that the configuration file for the service that does not specify version information.<br/>                                                                                |



 

## Remarks

This operation is supported only for sessions that are managed by the Azure HPC Scheduler.

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP3, or a later version of HPC Pack.<br/> |



 

 




