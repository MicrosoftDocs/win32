---
title: UnwrapKeyProtector method of the MSFT\_HgsKeyProtectorOperations class
description: Unwraps an existing key protector returning the ingress key along with a new egress key and egress key protector.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3e3e7c1b-1865-4da4-bc3f-89fd9f36e9e5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'host-guardian-service'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["UnwrapKeyProtector method", "UnwrapKeyProtector method, MSFT_HgsKeyProtectorOperations class", "MSFT_HgsKeyProtectorOperations class, UnwrapKeyProtector method"]
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtectorOperations.UnwrapKeyProtector
api_location:
- HgsClientWmi.dll
api_type:
- COM
---

# UnwrapKeyProtector method of the MSFT\_HgsKeyProtectorOperations class

Unwraps an existing key protector returning the ingress key along with a new egress key and egress key protector.

## Syntax


```mof
uint32 UnwrapKeyProtector(
  [in]  uint8 IngressKeyProtector[],
  [out] uint8 EncryptedTransferKey[],
  [out] uint8 EncryptedWrappingKey[],
  [out] uint8 EncryptedKeys[],
  [out] uint8 EgressKeyProtector[]
);
```



## Parameters

<dl> <dt>

*IngressKeyProtector* \[in\]
</dt> <dd>

The key protector containing the desired transport key.

</dd> <dt>

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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_HgsKeyProtectorOperations**](msft-hgskeyprotectoroperations.md)
</dt> </dl>

 

 





