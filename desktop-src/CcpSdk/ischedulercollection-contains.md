---
Description: 'Determines whether the collection contains the specified item.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6b794f1c-56c6-43f6-a4f7-9a967694b7d1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCollection::Contains method'
---

# ISchedulerCollection::Contains method

Determines whether the collection contains the specified item.

## Syntax


```C++
HRESULT Contains(
  [in]  VARIANT      item,
  [out] VARIANT_BOOL *pExists
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

The item to find.

</dd> <dt>

*pExists* \[out\]
</dt> <dd>

Is VARIANT\_TRUE if the item exists; otherwise, VARIANT\_FALSE.

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
</dt> </dl>

 

 




