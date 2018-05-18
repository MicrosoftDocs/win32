---
Description: 'Sets the run-time limit for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e2335e77-7272-46d3-be12-5ca574e5a76c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_Runtime method'
---

# IJob::put\_Runtime method

Sets the run-time limit for the job.

## Syntax


```C++
HRESULT put_Runtime(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The run-time limit. The value can be "Infinite" or a string in the format *dd*:*hh*:*mm* where *dd* is the number of days, *hh* is the number of hours, and *mm* is the number of minutes. You must provide leading zeros; for example, to specify a run time of one minute, use the string "00:00:01". The default is "Infinite".

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The wall clock is used to determine the run time. The time is your best guess of how long the job will take; however, it needs to be fairly accurate because it is used to allocate resources. If the job exceeds this time, the job is terminated and its status becomes JobStatus\_Cancelled.

For more information, see the JobRuntime configuration parameter in the Remarks section of [**ICluster::SetClusterParameter**](icluster-setclusterparameter.md).

The sum of all [**ITask::put\_Runtime**](itask-put-runtime.md) values should be less than the run-time value for the job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_Runtime**](ijob-get-runtime.md)
</dt> <dt>

[**ITask::put\_Runtime**](itask-put-runtime.md)
</dt> </dl>

 

 




