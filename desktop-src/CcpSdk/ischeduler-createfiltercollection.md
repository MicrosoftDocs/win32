---
Description: 'Creates an empty collection to which you add filter properties.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '16879ae4-6255-4b25-9e24-a325e1f38995'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateFilterCollection method'
---

# IScheduler::CreateFilterCollection method

Creates an empty collection to which you add filter properties.

## Syntax


```C++
HRESULT CreateFilterCollection(
  [out] IFilterCollection **pCollection
);
```



## Parameters

<dl> <dt>

*pCollection* \[out\]
</dt> <dd>

An [**IFilterCollection**](ifiltercollection.md) interface to which you add filter properties.

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

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::CreateSortCollection**](ischeduler-createsortcollection.md)
</dt> </dl>

 

 




