---
Description: 'Retrieves the list of required nodes for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9c8ff00d-83dc-42bb-8c8f-ee075097e0ac'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_RequiredNodes method'
---

# ITask::get\_RequiredNodes method

Retrieves the list of required nodes for the task.

## Syntax


```C++
HRESULT get_RequiredNodes(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The comma-delimited list of nodes. Returns **NULL** if not set.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::put\_RequiredNodes**](itask-put-requirednodes.md)
</dt> </dl>

 

 




