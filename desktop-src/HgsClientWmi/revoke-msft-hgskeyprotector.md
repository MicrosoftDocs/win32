---
title: Revoke method of the MSFT\_HgsKeyProtector class
description: Revokes key access for a given guardian. This operation requires access to the owner signing private key.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fcf3165c-afaa-4b49-9918-2e987765ebec
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Revoke method
- Revoke method, MSFT_HgsKeyProtector class
- MSFT_HgsKeyProtector class, Revoke method
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtector.Revoke
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Revoke method of the MSFT\_HgsKeyProtector class

Revokes key access for a given guardian. This operation requires access to the owner signing private key.

## Syntax


```mof
uint32 Revoke(
  [in]  MSFT_HgsKeyProtector KeyProtector,
  [in]  MSFT_HgsGuardian     Guardian,
  [out] MSFT_HgsKeyProtector cmdletOutput
);
```



## Parameters

<dl> <dt>

*KeyProtector* \[in\]
</dt> <dd>

An embedded instance of a [**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md) class that represents the key protector from which access will be revoked.

</dd> <dt>

*Guardian* \[in\]
</dt> <dd>

An embedded instance of a [**MSFT\_HgsGuardian**](msft-hgsguardian.md) class that represents the guardian whose access will be revoked.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, returns an embedded instance of the resulting [**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md) class.

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

 

 





