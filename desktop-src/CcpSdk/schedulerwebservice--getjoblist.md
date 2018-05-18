---
Description: 'Gets the values of the specified properties for all jobs for the HPC cluster, or optionally for jobs filtered by job owner or job state.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8C22B46E-3024-4A13-93BF-D0B463B7791C'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Get Job List
---

# Get Job List

Gets the values of the specified properties for all jobs for the HPC cluster, or optionally for jobs filtered by job owner or job state.

## Request

You can specify the Get Job List request as follows.



| Method                     | Request URI                                                            |
|----------------------------|------------------------------------------------------------------------|
| GET (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Jobs |
| GET (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Jobs                      |



 

For instances of the REST web service that are hosted in Azure, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for an HPC cluster that runs at least Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Properties*          | Optional. A comma-separated list of the names for the properties of the jobs for which you want to get values. For a list of properties for which you can get values, see the Remarks section.<br/> If you do not specify the *Properties* parameter, the response contains values for the **Id**, **Owner**, **Name**, **State**, and **Priority** properties of the jobs.<br/> If a property with a specified name does not exist for a job, an error occurs.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *Owner*               | Optional. The user who created, submitted, or queued the job.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| *QueryId*             | Specifies internal data from the x-ms-continuation-QueryId header from the response in the previous Get Job List operation in a set of Get Job List operations. For more information, see the Response Headers section later in this topic.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *CurrentObjectNumber* | Specifies internal data from the x-ms-continuation-CurrentObjectNumber header from the response in the previous Get Job List operation in a continuation sequence of Get Job List operations. For more information, see the Response Headers section later in this topic. Deprecated starting with Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| api-version           | Optional. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this URI parameter is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| $filter               | Optional. Specifies OData filters to use for this request in the following format "$filter=&lt;filter1&gt;%20and%20&lt;filter2&gt;…". <br/> To filter the jobs by a valid job state, use the filter "JobState%20eq%20&lt;JobState&gt;". To retrieve jobs whose state changed after a certain date and time, use the filter "ChangeTimeFrom%20eq%20&lt;DateTime&gt;". <br/> A null value is ignored. <br/> The minimum version that supports this URI parameter is Microsoft HPC Pack 2012. To use this parameter, also specify the Render URI parameter set to RestPropRender and a minimum api-version value of 2012-11-01.<br/> Example: "$filter=JobState%20eq%20queued%20and%20 ChangeTimeFrom%20eq%202015-10-16&Render=RestPropRender&api-version=2012-11-01". For information about job states, see [JobState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobstate.aspx). |
| Render                | Required if the $filter URI parameter is specified. Set the value to RestPropRender to specify that the response body is formatted in XML compatible with Microsoft HPC Pack 2008 R2 with Service Pack 2 (SP2). The minimum version that supports this URI parameter is Microsoft HPC Pack 2012.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SortJobsBy            | Optional. A job property by which jobs will be sorted. If this parameter is not specified or a property with a specified name does not exist for a job, the result will be sorted by job Id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RowsPerRead           | Optional. Specifies how many lines of data to retrieve each time. The default is set to 10. At least one record will be retrieved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |



 

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
| x-ms-continuation-queryId             | Enables large sets of data to be returned in smaller responses across a continuation sequence of several requests. The value of this header is to be assigned to the queryId query string parameter in the next call in the sequence of calls to the Get Job List operation. The response to the Get Job List operation contains this header as long as additional data remains to be processed. You use the values of this header for one operation in the queryId URI parameter for the next operation.<br/> The format of these data in this header is not guaranteed to remain unchanged. You should only copy the data in this header from one operation in a set of multiple operations to the queryId URI parameter for the next operation. You should not use the data in this header or depend on the format of the data in this header in any other way.<br/> For an example of how to use this header and URI parameter in a way that potential changes will not impact, see the code for the sample client applications for REST API. For information about how to get these sample client applications, see [Getting Sample Programs that use the REST API](creating-and-managing-jobs-with-the-web-service-interface.md#getting-sample-programs-that-use-the-rest-api).<br/> |
| x-ms-continuation-CurrentObjectNumber | Contains internal data that support working with sets of data that are too large or too expensive to get in a single response body by dividing the Get Job List operation into a set of multiple Get Job List operations. The response to the Get Job List operation contains this header as long as additional data remains to be processed. You use the values of this header for one operation in the CurrentObjectNumber URI parameter for the next operation.<br/> The format of the data in this header is not guaranteed to remain unchanged. You should only copy the data in this header from one operation in a set of multiple operations to the CurrentObjectNumber URI parameter for the next operation. You should not use the data in this header or depend on the format of the data in this header in any other way.<br/> For an example of how to use this header and URI parameter in a way that potential changes will not impact, see the code for the sample client applications for REST API.<br/> Deprecated starting with Microsoft HPC Pack 2008 R2 with SP3.<br/>                                                                                                                                                                                          |



 

The response for this operation also includes standard HTTP headers. All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The format of the response body is as follows.


```XML
<ArrayOfObject xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
    <Object>
        <Properties>
            <Property>
                <Name>job1_property1_name</Name>
                <Value>job1_property1_value</Value>
           </Property>
           <Property>
               <Name>job1_property2_name</Name>
               <Value>job1_property2_value</Value>
           </Property>
           ...
        </Properties>
    </Object>
        <Properties>
            <Property>
                <Name>job2_property1_name</Name>
                <Value>job2_property1_value</Value>
           </Property>
           <Property>
               <Name>job2_property2_name</Name>
               <Value>job2_property2_value</Value>
           </Property>
           ...
        </Properties>
    </Object>
    ...
</ArrayOfObject>
```



The following table describes each of the elements in the response XML.



| Element       | Description                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------|
| ArrayOfObject | Represents the set of jobs with the specified owner, or all jobs if no owner is specified.<br/> |
| Object        | Represents a single job.<br/>                                                                   |
| Properties    | Represents the set of properties for the job.<br/>                                              |
| Property      | Represents a single property for the job.<br/>                                                  |
| Name          | Contains the name of the property.<br/>                                                         |
| Value         | Contains the value of the property.<br/>                                                        |



 

## Remarks

The following table shows the job properties for which you can get the values or by which you can sort results. For information about the property, see the corresponding property of the ISchedulerJob interface in the managed API for Microsoft HPC Pack.



| Property               | Corresponding ISchedulerJob Property                                                                                                         |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Id                     | [ISchedulerJob.Id](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.id.aspx)                                         |
| Name                   | [ISchedulerJob.Name](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.name.aspx)                                     |
| Owner                  | [ISchedulerJob.Owner](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.owner.aspx)                                   |
| UserName               | [ISchedulerJob.UserName](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.username.aspx)                             |
| Project                | [ISchedulerJob.Project](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.project.aspx)                               |
| RuntimeSeconds         | [ISchedulerJob.Runtime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.runtime.aspx)                               |
| SubmitTime             | [ISchedulerJob.SubmitTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.submittime.aspx)                         |
| CreateTime             | [ISchedulerJob.CreateTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.createtime.aspx)                         |
| EndTime                | [ISchedulerJob.EndTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.endtime.aspx)                               |
| StartTime              | [ISchedulerJob.StartTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.starttime.aspx)                           |
| ChangeTime             | [ISchedulerJob.ChangeTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.changetime.aspx)                         |
| State                  | [ISchedulerJob.State](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.state.aspx)                                   |
| PreviousState          | [ISchedulerJob.PreviousState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.previousstate.aspx)                   |
| MinCores               | [ISchedulerJob.MinimumNumberOfCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.minimumnumberofcores.aspx)     |
| MaxCores               | [ISchedulerJob.MaximumNumberOfCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.maximumnumberofcores.aspx)     |
| MinNodes               | [ISchedulerJob.MinimumNumberOfNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.minimumnumberofnodes.aspx)     |
| MaxNodes               | [ISchedulerJob.MaximumNumberOfNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.maximumnumberofnodes.aspx)     |
| MinSockets             | [ISchedulerJob.MinimumNumberOfSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.minimumnumberofsockets.aspx) |
| MaxSockets             | [ISchedulerJob.MaximumNumberOfSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.maximumnumberofsockets.aspx) |
| UnitType               | [ISchedulerJob.UnitType](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.unittype.aspx)                             |
| RequestedNodes         | [ISchedulerJob.RequestedNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.requestednodes.aspx)                 |
| IsExclusive            | [ISchedulerJob.IsExclusive](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.isexclusive.aspx)                       |
| RunUntilCanceled       | [ISchedulerJob.RunUntilCanceled](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.rununtilcanceled.aspx)             |
| NodeGroups             | [ISchedulerJob.NodeGroups](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.nodegroups.aspx)                         |
| FailOnTaskFailure      | [ISchedulerJob.FailOnTaskFailure](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.failontaskfailure.aspx)           |
| AutoCalculateMax       | [ISchedulerJob.AutoCalculateMax](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.autocalculatemax.aspx)             |
| AutoCalculateMin       | [ISchedulerJob.AutoCalculateMin](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.autocalculatemin.aspx)             |
| CanGrow                | [ISchedulerJob.CanGrow](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.cangrow.aspx)                               |
| CanShrink              | [ISchedulerJob.CanShrink](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.canshrink.aspx)                           |
| Preemptable            | [ISchedulerJob.CanPreempt](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.canpreempt.aspx)                         |
| ErrorMessage           | [ISchedulerJob.ErrorMessage](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.errormessage.aspx)                     |
| HasRuntime             | [ISchedulerJob.HasRuntime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.hasruntime.aspx)                         |
| RequeueCount           | [ISchedulerJob.RequeueCount](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.requeuecount.aspx)                     |
| MinMemory              | [ISchedulerJob.MinMemory](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.minmemory.aspx)                           |
| MaxMemory              | [ISchedulerJob.MaxMemory](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.maxmemory.aspx)                           |
| MinCoresPerNode        | [ISchedulerJob.MinCoresPerNode](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.mincorespernode.aspx)               |
| MaxCoresPerNode        | I[SchedulerJob.MaxCoresPerNode](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.maxcorespernode.aspx)               |
| EndpointReference      | [ISchedulerJob.EndpointAddresses](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.endpointaddresses.aspx)           |
| SoftwareLicense        | [ISchedulerJob.SoftwareLicense](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.softwarelicense.aspx)               |
| OrderBy                | [ISchedulerJob.OrderBy](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.orderby.aspx)                               |
| ClientSource           | [ISchedulerJob.ClientSource](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.clientsource.aspx)                     |
| Progress               | [ISchedulerJob.Progress](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.progress.aspx)                             |
| ProgressMessage        | [ISchedulerJob.ProgressMessage](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.progressmessage.aspx)               |
| TargetResourceCount    | [ISchedulerJob.TargetResourceCount](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.targetresourcecount.aspx)       |
| ExpandedPriority       | [ISchedulerJob.ExpandedPriority](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.expandedpriority.aspx)             |
| ServiceName            | [ISchedulerJob.ServiceName](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.servicename.aspx)                       |
| JobTemplate            | [ISchedulerJob.JobTemplate](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.jobtemplate.aspx)                       |
| HoldUntil              | [ISchedulerJob.HoldUntil](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.holduntil.aspx)                           |
| NotifyOnStart          | [ISchedulerJob.NotifyOnStart](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.notifyonstart.aspx)                   |
| NotifyOnCompletion     | [ISchedulerJob.NotifyOnCompletion](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.notifyoncompletion.aspx)         |
| ExcludedNodes          | [ISchedulerJob.ExcludedNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.excludednodes.aspx)                   |
| EmailAddress           | [ISchedulerJob.EmailAddress](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.emailaddress.aspx)                     |
| Priority               | [ISchedulerJob.Priority](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.priority.aspx)                             |
| AllocatedNodes         | [ISchedulerJob.AllocatedNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.allocatednodes.aspx)                 |
| Pool                   | [ISchedulerJob.Pool](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.pool.aspx)                                     |
| JobValidExitCodes      | [ISchedulerJob.ValidExitCodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.validexitcodes.aspx)                 |
| ParentJobIds           | [ISchedulerJob.ParentJobIds](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.faildependenttasks.aspx)               |
| FailDependentTasks     | [ISchedulerJob.FailDependentTasks](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.name.aspx)                       |
| NodeGroupOp            | [ISchedulerJob.NodeGroupOp](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.nodegroupop.aspx)                       |
| SingleNode             | [ISchedulerJob.SingleNode](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.singlenode.aspx)                         |
| ChildJobIds            | [ISchedulerJob.ChildJobIds](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.childjobids.aspx)                       |
| EstimatedProcessMemory | [ISchedulerJob.EstimatedProcessMemory](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.estimatedprocessmemory.aspx) |



 

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP2, or a later version of HPC Pack.<br/> |



 

 




