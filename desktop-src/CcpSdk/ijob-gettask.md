---
Description: 'Retrieves the specified task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1649dccd-16f9-4cae-9dfd-d80ac087fd6b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::GetTask method'
---

# IJob::GetTask method

Retrieves the specified task.

## Syntax


```C++
HRESULT GetTask(
  [in]  long  taskId,
  [out] ITask **pRetVal
);
```



## Parameters

<dl> <dt>

*taskId* \[in\]
</dt> <dd>

The task identifier. The [**ITask::get\_Id**](itask-get-id.md) method contains this value.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**ITask**](itask.md) interface that represents the retrieved task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If the job has not been added to the cluster, the identifiers for each task in the job will be zero. If you try to retrieve one of the tasks using zero as the identifier, the method returns the first task in the job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::GetEnumerator**](ijob-getenumerator.md)
</dt> </dl>

 

 




