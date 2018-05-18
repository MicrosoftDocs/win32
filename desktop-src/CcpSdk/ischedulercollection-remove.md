---
Description: 'Removes the first occurrence of the specified item from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '552fb8cb-5db1-4b42-9ac3-83ead43e785a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCollection::Remove method'
---

# ISchedulerCollection::Remove method

Removes the first occurrence of the specified item from the collection.

## Syntax


```C++
HRESULT Remove(
  [in]  VARIANT      item,
  [out] VARIANT_BOOL *pIsRemoved
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

The item to remove from the collection.

</dd> <dt>

*pIsRemoved* \[out\]
</dt> <dd>

Is VARIANT\_TRUE if the item is found and removed from the collection; otherwise, VARIANT\_FALSE.

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

[**ISchedulerCollection::Add**](ischedulercollection-add.md)
</dt> <dt>

[**ISchedulerCollection::Clear**](ischedulercollection-clear.md)
</dt> </dl>

 

 




