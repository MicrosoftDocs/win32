---
title: WMDRMCryptoData structure (Wmdrmsdk.h)
description: The WMDRMCryptoData structure contains information about the cryptographic algorithm used to encrypt and decrypt content.
ms.assetid: ad14c6d3-4305-47c0-8f67-7ef6d11cc326
keywords:
- WMDRMCryptoData structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRMCryptoData
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMCryptoData structure

The **WMDRMCryptoData** structure contains information about the cryptographic algorithm used to encrypt and decrypt content.

## Syntax


```C++
typedef struct WMDRMCryptoData {
  DRM_CRYPTO_TYPE  cryptoType;
  unsigned __int64 qwCounterID;
  unsigned __int64 qwOffset;
} ;
```



## Members

<dl> <dt>

**cryptoType**
</dt> <dd>

Member of the [**DRM\_CRYPTO\_TYPE**](drm-crypto-type.md) enumeration specifying the type of cryptographic algorithm.

</dd> <dt>

**qwCounterID**
</dt> <dd>

The high 64 bits of the 128-bit AES counter mode. This member is only used if the **cryptoType** member is set to **CRYPTO\_TYPE\_MCE**.

</dd> <dt>

**qwOffset**
</dt> <dd>

The low 64 bits of the 128-bit AES counter mode. This member is only used if the **cryptoType** member is set to **CRYPTO\_TYPE\_MCE**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





