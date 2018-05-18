---
Description: 'Opens a pool based on the name of the pool on the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1D02AE67-5791-485A-8415-3FE398C88EC8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::OpenPool method'
---

# IScheduler::OpenPool method

Opens a pool based on the name of the pool on the cluster.

## Syntax


```C++
HRESULT OpenPool(
  [in]  BSTR           *poolName,
  [out] ISchedulerPool *pool
);
```



## Parameters

<dl> <dt>

*poolName* \[in\]
</dt> <dd>

The name of the pool to be opened.

</dd> <dt>

*pool* \[out\]
</dt> <dd>

The pool.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 Service Pack 2 (SP2) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                              |



 

 




