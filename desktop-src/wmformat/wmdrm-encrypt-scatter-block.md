---
title: WMDRM_ENCRYPT_SCATTER_BLOCK structure (Wmdrmsdk.h)
description: The WMDRM\_ENCRYPT\_SCATTER\_BLOCK structure contains a block of data to be encrypted.
ms.assetid: 73c871f0-3d0d-480f-856c-0f7d5dde5895
keywords:
- WMDRM_ENCRYPT_SCATTER_BLOCK structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRM_ENCRYPT_SCATTER_BLOCK
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRM\_ENCRYPT\_SCATTER\_BLOCK structure

The **WMDRM\_ENCRYPT\_SCATTER\_BLOCK** structure contains a block of data to be encrypted.

## Syntax


```C++
typedef struct WMDRM_ENCRYPT_SCATTER_BLOCK {
  DWORD dwStreamID;
  DWORD cbBlock;
  BYTE  *pbBlock;
} ;
```



## Members

<dl> <dt>

**dwStreamID**
</dt> <dd>

Identifier of the stream to which the data block belongs.

</dd> <dt>

**cbBlock**
</dt> <dd>

Size of block in bytes.

</dd> <dt>

**pbBlock**
</dt> <dd>

Pointer to a buffer containing the data block.

</dd> </dl>

## Remarks

This structure is used by the [**IWMDRMEncryptScatter::EncryptScatter**](iwmdrmencryptscatter-encryptscatter.md) method to identify blocks of data to encrypt.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





