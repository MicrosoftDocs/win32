---
Description: 'Gets or sets whether you want to receive an email notification when then job starts.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '16F8EC0E-C4E6-45DB-89AE-44C3E3E0660D'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::NotifyOnStart property'
---

# ISchedulerJob::NotifyOnStart property

Gets or sets whether you want to receive an email notification when then job starts.

This property is read/write.

## Syntax


```C++
HRESULT put_NotifyOnStart(
  [in]          VARIANT_BOOL pRetVal
);

HRESULT get_NotifyOnStart(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Property value

A VARIANT\_BOOL that specifies whether you want to receive an email notification when then job starts. VARIANT\_TRUE indicates that you want to receive an email notification when then job starts. VARIANT\_FALSE indicates that you do not want to receive an email notification when then job starts.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

A cluster administrator must configure the email notification feature before you can receive an email notification about a job.

By default, you do not receive an email notification when a job starts.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::NotifyOnCompletion**](ischedulerjob-notifyoncompletion.md)
</dt> </dl>

 

 




