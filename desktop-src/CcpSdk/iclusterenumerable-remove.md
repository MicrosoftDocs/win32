---
Description: 'Removes the first occurrence of the object from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '939b016e-0414-41e9-a19c-f0b76aa75f1c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterEnumerable::Remove method'
---

# IClusterEnumerable::Remove method

Removes the first occurrence of the object from the collection.

## Syntax


```C++
HRESULT Remove(
  [in] VARIANT item
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

An object to remove from the collection.

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

[**IClusterEnumerable**](iclusterenumerable.md)
</dt> <dt>

[**IClusterEnumerable::Add**](iclusterenumerable-add.md)
</dt> </dl>

 

 




