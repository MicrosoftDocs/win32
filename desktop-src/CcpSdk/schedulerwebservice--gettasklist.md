---
Description: 'Gets the values of the properties for all of the tasks in the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'AF7687DB-CE56-463F-A30E-3F83F240DCC3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Get Task List
---

# Get Task List

Gets the values of the properties for all of the tasks in the specified job.

## Request

You can specify the Get Task List request as follows.



| Method                     | Request URI                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------|
| GET (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Job/j*ob\_identifier*/Tasks |
| GET (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Job/j*ob\_identifier*/Tasks                      |



 

For instances of the REST web service that are hosted in Azure, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for an HPC cluster that runs at least Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Properties*          | Optional. A comma-separated list of the names for the properties of the tasks for which you want to get values.<br/> If you do not specify the *Properties* parameter, the response contains values for the TaskId, Name, State, CommandLine, ExitCode, ParentJobId, JobTaskId, and InstanceId properties. For a list of the properties that you can specify, see the Remarks section.<br/> If a property with a specified name does not exist for a task, an error occurs.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| *ExpandParametric*    | Optional. Specifies whether to get properties only for the master task for a parametric sweep task, or for all of the subtasks instead. True indicates that you want to get properties for all of the subtasks. False indicates that you want to get properties only for the master task. The default value is True.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *QueryId*             | Specifies internal data from the x-ms-continuation-QueryId header from the response in the previous Get Task List operation in a continuation sequence of Get Task List operations. For more information, see the Response Headers section later in this topic.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *CurrentObjectNumber* | Specifies internal data from the x-ms-continuation-CurrentObjectNumber header from the response in the previous Get Task List operation in a set of Get Task List operations. For more information, see the Response Headers section later in this topic. Deprecated starting with Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| api-version           | Optional. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this URI parameter is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| $filter               | Optional. Specifies OData filters to use for this request in the following format "$filter=&lt;filter1&gt;%20and%20&lt;filter2&gt;…". <br/> To filter the tasks by a valid task state, use the filter "TaskState%20eq%20&lt;TaskState&gt;". To retrieve tasks whose state changed after a certain date and time, use the filter "ChangeTimeFrom%20eq%20&lt;DateTime&gt;". <br/> A null value is ignored. <br/> The minimum version that supports this URI parameter is Microsoft HPC Pack 2012. To use this parameter, also specify the Render URI parameter set to RestPropRender and a minimum api-version value of 2012-11-01.<br/> Example: "$filter=TaskState%20eq%20queued%20and%20 ChangeTimeFrom%20eq%202015-10-16&Render=RestPropRender&api-version=2012-11-01". For information about task states, see [TaskState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskstate.aspx). |
| Render                | Required if the $filter URI parameter is specified. Set the value to RestPropRender to specify that the response body is formatted in XML compatible with Microsoft HPC Pack 2008 R2 with Service Pack 2 (SP2). The minimum version that supports this URI parameter is Microsoft HPC Pack 2012.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SortTasksBy           | Optional. A task property by which tasks will be sorted. If this parameter is not specified or a property with a specified name does not exist for a task, the result will be sorted by task Id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RowsPerRead           | Optional. Specifies how many lines of data to retrieve each time. The default is set to 10. At least one record will be retrieved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

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



| Response Header                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| x-ms-hpc-authoritychain               | A comma-separated list of RFC 1918 IP addresses that indicate the sequence of instances of the REST web service that the operation called in order from to right.<br/> Only responses from instances of the REST web service that are hosted on Azure contain this header. Responses from instances of the REST web service that are hosted on premise omit this header.<br/> This header is supported beginning with Microsoft HPC Pack 2008 R2 with SP3 and is not available in previous versions.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| x-ms-continuation-queryId             | Enables large sets of data to be returned in smaller responses across a continuation sequence of several requests. The value of this header is to be assigned to the queryId query string parameter in the next call in the sequence of calls to the Get Task List operation. The response to the Get Task List operation contains this header as long as additional data remains to be processed. You use the values of this header for one operation in the queryId URI parameter for the next operation.<br/> The format of the data in this header is not guaranteed to remain unchanged. You should only copy the data in this header from one operation in a set of multiple operations to the queryId URI parameter for the next operation. You should not use the data in this header or depend on the format of the data in this header in any other way.<br/> For an example of how to use this header and URI parameter in a way that potential changes will not impact, see the code for the sample client applications for REST API. For information about how to get these sample client applications, see [Getting Sample Programs that use the REST API](creating-and-managing-jobs-with-the-web-service-interface.md#getting-sample-programs-that-use-the-rest-api).<br/> |
| x-ms-continuation-CurrentObjectNumber | Contains internal data that support working with sets of data that are too large or too expensive to get in a single response body by dividing the Get Task List operation into a set of multiple Get Task List operations. The response to the Get Task List operation contains this header as long as additional data remains to be processed. You use the values of this header for one operation in the CurrentObjectNumber URI parameter for the next operation.<br/> The format of the data in this header is not guaranteed to remain unchanged. You should only copy the data in this header from one operation in a set of multiple operations to the CurrentObjectNumber URI parameter for the next operation. You should not use the data in this header or depend on the format of the data in this header in any other way.<br/> For an example of how to use this header and URI parameter in a way that potential changes will not impact, see the code for the sample client applications for REST API.<br/> Deprecated starting with Microsoft HPC Pack 2008 R2 with SP3.<br/>                                                                                                                                                                                       |



 

The response for this operation also includes standard HTTP headers. All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The format of the response body is as follows.


```XML
<ArrayOfObject xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
    <Object>
        <Properties>
            <Property>
                <Name>task1_property1_name</Name>
                <Value>task1_property1_value</Value>
           </Property>
           <Property>
               <Name>task1_property2_name</Name>
               <Value>task1_property2_value</Value>
           </Property>
           ...
        </Properties>
    </Object>
        <Properties>
            <Property>
                <Name>task2_property1_name</Name>
                <Value>task2_property1_value</Value>
           </Property>
           <Property>
               <Name>task2_property2_name</Name>
               <Value>task2_property2_value</Value>
           </Property>
           ...
        </Properties>
    </Object>
    ...
</ArrayOfObject>
```



The following table describes each of the elements in the response XML.



| Element       | Description                                                  |
|---------------|--------------------------------------------------------------|
| ArrayOfObject | Represents the set of tasks in the specified job.<br/> |
| Object        | Represents a single task.<br/>                         |
| Properties    | Represents the set of properties for the task.<br/>    |
| Property      | Represents a single property for the task.<br/>        |
| Name          | Contains the name of the property.<br/>                |
| Value         | Contains the value of the property.<br/>               |



 

## Remarks

The following table shows the task properties for which you can get the values or by which you can sort results. For information about the property, including the versions of Microsoft HPC Pack that support it, see the corresponding property of the ISchedulerTask or ITaskId interface in the managed API for Microsoft HPC Pack.



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



 

 




