---
Description: Describes a surface.
ms.assetid: fad8ffdb-36e5-4695-b343-e1315357c31a
title: D3DSURFACE\_DESC structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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

Type: **[**D3DRESOURCETYPE**](https://msdn.microsoft.com/en-us/library/Bb172601(v=VS.85).aspx)**

</dd> <dd>

Member of the [**D3DRESOURCETYPE**](https://msdn.microsoft.com/en-us/library/Bb172601(v=VS.85).aspx) enumerated type, identifying this resource as a surface.

</dd> <dt>

**Usage**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Either the D3DUSAGE\_DEPTHSTENCIL or D3DUSAGE\_RENDERTARGET values. For more information, see [**D3DUSAGE**](d3dusage.md).

</dd> <dt>

**Pool**
</dt> <dd>

Type: **[**D3DPOOL**](https://msdn.microsoft.com/en-us/library/Bb172584(v=VS.85).aspx)**

</dd> <dd>

Member of the [**D3DPOOL**](https://msdn.microsoft.com/en-us/library/Bb172584(v=VS.85).aspx) enumerated type, specifying the class of memory allocated for this surface.

</dd> <dt>

**MultiSampleType**
</dt> <dd>

Type: **[**D3DMULTISAMPLE\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb172574(v=VS.85).aspx)**

</dd> <dd>

Member of the [**D3DMULTISAMPLE\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb172574(v=VS.85).aspx) enumerated type, specifying the levels of full-scene multisampling supported by the surface.

</dd> <dt>

**MultiSampleQuality**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Quality level. The valid range is between zero and one less than the level returned by pQualityLevels used by [**CheckDeviceMultiSampleType**](/windows/desktop/api). Passing a larger value returns the error, D3DERR\_INVALIDCALL. The MultisampleQuality values of paired render targets, depth stencil surfaces and the MultiSample type must all match.

</dd> <dt>

**Width**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Width of the surface, in pixels.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Height of the surface, in pixels.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetLevelDesc**](/windows/desktop/api)
</dt> <dt>

[**GetDesc**](/windows/desktop/api)
</dt> <dt>

[**GetLevelDesc**](/windows/desktop/api)
</dt> </dl>

 

 




