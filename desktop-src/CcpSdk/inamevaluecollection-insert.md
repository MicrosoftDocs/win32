---
Description: 'Adds a name/value pair to the collection at the specified index.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c5ed92e4-8d1e-402a-b0e2-0379eb5ea1cb'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::Insert method'
---

# INameValueCollection::Insert method

Adds a name/value pair to the collection at the specified index.

## Syntax


```C++
HRESULT Insert(
  [in] long       index,
  [in] INameValue var
);
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

A zero-based index value.

</dd> <dt>

*var* \[in\]
</dt> <dd>

An [**INameValue**](inamevalue.md) interface that contains the name/value pair to add.

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

[**INameValueCollection**](inamevaluecollection.md)
</dt> </dl>

 

 




