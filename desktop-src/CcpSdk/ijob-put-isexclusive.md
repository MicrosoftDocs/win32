---
Description: 'Sets whether nodes should be exclusively allocated to the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bf24e34b-6e0b-4729-8914-b7e796d7afbc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_IsExclusive method'
---

# IJob::put\_IsExclusive method

Sets whether nodes should be exclusively allocated to the job.

## Syntax


```C++
HRESULT put_IsExclusive(
  [out] VARIANT_BOOL pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

Set the value to VARIANT\_TRUE if the nodes should be exclusively allocated to the job; otherwise, VARIANT\_FALSE. The default is VARIANT\_TRUE.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If a node is exclusively allocated to a job, the scheduler will not run any other jobs on the node.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_IsExclusive**](ijob-get-isexclusive.md)
</dt> <dt>

[**ITask::put\_IsExclusive**](itask-put-isexclusive.md)
</dt> </dl>

 

 




