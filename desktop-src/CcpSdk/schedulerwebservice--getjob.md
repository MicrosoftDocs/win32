---
Description: 'Gets information about the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'E61E72AE-414E-4AD8-977C-9BE07F6283F9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Get Job
---

# Get Job

Gets information about the specified job.

## Request

You can specify the Get Job request as follows.



| Method                     | Request URI                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------|
| GET (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Job/*job\_identifier* |
| GET (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Job/*job\_identifier*                      |



 

For instances of the REST web service that are hosted in Azure, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for an HPC cluster that runs at least Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter    | Description                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Properties* | Optional. A comma-separated list of the names for the properties of the job for which you want to get values. For a list of properties for which you can get values, see the Remarks section.<br/> If you do not specify the *Properties* parameter, the response contains values for all of the properties of the job. If a property with a specified name does not exist for the job, an error occurs.<br/> |
| *Render*     | Optional. Determines the schema used for the XML response.<br/> Specify RestPropRender to get job properties as &lt;name, value&gt; pairs. Specify HpcJobXml to get XML formatted as found in the Create Job From XML operation.<br/> The default value is RestPropRender.<br/>                                                                                                                         |
| api-version  | Optional. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this URI parameter is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/>                                  |



 

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
| x-ms-hpc-authoritychain | A comma-separated list of RFC 1918 IP addresses that indicate the sequence of instances of the REST web service that the operation called in order from to right.<br/> Only responses from instances of the REST web service that are hosted on Azure contain this header. Responses from instances of the REST web service that are hosted on premise omit this header.<br/> This header is supported beginning with Microsoft HPC Pack 2008 R2 with SP3 and is not available in previous versions.<br/> |



 

The response for this operation also includes standard HTTP headers. All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The format of the body of the response depends on the renderer that you specify. The following example shows the format if you specify RestPropRender for Render parameter.


```XML
<ArrayOfProperty xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
    <Property>
        <Name>job_property1_name</Name>
        <Value>job_property1_value</Value>
    </Property>
    <Property>
        <Name>job_property2_name</Name>
        <Value>job_property2_value</Value>
    </Property>
    ...
<ArrayOfProperty>
```



The following table describes each of the elements in this response XML.



| Element         | Description                                                                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ArrayOfProperty | Represents the set of properties for the job for which you requested values, or all of the properties for the job if you did not specify a list of properties.<br/> |
| Property        | Represents a single property for the job.<br/>                                                                                                                      |
| Name            | Contains the name of the property.<br/>                                                                                                                             |
| Value           | Contains the value of the property.<br/>                                                                                                                            |



 

The following example shows the format if you specify HpcJobXml for Render parameter and Id,CreateTime, State for the Properties parameter.

``` syntax
<Job Version="3.000" Id="115" CreateTime="2010/12/7 23:18:20" State="Configuring" />
```

If you specify HpcJobXml for Render parameter and do not specify a value for the Properties parameter, the job XML that you get contains information about custom properties, dependencies, and tasks, in addition to the values for the built-in job properties. For more information about the information in job XML files, see [Job Schema](jobschema-schema.md).

## Remarks

The following table shows the job properties for which you can get the values. For information about the property, including the versions of HPC Pack that support it, see the corresponding property of the [**ISchedulerJob**](ischedulerjob.md) interface in the managed API for Microsoft HPC Pack.



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
| JobTemplate            | [ISchedulerJob.JobTemplate](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.jobtemplate.aspx)                       |
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



 

 




