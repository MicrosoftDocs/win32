---
Description: 'Retrieves the number of nodes in the cluster that are not reachable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e1a8b80b-1da4-45a7-bb65-a5e15fbafe34'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_NumberOfUnreachableNodes method'
---

# IClusterCounter::get\_NumberOfUnreachableNodes method

Retrieves the number of nodes in the cluster that are not reachable.

## Syntax


```C++
HRESULT get_NumberOfUnreachableNodes(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of nodes in the cluster that are not reachable (nodes with the status **NodeStatus\_Unreachable**).

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

[**IClusterCounter**](iclustercounter.md)
</dt> </dl>

 

 




