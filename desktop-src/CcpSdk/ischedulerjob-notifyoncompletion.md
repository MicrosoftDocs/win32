---
Description: 'Gets or sets whether you want to receive an email notification when then job ends.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'B43E081E-FC02-4AE0-BCFA-0824EA504D55'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::NotifyOnCompletion property'
---

# ISchedulerJob::NotifyOnCompletion property

Gets or sets whether you want to receive an email notification when then job ends.

This property is read/write.

## Syntax


```C++
HRESULT put_NotifyOnCompletion(
  [in]          VARIANT_BOOL pRetVal
);

HRESULT get_NotifyOnCompletion(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Property value

A VARIANT\_BOOL that specifies whether you want to receive an email notification when then job ends. VARIANT\_TRUE indicates that you want to receive an email notification when then job ends. VARIANT\_FALSE indicates that you do not want to receive email an notification when then job ends.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

A job ends and an email notification is sent when the state of the job changes to Finished, Failed, or Canceled.

A cluster administrator must configure the email notification feature before you can receive an email notification about a job.

By default, you do not receive an email notification when a job ends.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::NotifyOnStart**](ischedulerjob-notifyonstart.md)
</dt> </dl>

 

 




