---
Description: 'Sets the job priority.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'af9f21c8-ead5-4e58-b080-82f19e13935c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_Priority method'
---

# IJob::put\_Priority method

Sets the job priority.

## Syntax


```C++
HRESULT put_Priority(
  [in] JobPriority Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The job priority. The default is JobPriority\_Normal. For a list of values, see [**JobPriority**](jobpriority.md).

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Compute cluster resources are allocated to jobs based on job priority, except for backfill jobs. For information about backfill jobs, see the Remarks section of [**IJob::get\_IsBackfill**](ijob-get-isbackfill.md). Jobs are not preempted; they run until they finish, fail or are canceled.

Within a job, tasks receive resources based on the order in which they were added to the job. If a processor is available, the task will run.

To retrieve the job priority, use the [**IJob::get\_Priority**](ijob-get-priority.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_Priority**](ijob-get-priority.md)
</dt> </dl>

 

 




