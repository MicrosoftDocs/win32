---
title: CreateKeyProtector method of the MSFT\_HgsKeyProtectorOperations class
description: Creates a new key protector.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 547d8071-7c88-4774-a889-28cf8ac259d4
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateKeyProtector method
- CreateKeyProtector method, MSFT_HgsKeyProtectorOperations class
- MSFT_HgsKeyProtectorOperations class, CreateKeyProtector method
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtectorOperations.CreateKeyProtector
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateKeyProtector method of the MSFT\_HgsKeyProtectorOperations class

Creates a new key protector.

## Syntax


```mof
uint32 CreateKeyProtector(
  [out] uint8 EncryptedTransferKey[],
  [out] uint8 EncryptedWrappingKey[],
  [out] uint8 EncryptedKeys[],
  [out] uint8 EgressKeyProtector[]
);
```



## Parameters

<dl> <dt>

*EncryptedTransferKey* \[out\]
</dt> <dd>

The transfer key encrypted to the caller.

</dd> <dt>

*EncryptedWrappingKey* \[out\]
</dt> <dd>

The wrapping key encrypted using the transfer key and the caller's trustlet information.

</dd> <dt>

*EncryptedKeys* \[out\]
</dt> <dd>

The key contained with the KP combined with a new export key contained in the egress KP.

</dd> <dt>

*EgressKeyProtector* \[out\]
</dt> <dd>

On success, contains the new egress Key Protector that describes the egress key.

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

[**MSFT\_HgsKeyProtectorOperations**](msft-hgskeyprotectoroperations.md)
</dt> </dl>

 

 





