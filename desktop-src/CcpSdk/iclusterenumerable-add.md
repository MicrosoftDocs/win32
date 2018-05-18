---
Description: 'Adds an object to the end of the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f6a0ea37-b7cb-4e20-b3c8-f824d8fdbb2f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterEnumerable::Add method'
---

# IClusterEnumerable::Add method

Adds an object to the end of the collection.

## Syntax


```C++
HRESULT Add(
  [in] VARIANT item
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

An object to add to the collection.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The collection allows duplicate elements.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IClusterEnumerable**](iclusterenumerable.md)
</dt> <dt>

[**IClusterEnumerable::Remove**](iclusterenumerable-remove.md)
</dt> </dl>

 

 




