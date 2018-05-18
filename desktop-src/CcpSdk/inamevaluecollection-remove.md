---
Description: 'Removes a name/value pair from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '867d2f21-a094-4aae-894a-8dcd905943d0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::Remove method'
---

# INameValueCollection::Remove method

Removes a name/value pair from the collection.

## Syntax


```C++
HRESULT Remove(
  [in] BSTR Name
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the name/value pair to remove.

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

 

 




