---
Description: 'Retrieves an enumerator that you use to enumerate the items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '163c75f6-3e56-40f3-b830-403925b2bb47'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IStringCollection::GetEnumerator method'
---

# IStringCollection::GetEnumerator method

Retrieves an enumerator that you use to enumerate the items in the collection.

## Syntax


```C++
HRESULT GetEnumerator(
  [out] IEnumVARIANT **pEnum
);
```



## Parameters

<dl> <dt>

*pEnum* \[out\]
</dt> <dd>

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the items in the collection. Each item in the collection is a VARIANT of type VT\_BSTR. Access the **bstrVal** member to get the string.

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

[**IStringCollection**](istringcollection.md)
</dt> <dt>

[**IStringCollection.Item**](istringcollection-item.md)
</dt> </dl>

 

 




