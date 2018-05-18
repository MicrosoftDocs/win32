---
Description: 'Retrieves or sets the email address to which the HPC Job Scheduler Service should send notifications when the job starts or finishes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4209D9CF-80CA-4A9A-806A-24B3D33CBE2C'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::EmailAddress property'
---

# ISchedulerJob::EmailAddress property

Retrieves or sets the email address to which the HPC Job Scheduler Service should send notifications when the job starts or finishes.

This property is read/write.

## Syntax


```C++
HRESULT put_EmailAddress(
  [in]  BSTR emailAddress
);

HRESULT get_EmailAddress(
  [out] BSTR *pEmailAddress
);
```



## Property value

Indicates the email address to which the HPC Job Scheduler Service should send notifications when the job starts or finishes.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

The maximum length for the email address that you specify is 256 characters. The HPC Job Scheduler Service sends notifications to the user who created the job by default.

When you specify an email address for receiving notifications about a job, the notifications are not turned on automatically. You still need to set the [**ISchedulerJob::NotifyOnStart**](ischedulerjob-notifyonstart.md) and/or [**ISchedulerJob::NotifyOnCompletion**](ischedulerjob-notifyoncompletion.md) property to True to specify when you want to receive notifications about the job.

## Requirements



|                         |                                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Server 2008 R2 with Service Pack 1 (SP1) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                                     |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




