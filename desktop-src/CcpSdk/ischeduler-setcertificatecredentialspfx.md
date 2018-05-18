---
Description: 'Uploads a certificate encoded with a password to the scheduler to use for running jobs as this user.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'EF254381-88A8-40B7-B58F-0F5850F6DDC9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::SetCertificateCredentialsPfx method'
---

# IScheduler::SetCertificateCredentialsPfx method

Uploads a certificate encoded with a password to the scheduler to use for running jobs as this user.

## Syntax


```C++
HRESULT SetCertificateCredentialsPfx(
  [in] BSTR          *userName,
  [in] BSTR          *pfxPassword,
  [in] unsigned char *certBytes
);
```



## Parameters

<dl> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form domain\\user. The user name is limited to 80 characters.

</dd> <dt>

*pfxPassword* \[in\]
</dt> <dd>

The password for the RunAs user. The password is limited to 127 characters.

</dd> <dt>

*certBytes* \[in\]
</dt> <dd>

A byte array that contains the certificate.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 Service Pack 2 (SP2) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                              |



 

 




