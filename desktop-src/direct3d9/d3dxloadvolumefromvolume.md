---
Description: 'Loads a volume from another volume.'
ms.assetid: 'bc162f91-feb7-4571-ae4a-abaa5e7953f6'
title: D3DXLoadVolumeFromVolume function
---

# D3DXLoadVolumeFromVolume function

Loads a volume from another volume.

## Syntax


```C++
HRESULT D3DXLoadVolumeFromVolume(
  _In_       LPDIRECT3DVOLUME9 pDestVolume,
  _In_ const PALETTEENTRY      *pDestPalette,
  _In_ const D3DBOX            *pDestBox,
  _In_       LPDIRECT3DVOLUME9 pSrcVolume,
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

Type: **[**LPDIRECT3DVOLUME9**](idirect3dvolume9.md)**

Pointer to an [**IDirect3DVolume9**](idirect3dvolume9.md) interface. Specifies the destination volume, which receives the image.

</dd> <dt>

*pDestPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](paletteentry.md)\***

Pointer to a [**PALETTEENTRY**](paletteentry.md) structure, the destination palette of 256 colors or **NULL**.

</dd> <dt>

*pDestBox* \[in\]
</dt> <dd>

Type: **const [**D3DBOX**](d3dbox.md)\***

Pointer to a [**D3DBOX**](d3dbox.md) structure. Specifies the destination box. Set this parameter to **NULL** to specify the entire volume.

</dd> <dt>

*pSrcVolume* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DVOLUME9**](idirect3dvolume9.md)**

A Pointer to an [**IDirect3DVolume9**](idirect3dvolume9.md) interface. Specifies the source volume.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](paletteentry.md)\***

Pointer to a [**PALETTEENTRY**](paletteentry.md) structure, the source palette of 256 colors or **NULL**.

</dd> <dt>

*pSrcBox* \[in\]
</dt> <dd>

Type: **const [**D3DBOX**](d3dbox.md)\***

Pointer to a [**D3DBOX**](d3dbox.md) structure. Specifies the source box. Set this parameter to **NULL** to specify the entire volume.

</dd> <dt>

*Filter* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

A combination of one or more [D3DX\_FILTER](d3dx-filter.md), controlling how the image is filtered. Specifying D3DX\_DEFAULT for this parameter is the equivalent of specifying D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER.

</dd> <dt>

*ColorKey* \[in\]
</dt> <dd>

Type: **[**D3DCOLOR**](d3dcolor.md)**

[**D3DCOLOR**](d3dcolor.md) value to replace with transparent black, or 0 to disable the colorkey. This is always a 32-bit ARGB color, independent of the source image format. Alpha is significant and should usually be set to FF for opaque color keys. Thus, for opaque black, the value would be equal to 0xFF000000.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

Writing to a non-level-zero surface of the volume texture will not cause the dirty rectangle to be updated. If **D3DXLoadVolumeFromVolume** is called and the surface was not already dirty (this is unlikely under normal usage scenarios), the application needs to explicitly call [**IDirect3DVolumeTexture9::AddDirtyBox**](idirect3dvolumetexture9--adddirtybox.md) on the surface.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[**D3DXLoadVolumeFromFile**](d3dxloadvolumefromfile.md)
</dt> <dt>

[**D3DXLoadVolumeFromFileInMemory**](d3dxloadvolumefromfileinmemory.md)
</dt> <dt>

[**D3DXLoadVolumeFromMemory**](d3dxloadvolumefrommemory.md)
</dt> <dt>

[**D3DXLoadVolumeFromResource**](d3dxloadvolumefromresource.md)
</dt> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




