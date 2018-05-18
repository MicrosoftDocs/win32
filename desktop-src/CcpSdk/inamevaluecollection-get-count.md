---
Description: 'Retrieves the number of items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1f0a16a6-3e57-4f26-beb3-3f185bdfdf93'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::get\_Count method'
---

# INameValueCollection::get\_Count method

Retrieves the number of items in the collection.

## Syntax


```C++
HRESULT get_Count(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of items.

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

 

 




