---
Description: 'Creates a new job on the HPC cluster by using the information in the specified job XML string.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'B9C6AC15-DA5D-421D-B3C9-F51B88A39622'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Create Job From XML
---

# Create Job From XML

Creates a new job on the HPC cluster by using the information in the specified job XML string.

## Request

You can specify the Create Job From XML request as follows.



| Method                      | Request URI                                                                   |
|-----------------------------|-------------------------------------------------------------------------------|
| POST (before HPC Pack 2016) | http://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Jobs/JobFile |
| POST (HPC Pack 2016)        | http://*head\_node\_name*:*port*/WindowsHPC/Jobs/JobFile                      |



 

For instances of the REST web service that are hosted in Azure, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for an HPC cluster that runs at least Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version | Optional. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this URI parameter is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/> |



 

### Request Headers

The following table describes required and optional request headers.



| Request Header | Description                                                                                                                                                                                                                                                                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version    | Optional. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with SP3, use a value of 2011-11-01. The minimum version that supports this header is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value specified in this header overrides the value specified in the api-version URI parameter if both are specified.<br/> |
| CCP\_Version   | Optional. Specifies the version of the operation to use for this request.<br/> Deprecated beginning with Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3).<br/>                                                                                                                                                                                                           |



 

### Request Body

The following example shows sample job XML. For more information about the information in job XML files, see [Job Schema](jobschema-schema.md).


```XML
<Job Version="3.000" Id="115" State="Configuring" CreateTime="2010/12/7 23:18:20" IsExclusive="false" RunUntilCanceled="false" UnitType="Core" Owner="CONTOSO\someone" UserName="" Project="" JobType="Batch" JobTemplate="Default" Priority="Normal" OrderBy=""
  RequeueCount="0" AutoRequeueCount="0" PendingReason="None" AutoCalculateMax="true" AutoCalculateMin="true" FailOnTaskFailure="false" Progress="0" ProgressMessage="" MinCores="1" MaxCores="1" NotifyOnStart="false" NotifyOnCompletion="false" 
  xmlns="http://schemas.microsoft.com/HPCS2008R2/scheduler/">
    <Dependencies />
    <Tasks>
        <Task Version="3.000" Id="161" ParentJobId="115" State="Configuring" UnitType="Core" NiceId="1" CommandLine="dir" RequeueCount="0" PendingReason="None" StartValue="0" EndValue="0" IncrementValue="1" GroupId="117" CreateTime="2010/12/7 23:18:20" MinCores="1" 
          MaxCores="1" AutoRequeueCount="0" Type="Basic" FailJobOnFailure="false" /> 
        <Task … />
    </Tasks>
</Job>
```



## Response

The response includes an HTTP status code, a set of response headers, and a response body in XML format.

### Status Code

A successful operation returns status code 200 (OK). For more information about status codes, see [HttpStatusCode](https://msdn.microsoft.com/library/system.net.httpstatuscode.aspx).

The error response is dependent upon the api-version used in the request. If the api-version is not provided, or CCP\_Version is specified, then the error response will be an XML string (Note: The error message will vary based on the error):


```XML
<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">Error message text.</string>
```



If the api-version is 2011-11-01 or later, the error message will be a more descriptive XML response (Note: Values will vary based on the error):


```XML
<HpcWebServiceFault xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
  <Code>267386880</Code>
  <Message>Error message text.</Message>
  <Values i:nil="true" xmlns:a="http://schemas.datacontract.org/2004/07/System.Collections.Generic"/>
</HpcWebServiceFault>
```



### Response Headers

The response for this operation includes the following headers.



| Response Header         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| x-ms-hpc-authoritychain | A comma-separated list of RFC 1918 IP addresses that indicate the sequence of instances of the REST web service that the operation called in order from to right.<br/> Only responses from instances of the REST web service that are hosted on Azure contain this header. Responses from instances of the REST web service that are hosted on premise omit this header.<br/> This header is supported beginning with Microsoft HPC Pack 2008 R2 with SP3 and is not available in previous versions.<br/> |



 

The response for this operation also includes standard HTTP headers. All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The format of the response body is as follows.


```XML
<int xmlns="http://schemas.microsoft.com/2003/10/Serialization/">Job Identifier</int>
```



The response XML consists of a single int element that contains the job identifier of the job that the HPC Job Scheduler Service created.

## Remarks

To get the job XML for an existing job, use the [**Get Job**](schedulerwebservice--getjob.md) operation with the render URI parameter set to HpcJobXml. You can then create a copy of that existing job by using the response XML from the Get Job operation as the request XML for the Create Job from XML operation.

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP2, or a later version of HPC Pack.<br/> |



 

 




