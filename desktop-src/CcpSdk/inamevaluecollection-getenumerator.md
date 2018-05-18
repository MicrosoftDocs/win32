---
Description: 'Retrieves an enumerator that you use to enumerate the name/value pairs in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7443ee4f-f20f-42e6-acfc-bc750b64d0c0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::GetEnumerator method'
---

# INameValueCollection::GetEnumerator method

Retrieves an enumerator that you use to enumerate the name/value pairs in the collection.

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

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the name/value pairs in the collection. The items of the enumeration are variants whose type is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue.md) interface.

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

 

 




