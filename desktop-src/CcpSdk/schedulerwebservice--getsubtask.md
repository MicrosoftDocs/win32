---
Description: 'Gets the values of the specified properties for the specified subtask, or the values of all of the properties if no properties are specified.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'F3FFA9AD-6EC2-4B0D-9CD3-2B42D586FC48'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Get Subtask
---

# Get Subtask

Gets the values of the specified properties for the specified subtask, or the values of all of the properties if no properties are specified.

## Request

You can specify the Get Subtask request as follows.



| Method                     | Request URI                                                                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| GET (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Job/*job\_identifier*/Task/*task\_identifier*/SubTask/*subtask\_identifier* |
| GET (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Job/*job\_identifier*/Task/*task\_identifier*/SubTask/*subtask\_identifier*                      |



 

For instances of the REST web service that are hosted in Azure, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for an HPC cluster that runs at least Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter    | Description                                                                                                                                                                                                                                                                                                                                                                              |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Properties* | Optional. A comma-separated list of the names for the properties of the subtask for which you want to get values.<br/> If you do not specify the *Properties* parameter, the response contains values for all of the properties of the subtask. If a property with a specified name does not exist for the subtask, an error occurs.<br/>                                    |
| *Render*     | Optional. Specifies the format in which to get the information about the subtask.<br/> Specify RestPropRender to get an XML string that lists the names and values of the properties of the subtask. Specify HpcJobXml to get the information about the subtask as an XML string in the same format as a task XML file.<br/> The default value is RestPropRender.<br/> |
| api-version  | Optional. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this URI parameter is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/> |



 

### Request Headers

The following table describes required and optional request headers.



| Request Header | Description                                                                                                                                                                                                                                                                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version    | Optional. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with SP3, use a value of 2011-11-01. The minimum version that supports this header is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value specified in this header overrides the value specified in the api-version URI parameter if both are specified.<br/> |
| CCP\_Version   | Optional. Specifies the version of the operation to use for this request.<br/> Deprecated beginning with Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3).<br/>                                                                                                                                                                                                           |



 

### Request Body

None.

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
| x-ms-hpc-authoritychain | A comma-separated list of RFC 1918 IP addresses that indicate the sequence of instances of the REST web service that the operation called in order from to right.<br/> Only responses from instances of the REST web service that are hosted on Azure contain this header. Responses from instances of the REST web service that are hosted on premise omit this header.<br/> This header is supported beginning with Microsoft HPC Pack 2008 R2 with SP3 and is not supported in previous versions.<br/> |



 

The response for this operation also includes standard HTTP headers. All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The format of the body of the response depends on the renderer that you specify. The following example shows the format if you specify RestPropRender for Render parameter.


```XML
<ArrayOfProperty xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
    <Property>
        <Name>subtask_property1_name</Name>
        <Value>subtask_property1_value</Value>
    </Property>
    <Property>
        <Name>subtask_property2_name</Name>
        <Value>subtask_property2_value</Value>
    </Property>
    ...
<ArrayOfProperty>
```



The following table describes each of the elements in the response XML.



| Element         | Description                                                  |
|-----------------|--------------------------------------------------------------|
| ArrayOfProperty | Represents the set of properties for the subtask.<br/> |
| Property        | Represents a single property for the task.<br/>        |
| Name            | Contains the name of the property.<br/>                |
| Value           | Contains the value of the property.<br/>               |



 

The following example shows the format if you specify HpcJobXml for Render parameter and CreateTime,State for the Properties parameter.

``` syntax
  <Task Version="3.000" CreateTime="9/26/2011 9:31:28 PM" State="Finished" xmlns="http://schemas.microsoft.com/HPCS2008R2/scheduler/" /> 
```

If you specify HpcJobXml for Render parameter and do not specify a value for the Properties parameter, the task XML that you get contains information about custom properties in addition to the values for the built-in subtask properties. For more information about the information in task XML files, see [Task Schema](taskschema-schema.md).

## Remarks

The following table shows the subtask properties for which you can get the values. For information about the property, see the corresponding property of the ISchedulerTask or ITaskId interface in the managed API for Microsoft HPC Pack.



| Property              | Corresponding ISchedulerTask or ITaskId Property                                                                                               |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| TaskId                | [ISchedulerTask.TaskId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.taskid.aspx)                                 |
| Name                  | [ISchedulerTask.Name](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.name.aspx)                                     |
| State                 | [ISchedulerTask.State](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.state.aspx)                                   |
| PreviousState         | [ISchedulerTask.PreviousState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.previousstate.aspx)                   |
| MinCores              | [ISchedulerTask.MinimumNumberOfCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.minimumnumberofcores.aspx)     |
| MaxCores              | [ISchedulerTask.MaximumNumberOfCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.maximumnumberofcores.aspx)     |
| MinNodes              | [ISchedulerTask.MinimumNumberOfNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.minimumnumberofnodes.aspx)     |
| MaxNodes              | [ISchedulerTask.MaximumNumberOfNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.maximumnumberofnodes.aspx)     |
| MinSockets            | [ISchedulerTask.MinimumNumberOfSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.minimumnumberofsockets.aspx) |
| MaxSockets            | [ISchedulerTask.MaximumNumberOfSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.maximumnumberofsockets.aspx) |
| RuntimeSeconds        | [ISchedulerTask.Runtime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.runtime.aspx)                               |
| SubmitTime            | [ISchedulerTask.SubmitTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.submittime.aspx)                         |
| CreateTime            | [ISchedulerTask.CreateTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.createtime.aspx)                         |
| EndTime               | [ISchedulerTask.EndTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.endtime.aspx)                               |
| ChangeTime            | [ISchedulerTask.ChangeTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.changetime.aspx)                         |
| StartTime             | [ISchedulerTask.StartTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.starttime.aspx)                           |
| ParentJobId           | [ISchedulerTask.ParentJobId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.parentjobid.aspx)                       |
| CommandLine           | [ISchedulerTask.CommandLine](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.commandline.aspx)                       |
| WorkDirectory         | [ISchedulerTask.WorkDirectory](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.workdirectory.aspx)                   |
| RequiredNodes         | [ISchedulerTask.RequiredNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.requirednodes.aspx)                   |
| DependsOn             | [ISchedulerTask.DependsOn](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.dependson.aspx)                           |
| IsExclusive           | [ISchedulerTask.IsExclusive](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.isexclusive.aspx)                       |
| IsRerunnable          | [ISchedulerTask.IsRerunnable](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.isrerunnable.aspx)                     |
| StdOutFilePath        | [ISchedulerTask.StdOutFilePath](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.stdoutfilepath.aspx)                 |
| StdInFilePath         | [ISchedulerTask.StdInFilePath](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.stdinfilepath.aspx)                   |
| StdErrFilePath        | [ISchedulerTask.StdErrFilePath](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.stderrfilepath.aspx)                 |
| ExitCode              | [ISchedulerTask.ExitCode](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.exitcode.aspx)                             |
| RequeueCount          | [ISchedulerTask.RequeueCount](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.requeuecount.aspx)                     |
| StartValue            | [ISchedulerTask.StartValue](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.startvalue.aspx)                         |
| EndValue              | [ISchedulerTask.EndValue](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.endvalue.aspx)                             |
| IncrementValue        | [ISchedulerTask.IncrementValue](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.incrementvalue.aspx)                 |
| ErrorMessage          | [ISchedulerTask.ErrorMessage](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.errormessage.aspx)                     |
| Output                | [ISchedulerTask.Output](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.output.aspx)                                 |
| UserBlob              | [ISchedulerTask.UserBlob](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.userblob.aspx)                             |
| Type                  | [ISchedulerTask.Type](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.type.aspx)                                     |
| IsServiceConcluded    | [ISchedulerTask.IsServiceConcluded](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.isserviceconcluded.aspx)         |
| FailJobOnFailure      | [ISchedulerTask.FailJobOnFailure](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.failjobonfailure.aspx)             |
| FailJobOnFailureCount | [ISchedulerTask.FailJobOnFailureCount](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.failjobonfailurecount.aspx)   |
| AllocatedCoreIds      | [ISchedulerTask.AllocatedCoreIds](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.allocatedcoreids.aspx)             |
| AllocatedNodes        | [ISchedulerTask.AllocatedNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.allocatednodes.aspx)                 |
| HasRuntime            | [ISchedulerTask.HasRuntime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.hasruntime.aspx)                         |
| JobTaskId             | [ITaskId.JobTaskId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.itaskid.jobtaskid.aspx)                              |
| InstanceId            | [ITaskId.InstanceId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.itaskid.instanceid.aspx)                            |
| TaskValidExitCodes    | [ISchedulerTask.ValidExitCodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulertask.validexitcodes.aspx)                 |



 

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP2, or a later version of HPC Pack.<br/> |



 

 




