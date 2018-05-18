---
Description: 'Creates a name/value pair and adds it to the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fc43b59a-0346-4294-80f3-a23be0f21139'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::Set method'
---

# INameValueCollection::Set method

Creates a name/value pair and adds it to the collection.

## Syntax


```C++
HRESULT Set(
  [in] BSTR Name,
  [in] BSTR Value
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The value.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

This method searches for the first occurrence of the name. If the name is found, the method replaces the value; otherwise, the name/value pair is added to the end of the collection.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INameValueCollection**](inamevaluecollection.md)
</dt> </dl>

 

 




