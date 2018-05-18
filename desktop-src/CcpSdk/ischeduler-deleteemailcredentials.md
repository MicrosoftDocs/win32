---
Description: 'Removes the email credentials for running jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'D39DD8FC-558A-45A0-B711-EB9FC3C5675D'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::DeleteEmailCredentials method'
---

# IScheduler::DeleteEmailCredentials method

Removes the email credentials for running jobs.

## Syntax


```C++
HRESULT DeleteEmailCredentials();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

Email credentials use the username and password of the email account as credentials for submitting jobs. To set the email credentials, use the [**IScheduler::SetEmailCredentials**](ischeduler-setemailcredentials.md) method.

## Requirements



|                         |                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 Service Pack 4 (SP4) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                              |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::AddExcludedNodes**](ischedulerjob-addexcludednodes.md)
</dt> <dt>

[**ISchedulerJob::RemoveExcludedNodes**](ischedulerjob-removeexcludednodes.md)
</dt> <dt>

[**ISchedulerJob::ExcludedNodes**](ischedulerjob-excludednodes.md)
</dt> </dl>

 

 




