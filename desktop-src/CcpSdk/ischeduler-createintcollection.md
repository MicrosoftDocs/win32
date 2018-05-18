---
Description: 'Creates an empty collection to which you add integer values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'edf4f23d-b793-47ed-a78e-259937a8c0a7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateIntCollection method'
---

# IScheduler::CreateIntCollection method

Creates an empty collection to which you add integer values.

## Syntax


```C++
HRESULT CreateIntCollection(
  [out] IIntCollection **pCollection
);
```



## Parameters

<dl> <dt>

*pCollection* \[out\]
</dt> <dd>

An [**IIntCollection**](iintcollection.md) interface to which you add integer values.

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

[**IScheduler**](ischeduler.md)
</dt> </dl>

 

 




