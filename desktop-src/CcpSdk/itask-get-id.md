---
Description: 'Retrieves the task identifier.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3766023e-fd2b-471c-98bc-c77c3f71da5d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_Id method'
---

# ITask::get\_Id method

Retrieves the task identifier.

## Syntax


```C++
HRESULT get_Id(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The task identifier.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The identifier is not generated until you add the job to the cluster. The identifier will be zero if you call the [**IJob::AddTask**](ijob-addtask.md) method to add the task to a job. If you call the [**ICluster::AddTask**](icluster-addtask.md) method to add the task to an existing job, the identifier is generated when you add the task to the job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> </dl>

 

 




