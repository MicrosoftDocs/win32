---
description: Describes a surface.
ms.assetid: fad8ffdb-36e5-4695-b343-e1315357c31a
title: D3DSURFACE_DESC structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DSURFACE_DESC
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DSURFACE\_DESC structure

Describes a surface.

## Syntax


```C++
typedef struct D3DSURFACE_DESC {
  D3DFORMAT           Format;
  D3DRESOURCETYPE     Type;
  DWORD               Usage;
  D3DPOOL             Pool;
  D3DMULTISAMPLE_TYPE MultiSampleType;
  DWORD               MultiSampleQuality;
  UINT                Width;
  UINT                Height;
} D3DSURFACE_DESC, *LPD3DSURFACE_DESC;
```



## Members

<dl> <dt>

**Format**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

Member of the [D3DFORMAT](d3dformat.md) enumerated type, describing the surface format.

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**D3DRESOURCETYPE**](./d3dresourcetype.md)**

</dd> <dd>

Member of the [**D3DRESOURCETYPE**](./d3dresourcetype.md) enumerated type, identifying this resource as a surface.

</dd> <dt>

**Usage**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Either the D3DUSAGE\_DEPTHSTENCIL or D3DUSAGE\_RENDERTARGET values. For more information, see [**D3DUSAGE**](d3dusage.md).

</dd> <dt>

**Pool**
</dt> <dd>

Type: **[**D3DPOOL**](./d3dpool.md)**

</dd> <dd>

Member of the [**D3DPOOL**](./d3dpool.md) enumerated type, specifying the class of memory allocated for this surface.

</dd> <dt>

**MultiSampleType**
</dt> <dd>

Type: **[**D3DMULTISAMPLE\_TYPE**](./d3dmultisample-type.md)**

</dd> <dd>

Member of the [**D3DMULTISAMPLE\_TYPE**](./d3dmultisample-type.md) enumerated type, specifying the levels of full-scene multisampling supported by the surface.

</dd> <dt>

**MultiSampleQuality**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Quality level. The valid range is between zero and one less than the level returned by pQualityLevels used by [**CheckDeviceMultiSampleType**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdevicemultisampletype). Passing a larger value returns the error, D3DERR\_INVALIDCALL. The MultisampleQuality values of paired render targets, depth stencil surfaces and the MultiSample type must all match.

</dd> <dt>

**Width**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Width of the surface, in pixels.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Height of the surface, in pixels.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetLevelDesc**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dcubetexture9-getleveldesc)
</dt> <dt>

[**GetDesc**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dsurface9-getdesc)
</dt> <dt>

[**GetLevelDesc**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dcubetexture9-getleveldesc)
</dt> </dl>

 

 
