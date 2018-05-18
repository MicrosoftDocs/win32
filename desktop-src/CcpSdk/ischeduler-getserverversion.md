---
Description: 'Retrieves the file version of the HPC server assembly.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3ea3c72b-029d-41ef-b0e5-ca0489cdf785'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetServerVersion method'
---

# IScheduler::GetServerVersion method

Retrieves the file version of the HPC server assembly.

## Syntax


```C++
HRESULT GetServerVersion(
  [out] IServerVersion **pVersion
);
```



## Parameters

<dl> <dt>

*pVersion* \[out\]
</dt> <dd>

An [**IServerVersion**](iserverversion.md) interface that contains the version information for the HPC server.

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

 

 




