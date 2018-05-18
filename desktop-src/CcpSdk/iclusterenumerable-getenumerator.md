---
Description: 'Retrieves an enumerator that you use to enumerate the items of the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '41e35152-b814-4f48-a9eb-1c5f8ae19934'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterEnumerable::GetEnumerator method'
---

# IClusterEnumerable::GetEnumerator method

Retrieves an enumerator that you use to enumerate the items of the collection.

## Syntax


```C++
HRESULT GetEnumerator(
  [out] IEnumVARIANT **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the items of the collection.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example that uses this method, see [Getting the List of Nodes in the Cluster](getting-the-list-of-nodes-in-the-cluster.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IClusterEnumerable**](iclusterenumerable.md)
</dt> </dl>

 

 




