---
description: Defines the compression mode used for storing compressed animation set data.
ms.assetid: 41592b71-52ba-4727-a885-fb10fc23c5f8
title: D3DXCOMPRESSION_FLAGS enumeration (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCOMPRESSION_FLAGS
api_type: 
- HeaderDef
api_location: 
- d3dx9anim.h
---

# D3DXCOMPRESSION\_FLAGS enumeration

Defines the compression mode used for storing compressed animation set data.

## Syntax


```C++
typedef enum D3DXCOMPRESSION_FLAGS { 
  D3DXCOMPRESS_DEFAULT      = 0,
  D3DXCOMPRESS_STRONG       = 1,
  D3DXCOMPRESS_FORCE_DWORD  = 0x7fffffff
} D3DXCOMPRESSION_FLAGS, *LPD3DXCOMPRESSION_FLAGS;
```



## Constants

<dl> <dt>

<span id="D3DXCOMPRESS_DEFAULT"></span><span id="d3dxcompress_default"></span>**D3DXCOMPRESS\_DEFAULT**
</dt> <dd>

Implements fast compression.

</dd> <dt>

<span id="D3DXCOMPRESS_STRONG"></span><span id="d3dxcompress_strong"></span>**D3DXCOMPRESS\_STRONG**
</dt> <dd>

Implements slow compression. Typically results in a better quality compressed animation set than if D3DXCOMPRESS\_DEFAULT is used.

</dd> <dt>

<span id="D3DXCOMPRESS_FORCE_DWORD"></span><span id="d3dxcompress_force_dword"></span>**D3DXCOMPRESS\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




