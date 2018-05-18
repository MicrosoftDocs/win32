---
Description: 'Retrieves a certificate matching the thumbprint from the local store encoded as a stream of bytes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '925DA801-C217-44FC-B62F-325C79C4D7F2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetCertificateFromStore method'
---

# IScheduler::GetCertificateFromStore method

Retrieves a certificate matching the thumbprint from the local store encoded as a stream of bytes.

## Syntax


```C++
HRESULT GetCertificateFromStore(
  [in]  BSTR          *thumbprint,
  [out] SecureString  *pfxPassword,
  [out] unsigned char *certificateFromStore
);
```



## Parameters

<dl> <dt>

*thumbprint* \[in\]
</dt> <dd>

Thumbprint that matches the certificate. If null, a certificate that matches the requirements will be used.

</dd> <dt>

*pfxPassword* \[out\]
</dt> <dd>

The password to encrypt the certificate.

</dd> <dt>

*certificateFromStore* \[out\]
</dt> <dd>

The certificate matching the thumbprint or any certificate matching the requirements if thumbprint is null.

</dd> </dl>

## Return value

If the method succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

**ISchedulerJob::GetCertificateFromStore** also uses a random generated password to encrypt the password.

HPC Softcards are required to use **ISchedulerJob::GetCertificateFromStore**.

## Requirements



|                         |                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 Service Pack 2 (SP2) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                              |



 

 




