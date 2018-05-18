---
Description: 'Gets or sets the percentage of the job that is complete.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'A5006D5F-AF79-487A-9DD6-32F52B48BB76'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Progress property'
---

# ISchedulerJob::Progress property

Gets or sets the percentage of the job that is complete.

This property is read/write.

## Syntax


```C++
HRESULT put_Progress(
  [in]          long pRetVal
);

HRESULT get_Progress(
  [out, retval] long *pRetVal
);
```



## Property value

A long integer that specifies the percentage of the job that is complete. It is a value between 0 and 100.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

If your application does not set the value of this property, the HPC Job Scheduler Service calculates the progress based on the percentage of tasks that are complete for the job. After your application sets this property for a job, the HPC Job Scheduler Service does not continue to update this property, and your application must continue to update the property.

You can set the value of this property for jobs in any state.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::ProgressMessage**](ischedulerjob-progressmessage.md)
</dt> </dl>

 

 




