---
Description: 'Adds an item to the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '20ceab56-211b-42c2-a6d6-0e5850a42a28'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IFilterCollection::Add method'
---

# IFilterCollection::Add method

Adds an item to the collection.

## Syntax


```C++
HRESULT Add(
  [in] FilterOperator operator,
  [in] PropId         propertyId,
  [in] VARIANT        value
);
```



## Parameters

<dl> <dt>

*operator* \[in\]
</dt> <dd>

The operator to use when comparing the specified value to the object's property value. For a list of possible operators, see the [**FilterOperator**](filteroperator.md) enumeration.

</dd> <dt>

*propertyId* \[in\]
</dt> <dd>

An identifier that uniquely identifies the property whose value you want to compare. For possible values, see the [**PropId**](propid.md) enumeration.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The value to use in the comparison.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example, see [Filtering and Sorting Lists of Objects](filtering-and-sorting-lists-of-objects.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IFilterCollection**](ifiltercollection.md)
</dt> </dl>

 

 




