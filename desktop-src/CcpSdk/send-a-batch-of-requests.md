---
Description: 'Sends a batch of SOA requests to the SOA service that you specified when you created the session.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1E2E94E5-473E-4693-A35D-9D33AC7366A9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Send Requests
---

# Send Requests

Sends a batch of SOA requests to the SOA service that you specified when you created the session.

## Request

You can specify the Send Requests request as follows.



| Method                      | Request URI                                                                                                         |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------|
| POST (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Session/*session\_identifier*/batch/*batch\_name* |
| POST (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Session/*session\_identifier*/batch/*batch\_name*                      |



 

For sessions that are managed by the Azure HPC Scheduler, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for the HPC cluster, use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI. 

| Parameter      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| genericservice | Optional. Indicates whether the service to which you want to send the SOA requests is a generic service. A generic service implements the http://hpc.microsoft.com/GenericService/IGenericService/GenericOperation action and the http://hpc.microsoft.com/GenericService/IGenericService/GenericOperationResponse reply action. These actions are used to process the SOA requests and generate SOA responses.<br/> True indicates that you want to send the SOA requests to a generic service. False indicates that you want to send the SOA requests to a service that is not a generic service.<br/> The default value is false.<br/>                                                                              |
| commit         | Optional. Indicates whether the SOA requests that you send with this operation are the final SOA requests that you will send for the batch, and whether the broker should commit all of the SOA requests for the batch.<br/> True indicates that the SOA requests you send with this operation are the final SOA requests for the batch,and that the broker should commit all of the SOA requests for the batch. False indicates that the SOA requests you send with this operation are not the final SOA requests for the batch, and that the broker should not commit all of the SOA requests for the batch. See the [**Indicate the End of Requests**](indicate-the-end-of-requests.md) topic for more information.<br/> |
| api-version    | Required if the request does not contain the api-version header. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/>                                                                                                                                                                                                                                                                                              |



 

### Request Headers

The following table describes required and optional request headers.



| Request Header | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version    | Required if the request does not include the api-version URI parameter. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with SP3, use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value specified in this header overrides the value specified in the api-version URI parameter if both are specified.<br/> |
| CONTENT-TYPE   | Required. Indicates type of content that the request contains. For this request, specify application/octet-stream.<br/>                                                                                                                                                                                                                                                                                                                              |
| Accept         | Optional. Specifies the type of content accepted in the response. Specify application/json to get a response body that is an object represented as text in JavaScript Object Notation (JSON), or specify application/xml to get a response body that is formatted as XML. The default value is application/xml.<br/>                                                                                                                                 |



 

### Request Body

The format of the request body depends on whether you send the SOA requests to a generic service or a service that is not a generic service.

For a generic service, the request body is a string with a format of *SOA\_request1\_input\_string*\\xffff*SOA\_request1\_user\_data*\\x0000 *SOA\_request2\_input\_string*\\xffff*SOA\_request2\_user\_data*\\x0000.... Each SOA request includes two items, an input string and user data, separated by a value of 0xFFFF. The SOA requests are separated from each other by a value of 0x0.

The input string contains the value that you want to use for the parameter of the GenericOperation action for that SOA request. The user data contains data that the service should return with the SOA response to so that the client can correlate SOA requests with SOA responses.

If you do not want to specify user data for your SOA request, you can use a format of *SOA\_request1\_input\_string*\\xffff\\x0000 *SOA\_request2\_input\_string*\\xffff\\x0000....

For a service that is not a generic service, the request body is XML that specifies a set SOAP messages that correspond to the SOA requests that you want to send. The following example shows the format of this XML request body.

``` syntax
<root_element_name>
    <s:Envelope xmlns:s=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:a=\"http://www.w3.org/2005/08/addressing\">
        <s:Header>
            <a:Action s:mustUnderstand=\"1\">http://tempuri.org/service_interface_name/service_operation_name</a:Action>
            <a:MessageID>urn:uuid:01234567-78ab-cdef-0123-456789abcdef</a:MessageID>
            <HPCPack2008_Broker_UserDataNS xmlns=\"http://www.microsoft.com/hpc\">SOA_request1_user_data</HPCPack2008_Broker_UserDataNS>
            <HPCPack2008_Broker_ClientIdNS xmlns=\"http://www.microsoft.com/hpc\">batch_name</HPCPack2008_Broker_ClientIdNS>
        </s:Header>
        <s:Body>
            <service_operation_name xmlns=\"http://tempuri.org/\">
                <operation_parameter_name>SOA_request1_input_string</operation_parameter_name>
            </service_operation_name>
        </s:Body>
    </s:Envelope>
    <s:Envelope xmlns:s=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:a=\"http://www.w3.org/2005/08/addressing\">
        <s:Header>
            <a:Action s:mustUnderstand=\"1\">http://tempuri.org/service_interface_name/service_operation_name</a:Action>
            <a:MessageID>urn:uuid:fedcba98-7654-3210-fedc-ba9876543210</a:MessageID>
            <HPCPack2008_Broker_UserDataNS xmlns=\"http://www.microsoft.com/hpc\">SOA_request2_user_data</HPCPack2008_Broker_UserDataNS>
            <HPCPack2008_Broker_ClientIdNS xmlns=\"http://www.microsoft.com/hpc\">batch_name</HPCPack2008_Broker_ClientIdNS>
        </s:Header>
        <s:Body>
            <service_operation_name xmlns=\"http://tempuri.org/\">
                <operation_parameter_name>SOA_request2_input_string</operation_parameter_name>
            </service_operation_name>
        </s:Body>
    </s:Envelope>
    ...
</root_element_name>
```

The following table describes the elements of this XML request.



| Element                         | Description                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *root\_element\_name*           | Contains a set of SOAP messages that correspond to the SOA requests that you want to send. You can use any name for this element.<br/>                                                                                                                                                                                                                                                            |
| Envelope                        | Contains a SOAP message that corresponds to one of the SOA requests that you want to send.<br/>                                                                                                                                                                                                                                                                                                   |
| Header                          | Contains the header information for the SOAP message.<br/>                                                                                                                                                                                                                                                                                                                                        |
| Action                          | Specifies the action to use to process this SOA request.<br/> The *service\_interface\_name* part of this value should correspond to the name of the interface for the service that includes the ServiceContract attribute. The *service\_operation\_name* part of this value should correspond to the name of a method for the service that includes the OperationContract attribute.<br/> |
| MessageId                       | Optional. Contains a string that represents the universally unique identifier (UUID) for the message as a uniform resource name (URN).<br/>                                                                                                                                                                                                                                                       |
| HPCPack2008\_Broker\_UserDataNS | Optional. Specifies the data that the service should return with the SOA response to so that the client can correlate SOA requests with SOA responses.<br/>                                                                                                                                                                                                                                       |
| HPCPack2008\_Broker\_ClientIdNS | Optional. Specifies the name of the batch of SOA requests to which the SOA request belongs.<br/>                                                                                                                                                                                                                                                                                                  |
| Body                            | Contains the body of the SOAP message.<br/>                                                                                                                                                                                                                                                                                                                                                       |
| *service\_operation\_name*      | Specifies the operation that you want service to perform for the SOA request. The name of this element should correspond to the name of a method for the service that has the OperationContract attribute.<br/>                                                                                                                                                                                   |
| *operation\_parameter\_name*    | Specifies the value that you want to use for this SOA request for the parameter of the method to which the *service\_operation\_name* corresponds. The name of this element should correspond to the name of the parameter for that method.<br/>                                                                                                                                                  |



 

## Response

The response includes an HTTP status code and a set of response headers.

### Status Code

A successful operation returns status code 200 (OK), if you specified a value of false for the *commit* URI parameter. A successful operation returns status code 201 (Created) if you specified a value of true for the *commit* URI parameter.

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

Before you can send SOA requests to a service, you must create a session for that service with the [**Create Session**](create-session.md) operation. To get the responses to the requests, use the [**Get Responses**](get-all-repsonses-to-a-batch-of-requests.md) operation.

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP3, or a later version of HPC Pack.<br/> |



 

 




