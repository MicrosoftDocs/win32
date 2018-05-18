---
Description: 'Retrieves the specified item from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c8956751-c447-4df2-9f23-b4c5477003ad'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISortCollection::Item property'
---

# ISortCollection::Item property

Retrieves the specified item from the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long index,
  [out] VARIANT *pItem
);
```



## Property value

The specified item from the collection. The item is a VARIANT of type VT\_DISPATCH. Query the **pdispVal** member for the [**ISortProperty**](isortproperty.md) interface.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Because the sort objects are opaque, you should not retrieve the sort objects from the collection.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISortCollection**](isortcollection.md)
</dt> <dt>

[**ISortCollection::GetEnumerator**](isortcollection-getenumerator.md)
</dt> </dl>

 

 




