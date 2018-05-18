---
Description: 'Adds an item to the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7bf83ed3-d460-4e42-a46c-a514b55ed0f6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISortCollection::Add method'
---

# ISortCollection::Add method

Adds an item to the collection.

## Syntax


```C++
HRESULT Add(
  [in] order  order,
  [in] PropId propertyId
);
```



## Parameters

<dl> <dt>

*order* \[in\]
</dt> <dd>

The order in which the objects are returned (for example, ascending or descending). For possible values, see the [**SortOrder**](sortorder.md) enumeration.

</dd> <dt>

*propertyId* \[in\]
</dt> <dd>

An identifier that uniquely identifies the property on which the returned list is sorted. For possible values, see the [**PropId**](propid.md) enumeration.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The order in which you add the properties to the collection determines the sort order of the results. For example, the first property is the primary sort key, the second property is the secondary sort key, and so on.

## Examples

For an example, see [Filtering and Sorting Lists of Objects](filtering-and-sorting-lists-of-objects.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISortCollection**](isortcollection.md)
</dt> </dl>

 

 




