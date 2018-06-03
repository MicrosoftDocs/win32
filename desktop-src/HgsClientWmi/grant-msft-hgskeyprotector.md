---
title: Grant method of the MSFT\_HgsKeyProtector class
description: Grants access to a key protected by a key protector to a given guardian. This operation requires access to the owner signing private key, to prove ownership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b91fdc01-079d-4280-8aa7-b3e36f70b2b2
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Grant method
- Grant method, MSFT_HgsKeyProtector class
- MSFT_HgsKeyProtector class, Grant method
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtector.Grant
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Grant method of the MSFT\_HgsKeyProtector class

Grants access to a key protected by a key protector to a given guardian. This operation requires access to the owner signing private key, to prove ownership.

## Syntax


```mof
uint32 Grant(
  [in]  MSFT_HgsKeyProtector KeyProtector,
  [in]  MSFT_HgsGuardian     Guardian,
  [in]  boolean              AllowExpired,
  [in]  boolean              AllowUntrustedRoot,
  [out] MSFT_HgsKeyProtector cmdletOutput
);
```



## Parameters

<dl> <dt>

*KeyProtector* \[in\]
</dt> <dd>

Embedded instance of a [**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md) class that represents the key protector on which to grant access.

</dd> <dt>

*Guardian* \[in\]
</dt> <dd>

Embedded instance of a [**MSFT\_HgsGuardian**](msft-hgsguardian.md) class that represents the guardian to grant access to.

</dd> <dt>

*AllowExpired* \[in\]
</dt> <dd>

When specified, allows access to the specified Key Protector for one or more guardians using expired certificates.

</dd> <dt>

*AllowUntrustedRoot* \[in\]
</dt> <dd>

When specified, allows access to the specified Key Protector creation with one or more guardians using self-signed certificates.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of a [**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md) class with the updated access.

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

[**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md)
</dt> <dt>

[**MSFT\_HgsGuardian**](msft-hgsguardian.md)
</dt> </dl>

 

 





