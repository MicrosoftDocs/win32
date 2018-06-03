---
title: NewByGenerateCertificates method of the MSFT\_HgsGuardian class
description: Creates a guardian and a self-signed encryption certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dc64e574-feeb-4fd0-8655-bddb05b5f321
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewByGenerateCertificates method
- NewByGenerateCertificates method, MSFT_HgsGuardian class
- MSFT_HgsGuardian class, NewByGenerateCertificates method
topic_type:
- apiref
api_name:
- MSFT_HgsGuardian.NewByGenerateCertificates
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewByGenerateCertificates method of the MSFT\_HgsGuardian class

Creates a guardian and a self-signed encryption certificate.

## Syntax


```mof
uint32 NewByGenerateCertificates(
  [in]  string           Name,
  [in]  boolean          GenerateCertificates,
  [out] MSFT_HgsGuardian cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

A name to associate with this guardian when it is persisted to the guardian store.

</dd> <dt>

*GenerateCertificates* \[in\]
</dt> <dd>

Generates self-signed signing encryption certificates for the guardian that contain the public and private keys.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, returns a [**MSFT\_HgsGuardian**](msft-hgsguardian.md) instance containing the new guardian object.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_HgsGuardian**](msft-hgsguardian.md)
</dt> </dl>

 

 





