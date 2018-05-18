---
Description: 'Sets the list of required nodes for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e2a05786-fa4f-4e0e-b30d-f2391b081d6c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_RequiredNodes method'
---

# ITask::put\_RequiredNodes method

Sets the list of required nodes for the task.

## Syntax


```C++
HRESULT put_RequiredNodes(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

A comma-delimited list of node names.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If the task belongs to a job, the list of required nodes must be a subset of the [**IJob::put\_AskedNodes**](ijob-put-askednodes.md) method, if set.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_RequiredNodes**](itask-get-requirednodes.md)
</dt> <dt>

[**IJob::put\_AskedNodes**](ijob-put-askednodes.md)
</dt> </dl>

 

 




