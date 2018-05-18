---
Description: 'Deletes a pool on a cluster based on the supplied name. An exception is thrown if the pool doesn’t exist.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4EE08EE0-83E8-467B-ACAA-3D656B76C695'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::DeletePool method'
---

# IScheduler::DeletePool method

Deletes a pool on a cluster based on the supplied name. An exception is thrown if the pool doesn’t exist.

## Syntax


```C++
HRESULT DeletePool(
  [in] BSTR         *poolName,
  [in] VARIANT_BOOL force
);
```



## Parameters

<dl> <dt>

*poolName* \[in\]
</dt> <dd>

The name of the pool on the cluster that will be deleted.

</dd> <dt>

*force* \[in\]
</dt> <dd>

If VARIANT\_TRUE, all job templates that reference the pool are moved to the default pool in addition to any jobs that use that template. After the job templates and jobs are moved to the default pool, the pool is deleted. If VARIANT\_FALSE, the pool is only deleted if no job template uses that pool. If a job template is currently using the pool, an exception is thrown.

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
</dt> </dl>

 

 




