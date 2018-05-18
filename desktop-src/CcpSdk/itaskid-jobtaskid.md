---
Description: 'Retrieves the sequential identifier that identifies the task in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f4554374-9480-448c-a66d-5c96a4c67c4f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITaskId::JobTaskId property'
---

# ITaskId::JobTaskId property

Retrieves the sequential identifier that identifies the task in the job.

This property is read-only.

## Syntax


```C++
HRESULT get_JobTaskId(
  [out] long *pJobTaskId
);
```



## Property value

The display task identifier.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Typically, you use this identifier for display. If the task is a parametric task, you use this identifier with the [**InstanceId**](itaskid-instanceid.md) identifier to create a display identifier for the task (for example, *JobTaskId*.*InstanceId*).

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

 

 




