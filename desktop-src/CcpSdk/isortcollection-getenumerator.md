---
Description: 'Retrieves an enumerator that you use to enumerate the items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '33834de2-4ef6-4b85-862f-b8c677b56d9e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISortCollection::GetEnumerator method'
---

# ISortCollection::GetEnumerator method

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

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the items in the collection. The items of the enumeration are VARIANTs of type VT\_DISPATCH. Query the **pdispVal** member for the [**ISortProperty**](isortproperty.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Because the sort objects are opaque, do not try to enumerate the objects in the collection.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISortCollection**](isortcollection.md)
</dt> <dt>

[**ISortCollection.Item**](isortcollection-item.md)
</dt> </dl>

 

 




