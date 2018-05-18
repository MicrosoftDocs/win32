---
Description: 'Gets a list of all pools on the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '018B9022-972C-4BEF-A69D-88819448E65A'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetPoolList method'
---

# IScheduler::GetPoolList method

Gets a list of all pools on the cluster.

## Syntax


```C++
HRESULT GetPoolList(
  [out] ISchedulerCollection *poolList
);
```



## Parameters

<dl> <dt>

*poolList* \[out\]
</dt> <dd>

The list of all pools on the cluster.

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

 

 




