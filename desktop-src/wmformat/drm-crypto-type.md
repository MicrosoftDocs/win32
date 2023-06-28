---
title: DRM_CRYPTO_TYPE enumeration (Wmdrmsdk.h)
description: The DRM\_CRYPTO\_TYPE enumeration defines the cryptographic algorithm types that can be used to encrypt content.
ms.assetid: e04d22cd-04fe-4b80-9644-7cd24dc99f04
keywords:
- DRM_CRYPTO_TYPE enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- DRM_CRYPTO_TYPE
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_CRYPTO\_TYPE enumeration

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_CRYPTO\_TYPE** enumeration defines the cryptographic algorithm types that can be used to encrypt content.

## Syntax


```C++
typedef enum DRM_CRYPTO_TYPE { 
  CRYPTO_TYPE_MCE  = 0
} ;
```



## Constants

<dl> <dt>

<span id="CRYPTO_TYPE_MCE"></span><span id="crypto_type_mce"></span>**CRYPTO\_TYPE\_MCE**
</dt> <dd>

Specifies 128-bit counter mode Advanced Encryption Standard (AES) encryption.

</dd> </dl>

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](drm-enumeration-types.md)
</dt> </dl>

 

 





