---
Description: 'Removes the name/value pair at the specified index from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e191e9b2-771f-4a2f-825f-4f97ca861719'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::RemoveAt method'
---

# INameValueCollection::RemoveAt method

Removes the name/value pair at the specified index from the collection.

## Syntax


```C++
HRESULT RemoveAt(
  [in] long index
);
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

A zero-based index value.

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

 

 




