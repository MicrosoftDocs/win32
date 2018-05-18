---
Description: 'Uploads a certificate in the client’s certificate store to the scheduler for running jobs as this user.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '59ACE31E-BB0F-4965-8532-A02EEF1BDC18'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::SetCertificateCredentials method'
---

# IScheduler::SetCertificateCredentials method

Uploads a certificate in the client’s certificate store to the scheduler for running jobs as this user.

## Syntax


```C++
HRESULT SetCertificateCredentials(
  [in] BSTR *userName,
  [in] BSTR *thumbprint
);
```



## Parameters

<dl> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form domain\\user. The user name is limited to 80 characters.

</dd> <dt>

*thumbprint* \[in\]
</dt> <dd>

The thumbprint of the certificate to upload.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

If userName is null or empty, the owner is treated as the user. Only SYSTEM on the cluster headnode is allowed to submit credentials as another user. To set the user as the owner, set username as either null or empty.

If thumbprint is null, the certificate store will be searched for relevant certificates. If there are multiple certificates, the user will be prompted to choose a password depending on the interface mode.

## Requirements



|                         |                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 Service Pack 2 (SP2) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                              |



 

 




