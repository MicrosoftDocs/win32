---
title: Import method of the MSFT\_HgsGuardian class
description: Imports a guardian from an XML file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 545422f1-2a83-4836-a06e-6b2346ea94fd
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Import method
- Import method, MSFT_HgsGuardian class
- MSFT_HgsGuardian class, Import method
topic_type:
- apiref
api_name:
- MSFT_HgsGuardian.Import
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Import method of the MSFT\_HgsGuardian class

Imports a guardian from an XML file

## Syntax


```mof
uint32 Import(
  [in]  string           Path,
  [in]  string           Name,
  [in]  boolean          AllowExpired,
  [in]  boolean          AllowUntrustedRoot,
  [out] MSFT_HgsGuardian cmdletOutput
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

A path to an XML file containing the guardian information.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

A name to associate with this guardian when it is persisted to the local guardian store.

</dd> <dt>

*AllowExpired* \[in\]
</dt> <dd>

When specified allows a new guardian creation with certificates that are expired.

</dd> <dt>

*AllowUntrustedRoot* \[in\]
</dt> <dd>

When specified, allows a new guardian to be created using self-signed certificates.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, returns a [**MSFT\_HgsGuardian**](msft-hgsguardian.md) object containing the imported guardian.

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

 

 





