---
Description: 'Retrieves the user-mode processor time that is used by the job or task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9778bc08-d7de-4f3f-945f-0f8263057687'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IResourceUsage::get\_UserProcessorTime method'
---

# IResourceUsage::get\_UserProcessorTime method

Retrieves the user-mode processor time that is used by the job or task.

## Syntax


```C++
HRESULT get_UserProcessorTime(
  [out] __int64 *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The user-mode processor time, in milliseconds.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

For a task, the value is the user-mode processor time used by the task.

For a job, the value is the cumulative user-mode processor time for all tasks in the job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IResourceUsage**](iresourceusage.md)
</dt> </dl>

 

 




