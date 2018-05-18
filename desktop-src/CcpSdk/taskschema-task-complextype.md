---
Description: 'Defines a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3ec8f6bc-7a20-4b5c-9948-0326167d85d8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Task Complex Type
---

# Task Complex Type

Defines a task.

``` syntax
<xs:complexType name="Task">
    <xs:sequence>
        <xs:element name="EnvironmentVariables"
            type="NameValueCollection"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="CustomProperties"
            type="NameValueCollection1"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="ExtendedTerms"
            type="NameValueCollection1"
            minOccurs="0"
            maxOccurs="1"
         />
    </xs:sequence>
    <xs:attribute name="Version"
        type="decimal"
     />
    <xs:attribute name="Name"
        type="string"
     />
    <xs:attribute name="State"
        type="TaskState"
        default="Configuring"
     />
    <xs:attribute name="PreviousState"
        type="TaskState"
        default="Configuring"
     />
    <xs:attribute name="ParentJobId"
        type="int"
        default="0"
     />
    <xs:attribute name="RuntimeSeconds"
        type="int"
     />
    <xs:attribute name="InstanceId"
        type="int"
     />
    <xs:attribute name="InstanceValue"
        type="int"
     />
    <xs:attribute name="UnitType"
        type="UnitType"
        default="Core"
     />
    <xs:attribute name="MinCores"
        type="int"
        default="1"
     />
    <xs:attribute name="MaxCores"
        type="int"
        default="1"
     />
    <xs:attribute name="MinNodes"
        type="int"
        default="1"
     />
    <xs:attribute name="MaxNodes"
        type="int"
        default="1"
     />
    <xs:attribute name="MinSockets"
        type="int"
        default="1"
     />
    <xs:attribute name="MaxSockets"
        type="int"
        default="1"
     />
    <xs:attribute name="NiceId"
        type="int"
     />
    <xs:attribute name="Id"
        type="int"
        default="0"
     />
    <xs:attribute name="CommandLine"
        type="string"
     />
    <xs:attribute name="RequiredNodes"
        type="string"
     />
    <xs:attribute name="DependsOn"
        type="string"
     />
    <xs:attribute name="IsParametric"
        type="boolean"
        default="false"
     />
    <xs:attribute name="IsExclusive"
        type="boolean"
        default="false"
     />
    <xs:attribute name="IsRerunnable"
        type="boolean"
        default="true"
     />
    <xs:attribute name="ErrorMessage"
        type="string"
     />
    <xs:attribute name="ExitCode"
        type="int"
        default="0"
     />
    <xs:attribute name="GroupId"
        type="int"
     />
    <xs:attribute name="StdOutFilePath"
        type="string"
     />
    <xs:attribute name="StdInFilePath"
        type="string"
     />
    <xs:attribute name="StdErrFilePath"
        type="string"
     />
    <xs:attribute name="WorkDirectory"
        type="string"
     />
    <xs:attribute name="StartValue"
        type="int"
     />
    <xs:attribute name="EndValue"
        type="int"
     />
    <xs:attribute name="IncrementValue"
        type="int"
     />
    <xs:attribute name="Output"
        type="string"
     />
    <xs:attribute name="RequestCancel"
        type="string"
     />
    <xs:attribute name="Closed"
        type="boolean"
     />
    <xs:attribute name="RequeueCount"
        type="int"
     />
    <xs:attribute name="FailureReason"
        type="string"
     />
    <xs:attribute name="PendingReason"
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
    <xs:attribute name="ErrorCode"
        type="int"
     />
    <xs:attribute name="ErrorParams"
        type="string"
     />
    <xs:attribute name="ParentJobState"
        type="JobState"
        default="Configuring"
     />
    <xs:attribute name="AutoRequeueCount"
        type="int"
     />
    <xs:attribute name="TaskOwner"
        type="string"
        default="Infinite"
     />
    <xs:attribute name="ProcessIds"
        type="string"
        default="Infinite"
     />
    <xs:attribute name="RecordId"
        type="int"
     />
    <xs:attribute name="ParametricRunningCount"
        type="int"
     />
    <xs:attribute name="ParametricCanceledCount"
        type="int"
     />
    <xs:attribute name="ParametricFailedCount"
        type="int"
     />
    <xs:attribute name="ParametricQueuedCount"
        type="int"
     />
    <xs:attribute name="HasCustomProps"
        type="boolean"
     />
</xs:complexType>
```

## Child elements



| Element                                                                      | Type                                                                        | Description                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CustomProperties**](taskschema-customproperties-task-element.md)         | [**NameValueCollection1**](taskschema-namevaluecollection1-complextype.md) | A collection of custom properties that the submission and activation filters access. See [**ISchedulerTask::GetCustomProperties**](ischedulertask-getcustomproperties.md). <br/>                                                          |
| [**EnvironmentVariables**](taskschema-environmentvariables-task-element.md) | [**NameValueCollection**](taskschema-namevaluecollection-complextype.md)   | A collection of environment variables available to the task. See [**ISchedulerTask.EnvironmentVariables**](ischedulertask-environmentvariables.md).<br/>                                                                                  |
| [**ExtendedTerms**](taskschema-extendedterms-task-element.md)               | [**NameValueCollection1**](taskschema-namevaluecollection1-complextype.md) | Do not use. Use [**CustomProperties**](taskschema-customproperties-task-element.md) instead.<br/> **Microsoft Compute Cluster Server 2003:** A collection of extended terms that the submission and activation filters access.<br/> |



## Attributes



| Name                    | Type                                                 | Description                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoRequeueCount        | int                                                  | The number of times that the system reran the task when a system error occurred. See [TaskPropertyIds.AutoRequeueCount](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.autorequeuecount.aspx).<br/>     |
| ChangeTime              | string                                               | The last time that the user or server changed a property of the task. See [**ISchedulerTask.ChangeTime**](ischedulertask-changetime.md).<br/>                                                                                                 |
| Closed                  | boolean                                              | Indicates whether the task was closed. See [ITaskPropertyIds.Closed](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.closed.aspx).<br/>                                                                  |
| CommandLine             | string                                               | The command line for the task. See [**ISchedulerTask.CommandLine**](ischedulertask-commandline.md).<br/>                                                                                                                                      |
| CreateTime              | string                                               | The time that the task was created. See [**ISchedulerTask.CreateTime**](ischedulertask-createtime.md).<br/>                                                                                                                                   |
| DependsOn               | string                                               | A semicolon-delimited list of the tasks on which this task depends. See [**ISchedulerTask.DependsOn**](ischedulertask-dependson.md).<br/>                                                                                                     |
| EndTime                 | string                                               | The time that the task finished running. See [**ISchedulerTask.EndTime**](ischedulertask-endtime.md).<br/>                                                                                                                                    |
| EndValue                | int                                                  | The ending value for a parametric task. See [**ISchedulerTask.EndValue**](ischedulertask-endvalue.md).<br/>                                                                                                                                   |
| ErrorCode               | int                                                  | An error code that identifies the error that occurred while running or trying to run the task. See [TaskPropertyIds.ErrorCode](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.errorcode.aspx).<br/>     |
| ErrorMessage            | string                                               | The task-related error message or the message specified when the user canceled the task. See [**ISchedulerTask.ErrorMessage**](ischedulertask-errormessage.md).<br/>                                                                          |
| ErrorParams             | string                                               | A delimited list of insertion strings that are inserted into the message string. See [TaskPropertyIds.ErrorParams](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.errorparams.aspx).<br/>               |
| ExitCode                | int                                                  | The exit code that the task set. See [**ISchedulerTask.ExitCode**](ischedulertask-exitcode.md).<br/>                                                                                                                                          |
| FailureReason           | string                                               | The reason that the task failed. See [TaskPropertyIds.FailureReason](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.failurereason.aspx).<br/>                                                           |
| GroupId                 | int                                                  | The task group to which the task belongs. See [TaskPropertyIds.GroupId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.groupid.aspx).<br/>                                                              |
| HasCustomProps          | boolean                                              | Determines whether the task contains user-defined properties. See [TaskPropertyIds.HasCustomProperties](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.hascustomproperties.aspx).<br/>                  |
| Id                      | int                                                  | An identifier that uniquely identifies the task within the scheduler store. See [TaskPropertyIds.Id](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.id.aspx).<br/>                                      |
| IncrementValue          | int                                                  | The number by which to increment the instance value for a parametric task. See [**ISchedulerTask.IncrementValue**](ischedulertask-incrementvalue.md).<br/>                                                                                    |
| InstanceId              | int                                                  | An identifier that uniquely identifies the instance of a parametric task in the scheduler store. See [TaskPropertyIds.InstanceId](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.instanceid.aspx).<br/> |
| InstanceValue           | int                                                  | The value used for the parametric instance. See See [TaskPropertyIds.InstanceValue](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.instancevalue.aspx).<br/>                                            |
| IsExclusive             | boolean                                              | Determines whether other tasks from the job can run on the node at the same time as this task. See [**ISchedulerTask.IsExclusive**](ischedulertask-isexclusive.md).<br/>                                                                      |
| IsParametric            | boolean                                              | Determines whether the task is a parametric task. See [**ISchedulerTask.IsParametric**](ischedulertask-isparametric.md).<br/>                                                                                                                 |
| IsRerunnable            | boolean                                              | Determines whether the task can run again after a failure. See [**ISchedulerTask.IsRerunnable**](ischedulertask-isrerunnable.md).<br/>                                                                                                        |
| MaxCores                | int                                                  | The maximum number of cores that the scheduler may allocate for the task. See [**ISchedulerTask.MaximumNumberOfCores**](ischedulertask-maximumnumberofcores.md).<br/>                                                                         |
| MaxNodes                | int                                                  | The maximum number of nodes that the scheduler may allocate for the task. See [**ISchedulerTask.MaximumNumberOfNodes**](ischedulertask-maximumnumberofnodes.md).<br/>                                                                         |
| MaxSockets              | int                                                  | The maximum number of sockets that the scheduler may allocate for the task. See [**ISchedulerTask.MaximumNumberOfSockets**](ischedulertask-maximumnumberofsockets.md).<br/>                                                                   |
| MinCores                | int                                                  | The minimum number of cores that the task requires to run. See [**ISchedulerTask.MinimumNumberOfCores**](ischedulertask-minimumnumberofcores.md).<br/>                                                                                        |
| MinNodes                | int                                                  | The minimum number of nodes that the task requires to run. See [**ISchedulerTask.MinimumNumberOfNodes**](ischedulertask-minimumnumberofnodes.md).<br/>                                                                                        |
| MinSockets              | int                                                  | The minimum number of sockets that the task requires to run. See [**ISchedulerTask.MinimumNumberOfSockets**](ischedulertask-minimumnumberofsockets.md).<br/>                                                                                  |
| Name                    | string                                               | The display name of the task. See [**ISchedulerTask.Name**](ischedulertask-name.md).<br/>                                                                                                                                                     |
| NiceId                  | int                                                  | An identifier that uniquely identifies the task in a job. See the [**JobTaskId**](itaskid-jobtaskid.md) member of [**ISchedulerTask.TaskId**](ischedulertask-taskid.md).<br/>                                                                |
| Output                  | string                                               | The output generated by the task. See [**ISchedulerTask.Output**](ischedulertask-output.md).<br/>                                                                                                                                             |
| ParametricCanceledCount | int                                                  | The number of parametric tasks that were canceled. <br/>                                                                                                                                                                                       |
| ParametricFailedCount   | int                                                  | The number of parametric tasks that failed. <br/>                                                                                                                                                                                              |
| ParametricQueuedCount   | int                                                  | The number of parametric tasks that are queued. <br/>                                                                                                                                                                                          |
| ParametricRunningCount  | int                                                  | The number of parametric tasks that are running. <br/>                                                                                                                                                                                         |
| ParentJobId             | int                                                  | The identifier of the parent job. See [**ISchedulerTask.ParentJobId**](ischedulertask-parentjobid.md).<br/>                                                                                                                                   |
| ParentJobState          | [**JobState**](taskschema-jobstate-simpletype.md)   | The state of the job that contains this task. See [TaskPropertyIds.ParentJobState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.parentjobstate.aspx).<br/>                                            |
| PendingReason           | string                                               | The reason that the task is pending. See [TaskPropertyIds.PendingReason](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.pendingreason.aspx).<br/>                                                       |
| PreviousState           | [**TaskState**](taskschema-taskstate-simpletype.md) | The previous state of the task. See [**ISchedulerTask.PreviousState**](ischedulertask-previousstate.md).<br/>                                                                                                                                 |
| ProcessIds              | string                                               | A command-delimited list of the process identifiers associated with the task. See [TaskPropertyIds.ProcessIds](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.processids.aspx).<br/>                    |
| RecordId                | int                                                  | For internal use only. <br/>                                                                                                                                                                                                                   |
| RequestCancel           | string                                               | Indicates whether the user has requested that the task be canceled. See [ITaskPropertyIds.RequestCancel](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.requestcancel.aspx).<br/>                       |
| RequeueCount            | int                                                  | The number of times that the task has been queued again. See [**ISchedulerTask.RequeueCount**](ischedulertask-requeuecount.md).<br/>                                                                                                          |
| RequiredNodes           | string                                               | A semicolon-delimited list of the nodes that the task requires. See [**ISchedulerTask.RequiredNodes**](ischedulertask-requirednodes.md).<br/>                                                                                                 |
| RuntimeSeconds          | int                                                  | The run-time limit for the task. See [**ISchedulerTask.Runtime**](ischedulertask-runtime.md).<br/>                                                                                                                                            |
| StartTime               | string                                               | The time that the task started running. See [**ISchedulerTask.StartTime**](ischedulertask-starttime.md).<br/>                                                                                                                                 |
| StartValue              | int                                                  | The starting instance value for a parametric task. See [**ISchedulerTask.StartValue**](ischedulertask-startvalue.md).<br/>                                                                                                                    |
| State                   | [**TaskState**](taskschema-taskstate-simpletype.md) | The state of the task. See [**ISchedulerTask.State**](ischedulertask-state.md).<br/>                                                                                                                                                          |
| StdErrFilePath          | string                                               | The path to which the server redirects standard error. See [**ISchedulerTask.StdErrFilePath**](ischedulertask-stderrfilepath.md).<br/>                                                                                                        |
| StdInFilePath           | string                                               | The path from which the server redirects standard input. See [**ISchedulerTask.StdInFilePath**](ischedulertask-stdinfilepath.md).<br/>                                                                                                        |
| StdOutFilePath          | string                                               | The path to which the server redirects standard output. See [**ISchedulerTask.StdOutFilePath**](ischedulertask-stdoutfilepath.md).<br/>                                                                                                       |
| SubmitTime              | string                                               | The time that the task was submitted. See [**ISchedulerTask.SubmitTime**](ischedulertask-submittime.md).<br/>                                                                                                                                 |
| TaskOwner               | string                                               | The owner of the task. See [TaskPropertyIds.TaskOwner](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.taskpropertyids.taskowner.aspx).<br/>                                                                             |
| UnitType                | [**UnitType**](taskschema-unittype-simpletype.md)   | Determines whether cores, nodes, or sockets are used to allocate resources for the task. See [**ISchedulerJob.UnitType**](ischedulerjob-unittype.md).<br/>                                                                                    |
| Version                 | decimal                                              | The file version of the HPC server assembly. The decimal value is in the form, *Major*.*Minor*. See [**IScheduler::GetServerVersion**](ischeduler-getserverversion.md).<br/>                                                                  |
| WorkDirectory           | string                                               | The directory in which to start the task. See [**ISchedulerTask.WorkDirectory**](ischedulertask-workdirectory.md).<br/>                                                                                                                       |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




