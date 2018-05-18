---
Description: 'Gets the date and time (in Coordinated Universal Time) until which the HPC Job Scheduler Service should wait before trying to start the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4BF9506A-058F-4979-9DDC-32E8738CC0FD'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::HoldUntil property'
---

# ISchedulerJob::HoldUntil property

Gets the date and time (in Coordinated Universal Time) until which the HPC Job Scheduler Service should wait before trying to start the job.

This property is read-only.

## Syntax


```C++
HRESULT get_HoldUntil(
  [out, retval] DATE *pRetVal
);
```



## Property value

A [**DATE**](695853ed-b614-4575-b793-b8c287372038) that indicates the date and time until which the HPC Job Scheduler Service should wait before trying to start the job.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

The HPC Job Scheduler Service only runs the job at the date and time that this property specifies if the resources needed for the job are available. If the resources needed for the job are not available at that date and time, the job remains queued until the necessary resources become available.

If the job is not on hold, the [**DATE**](695853ed-b614-4575-b793-b8c287372038) returned has a value of 0.0, which represents midnight of December 30, 1899.

You cannot set the value of this property by using the COM API that the Microsoft HPC Pack 2008 R2 SDK provides. You can set this property by using one of the following items:

-   The [ISchedulerJob.SetHoldUntil]( http://go.microsoft.com/fwlink/p/?linkid=204003) method of the .NET API.
-   The [job modify](http://go.microsoft.com/fwlink/p/?linkid=152318) command.
-   The SetHoldUntil property of the HpcJob object that the [Get-HpcJob](http://go.microsoft.com/fwlink/p/?linkid=182806) cmdlet returns.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




