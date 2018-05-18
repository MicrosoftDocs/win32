---
title: CARD\_DH\_AGREEMENT\_INFO structure
description: Specifies information necessary for the CardConstructDHAgreement function to calculate a Diffie-Hellman key exchange secret agreement.
ms.assetid: '20f69e8e-c5ed-4291-8289-7e7588bc0ac2'
keywords: ["CARD_DH_AGREEMENT_INFO structure Security", "PCARD_DH_AGREEMENT_INFO structure pointer Security"]
topic_type:
- apiref
api_name:
- CARD_DH_AGREEMENT_INFO
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CARD\_DH\_AGREEMENT\_INFO structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_DH\_AGREEMENT\_INFO** structure specifies information necessary for the [**CardConstructDHAgreement**](cardconstructdhagreement.md) function to calculate a Diffie-Hellman key exchange secret agreement.

**Windows Server 2003, Windows XP, Windows 2000 Server and Windows 2000 Professional:** Diffie-Hellman key exchange secret calculation is not supported.

## Syntax


```C++
typedef struct _CARD_DH_AGREEMENT_INFO {
  DWORD dwVersion;
  BYTE  bContainerIndex;
  DWORD dwFlags;
  DWORD dwPublicKey;
  PBYTE pbPublicKey;
  PBYTE pbReserved;
  DWORD cbReserved;
  BYTE  bSecretAgreementIndex;
} CARD_DH_AGREEMENT_INFO, *PCARD_DH_AGREEMENT_INFO;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version of this structure, to be set by the caller. The current version is 2.

</dd> <dt>

**bContainerIndex**
</dt> <dd>

The key container index number. The container holds the keys that perform the calculation.

</dd> <dt>

**dwFlags**
</dt> <dd>

Reserved. You must set this member to zero.

</dd> <dt>

**dwPublicKey**
</dt> <dd>

The size, in bytes, of the **pbPublicKey** buffer.

</dd> <dt>

**pbPublicKey**
</dt> <dd>

A pointer to a buffer that specifies the public key. The [**CardConstructDHAgreement**](cardconstructdhagreement.md) function constructs the agreement from this key.

</dd> <dt>

**pbReserved**
</dt> <dd>

Reserved.

</dd> <dt>

**cbReserved**
</dt> <dd>

Reserved.

</dd> <dt>

**bSecretAgreementIndex**
</dt> <dd>

The index of the container that holds the secret agreement on successful completion of the [**CardConstructDHAgreement**](cardconstructdhagreement.md) function.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> </dl>

 

 





