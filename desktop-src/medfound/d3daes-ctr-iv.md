---
description: Contains an initialization vector (IV) for 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher encryption.
ms.assetid: 2ee738c2-d56c-4a50-94b8-b7180918aa8c
title: D3DAES_CTR_IV structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAES_CTR_IV
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAES\_CTR\_IV structure

Contains an initialization vector (IV) for 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher encryption.

## Syntax


```C++
typedef struct _D3DAES_CTR_IV {
  UINT64 IV;
  UINT64 Count;
} D3DAES_CTR_IV;
```



## Members

<dl> <dt>

**IV**
</dt> <dd>

The IV, in big-endian format.

</dd> <dt>

**Count**
</dt> <dd>

The block count, in big-endian format.

</dd> </dl>

## Remarks

The **D3DAES\_CTR\_IV** structure and the [**DXVA2\_AES\_CTR\_IV**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_aes_ctr_iv) structure are equivalent.

For details, see [**DXVA2\_AES\_CTR\_IV**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_aes_ctr_iv).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>D3d9types.h (include D3d9.h)</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Video Structures](direct3d-video-structures.md)
</dt> </dl>

 

 




