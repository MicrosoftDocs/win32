---
Description: 'Creates an empty collection to which you add sort properties.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bb34e592-8cbc-4d09-a6e2-b2a7363edabf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateSortCollection method'
---

# IScheduler::CreateSortCollection method

Creates an empty collection to which you add sort properties.

## Syntax


```C++
HRESULT CreateSortCollection(
  [out] ISortCollection **pCollection
);
```



## Parameters

<dl> <dt>

*pCollection* \[out\]
</dt> <dd>

An [**ISortCollection**](isortcollection.md) interface to which you add sort properties.

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

[**IScheduler::CreateFilterCollection**](ischeduler-createfiltercollection.md)
</dt> </dl>

 

 




