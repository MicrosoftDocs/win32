---
title: NewByGuardians method of the MSFT\_HgsKeyProtector class
description: Creates a new key protector.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: BCE05C92-D382-4ADD-B816-26A8907A3375
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewByGuardians method
- NewByGuardians method, MSFT_HgsKeyProtector interface
- MSFT_HgsKeyProtector interface, NewByGuardians method
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtector.NewByGuardians
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewByGuardians method of the MSFT\_HgsKeyProtector class

Creates a new key protector.

## Syntax


```mof
uint32 NewByGuardians(
  [in]  boolean              AllowUntrustedRoot,
  [in]  boolean              AllowExpired,
  [in]  MSFT_HgsGuardian     Owner,
  [in]  MSFT_HgsGuardian     Guardian[],
  [out] MSFT_HgsKeyProtector cmdletOutput
);
```



## Parameters

<dl> <dt>

*AllowUntrustedRoot* \[in\]
</dt> <dd>

When specified, allows new key protector creation with one or more guardians using self-signed certificates.

</dd> <dt>

*AllowExpired* \[in\]
</dt> <dd>

When specified allows new key protector creation with one or more guardians using expired certificates.

</dd> <dt>

*Owner* \[in\]
</dt> <dd>

An embedded instance of a [**MSFT\_HgsGuardian**](msft-hgsguardian.md) class that represents the owner.

</dd> <dt>

*Guardian* \[in\]
</dt> <dd>

An array of embedded instances of [**MSFT\_HgsGuardian**](msft-hgsguardian.md) classes that represents the guardians who are granted access to the key protected by the new key protector.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of a [**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md) class that represents the new key protector.

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
</dt> </dl>

 

 





