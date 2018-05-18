---
Description: 'Retrieves the job identifier.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'dc5c0014-4cac-4f1c-ac2a-2f3b74cd0c83'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Id property'
---

# ISchedulerJob::Id property

Retrieves the job identifier.

This property is read-only.

## Syntax


```C++
HRESULT get_Id(
  [out] long *pId
);
```



## Property value

The job identifier.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The identifier is set when you call the [**IScheduler::AddJob**](ischeduler-addjob.md) method to add the job to the scheduler. The [**ISchedulerJob::SubmitJob**](ischeduler-submitjob.md) method will also set the identifier if the job has not been added to the scheduler.

## Examples

For an example, see [Creating a Parametric Sweep Task](creating-parametric-sweep-task.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




