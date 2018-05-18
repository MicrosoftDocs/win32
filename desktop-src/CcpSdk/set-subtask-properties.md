---
Description: 'Sets the values of properties for the task that contains that specified subtask.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '438150D0-36A5-4B23-A89C-9746340CCF99'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Set Subtask Properties
---

# Set Subtask Properties

Sets the values of properties for the task that contains that specified subtask.

## Request

You can specify the Set Subtask Properties request as follows.



| Method                     | Request URI                                                                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| PUT (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Job/*job\_identifier*/Task/*task\_identifier*/SubTask/*subtask\_identifier* |
| PUT (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Job/*job\_identifier*/Task/*task\_identifier*/SubTask/*subtask\_identifier*                      |



 

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

The format of the request body is as follows.


```XML
<ArrayOfProperty xmlns="http://schemas.microsoft.com/HPCS2008R2/common">
    <Property>
        <Name>Property Name</Name> 
        <Type>Property Type</Type> 
        <Value>Property Value</Value>
    </Property>
    <Property>
        <Name>Property Name</Name> 
        <Type>Property Type</Type> 
        <Value>Property Value</Value>
    </Property>
    …
</ArrayOfProperty>
```



The following table describes each of the elements in this request XML.



| Element         | Description                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|
| ArrayOfProperty | Represents the set of properties for the subtask for which you want to set values.<br/> |
| Property        | Represents a single property for the subtask.<br/>                                      |
| Name            | Contains the name of the property that you want to set.<br/>                            |
| Type            | Optional. Contains the data type of the property that you want to set.<br/>             |
| Value           | Contains the value to which you want to set the property.<br/>                          |



 

## Response

The response includes an HTTP status code and a set of response headers.

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

None.

## Remarks

The following table shows the subtask properties for which you can get the values. For information about the property, including the versions of Microsoft HPC Pack that support it, see the corresponding property of the ISchedulerTask interface in the managed API for Microsoft HPC Pack.



| Property              | Corresponding ISchedulerTask Property                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                  | [ISchedulerTask.Name](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.name.aspx)                                     |
| MinCores              | [ISchedulerTask.MinimumNumberOfCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.minimumnumberofcores.aspx)     |
| MaxCores              | [ISchedulerTask.MaximumNumberOfCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.maximumnumberofcores.aspx)     |
| MinNodes              | [ISchedulerTask.MinimumNumberOfNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.minimumnumberofnodes.aspx)     |
| MaxNodes              | [ISchedulerTask.MaximumNumberOfNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.maximumnumberofnodes.aspx)     |
| MinSockets            | [ISchedulerTask.MinimumNumberOfSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.minimumnumberofsockets.aspx) |
| MaxSockets            | [ISchedulerTask.MaximumNumberOfSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.maximumnumberofsockets.aspx) |
| RuntimeSeconds        | [ISchedulerTask.Runtime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.runtime.aspx)                               |
| CommandLine           | [ISchedulerTask.CommandLine](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.commandline.aspx)                       |
| WorkDirectory         | [ISchedulerTask.WorkDirectory](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.workdirectory.aspx)                   |
| RequiredNodes         | [ISchedulerTask.RequiredNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.requirednodes.aspx)                   |
| DependsOn             | [ISchedulerTask.DependsOn](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.dependson.aspx)                           |
| IsExclusive           | [ISchedulerTask.IsExclusive](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.isexclusive.aspx)                       |
| IsRerunnable          | [ISchedulerTask.IsRerunnable](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.isrerunnable.aspx)                     |
| StdOutFilePath        | [ISchedulerTask.StdOutFilePath](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.stdoutfilepath.aspx)                 |
| StdInFilePath         | [ISchedulerTask.StdInFilePath](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.stdinfilepath.aspx)                   |
| StdErrFilePath        | [ISchedulerTask.StdErrFilePath](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.stderrfilepath.aspx)                 |
| StartValue            | [ISchedulerTask.StartValue](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.startvalue.aspx)                         |
| EndValue              | [ISchedulerTask.EndValue](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.endvalue.aspx)                             |
| IncrementValue        | [ISchedulerTask.IncrementValue](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.incrementvalue.aspx)                 |
| UserBlob              | [ISchedulerTask.UserBlob](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.userblob.aspx)                             |
| Type                  | [ISchedulerTask.Type](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.type.aspx)                                     |
| FailJobOnFailure      | [ISchedulerTask.FailJobOnFailure](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.failjobonfailure.aspx)             |
| FailJobOnFailureCount | [ISchedulerTask.FailJobOnFailureCount](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.failjobonfailurecount.aspx)   |
| TaskValidExitCodes    | [ISchedulerTask.ValidExitCodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.validexitcodes.aspx)                 |



 

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP2, or a later version of HPC Pack.<br/> |



 

 




