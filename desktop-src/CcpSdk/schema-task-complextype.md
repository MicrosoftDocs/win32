---
Description: 'Defines a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f3a6c57c-01fb-4cd5-857e-4bf8e5049858'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Task
---

# Task

Defines a task.

``` syntax
<xs:complexType name="Task">
    <xs:sequence>
        <xs:element name="EnvironmentVariables"
            type="NameValueCollection1"
            minOccurs="1"
            maxOccurs="1"
            nillable="true"
         />
        <xs:element name="ExtendedTerms"
            type="NameValueCollection"
            minOccurs="1"
            maxOccurs="1"
            nillable="true"
         />
    </xs:sequence>
    <xs:attribute name="AllocatedNodes"
        type="string"
        default=""
     />
    <xs:attribute name="RequiredNodes"
        type="string"
        default=""
     />
    <xs:attribute name="CommandLine"
        type="string"
     />
    <xs:attribute name="Depend"
        type="string"
        default=""
     />
    <xs:attribute name="ExitCode"
        type="int"
        default="0"
     />
    <xs:attribute name="Id"
        type="int"
        default="0"
     />
    <xs:attribute name="IsExclusive"
        type="boolean"
        default="false"
     />
    <xs:attribute name="IsRerunnable"
        type="boolean"
        default="false"
     />
    <xs:attribute name="MaximumNumberOfProcessors"
        type="int"
        default="1"
     />
    <xs:attribute name="MinimumNumberOfProcessors"
        type="int"
        default="1"
     />
    <xs:attribute name="ErrorMessage"
        type="string"
        default=""
     />
    <xs:attribute name="Name"
        type="string"
        default=""
     />
    <xs:attribute name="ParentJobId"
        type="int"
        default="0"
     />
    <xs:attribute name="Runtime"
        type="string"
        default="Infinite"
     />
    <xs:attribute name="Status"
        type="TaskStatus"
        default="NotSubmitted"
     />
    <xs:attribute name="Stdin"
        type="string"
        default=""
     />
    <xs:attribute name="Stdout"
        type="string"
        default=""
     />
    <xs:attribute name="Stderr"
        type="string"
        default=""
     />
    <xs:attribute name="WorkDirectory"
        type="string"
        default=""
     />
</xs:complexType>
```

## Child elements



| Element                                                                  | Type                                                                    | Description                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnvironmentVariables**](schema-environmentvariables-task-element.md) | [**NameValueCollection1**](schema-namevaluecollection1-complextype.md) | Contains zero or more environment variables that are made available to the task. For details, see [**ITask::SetEnvironmentVariable**](itask-setenvironmentvariable.md).<br/>                                             |
| [**ExtendedTerms**](schema-extendedterms-task-element.md)               | [**NameValueCollection**](schema-namevaluecollection-complextype.md)   | Contains zero or more application-defined extended task terms. The terms can be accessed by the submission and activation filters. For details, see [**ITask::SetExtendedTaskTerm**](itask-setextendedtaskterm.md).<br/> |



## Attributes



| Name                      | Type                                                              | Description                                                                                                                                                                                                                                                                                                                            |
|---------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AllocatedNodes            | [string](https://msdn.microsoft.com/library/system.string.aspx)   | Comma-delimited list of nodes that are allocated to the task. For details, see [**IResourceUsage::get\_AllocatedNodes**](iresourceusage-get-allocatednodes.md). The attribute is passed to the activation filter but is ignored when calling the [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md) method.<br/> |
| CommandLine               | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The command line for the task. You must specify this attribute. For details, see [**ITask::put\_CommandLine**](itask-put-commandline.md).<br/>                                                                                                                                                                                  |
| Depend                    | [string](https://msdn.microsoft.com/library/system.string.aspx)   | Comma-delimited list of task names that must run before this task can run. For details, see [**ITask::put\_Depend**](itask-put-depend.md).<br/>                                                                                                                                                                                 |
| ErrorMessage              | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The task error message set when a run-time error occurs or the task is canceled. For details, see [**ITask::get\_ErrorMessage**](itask-get-errormessage.md). This attribute is ignored when calling the [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md) method.<br/>                                          |
| ExitCode                  | [int](https://msdn.microsoft.com/library/system.int32.aspx)       | The exit code for the task. This attribute is ignored when calling the [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md) method. For details, see [**ITask::get\_ExitCode**](itask-get-exitcode.md).<br/>                                                                                                       |
| Id                        | [int](https://msdn.microsoft.com/library/system.int32.aspx)       | The task identifier. For details, see [**ITask::get\_Id**](itask-get-id.md). This attribute is ignored when calling the [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md) method. Treat this attribute as read-only.<br/>                                                                                       |
| IsExclusive               | [boolean](https://msdn.microsoft.com/library/system.boolean.aspx) | Indicates whether the task should run exclusively within the job on the node. For details, see [**ITask::put\_IsExclusive**](itask-put-isexclusive.md).<br/>                                                                                                                                                                    |
| IsRerunnable              | [boolean](https://msdn.microsoft.com/library/system.boolean.aspx) | Indicates whether the task can be rerun after a failure. For details, see [**ITask::put\_IsRerunnable**](itask-put-isrerunnable.md).<br/>                                                                                                                                                                                       |
| MaximumNumberOfProcessors | [int](https://msdn.microsoft.com/library/system.int32.aspx)       | The maximum number of processors required by the task. For details, see [**ITask::put\_MaximumNumberOfProcessors**](itask-put-maximumnumberofprocessors.md).<br/>                                                                                                                                                               |
| MinimumNumberOfProcessors | [int](https://msdn.microsoft.com/library/system.int32.aspx)       | The minimum number of processors required by the task. For details, see [**ITask::put\_MinimumNumberOfProcessors**](itask-put-minimumnumberofprocessors.md).<br/>                                                                                                                                                               |
| Name                      | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The display name of the task. For details, see [**ITask::put\_Name**](itask-put-name.md).<br/>                                                                                                                                                                                                                                  |
| ParentJobId               | [int](https://msdn.microsoft.com/library/system.int32.aspx)       | The identifier of the parent job. This attribute is ignored when calling the [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md) method.<br/>                                                                                                                                                                      |
| RequiredNodes             | [string](https://msdn.microsoft.com/library/system.string.aspx)   | Comma-delimited list of required nodes. For details, see [**ITask::put\_RequiredNodes**](itask-put-requirednodes.md).<br/>                                                                                                                                                                                                      |
| Runtime                   | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The run-time limit for the task. For details, see [**ITask::put\_Runtime**](itask-put-runtime.md).<br/>                                                                                                                                                                                                                         |
| Status                    | [**TaskStatus**](schema-taskstatus-simpletype.md)                | The task status. For details, see [**ITask::get\_Status**](itask-get-status.md). This attribute is ignored when calling the [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md) method.<br/>                                                                                                                      |
| Stderr                    | [string](https://msdn.microsoft.com/library/system.string.aspx)   | Path to the file to use for standard error. For details, see [**ITask::put\_Stderr**](itask-put-stderr.md).<br/>                                                                                                                                                                                                                |
| Stdin                     | [string](https://msdn.microsoft.com/library/system.string.aspx)   | Path to the file to use for standard input. For details, see [**ITask::put\_Stdin**](itask-put-stdin.md).<br/>                                                                                                                                                                                                                  |
| Stdout                    | [string](https://msdn.microsoft.com/library/system.string.aspx)   | Path to the file to use for standard output. For details, see [**ITask::put\_Stdout**](itask-put-stdout.md).<br/>                                                                                                                                                                                                               |
| WorkDirectory             | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The startup directory for the task. For details, see [**ITask::put\_WorkDirectory**](itask-put-workdirectory.md).<br/>                                                                                                                                                                                                          |



## Remarks

The [**Task**](schema-task-arrayoftask-element.md) element is of this type.

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Complex Types](schema-job-complex-types.md)
</dt> </dl>

 

 




