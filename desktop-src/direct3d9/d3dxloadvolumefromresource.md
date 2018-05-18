---
Description: 'Loads a volume from a resource.'
ms.assetid: '3fa1243b-5e31-4737-8d3c-08852d6528d9'
title: D3DXLoadVolumeFromResource function
---

# D3DXLoadVolumeFromResource function

Loads a volume from a resource.

## Syntax


```C++
HRESULT D3DXLoadVolumeFromResource(
  _In_       LPDIRECT3DVOLUME9 pDestVolume,
  _In_ const PALETTEENTRY      *pDestPalette,
  _In_ const D3DBOX            *pDestBox,
  _In_       HMODULE           hSrcModule,
  _In_       LPCSTR            pSrcResource,
  _In_ const D3DBOX            *pSrcBox,
  _In_       DWORD             Filter,
  _In_       D3DCOLOR          ColorKey,
  _In_       D3DXIMAGE_INFO    *pSrcInfo
);
```



## Parameters

<dl> <dt>

*pDestVolume* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DVOLUME9**](idirect3dvolume9.md)**

Pointer to an [**IDirect3DVolume9**](idirect3dvolume9.md) interface. Specifies the destination volume.

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

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](winprog.windows_data_types)**

Handle to the module where the resource is located, or **NULL** for module associated with the image the operating system used to create the current process.

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Pointer to a string that specifies the file name of the source image. If UNICODE or \_UNICODE are defined, this parameter type is LPCWSTR, otherwise, the type is LPCSTR.

</dd> <dt>

*pSrcBox* \[in\]
</dt> <dd>

Type: **const [**D3DBOX**](d3dbox.md)\***

Pointer to a [**D3DBOX**](d3dbox.md) structure. Specifies the source box. Set this parameter to **NULL** to specify the entire volume.

</dd> <dt>

*Filter* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Combination of one or more [D3DX\_FILTER](d3dx-filter.md), controlling how the image is filtered. Specifying D3DX\_DEFAULT for this parameter is the equivalent of specifying D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER.

</dd> <dt>

*ColorKey* \[in\]
</dt> <dd>

Type: **[**D3DCOLOR**](d3dcolor.md)**

[**D3DCOLOR**](d3dcolor.md) value to replace with transparent black, or 0 to disable the colorkey. This is always a 32-bit ARGB color, independent of the source image format. Alpha is significant and should usually be set to FF for opaque color keys. Thus, for opaque black, the value would be equal to 0xFF000000.

</dd> <dt>

*pSrcInfo* \[in\]
</dt> <dd>

Type: **[**D3DXIMAGE\_INFO**](d3dximage-info.md)\***

Pointer to a [**D3DXIMAGE\_INFO**](d3dximage-info.md) structure to be filled with a description of the data in the source image file, or **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

The resource being loaded must be a bitmap resource(RT\_BITMAP).

This function handles conversion to and from compressed texture formats.

Writing to a non-level-zero surface of the volume texture will not cause the dirty rectangle to be updated. If [**D3DXLoadVolumeFromFile**](d3dxloadvolumefromfile.md) is called and the texture was not already dirty (this is unlikely under normal usage scenarios), the application needs to explicitly call [**IDirect3DVolumeTexture9::AddDirtyBox**](idirect3dvolumetexture9--adddirtybox.md) on the volume texture.

This function supports both Unicode and ANSI strings.

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

[**D3DXLoadVolumeFromVolume**](d3dxloadvolumefromvolume.md)
</dt> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




