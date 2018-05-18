---
Description: 'Creates an empty collection to which you add string values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd413cc4e-5c4d-46d7-ac52-cde19ef0d6bf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateStringCollection method'
---

# IScheduler::CreateStringCollection method

Creates an empty collection to which you add string values.

## Syntax


```C++
HRESULT CreateStringCollection(
  [out] IStringCollection **pCollection
);
```



## Parameters

<dl> <dt>

*pCollection* \[out\]
</dt> <dd>

An [**IStringCollection**](istringcollection.md) interface to which you add string values.

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

 

 




