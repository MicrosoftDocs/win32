---
Description: 'Retrieves an enumerator that you use to enumerate the items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b326bd6b-43ac-4943-b9a8-e4ebc726efe2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCollection::GetEnumerator method'
---

# ISchedulerCollection::GetEnumerator method

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

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the items in the collection. The items of the enumeration are VARIANTs. The type of the variant depends on the contents of the collection (see the method or property that returned the collection for the type).

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example, see [Enumerating Lists of Objects](enumerating-lists-of-objects.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerCollection**](ischedulercollection.md)
</dt> <dt>

[**ISchedulerCollection.Item**](ischedulercollection-item.md)
</dt> </dl>

 

 




