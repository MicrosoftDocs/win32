---
description: Defines constants that describe transformation state values.
ms.assetid: 53535d9f-246a-42cf-82a2-fb3cf6d4ebac
title: D3DTRANSFORMSTATETYPE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DTRANSFORMSTATETYPE
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DTRANSFORMSTATETYPE enumeration

Defines constants that describe transformation state values.

## Syntax


```C++
typedef enum D3DTRANSFORMSTATETYPE { 
  D3DTS_VIEW         = 2,
  D3DTS_PROJECTION   = 3,
  D3DTS_TEXTURE0     = 16,
  D3DTS_TEXTURE1     = 17,
  D3DTS_TEXTURE2     = 18,
  D3DTS_TEXTURE3     = 19,
  D3DTS_TEXTURE4     = 20,
  D3DTS_TEXTURE5     = 21,
  D3DTS_TEXTURE6     = 22,
  D3DTS_TEXTURE7     = 23,
  D3DTS_FORCE_DWORD  = 0x7fffffff
} D3DTRANSFORMSTATETYPE, *LPD3DTRANSFORMSTATETYPE;
```



## Constants

<dl> <dt>

<span id="D3DTS_VIEW"></span><span id="d3dts_view"></span>**D3DTS\_VIEW**
</dt> <dd>

Identifies the transformation matrix being set as the view transformation matrix. The default value is **NULL** (the identity matrix).

</dd> <dt>

<span id="D3DTS_PROJECTION"></span><span id="d3dts_projection"></span>**D3DTS\_PROJECTION**
</dt> <dd>

Identifies the transformation matrix being set as the projection transformation matrix. The default value is **NULL** (the identity matrix).

</dd> <dt>

<span id="D3DTS_TEXTURE0"></span><span id="d3dts_texture0"></span>**D3DTS\_TEXTURE0**
</dt> <dd>

Identifies the transformation matrix being set for the specified texture stage.

</dd> <dt>

<span id="D3DTS_TEXTURE1"></span><span id="d3dts_texture1"></span>**D3DTS\_TEXTURE1**
</dt> <dd>

Identifies the transformation matrix being set for the specified texture stage.

</dd> <dt>

<span id="D3DTS_TEXTURE2"></span><span id="d3dts_texture2"></span>**D3DTS\_TEXTURE2**
</dt> <dd>

Identifies the transformation matrix being set for the specified texture stage.

</dd> <dt>

<span id="D3DTS_TEXTURE3"></span><span id="d3dts_texture3"></span>**D3DTS\_TEXTURE3**
</dt> <dd>

Identifies the transformation matrix being set for the specified texture stage.

</dd> <dt>

<span id="D3DTS_TEXTURE4"></span><span id="d3dts_texture4"></span>**D3DTS\_TEXTURE4**
</dt> <dd>

Identifies the transformation matrix being set for the specified texture stage.

</dd> <dt>

<span id="D3DTS_TEXTURE5"></span><span id="d3dts_texture5"></span>**D3DTS\_TEXTURE5**
</dt> <dd>

Identifies the transformation matrix being set for the specified texture stage.

</dd> <dt>

<span id="D3DTS_TEXTURE6"></span><span id="d3dts_texture6"></span>**D3DTS\_TEXTURE6**
</dt> <dd>

Identifies the transformation matrix being set for the specified texture stage.

</dd> <dt>

<span id="D3DTS_TEXTURE7"></span><span id="d3dts_texture7"></span>**D3DTS\_TEXTURE7**
</dt> <dd>

Identifies the transformation matrix being set for the specified texture stage.

</dd> <dt>

<span id="D3DTS_FORCE_DWORD"></span><span id="d3dts_force_dword"></span>**D3DTS\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

The transform states in the range 256 through 511 are reserved to store up to 256 world matrices that can be indexed using the D3DTS\_WORLDMATRIX and D3DTS\_WORLD macros.



| Macros                                                  | Description                                                                                                                                                                      |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3DTS\_WORLD**](d3dts-world.md)                     | Equivalent to D3DTS\_WORLDMATRIX(0).                                                                                                                                  |
| [**D3DTS\_WORLDMATRIX**](d3dts-worldmatrix.md) (index) | Identifies the transform matrix to set for the world matrix at index. Multiple world matrices are used only for vertex blending. Otherwise only D3DTS\_WORLD is used. |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**IDirect3DDevice9::GetTransform**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-gettransform)
</dt> <dt>

[**IDirect3DDevice9::MultiplyTransform**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-multiplytransform)
</dt> <dt>

[**IDirect3DDevice9::SetTransform**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settransform)
</dt> <dt>

[**D3DTS\_WORLD**](d3dts-world.md)
</dt> <dt>

[**D3DTS\_WORLDn**](d3dts-worldn.md)
</dt> <dt>

[**D3DTS\_WORLDMATRIX**](d3dts-worldmatrix.md)
</dt> </dl>

 

 
