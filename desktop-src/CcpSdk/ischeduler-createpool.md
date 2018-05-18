---
Description: 'Creates a pool on a cluster based on the supplied name with a desired weight. An exception is thrown if a pool with the same name exists.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7C1A1592-5BBC-4097-AF9D-1EC04910B576'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreatePool method'
---

# IScheduler::CreatePool method

Creates a pool on a cluster based on the supplied name with a desired weight. An exception is thrown if a pool with the same name exists.

## Syntax


```C++
HRESULT CreatePool(
  [in]  BSTR           *poolName,
  [in]  long           poolWeight,
  [out] ISchedulerPool *pool
);
```



## Parameters

<dl> <dt>

*poolName* \[in\]
</dt> <dd>

The name of the pool that will be created on the cluster.

</dd> <dt>

*poolWeight* \[in\]
</dt> <dd>

The weight of the pool that will be created on the cluster. The pool weight must be greater or equal to 0, otherwise an exception is thrown.

</dd> <dt>

*pool* \[out\]
</dt> <dd>

The new pool.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 Service Pack 2 (SP2) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                              |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::CreatePool**](ischeduler-createpool.md)
</dt> <dt>

[**IScheduler::DeletePool**](ischeduler-deletepool.md)
</dt> <dt>

[**IScheduler::GetPoolList**](ischeduler-getpoollist.md)
</dt> <dt>

[**IScheduler::OpenPool**](ischeduler-openpool.md)
</dt> <dt>

[**Pool Property of ISchedulerJob**](ischedulerjob-pool.md)
</dt> </dl>

 

 




