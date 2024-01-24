---
description: Texture wrapping options for IMT computation APIs.
ms.assetid: ec364418-67c6-42c7-9c5d-b97aa7e17c24
title: D3DXIMT FLAGS enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXIMT
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXIMT FLAGS enumeration

Texture wrapping options for IMT computation APIs.

## Syntax


```C++
typedef enum D3DXIMT_FLAGS { 
  D3DXIMT_WRAP_U   = 1,
  D3DXIMT_WRAP_V   = 2,
  D3DXIMT_WRAP_UV  = 3
} D3DXIMT FLAGS, *LPD3DXIMT FLAGS;
```



## Constants

<dl> <dt>

<span id="D3DXIMT_WRAP_U"></span><span id="d3dximt_wrap_u"></span>**D3DXIMT\_WRAP\_U**
</dt> <dd>

The texture wraps in the U direction.

</dd> <dt>

<span id="D3DXIMT_WRAP_V"></span><span id="d3dximt_wrap_v"></span>**D3DXIMT\_WRAP\_V**
</dt> <dd>

The texture wraps in the V direction.

</dd> <dt>

<span id="D3DXIMT_WRAP_UV"></span><span id="d3dximt_wrap_uv"></span>**D3DXIMT\_WRAP\_UV**
</dt> <dd>

The texture wraps in both the U and V direction.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> <dt>

[**D3DXComputeIMTFromSignal**](d3dxcomputeimtfromsignal.md)
</dt> <dt>

[**D3DXComputeIMTFromTexture**](d3dxcomputeimtfromtexture.md)
</dt> <dt>

[**D3DXComputeIMTFromPerTexelSignal**](d3dxcomputeimtfrompertexelsignal.md)
</dt> <dt>

[**D3DXComputeIMTFromPerVertexSignal**](d3dxcomputeimtfrompervertexsignal.md)
</dt> </dl>

 

 




