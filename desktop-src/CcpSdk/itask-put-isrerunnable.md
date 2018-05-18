---
Description: 'Sets whether the task can be rerun after a failure.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '293f494a-e375-499c-9b46-925394b2762b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_IsRerunnable method'
---

# ITask::put\_IsRerunnable method

Sets whether the task can be rerun after a failure.

## Syntax


```C++
HRESULT put_IsRerunnable(
  [in] VARIANT_BOOL Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

Set the value to VARIANT\_TRUE if the task can be rerun after a failure; otherwise, VARIANT\_FALSE. The default is VARIANT\_TRUE.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If this value is VARIANT\_FALSE, you cannot call the [**ICluster::RequeueTask**](icluster-requeuetask.md) method to rerun the task.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_IsRerunnable**](itask-get-isrerunnable.md)
</dt> </dl>

 

 




