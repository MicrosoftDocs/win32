---
Description: 'Adds an item to the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e378fac0-398a-4f7c-8c10-2480d74ddc20'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCollection::Add method'
---

# ISchedulerCollection::Add method

Adds an item to the collection.

## Syntax


```C++
HRESULT Add(
  [in] VARIANT item
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

The item to add to the collection. The type for all items in the collection must be the same.

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

[**ISchedulerCollection**](ischedulercollection.md)
</dt> <dt>

[**ISchedulerCollection::Remove**](ischedulercollection-remove.md)
</dt> </dl>

 

 




