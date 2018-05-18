---
Description: 'Returns the name of the job’s pool.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'E686956D-5ACF-4590-A9A1-650F22F0AAB5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Pool property'
---

# ISchedulerJob::Pool property

Returns the name of the job’s pool.

This property is read-only.

## Syntax


```C++
HRESULT get_Pool(
  [out] BSTR *pPool
);
```



## Property value

The name of the job’s pool.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Server 2008 R2 with Service Pack 1 (SP1) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                                     |



## See also

<dl> <dt>

[**IScheduler::CreatePool**](ischeduler-createpool.md)
</dt> <dt>

[**IScheduler::DeletePool**](ischeduler-deletepool.md)
</dt> <dt>

[**IScheduler::GetPoolList**](ischeduler-getpoollist.md)
</dt> <dt>

[**IScheduler::OpenPool**](ischeduler-openpool.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




