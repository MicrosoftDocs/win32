---
Description: 'Gets the responses that the service-oriented architecture (SOA) service returned for the SOA requests in the specified batch.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '091F2D66-AA26-4AA4-8BDD-F3FCF30288C2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Get Responses
---

# Get Responses

Gets the responses that the service-oriented architecture (SOA) service returned for the SOA requests in the specified batch.

## Request

You can specify the Get Responses request as follows.



| Method                      | Request URI                                                                                                                  |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|
| POST (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Session/*session\_identifier*/batch/*batch\_name*/Response |
| POST (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Session/*session\_identifier*/batch/*batch\_name*/Response                      |



 

For sessions that are managed by the Azure HPC Scheduler, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for the HPC cluster, use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| genericservice | Optional. Indicates whether the service from which you want to get the SOA responses is a generic service. A generic service implements the http://hpc.microsoft.com/GenericService/IGenericService/GenericOperation action and the http://hpc.microsoft.com/GenericService/IGenericService/GenericOperationResponse reply action. These actions are used to process the SOA requests and generate SOA responses.<br/> True indicates that you want to get the SOA responses from a generic service. False indicates that you want to get the SOA responses from a service that is not a generic service.<br/> The default value is false.<br/>                                                                                                                                                                             |
| count          | Optional. Specifies the number of SOA responses that you want to get. Specify -1 to get all of the SOA responses. The default value is -1.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| action         | Optional. Specifies the action for which you want to get SOA responses. If the SOA service supports more than one action, this parameter allows you to get the SOA responses to SOA requests for the specified action.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| reset          | Optional. Specifies whether to return the response cursor to the beginning of the SOA response queue instead of leaving the response cursor after the last SOA response returned by the previous Get Responses operation, and whether to delete the SOA responses that the previous operation already returned if the session is an interactive session.<br/> True indicates that you want to return the response cursor to the beginning of the SOA response queue, and that you do not want to delete the SOA responses that the previous Get Responses operation returned. False indicates that you want to leave the response cursor after the last SOA responses returned by the previous Get Responses operation, and that you do want to delete the SOA responses that the previous Get Responses operation returned.<br/> |
| api-version    | Required if the request does not contain the api-version header. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/>                                                                                                                                                                                                                                                                                                                                                                                                   |



 

### Request Headers

The following table describes required and optional request headers.



| Request Header | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version    | Required if the request does not include the api-version URI parameter. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with SP3, use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value specified in this header overrides the value specified in the api-version URI parameter if both are specified.<br/> |
| CONTENT-TYPE   | Indicates type of content that the request contains.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| Content-Length | Required. Indicates the length of the request body. Specify 0 for this request.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| Accept         | Optional. Specifies the type of content accepted in the response. Specify application/json to get a response body that is an object represented as text in JavaScript Object Notation (JSON), or specify application/xml to get a response body that is formatted as XML. Currently, JSON responses are only implemented for error messages. The default value is application/xml.<br/>                                                              |



 

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

The format of the response body depends on whether you get the SOA responses from a generic service or a service that is not a generic service.

For a generic service, the response body is a string with a format of *SOA\_response1\_action*\\xffff*SOA\_response1\_output\_string*\\xffff*SOA\_response1\_user\_data*\\x0000*SOA\_response2\_action*\\xffff*SOA\_response2\_output\_string*\\xffff*SOA\_response2\_user\_data*\\x0000...http://hpc.microsoft.com/EndOfGetResponse\\xffff*number\_of\_responses*\\xffff*reason\_responses\_ended*\\x0000. Each SOA response includes three items: the action, the output string, and user data. The three parts of the SOA response are separated by a value of 0xFFFF. The SOA responses are separated from each other by a value of 0x0.

The action portion of the SOA response string indicates the reply action that generated the SOA response. The output string contains the value that was generated by processing the SOA request. The user data contains data that you sent with the SOA request so that you could correlate SOA requests with SOA responses.

If you did not specify user data for your SOA request, the format of the response body is *SOA\_response1\_action*\\xffff*SOA\_response1\_output\_string*\\xffff\\x0000*SOA\_response2\_action*\\xffff*SOA\_response2\_output\_string*\\xffff\\x0000...http://hpc.microsoft.com/EndOfGetResponse\\xffff*number\_of\_responses*\\xffff*reason\_responses\_ended*\\x0000.

For a service that is not a generic service, the response body is XML that contains a set SOAP messages that correspond to the SOA responses. The following example shows the format of this XML response body.

``` syntax
<HPCPack2008_WebAPI_MessageArray>
    <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing">
        <s:Header>
            <a:Action s:mustUnderstand="1">http://tempuri.org/service_interface_name/service_reply_action_name</a:Action>
            <a:RelatesTo>urn:uuid:b1cc0d55-db71-4379-a3df-a2c42c28573d</a:RelatesTo>
            <a:To s:mustUnderstand="1">http://www.w3.org/2005/08/addressing/anonymous</a:To>
            <HPCPack2008_Broker_RequestActionNS xmlns="http://www.microsoft.com/hpc">http://tempuri.org/service_interface_name/service_operation_name</HPCPack2008_Broker_RequestActionNS>
            <HPCPack2008_Broker_UserDataNS xmlns="http://www.microsoft.com/hpc">SOA_response1_user_data</HPCPack2008_Broker_UserDataNS>
            <HPCPack2008_Broker_ResponseCallbackId xmlns="http://www.microsoft.com/hpc"/>
        </s:Header>
        <s:Body>
            <service_reply_action_name xmlns="http://tempuri.org/">
                <service_operation_nameResult>SOA_response1_output_string</service_operation_nameResult>
            </service_reply_action_name>
        </s:Body>
    </s:Envelope>
    <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing">
        <s:Header>
            <a:Action s:mustUnderstand="1">http://tempuri.org/service_interface_name/service_reply_action_name</a:Action>
            <a:RelatesTo>urn:uuid:be93034b-e28b-42cc-8338-1efbb1199aa1</a:RelatesTo>
            <a:To s:mustUnderstand="1">http://www.w3.org/2005/08/addressing/anonymous</a:To>
            <HPCPack2008_Broker_RequestActionNS xmlns="http://www.microsoft.com/hpc">http://tempuri.org/service_interface_name/service_operation_name</HPCPack2008_Broker_RequestActionNS>
            <HPCPack2008_Broker_UserDataNS xmlns="http://www.microsoft.com/hpc">SOA_response2_user_data</HPCPack2008_Broker_UserDataNS>
            <HPCPack2008_Broker_ResponseCallbackId xmlns="http://www.microsoft.com/hpc"/>
        </s:Header>
        <s:Body>
            <service_reply_action_name xmlns="http://tempuri.org/">
                <service_operation_nameResult>SOA_response2_output_string</service_operation_nameResult>
            </service_reply_action_name>
        </s:Body>
    </s:Envelope>
    ...
    <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing">
        <s:Header>
            <a:Action s:mustUnderstand="1">http://hpc.microsoft.com/EndOfGetResponse</a:Action>
            <HPCPack2008_Broker_ResponseCallbackId xmlns="http://www.microsoft.com/hpc"/>
            <a:To s:mustUnderstand="1">http://www.w3.org/2005/08/addressing/anonymous</a:To>
        </s:Header>
        <s:Body>
            <EndOfResponses xmlns="http://tempuri.org/">
                <Count>number_of_responses</Count>
                <Reason>reason_responses_ended</Reason>
            </EndOfResponses>
        </s:Body>
    </s:Envelope>
</HPCPack2008_WebAPI_MessageArray>
```

The following table describes the key elements of this XML request.



| Element                              | Description                                                                                                                                                                                                  |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HPCPack2008\_WebAPI\_MessageArray    | Contains a set of SOAP messages that correspond to the SOA responses that you received.<br/>                                                                                                           |
| Envelope                             | Contains a SOAP message that corresponds to one of the SOA responses that your received.<br/>                                                                                                          |
| Header                               | Contains the header information for the SOAP message.<br/>                                                                                                                                             |
| Action                               | Specifies the reply action that generated the SOA response.<br/>                                                                                                                                       |
| RelatesTo                            | Contains a string that represents the universally unique identifier (UUID) for the message that specified the SOA request that corresponds to this SOA response as a uniform resource name (URN).<br/> |
| HPCPack2008\_Broker\_RequestActionNS | Specifies the action that the SOA request that corresponds to this SOA response specified for processing the SOA request.<br/>                                                                         |
| HPCPack2008\_Broker\_UserDataNS      | Specifies the data that was specified with the SOA request so that you can correlate SOA requests with SOA responses.<br/>                                                                             |
| Body                                 | Contains the body of the SOAP message.<br/>                                                                                                                                                            |
| *service\_reply\_action\_name*       | Represents the SOA response.<br/>                                                                                                                                                                      |
| *service\_operation\_name*Result     | Contains output value that was generated by processing the SOA request.<br/>                                                                                                                           |
| EndOfResponses                       | Specifies that the SOAP message indicates the end of the SOA responses for the session.<br/>                                                                                                           |
| Count                                | Specifies the number of SOA responses that the operation returned.<br/>                                                                                                                                |
| Reason                               | Specifies the reason that the SOA responses for the session ended.<br/>                                                                                                                                |



 

## Remarks

This operation is supported only for sessions that are managed by the Azure HPC Scheduler.

Your application should extract the output strings in the SOA responses from the response body and present that output to the user as appropriate for your service.

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP3, or a later version of HPC Pack.<br/> |



 

 




