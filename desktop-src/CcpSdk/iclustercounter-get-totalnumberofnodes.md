---
Description: 'Retrieves the number of nodes in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bb501133-cba8-42b9-aa8e-e741884143ca'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_TotalNumberOfNodes method'
---

# IClusterCounter::get\_TotalNumberOfNodes method

Retrieves the number of nodes in the cluster.

## Syntax


```C++
HRESULT get_TotalNumberOfNodes(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of nodes in the cluster.

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

 

 




