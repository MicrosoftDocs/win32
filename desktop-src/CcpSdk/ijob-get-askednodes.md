---
Description: 'Retrieves the list of nodes that are requested for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f1563f04-1dc7-4af4-8490-4a6d05026c74'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_AskedNodes method'
---

# IJob::get\_AskedNodes method

Retrieves the list of nodes that are requested for the job.

## Syntax


```C++
HRESULT get_AskedNodes(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The comma-delimited list of node names.

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

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::put\_AskedNodes**](ijob-put-askednodes.md)
</dt> <dt>

[**ITask::put\_RequiredNodes**](itask-put-requirednodes.md)
</dt> </dl>

 

 




