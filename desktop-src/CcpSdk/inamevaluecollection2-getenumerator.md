---
Description: 'Retrieves an enumerator that you use to enumerate the name/value pairs in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2b68a047-6711-4828-80e2-3c06e8a2d10b'
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

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the name/value pairs in the collection. The items of the enumeration are variants of type VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue2.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INameValueCollection**](inamevaluecollection2.md)
</dt> <dt>

[**INameValueCollection.Count**](inamevaluecollection2-count.md)
</dt> </dl>

 

 




