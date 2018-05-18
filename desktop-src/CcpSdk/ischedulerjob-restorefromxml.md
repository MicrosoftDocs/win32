---
Description: 'Overwrites the properties and tasks of the job using the XML at the specified URL.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '78d9b741-950d-49fa-9e15-792af3980c59'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::RestoreFromXml method'
---

# ISchedulerJob::RestoreFromXml method

Overwrites the properties and tasks of the job using the XML at the specified URL.

## Syntax


```C++
HRESULT RestoreFromXml(
  [in] BSTR url
);
```



## Parameters

<dl> <dt>

*url* \[in\]
</dt> <dd>

The URL of the XML file that contains the job properties and tasks that are used to update the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

Typically, you call this method when the job is in the Configuring state. The method changes the values of the local copy. To save the changes, call the [**ISchedulerJob::Commit**](ischedulerjob-commit.md) method.

The method uses the following [**Job**](jobschema-job-complextype.md) attributes from the XML file to overwrite the properties with the similar name in the job:

-   AutoCalculateMax
-   AutoCalculateMin
-   FailOnTaskFailure
-   IsExclusive
-   JobTemplate
-   MaxCores
-   MaxCoresPerNode
-   MaxMemory
-   MaxNodes
-   MaxSockets
-   MinCores
-   MinCoresPerNode
-   MinMemory
-   MinNodes
-   MinSockets
-   Name
-   NodeGroups
-   OrderBy
-   Priority
-   Project
-   RequestedNodes
-   RuntimeSeconds
-   RunUntilCanceled
-   SoftwareLicense
-   UnitType
-   UserName

The method uses the following [**Task**](jobschema-task-complextype.md) attributes from the XML file to overwrite the properties with the similar name in the task:

-   CommandLine
-   DependsOn
-   EndValue
-   IncrementValue
-   IsExclusive
-   IsParametric
-   IsRerunnable
-   MaxCores
-   MaxNodes
-   MaxSockets
-   MinCores
-   MinNodes
-   MinSockets
-   Name
-   RequiredNodes
-   RuntimeSeconds
-   StartValue
-   StdErrFilePath
-   StdInFilePath
-   StdOutFilePath
-   WorkDirectory

For details of the schema, see [Job Schema](jobschema-schema.md) and [Task Schema](taskschema-schema.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**IScheduler::CloneJob**](ischeduler-clonejob.md)
</dt> </dl>

 

 




