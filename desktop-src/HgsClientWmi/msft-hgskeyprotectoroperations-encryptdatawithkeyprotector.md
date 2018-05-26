---
title: EncryptDataWithKeyProtector method of the MSFT\_HgsKeyProtectorOperations class
description: Encrypts data returning the encrypted data along with an egress key protector based on the provided key protector. This is only supported in KDS Local mode.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E4C3349C-B9B9-4408-B32E-5FBE5C950A78
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EncryptDataWithKeyProtector method
- EncryptDataWithKeyProtector method, MSFT_HgsKeyProtectorOperations interface
- MSFT_HgsKeyProtectorOperations interface, EncryptDataWithKeyProtector method
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtectorOperations.EncryptDataWithKeyProtector
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EncryptDataWithKeyProtector method of the MSFT\_HgsKeyProtectorOperations class

Encrypts data returning the encrypted data along with an egress key protector based on the provided key protector. This is only supported in KDS Local mode.

## Syntax


```mof
uint32 EncryptDataWithKeyProtector(
  [in]  uint8   BaseKeyProtector[],
  [in]  uint32  UniqueEncryptionIdentifier,
  [in]  uint8   PlaintextData[],
  [in]  boolean RollKeyProtector,
  [out] uint8   EgressKeyProtector[],
  [out] uint8   EncryptedData[]
);
```



## Parameters

<dl> <dt>

*BaseKeyProtector* \[in\]
</dt> <dd>

The key protector desired for the data.

</dd> <dt>

*UniqueEncryptionIdentifier* \[in\]
</dt> <dd>

A unique encryption identifier that is used only once per key, usually based upon the message type.

</dd> <dt>

*PlaintextData* \[in\]
</dt> <dd>

The data to be encrypted.

</dd> <dt>

*RollKeyProtector* \[in\]
</dt> <dd>

Determines if **BaseKeyProtector** is rolled to a new egress key protector.

</dd> <dt>

*EgressKeyProtector* \[out\]
</dt> <dd>

The Key Protector derived from the **BaseKeyProtector** describing the key used to encrypt the data.

</dd> <dt>

*EncryptedData* \[out\]
</dt> <dd>

The data encrypted using the key described in **EgressKeyProtector**.

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

 

 





