---
Description: 'Defines a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7f250dee-6bbc-45ba-91b4-1d2a094efd2b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Job
---

# Job

Defines a job.

``` syntax
<xs:complexType name="Job">
    <xs:sequence>
        <xs:element name="ExtendedTerms"
            type="NameValueCollection"
            minOccurs="1"
            maxOccurs="1"
            nillable="true"
         />
        <xs:element name="Tasks"
            type="ArrayOfTask"
            minOccurs="1"
            maxOccurs="1"
            nillable="true"
         />
    </xs:sequence>
    <xs:attribute name="AllocatedNodes"
        type="string"
        default=""
     />
    <xs:attribute name="AskedNodes"
        type="string"
        default=""
     />
    <xs:attribute name="Id"
        type="int"
        default="0"
     />
    <xs:attribute name="IsBackfill"
        type="boolean"
        default="false"
     />
    <xs:attribute name="IsExclusive"
        type="boolean"
        default="true"
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
    <xs:attribute name="SubmittedBy"
        type="string"
        default=""
     />
    <xs:attribute name="Priority"
        type="JobPriority"
        default="Normal"
     />
    <xs:attribute name="Project"
        type="string"
        default=""
     />
    <xs:attribute name="RunUntilCanceled"
        type="boolean"
        default="false"
     />
    <xs:attribute name="Runtime"
        type="string"
        default="Infinite"
     />
    <xs:attribute name="SoftwareLicense"
        type="string"
        default=""
     />
    <xs:attribute name="Status"
        type="JobStatus"
        default="NotSubmitted"
     />
    <xs:attribute name="User"
        type="string"
        default=""
     />
</xs:complexType>
```

## Child elements



| Element                                                   | Type                                                                  | Description                                                                                                                                                                                                                                        |
|-----------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExtendedTerms**](schema-extendedterms-job-element.md) | [**NameValueCollection**](schema-namevaluecollection-complextype.md) | Contains zero or more extended job terms. Extended job terms are application-defined terms that can be accessed by the submission and activation filters. For details, see [**IJob::SetExtendedJobTerm**](ijob-setextendedjobterm.md).<br/> |
| [**Tasks**](schema-tasks-job-element.md)                 | [**ArrayOfTask**](schema-arrayoftask-complextype.md)                 | Contains the tasks to run.<br/>                                                                                                                                                                                                              |



## Attributes



| Name                      | Type                                                              | Description                                                                                                                                                                                                                                                                                                                         |
|---------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AllocatedNodes            | [string](https://msdn.microsoft.com/library/system.string.aspx)   | Comma-delimited list of nodes that are allocated to the job. For details, see [**IResourceUsage::get\_AllocatedNodes**](iresourceusage-get-allocatednodes.md). The attribute is passed to the activation filter but is ignored when calling the [**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md) method.<br/> |
| AskedNodes                | [string](https://msdn.microsoft.com/library/system.string.aspx)   | Comma-delimited list of requested nodes. For details, see [**IJob::put\_AskedNodes**](ijob-put-askednodes.md).<br/>                                                                                                                                                                                                          |
| ErrorMessage              | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The job error message set when a run-time error occurs or the job is canceled. For details, see [**IJob::get\_ErrorMessage**](ijob-get-errormessage.md).<br/>                                                                                                                                                                |
| Id                        | [int](https://msdn.microsoft.com/library/system.int32.aspx)       | The job identifier. This attribute is ignored when calling the [**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md) method. Treat this attribute as read-only. For details, see [**IJob::get\_Id**](ijob-get-id.md).<br/>                                                                                         |
| IsBackfill                | [boolean](https://msdn.microsoft.com/library/system.boolean.aspx) | Indicates whether the job is running as a backfill job. For details, see [**IJob::get\_IsBackfill**](ijob-get-isbackfill.md). The attribute is passed to the activation filter but is ignored when calling the [**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md) method.<br/>                                  |
| IsExclusive               | [boolean](https://msdn.microsoft.com/library/system.boolean.aspx) | Indicates whether nodes should be exclusively allocated to the job. For details, see [**IJob::put\_IsExclusive**](ijob-put-isexclusive.md).<br/>                                                                                                                                                                             |
| MaximumNumberOfProcessors | [int](https://msdn.microsoft.com/library/system.int32.aspx)       | The maximum number of processors required by the job. For details, see [**IJob::put\_MaximumNumberOfProcessors**](ijob-put-maximumnumberofprocessors.md).<br/>                                                                                                                                                               |
| MinimumNumberOfProcessors | [int](https://msdn.microsoft.com/library/system.int32.aspx)       | The minimum number of processors required by the job. For details, see [**IJob::put\_MinimumNumberOfProcessors**](ijob-put-minimumnumberofprocessors.md).<br/>                                                                                                                                                               |
| Name                      | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The display name of the job. For details, see [**IJob::put\_Name**](ijob-put-name.md).<br/>                                                                                                                                                                                                                                  |
| Priority                  | [**JobPriority**](schema-jobpriority-simpletype.md)              | The priority of the job related to other jobs in the scheduling queue. For details, see [**IJob::put\_Priority**](ijob-put-priority.md).<br/>                                                                                                                                                                                |
| Project                   | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The project name that is associated with the job for accounting purposes. For details, see [**IJob::put\_Project**](ijob-put-project.md).<br/>                                                                                                                                                                               |
| Runtime                   | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The run-time limit for the job. For details, see [**IJob::put\_Runtime**](ijob-put-runtime.md).<br/>                                                                                                                                                                                                                         |
| RunUntilCanceled          | [boolean](https://msdn.microsoft.com/library/system.boolean.aspx) | Indicates whether the resources allocated to a job are reserved until the job is canceled even when it has no active tasks. For details, see [**IJob::put\_RunUntilCanceled**](ijob-put-rununtilcanceled.md).<br/>                                                                                                           |
| SoftwareLicense           | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The required license features. For details, see [**IJob::put\_SoftwareLicense**](ijob-put-softwarelicense.md).<br/>                                                                                                                                                                                                          |
| Status                    | [**JobStatus**](schema-jobstatus-simpletype.md)                  | The current job status. This attribute is ignored when calling the [**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md) method. For details, see [**IJob::get\_Status**](ijob-get-status.md).<br/>                                                                                                                |
| SubmittedBy               | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The name of the user who submitted the job. For details, see [**IJob::get\_SubmittedBy**](ijob-get-submittedby.md). The attribute is passed to the submission and activation filters but is ignored when calling the [**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md) method.<br/>                            |
| User                      | [string](https://msdn.microsoft.com/library/system.string.aspx)   | The RunAs user for the job, if different from the SubmittedBy user. For details, see [**IJob::put\_User**](ijob-put-user.md).<br/>                                                                                                                                                                                           |



## Remarks

The [**Job**](schema-job-element.md) element is of this type.

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Complex Types](schema-job-complex-types.md)
</dt> </dl>

 

 




