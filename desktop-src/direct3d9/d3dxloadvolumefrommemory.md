---
description: Loads a volume from memory.
ms.assetid: 9f74fcc0-f935-4466-865b-e798711a1f2f
title: D3DXLoadVolumeFromMemory function (D3dx9tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXLoadVolumeFromMemory
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXLoadVolumeFromMemory function

Loads a volume from memory.

## Syntax


```C++
HRESULT D3DXLoadVolumeFromMemory(
  _In_       LPDIRECT3DVOLUME9 pDestVolume,
  _In_ const PALETTEENTRY      *pDestPalette,
  _In_ const D3DBOX            *pDestBox,
  _In_       LPCVOID           pSrcMemory,
  _In_       D3DFORMAT         SrcFormat,
  _In_       UINT              SrcRowPitch,
  _In_       UINT              SrcSlicePitch,
  _In_ const PALETTEENTRY      *pSrcPalette,
  _In_ const D3DBOX            *pSrcBox,
  _In_       DWORD             Filter,
  _In_       D3DCOLOR          ColorKey
);
```



## Parameters

<dl> <dt>

*pDestVolume* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DVOLUME9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dvolume9)**

Pointer to an [**IDirect3DVolume9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dvolume9) interface. Specifies the destination volume, which receives the image.

</dd> <dt>

*pDestPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry) structure, the destination palette of 256 colors or **NULL**.

</dd> <dt>

*pDestBox* \[in\]
</dt> <dd>

Type: **const [**D3DBOX**](d3dbox.md)\***

Pointer to a [**D3DBOX**](d3dbox.md) structure. Specifies the destination box. Set this parameter to **NULL** to specify the entire volume.

</dd> <dt>

*pSrcMemory* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](../winprog/windows-data-types.md)**

Pointer to the top-left corner of the source volume in memory.

</dd> <dt>

*SrcFormat* \[in\]
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

Member of the [D3DFORMAT](d3dformat.md) enumerated type, the pixel format of the source volume.

</dd> <dt>

*SrcRowPitch* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Pitch of source image, in bytes. For DXT formats (compressed texture formats), this number should represent the size of one row of cells, in bytes.

</dd> <dt>

*SrcSlicePitch* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Pitch of source image, in bytes. For DXT formats (compressed texture formats), this number should represent the size of one slice of cells, in bytes.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry) structure, the source palette of 256 colors or **NULL**.

</dd> <dt>

*pSrcBox* \[in\]
</dt> <dd>

Type: **const [**D3DBOX**](d3dbox.md)\***

Pointer to a [**D3DBOX**](d3dbox.md) structure. Specifies the source box. **NULL** is not a valid value for this parameter.

</dd> <dt>

*Filter* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

A combination of one or more [D3DX\_FILTER](d3dx-filter.md) controlling how the image is filtered. Specifying D3DX\_DEFAULT for this parameter is the equivalent of specifying D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER.

</dd> <dt>

*ColorKey* \[in\]
</dt> <dd>

Type: **[**D3DCOLOR**](d3dcolor.md)**

[**D3DCOLOR**](d3dcolor.md) value to replace with transparent black, or 0 to disable the colorkey. This is always a 32-bit ARGB color, independent of the source image format. Alpha is significant and should usually be set to FF for opaque color keys. Thus, for opaque black, the value would be equal to 0xFF000000.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

Writing to a non-level-zero surface of the volume texture will not cause the dirty rectangle to be updated. If **D3DXLoadVolumeFromMemory** is called and the texture was not already dirty (this is unlikely under normal usage scenarios), the application needs to explicitly call [**IDirect3DVolumeTexture9::AddDirtyBox**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dvolumetexture9-adddirtybox) on the volume texture.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[**D3DXLoadVolumeFromFile**](d3dxloadvolumefromfile.md)
</dt> <dt>

[**D3DXLoadVolumeFromResource**](d3dxloadvolumefromresource.md)
</dt> <dt>

[**D3DXLoadVolumeFromVolume**](d3dxloadvolumefromvolume.md)
</dt> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 
