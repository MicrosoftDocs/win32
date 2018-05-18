---
Description: 'Retrieves the specified item from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bea9733e-8dab-440c-b3e4-75fce84ec5b2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IFilterCollection::Item property'
---

# IFilterCollection::Item property

Retrieves the specified item from the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long index,
  [out] IFilterProperty **pItem
);
```



## Property value

An [**IFilterProperty**](ifilterproperty.md) interface that defines the filter.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Because the filter objects are opaque objects do not try to enumerate the filters in the collection.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IFilterCollection**](ifiltercollection.md)
</dt> <dt>

[**IFilterCollection::GetEnumerator**](ifiltercollection-getenumerator.md)
</dt> </dl>

 

 




