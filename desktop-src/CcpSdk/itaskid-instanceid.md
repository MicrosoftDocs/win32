---
Description: 'Retrieves the instance identifier of a parametric task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3f84e381-69d4-4173-842f-c1b9f5f03d31'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITaskId::InstanceId property'
---

# ITaskId::InstanceId property

Retrieves the instance identifier of a parametric task.

This property is read-only.

## Syntax


```C++
HRESULT get_InstanceId(
  [out] long *pInstanceId
);
```



## Property value

The instance identifier.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Typically, you use the instance identifier with the [**JobTaskId**](itaskid-jobtaskid.md) identifier to create a display identifier for the task (for example, *JobTaskId*.*InstanceId*).

Use this property only if the [**ISchedulerTask.IsParametric**](ischedulertask-isparametric.md) property is VARIANT\_TRUE.

## Examples

For an example, see [Cloning a Job](cloning-a-job.md).

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITaskId**](itaskid.md)
</dt> </dl>

 

 




