---
Description: 'Defines a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c64702a8-4768-4ef8-95d6-3b376399e30a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Job Complex Type
---

# Job Complex Type

Defines a job.

``` syntax
<xs:complexType name="Job">
    <xs:sequence>
        <xs:element name="CustomProperties"
            type="NameValueCollection"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="ExtendedTerms"
            type="NameValueCollection"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="Dependencies"
            type="ArrayOfTaskGroupDependency"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="Tasks"
            type="ArrayOfTask"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
    <xs:attribute name="Version"
        type="decimal"
     />
    <xs:attribute name="Id"
        type="int"
     />
    <xs:attribute name="Name"
        type="string"
     />
    <xs:attribute name="SubmitTime"
        type="string"
     />
    <xs:attribute name="CreateTime"
        type="string"
     />
    <xs:attribute name="StartTime"
        type="string"
     />
    <xs:attribute name="EndTime"
        type="string"
     />
    <xs:attribute name="ChangeTime"
        type="string"
     />
    <xs:attribute name="UnitType"
        type="UnitType"
        default="Core"
     />
    <xs:attribute name="MinCores"
        type="int"
     />
    <xs:attribute name="MaxCores"
        type="int"
     />
    <xs:attribute name="MinSockets"
        type="int"
     />
    <xs:attribute name="MaxSockets"
        type="int"
     />
    <xs:attribute name="MinNodes"
        type="int"
     />
    <xs:attribute name="MaxNodes"
        type="int"
     />
    <xs:attribute name="RunUntilCanceled"
        type="boolean"
        default="false"
     />
    <xs:attribute name="IsExclusive"
        type="boolean"
        default="false"
     />
    <xs:attribute name="ErrorCode"
        type="int"
     />
    <xs:attribute name="ErrorParams"
        type="string"
     />
    <xs:attribute name="ErrorMessage"
        type="string"
     />
    <xs:attribute name="State"
        type="JobState"
     />
    <xs:attribute name="PreviousState"
        type="JobState"
     />
    <xs:attribute name="UserName"
        type="string"
     />
    <xs:attribute name="JobType"
        type="JobType"
     />
    <xs:attribute name="Priority"
        type="JobPriority"
     />
    <xs:attribute name="RequiredNodes"
        type="string"
     />
    <xs:attribute name="RequestedNodes"
        type="string"
     />
    <xs:attribute name="NodeGroups"
        type="string"
     />
    <xs:attribute name="RuntimeSeconds"
        type="int"
     />
    <xs:attribute name="IsBackfill"
        type="boolean"
     />
    <xs:attribute name="NextTaskNiceID"
        type="int"
     />
    <xs:attribute name="HasGrown"
        type="boolean"
     />
    <xs:attribute name="HasShrunk"
        type="boolean"
     />
    <xs:attribute name="CanGrow"
        type="boolean"
     />
    <xs:attribute name="CanShrink"
        type="boolean"
     />
    <xs:attribute name="ComputedMinCores"
        type="int"
     />
    <xs:attribute name="ComputedMaxCores"
        type="int"
     />
    <xs:attribute name="ComputedMinSockets"
        type="int"
     />
    <xs:attribute name="ComputedMaxSockets"
        type="int"
     />
    <xs:attribute name="ComputedMinNodes"
        type="int"
     />
    <xs:attribute name="ComputedMaxNodes"
        type="int"
     />
    <xs:attribute name="OrderBy"
        type="string"
     />
    <xs:attribute name="WaitTime"
        type="int"
     />
    <xs:attribute name="TaskLevelUpdateTime"
        type="string"
     />
    <xs:attribute name="MinMaxUpdateTime"
        type="string"
     />
    <xs:attribute name="RequestCancel"
        type="string"
     />
    <xs:attribute name="RequeueCount"
        type="int"
     />
    <xs:attribute name="AutoRequeueCount"
        type="int"
     />
    <xs:attribute name="FailureReason"
        type="string"
     />
    <xs:attribute name="PendingReason"
        type="string"
     />
    <xs:attribute name="AutoCalculateMax"
        type="boolean"
     />
    <xs:attribute name="AutoCalculateMin"
        type="boolean"
     />
    <xs:attribute name="ParentJobId"
        type="int"
     />
    <xs:attribute name="ChildJobId"
        type="int"
     />
    <xs:attribute name="NumberOfCalls"
        type="int"
     />
    <xs:attribute name="NumberOfOutstandingCalls"
        type="int"
     />
    <xs:attribute name="CallDuration"
        type="int"
     />
    <xs:attribute name="CallsPerSecond"
        type="int"
     />
    <xs:attribute name="FailOnTaskFailure"
        type="boolean"
     />
    <xs:attribute name="Preemptable"
        type="boolean"
     />
    <xs:attribute name="ProjectId"
        type="int"
     />
    <xs:attribute name="JobTemplateId"
        type="int"
     />
    <xs:attribute name="OwnerId"
        type="int"
     />
    <xs:attribute name="ClientSourceId"
        type="int"
     />
    <xs:attribute name="Project"
        type="string"
     />
    <xs:attribute name="JobTemplate"
        type="string"
     />
    <xs:attribute name="DefaultTaskGroupId"
        type="int"
     />
    <xs:attribute name="Owner"
        type="string"
     />
    <xs:attribute name="ClientSource"
        type="string"
     />
    <xs:attribute name="ClientSubSource"
        type="string"
     />
    <xs:attribute name="SoftwareLicense"
        type="string"
     />
    <xs:attribute name="ServiceName"
        type="string"
     />
    <xs:attribute name="MinCoresPerNode"
        type="int"
     />
    <xs:attribute name="MaxCoresPerNode"
        type="int"
     />
    <xs:attribute name="MinMemory"
        type="int"
     />
    <xs:attribute name="MaxMemory"
        type="int"
     />
    <xs:attribute name="EndpointReference"
        type="string"
     />
    <xs:attribute name="ComputedNodeList"
        type="string"
     />
    <xs:attribute name="DefaultTaskGroupId"
        type="int"
     />
    <xs:attribute name="ProcessIds"
        type="string"
     />
</xs:complexType>
```

## Child elements



| Element                                                            | Type                                                                                   | Description                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CustomProperties**](jobschema-customproperties-job-element.md) | [**NameValueCollection**](jobschema-namevaluecollection-complextype.md)               | A collection of custom properties that the submission and activation filters access. See [**ISchedulerJob::GetCustomProperties**](ischedulerjob-getcustomproperties.md).<br/>                                                           |
| [**Dependencies**](jobschema-dependencies-job-element.md)         | [**ArrayOfTaskGroupDependency**](jobschema-arrayoftaskgroupdependency-complextype.md) | A collection of task group dependencies.<br/>                                                                                                                                                                                            |
| [**ExtendedTerms**](jobschema-extendedterms-job-element.md)       | [**NameValueCollection**](jobschema-namevaluecollection-complextype.md)               | Do not use. Use [**CustomProperties**](jobschema-customproperties-job-element.md) instead.<br/> **Microsoft Compute Cluster Server 2003:** A collection of extended terms that the submission and activation filters access.<br/> |
| [**Tasks**](jobschema-tasks-job-element.md)                       | [**ArrayOfTask**](jobschema-arrayoftask-complextype.md)                               | An array of the tasks to run. <br/>                                                                                                                                                                                                      |



## Attributes



| Name                     | Type                                                    | Description                                                                                                                                                                                                                                                                                                                                          |
|--------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoCalculateMax         | boolean                                                 | Determines whether the server automatically calculates the maximum resource value. See [**ISchedulerJob.AutoCalculateMax**](ischedulerjob-autocalculatemax.md).<br/>                                                                                                                                                                          |
| AutoCalculateMin         | boolean                                                 | Determines whether the server automatically calculates the minimum resource value. See [**ISchedulerJob.AutoCalculateMin**](ischedulerjob-autocalculatemin.md).<br/>                                                                                                                                                                          |
| AutoRequeueCount         | int                                                     | The number of times that the system reran the job when a system error occurred. See [JobPropertyIds.AutoRequeueCount](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.autorequeuecount.aspx).<br/>                                                                                                        |
| CallDuration             | int                                                     | The average duration of a web-service message call in the session. See [JobPropertyIds.CallDuration](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.callduration.aspx).<br/>                                                                                                                             |
| CallsPerSecond           | int                                                     | The number of web-service calls made in the session in the last second. See [JobPropertyIds.CallsPerSecond](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.callspersecond.aspx).<br/>                                                                                                                    |
| CanGrow                  | boolean                                                 | Determines whether the job resources can grow. See [**ISchedulerJob.CanGrow**](ischedulerjob-cangrow.md).<br/>                                                                                                                                                                                                                                |
| CanShrink                | boolean                                                 | Determines whether the job resources can shrink. See [**ISchedulerJob.CanShrink**](ischedulerjob-canshrink.md).<br/>                                                                                                                                                                                                                          |
| ChangeTime               | string                                                  | The last time that the user or server changed a property of the job. See [**ISchedulerJob.ChangeTime**](ischedulerjob-changetime.md).<br/>                                                                                                                                                                                                    |
| ChildJobId               | int                                                     | An identifier that uniquely identifies the child job. See [JobPropertyIds.ChildJobId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.childjobid.aspx).<br/>                                                                                                                                              |
| ClientSource             | string                                                  | The name of the process that created the job. See [**ISchedulerJob.ClientSource**](ischedulerjob-clientsource.md).<br/>                                                                                                                                                                                                                       |
| ClientSourceId           | int                                                     | An identifier that identifies the process that created the job. For internal use only.<br/>                                                                                                                                                                                                                                                    |
| ClientSubSource          | string                                                  | Indicates whether the source was an XML file, executable, DLL, or a script. See [JobPropertyIds.ClientSubSource](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.clientsubsource.aspx).<br/>                                                                                                              |
| ComputedMaxCores         | int                                                     | The maximum number of cores that the server has currently allocated to the job. See [JobPropertyIds.ComputedMaxCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.computedmaxcores.aspx).<br/>                                                                                                        |
| ComputedMaxNodes         | int                                                     | The maximum number of nodes that the server has currently allocated to the job. See [JobPropertyIds.ComputedMaxNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.computedmaxnodes.aspx).<br/>                                                                                                        |
| ComputedMaxSockets       | int                                                     | The maximum number of sockets that the server has currently allocated to the job. See [JobPropertyIds.ComputedMaxSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.computedmaxsockets.aspx).<br/>                                                                                                  |
| ComputedMinCores         | int                                                     | The minimum number of cores that the server has currently allocated to the job. See [JobPropertyIds.ComputedMinCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.computedmincores.aspx).<br/>                                                                                                        |
| ComputedMinNodes         | int                                                     | The minimum number of nodes that the server has currently allocated to the job. See [JobPropertyIds.ComputedMinNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.computedminnodes.aspx).<br/>                                                                                                        |
| ComputedMinSockets       | int                                                     | The minimum number of sockets that the server has currently allocated to the job. See [JobPropertyIds.ComputedMinSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.computedminsockets.aspx).<br/>                                                                                                  |
| ComputedNodeList         | string                                                  | A comma-delimited list of node names of the nodes that are currently allocated to your running job. See [JobPropertyIds.ComputedNodeList](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.computednodelist.aspx).<br/>                                                                                    |
| CreateTime               | string                                                  | The time that the job was created. See [**ISchedulerJob.CreateTime**](ischedulerjob-createtime.md).<br/>                                                                                                                                                                                                                                      |
| DefaultTaskGroupId       | int                                                     | The default task group for the job. See [JobPropertyIds.DefaultTaskGroupId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.defaulttaskgroupid.aspx).<br/>                                                                                                                                                |
| DefaultTaskGroupId       | int                                                     | The default task group for the job. For internal use only. See [JobPropertyIds.DefaultTaskGroupId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.defaulttaskgroupid.aspx).<br/>                                                                                                                         |
| EndpointReference        | string                                                  | A semicolon-delimited list of endpoint addresses that you can use to connect to a shared session. See [**ISchedulerJob.EndpointAddresses**](ischedulerjob-endpointaddresses.md).<br/>                                                                                                                                                         |
| EndTime                  | string                                                  | The time that the job finished running. See [**ISchedulerJob.EndTime**](ischedulerjob-endtime.md).<br/>                                                                                                                                                                                                                                       |
| ErrorCode                | int                                                     | An error code that identifies an error message string. See [JobPropertyIds.ErrorCode](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.errorcode.aspx).<br/>                                                                                                                                               |
| ErrorMessage             | string                                                  | The job-related error message or the message specified when the user canceled the job. See [**ISchedulerJob.ErrorMessage**](ischedulerjob-errormessage.md).<br/>                                                                                                                                                                              |
| ErrorParams              | string                                                  | The insert strings that are applied to the error message string. See [JobPropertyIds.ErrorParams](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.errorparams.aspx).<br/>                                                                                                                                 |
| FailOnTaskFailure        | boolean                                                 | Determines whether the job fails when one of the tasks in the job fails. See [**ISchedulerJob.FailOnTaskFailure**](ischedulerjob-failontaskfailure.md).<br/>                                                                                                                                                                                  |
| FailureReason            | string                                                  | The reason a task in the job failed. See [JobPropertyIds.FailureReason](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.failurereason.aspx).<br/>                                                                                                                                                         |
| HasGrown                 | boolean                                                 | Indicates whether the number of resources allocated to the job has grown since resources were last allocated. See [JobPropertyId.HasGrown](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.hasgrown.aspx).<br/>                                                                                           |
| HasShrunk                | boolean                                                 | Indicates whether the number of resources allocated to the job has shrunk since resources were last allocated. See [JobPropertyId.HasShrunk](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.hasshrunk.aspx).<br/>                                                                                        |
| Id                       | int                                                     | An identifier that uniquely identifies the job. See [**ISchedulerJob.Id**](ischedulerjob-id.md).<br/>                                                                                                                                                                                                                                         |
| IsBackfill               | boolean                                                 | Determines whether the job is running as a backfill job. See [JobPropertyIds.IsBackfill](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.isbackfill.aspx).<br/>                                                                                                                                           |
| IsExclusive              | boolean                                                 | Determines whether nodes are exclusively allocated to the job. See [**ISchedulerJob.IsExclusive**](ischedulerjob-isexclusive.md).<br/>                                                                                                                                                                                                        |
| JobTemplate              | string                                                  | The job template used to initialize the properties of the job. See [**ISchedulerJob.JobTemplate**](ischedulerjob-jobtemplate.md).<br/>                                                                                                                                                                                                        |
| JobTemplateId            | int                                                     | An identifier that identifies the job template. For internal use only.<br/>                                                                                                                                                                                                                                                                    |
| JobType                  | [**JobType**](jobschema-jobtype-simpletype.md)         | The type of job (for example, a normally scheduled batch job or a command). See [JobPropertyIds.JobType](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.jobtype.aspx).<br/>                                                                                                                              |
| MaxCores                 | int                                                     | The maximum number of cores that the scheduler may allocate for the job. See [**ISchedulerJob.MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md).<br/>                                                                                                                                                                            |
| MaxCoresPerNode          | int                                                     | The maximum number of cores that a node can have for the job to run on it. See [**ISchedulerJob.MaxCoresPerNode**](ischedulerjob-maxcorespernode.md).<br/>                                                                                                                                                                                    |
| MaxMemory                | int                                                     | The maximum number of cores that a node can have for the job to run on it. See [**ISchedulerJob.MaxMemory**](ischedulerjob-maxmemory.md).<br/>                                                                                                                                                                                                |
| MaxNodes                 | int                                                     | The maximum number of nodes that the scheduler may allocate for the job. See [**ISchedulerJob.MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md).<br/>                                                                                                                                                                            |
| MaxSockets               | int                                                     | The maximum number of sockets that the scheduler may allocate for the job. See [**ISchedulerJob.MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md).<br/>                                                                                                                                                                      |
| MinCores                 | int                                                     | The minimum number of cores that the job requires to run. See [**ISchedulerJob.MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md).<br/>                                                                                                                                                                                           |
| MinCoresPerNode          | int                                                     | The minimum number of cores that a node must have for the job to run on it. See [**ISchedulerJob.MinCoresPerNode**](ischedulerjob-mincorespernode.md).<br/>                                                                                                                                                                                   |
| MinMaxUpdateTime         | string                                                  | The last time that the server checked the computed minimum and maximum resource values for the job. See [JobPropertyIds.MinMaxUpdateTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.minmaxupdatetime.aspx).<br/>                                                                                    |
| MinMemory                | int                                                     | The maximum amount of memory that a node may have for the job to run on it. See [**ISchedulerJob.MinMemory**](ischedulerjob-minmemory.md).<br/>                                                                                                                                                                                               |
| MinNodes                 | int                                                     | The minimum number of nodes that the job requires to run. See [**ISchedulerJob.MinimumNumberOfNodes**](ischedulerjob-minimumnumberofnodes.md).<br/>                                                                                                                                                                                           |
| MinSockets               | int                                                     | The minimum number of sockets that the job requires to run. See [**ISchedulerJob.MinimumNumberOfSockets**](ischedulerjob-minimumnumberofsockets.md).<br/>                                                                                                                                                                                     |
| Name                     | string                                                  | The display name of the job. See [**ISchedulerJob.Name**](ischedulerjob-name.md).<br/>                                                                                                                                                                                                                                                        |
| NextTaskNiceID           | int                                                     | The sequential task identifier that will be given to the next task that is added to the job. See [JobPropertyIds.NextJobTaskId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.nextjobtaskid.aspx).<br/>                                                                                                 |
| NodeGroups               | string                                                  | A semicolon-delimited list of the node group names that identify the nodes on which the job can run. See [**ISchedulerJob.NodeGroups**](ischedulerjob-nodegroup.md).<br/>                                                                                                                                                                     |
| NumberOfCalls            | int                                                     | The number of web-service calls made in the session. See [JobPropertyIds.NumberOfCalls](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.numberofcalls.aspx).<br/>                                                                                                                                         |
| NumberOfOutstandingCalls | int                                                     | The number of web-service calls to which the broker as not yet replied to the client. See [JobPropertyIds.NumberOfOutstandingCalls](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.numberofoutstandingcalls.aspx).<br/>                                                                                  |
| OrderBy                  | string                                                  | The preference given to the order in which the job is scheduled on nodes. See [**ISchedulerJob.OrderBy**](ischedulerjob-orderby.md).<br/>                                                                                                                                                                                                     |
| Owner                    | string                                                  | The name of the user who created, submitted, or queued the job. See [**ISchedulerJob.Owner**](ischedulerjob-owner.md).<br/>                                                                                                                                                                                                                   |
| OwnerId                  | int                                                     | An identifier that identifies the owner of the job. For internal use only.<br/>                                                                                                                                                                                                                                                                |
| ParentJobId              | int                                                     | An identifier that uniquely identifies the parent job. See [JobPropertyIds.ParentJobId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.parentjobid.aspx).<br/>                                                                                                                                           |
| PendingReason            | string                                                  | The reason the job has not yet run. See [JobPropertyIds.PendingReason](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.pendingreason.aspx).<br/>                                                                                                                                                          |
| Preemptable              | boolean                                                 | Determines whether the job can be preempted by a higher priority job. See [**ISchedulerJob.CanPreempt**](ischedulerjob-canpreempt.md).<br/>                                                                                                                                                                                                   |
| PreviousState            | [**JobState**](jobschema-jobstate-simpletype.md)       | The previous state of the job. See [**ISchedulerJob.PreviousState**](ischedulerjob-previousstate.md).<br/>                                                                                                                                                                                                                                    |
| Priority                 | [**JobPriority**](jobschema-jobpriority-simpletype.md) | The priority at which to run the job. See [**ISchedulerJob.Priority**](ischedulerjob-priority.md).<br/>                                                                                                                                                                                                                                       |
| ProcessIds               | string                                                  | A comma-delimited list of the process identifiers associated with the job. See [JobPropertyIds.ProcessIds](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.processids.aspx).<br/>                                                                                                                         |
| Project                  | string                                                  | The project name to associate with the job. See [**ISchedulerJob.Project**](ischedulerjob-project.md).<br/>                                                                                                                                                                                                                                   |
| ProjectId                | int                                                     | An identifier that identifies the project. For internal use only.<br/>                                                                                                                                                                                                                                                                         |
| RequestCancel            | string                                                  | Indicates that a cancel request is pending for the job. See [JobPropertyIds.RequestCancel](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.requestcancel.aspx).<br/>                                                                                                                                      |
| RequestedNodes           | string                                                  | A semicolon-delimited list of nodes on which the job can run. See [**ISchedulerJob.RequestedNodes**](ischedulerjob-requestednodes.md).<br/>                                                                                                                                                                                                   |
| RequeueCount             | int                                                     | The number of times that the job has been queued again. See [**ISchedulerJob.RequeueCount**](ischedulerjob-requeuecount.md).<br/>                                                                                                                                                                                                             |
| RequiredNodes            | string                                                  | A semicolon-delimited list of nodes on which the tasks in the job are required to run. See [JobPropertyIds.RequiredNodes](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.requirednodes.aspx).<br/>                                                                                                       |
| RuntimeSeconds           | int                                                     | The run-time limit for the job. See [**ISchedulerJob.Runtime**](ischedulerjob-runtime.md).<br/>                                                                                                                                                                                                                                               |
| RunUntilCanceled         | boolean                                                 | Determines whether the server reserves resources for the job until the job is canceled. See [**ISchedulerJob.RunUntilCanceled**](ischedulerjob-rununtilcanceled.md).<br/>                                                                                                                                                                     |
| ServiceName              | string                                                  | The name of the SOA service that runs on the nodes of the cluster. See [JobPropertyIds.ServiceName](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.servicename.aspx).<br/>                                                                                                                               |
| SoftwareLicense          | string                                                  | A comma-delimited list of software licensing requirements for the job. The format is *string*:*integer*{,*string*:*integer*}, where each string is the name of an application and each integer represents how many licenses for the application are required. See [**ISchedulerJob.SoftwareLicense**](ischedulerjob-softwarelicense.md).<br/> |
| StartTime                | string                                                  | The time that the job started running. See [**ISchedulerJob.StartTime**](ischedulerjob-starttime.md).<br/>                                                                                                                                                                                                                                    |
| State                    | [**JobState**](jobschema-jobstate-simpletype.md)       | The state of the job. See [**ISchedulerJob.State**](ischedulerjob-state.md).<br/>                                                                                                                                                                                                                                                             |
| SubmitTime               | string                                                  | The time that the job was submitted. See [**ISchedulerJob.SubmitTime**](ischedulerjob-submittime.md).<br/>                                                                                                                                                                                                                                    |
| TaskLevelUpdateTime      | string                                                  | The last time that the Scheduler computed the maximum and minimum resource values. See [JobPropertyIds.TaskLevelUpdateTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.tasklevelupdatetime.aspx).<br/>                                                                                               |
| UnitType                 | [**UnitType**](jobschema-unittype-simpletype.md)       | Specifies whether cores, nodes, or sockets are used to allocate resources for the job. See [**ISchedulerJob.UnitType**](ischedulerjob-unittype.md).<br/>                                                                                                                                                                                      |
| UserName                 | string                                                  | The name of the RunAs user for the job. See [**ISchedulerJob.UserName**](ischedulerjob-username.md).<br/>                                                                                                                                                                                                                                     |
| Version                  | decimal                                                 | The file version of the HPC server assembly. The decimal value is in the form, *Major*.*Minor*. See [**IScheduler::GetServerVersion**](ischeduler-getserverversion.md).<br/>                                                                                                                                                                  |
| WaitTime                 | int                                                     | The amount of time that the job has been or is waiting to run. See [JobPropertyIds.WaitTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.waittime.aspx).<br/>                                                                                                                                         |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




