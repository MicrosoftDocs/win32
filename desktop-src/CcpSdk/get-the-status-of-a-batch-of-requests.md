---
Description: 'Gets the status of a batch of SOA requests.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'E97CE351-57F6-438D-87AC-FD759FF4C5D7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Get Request Status
---

# Get Request Status

Gets the status of a batch of SOA requests.

## Request

You can specify the Get Request Status request as follows.



| Method                     | Request URI                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------|
| GET (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/session/*session\_identifier*/batch/*batch\_name*/Status |
| GET (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/session/*session\_identifier*/batch/*batch\_name*/Status                      |



 

For sessions that are managed by the Azure HPC Scheduler, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

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

-   Pack

All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The response body consists of a single numeric value that corresponds to a member of the [BrokerClientStatus](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.interface.brokerclientstatus.aspx) enumeration, if the value of the Accept request header is application\\json. The following table shows how the numeric values correspond to the members of the [BrokerClientStatus](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.interface.brokerclientstatus.aspx) enumeration.

| Value | Corresponding BrokerClientStatus member |
|-------|-----------------------------------------|
| 0     | Unknown<br/>                      |
| 1     | Ready<br/>                        |
| 2     | Processing<br/>                   |
| 3     | Finished<br/>                     |



 

The response body consists of a single BrokerClientStatus XML element that contains a member of the [BrokerClientStatus](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.interface.brokerclientstatus.aspx) enumeration, if the value of the Accept request header is application\\xml.

## Remarks

This operation is supported only for sessions that are managed by the Azure HPC Scheduler.

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP3, or a later version of HPC Pack.<br/> |



 

 




