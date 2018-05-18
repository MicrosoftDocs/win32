---
Description: 'Creates an empty collection to which you can add name/value pairs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1fa7d4d7-185b-4d06-b56b-0e5912e26306'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateNameValueCollection method'
---

# IScheduler::CreateNameValueCollection method

Creates an empty collection to which you can add name/value pairs.

## Syntax


```C++
HRESULT CreateNameValueCollection(
  [out] INameValueCollection **pCollection
);
```



## Parameters

<dl> <dt>

*pCollection* \[out\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection2.md) interface to which you can add name/value pairs.

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

 

 




