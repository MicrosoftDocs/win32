---
Description: 'Retrieves an enumerator that you use to enumerate the items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a3620f83-a676-431f-950b-a138a5574b7c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IIntCollection::GetEnumerator method'
---

# IIntCollection::GetEnumerator method

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

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the items in the collection. Each item in the collection is a VARIANT of type VT\_I4. Access the **lVal** member to get the integer.

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

[**IIntCollection**](iintcollection.md)
</dt> <dt>

[**IIntCollection.Item**](iintcollection-item.md)
</dt> </dl>

 

 




