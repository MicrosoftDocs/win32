---
Description: 'Enrolls the user in a certificate based on the supplied template.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '036EC3EF-07DC-4914-87BA-998625A305E9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::EnrollCertificate method'
---

# IScheduler::EnrollCertificate method

Enrolls the user in a certificate based on the supplied template.

## Syntax


```C++
HRESULT EnrollCertificate(
  [in]  BSTR          *templateName,
  [out] unsigned char *certBytes
);
```



## Parameters

<dl> <dt>

*templateName* \[in\]
</dt> <dd>

The template name. If the scheduler specifies an hpcsoftcard template, this parameter is ignored.

</dd> <dt>

*certBytes* \[out\]
</dt> <dd>

The certificate thumbprint.

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

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md)
</dt> <dt>

[**ISchedulerJob::GetTaskIdList**](ischedulerjob-gettaskidlist.md)
</dt> <dt>

[**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




