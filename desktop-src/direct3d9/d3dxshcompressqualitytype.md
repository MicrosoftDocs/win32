---
description: Spherical harmonic (SH) compression setting.
ms.assetid: 214d6efb-419d-4eea-8360-322885c26bc3
title: D3DXSHCOMPRESSQUALITYTYPE enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHCOMPRESSQUALITYTYPE
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXSHCOMPRESSQUALITYTYPE enumeration

Spherical harmonic (SH) compression setting.

## Syntax


```C++
typedef enum D3DXSHCOMPRESSQUALITYTYPE { 
  D3DXSHCQUAL_FASTLOWQUALITY   = 1,
  D3DXSHCQUAL_SLOWHIGHQUALITY  = 2,
  D3DXSHCQUAL_FORCE_DWORD      = 0x7fffffff
} D3DXSHCOMPRESSQUALITYTYPE, *LPD3DXSHCOMPRESSQUALITYTYPE;
```



## Constants

<dl> <dt>

<span id="D3DXSHCQUAL_FASTLOWQUALITY"></span><span id="d3dxshcqual_fastlowquality"></span>**D3DXSHCQUAL\_FASTLOWQUALITY**
</dt> <dd>

The data compression is low quality, but is fast to compress.

</dd> <dt>

<span id="D3DXSHCQUAL_SLOWHIGHQUALITY"></span><span id="d3dxshcqual_slowhighquality"></span>**D3DXSHCQUAL\_SLOWHIGHQUALITY**
</dt> <dd>

The data compression is high quality, but is slow to compress.

</dd> <dt>

<span id="D3DXSHCQUAL_FORCE_DWORD"></span><span id="d3dxshcqual_force_dword"></span>**D3DXSHCQUAL\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




