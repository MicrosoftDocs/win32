---
title: WMDRM_ENCRYPT_SCATTER_INFO structure (Wmdrmsdk.h)
description: The WMDRM\_ENCRYPT\_SCATTER\_INFO structure contains information needed to configure the IWMDRMEncryptScatter interface for use.
ms.assetid: 25e19511-56ac-441b-b521-5097dd792ead
keywords:
- WMDRM_ENCRYPT_SCATTER_INFO structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRM_ENCRYPT_SCATTER_INFO
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRM\_ENCRYPT\_SCATTER\_INFO structure

The **WMDRM\_ENCRYPT\_SCATTER\_INFO** structure contains information needed to configure the [**IWMDRMEncryptScatter**](iwmdrmencryptscatter.md) interface for use.

## Syntax


```C++
typedef struct WMDRM_ENCRYPT_SCATTER_INFO {
  DWORD dwStreamID;
  DWORD dwSampleProtectionVersion;
  DWORD cbProtectionInfo;
  BYTE  *pbProtectionInfo;
} ;
```



## Members

<dl> <dt>

**dwStreamID**
</dt> <dd>

Identifier of the stream to be encrypted.

</dd> <dt>

**dwSampleProtectionVersion**
</dt> <dd>

Sample protection version to be used to encode data from the specified stream.

</dd> <dt>

**cbProtectionInfo**
</dt> <dd>

Size of the **pbProtectionInfo** buffer in bytes.

</dd> <dt>

**pbProtectionInfo**
</dt> <dd>

Buffer containing additional protection information.

</dd> </dl>

## Remarks

This structure is used by the [**IWMDRMEncryptScatter::InitEncryptScatter**](iwmdrmencryptscatter-initencryptscatter.md) method.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





