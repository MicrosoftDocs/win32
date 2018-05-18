---
Description: 'Adds a name/value pair to the end of the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '494e186e-9cd0-4527-861e-4750fea12869'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::Add method'
---

# INameValueCollection::Add method

Adds a name/value pair to the end of the collection.

## Syntax


```C++
HRESULT Add(
  [in] VARIANT obj
);
```



## Parameters

<dl> <dt>

*obj* \[in\]
</dt> <dd>

The name/value object.

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

 

 




