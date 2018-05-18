---
title: CONTAINER\_INFO structure
description: Contains information about a key container on a smart card.
ms.assetid: '061aefe0-89e0-4d47-af1f-674b06bd761d'
keywords: ["CONTAINER_INFO structure Security", "PCONTAINER_INFO structure pointer Security"]
topic_type:
- apiref
api_name:
- CONTAINER_INFO
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CONTAINER\_INFO structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CONTAINER\_INFO** structure contains information about a [*key container*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-container-gly) on a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
typedef struct _CONTAINER_INFO {
  DWORD dwVersion;
  DWORD dwReserved;
  DWORD cbSigPublicKey;
  PBYTE pbSigPublicKey;
  DWORD cbKeyExPublicKey;
  PBYTE pbKeyExPublicKey;
} CONTAINER_INFO, *PCONTAINER_INFO;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the structure.

</dd> <dt>

**dwReserved**
</dt> <dd>

This member is reserved for use by the smart card module.

</dd> <dt>

**cbSigPublicKey**
</dt> <dd>

The size, in bytes, of the **pbSigPublicKey** buffer.

</dd> <dt>

**pbSigPublicKey**
</dt> <dd>

A pointer to a buffer that contains the [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly) used to create and verify [*digital signatures*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-digital-signature-gly).

</dd> <dt>

**cbKeyExPublicKey**
</dt> <dd>

The size, in bytes, of the **pbKeyExPublicKey** buffer.

</dd> <dt>

**pbKeyExPublicKey**
</dt> <dd>

A pointer to a buffer that contains the public key used to encrypt and decrypt [*session keys*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-session-key-gly).

</dd> </dl>

## Remarks

This structure is initialized by the [**CardGetContainerInfo**](cardgetcontainerinfo.md) function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CardCreateContainer**](cardcreatecontainer.md)
</dt> <dt>

[**CardGetContainerInfo**](cardgetcontainerinfo.md)
</dt> </dl>

 

 





