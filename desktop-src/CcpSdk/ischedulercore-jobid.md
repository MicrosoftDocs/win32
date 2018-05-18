---
Description: 'Retrieves the identifier of the job running on the core.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '956c42f6-82d6-4576-ac73-60daae642a6a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCore::JobId property'
---

# ISchedulerCore::JobId property

Retrieves the identifier of the job running on the core.

This property is read-only.

## Syntax


```C++
HRESULT get_JobId(
  [out] long *pJobId
);
```



## Property value

The identifier of the job running on the core; otherwise, zero.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

This job identifier and the **ParentJobId** property of [**ISchedulerCore.TaskId**](ischedulercore-taskid.md) will be the same value if a task is running. If the job is reserving resources (the job does not include tasks and the [**RunUntilCanceled**](ischedulerjob-rununtilcanceled.md) property is VARIANT\_TRUE), this identifier will contain the job identifier and the **ParentJobId** property will be zero.

## Examples

For an example, see [Getting a List of Nodes in the Cluster](getting-a-list-of-nodes-in-the-cluster.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerCore**](ischedulercore.md)
</dt> </dl>

 

 




