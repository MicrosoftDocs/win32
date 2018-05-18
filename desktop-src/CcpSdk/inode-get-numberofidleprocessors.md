---
Description: 'Retrieves the number of idle processors.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f215c46b-78bb-428d-a6ca-55456e2803b4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INode::get\_NumberOfIdleProcessors method'
---

# INode::get\_NumberOfIdleProcessors method

Retrieves the number of idle processors.

## Syntax


```C++
HRESULT get_NumberOfIdleProcessors(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of idle processors.

</dd> </dl>

## Return value

If the method succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INode**](inode.md)
</dt> </dl>

 

 




