---
title: DecryptDataWithKeyProtector method of the MSFT\_HgsKeyProtectorOperations class
description: Decrypts data by using a supplied key protector.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 159D7A04-0459-4AE5-ADE0-21FF40619EAF
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DecryptDataWithKeyProtector method
- DecryptDataWithKeyProtector method, MSFT_HgsKeyProtectorOperations interface
- MSFT_HgsKeyProtectorOperations interface, DecryptDataWithKeyProtector method
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtectorOperations.DecryptDataWithKeyProtector
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DecryptDataWithKeyProtector method of the MSFT\_HgsKeyProtectorOperations class

Decrypts data by using a supplied key protector.

## Syntax


```mof
uint32 DecryptDataWithKeyProtector(
  [in]  uint8 BaseKeyProtector[],
  [in]  uint8 EncryptedData[],
  [out] uint8 PlaintextData[]
);
```



## Parameters

<dl> <dt>

*BaseKeyProtector* \[in\]
</dt> <dd>

The key protector desired for the data.

</dd> <dt>

*EncryptedData* \[in\]
</dt> <dd>

The encrypted data.

</dd> <dt>

*PlaintextData* \[out\]
</dt> <dd>

The decrypted data.

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

 

 





