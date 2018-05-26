---
Description: Loads a surface from memory.
ms.assetid: 9a36e395-fd00-47fe-8df1-cda8c80182ef
title: D3DXLoadSurfaceFromMemory function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXLoadSurfaceFromMemory function

Loads a surface from memory.

## Syntax


```C++
HRESULT D3DXLoadSurfaceFromMemory(
  _In_       LPDIRECT3DSURFACE9 pDestSurface,
  _In_ const PALETTEENTRY       *pDestPalette,
  _In_ const RECT               *pDestRect,
  _In_       LPCVOID            pSrcMemory,
  _In_       D3DFORMAT          SrcFormat,
  _In_       UINT               SrcPitch,
  _In_ const PALETTEENTRY       *pSrcPalette,
  _In_ const RECT               *pSrcRect,
  _In_       DWORD              Filter,
  _In_       D3DCOLOR           ColorKey
);
```



## Parameters

<dl> <dt>

*pDestSurface* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DSURFACE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dsurface9?branch=master)**

Pointer to an [**IDirect3DSurface9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dsurface9?branch=master) interface. Specifies the destination surface, which receives the image.

</dd> <dt>

*pDestPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master) structure, the destination palette of 256 colors or **NULL**.

</dd> <dt>

*pDestRect* \[in\]
</dt> <dd>

Type: **const [**RECT**](gdi.rect)\***

Pointer to a [**RECT**](gdi.rect) structure. Specifies the destination rectangle. Set this parameter to **NULL** to specify the entire surface.

</dd> <dt>

*pSrcMemory* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](winprog.windows_data_types)**

Pointer to the upper left corner of the source image in memory.

</dd> <dt>

*SrcFormat* \[in\]
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

Member of the [D3DFORMAT](d3dformat.md) enumerated type, the pixel format of the source image.

</dd> <dt>

*SrcPitch* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Pitch of source image, in bytes. For DXT formats, this number should represent the width of one row of cells, in bytes.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master) structure, the source palette of 256 colors or **NULL**.

</dd> <dt>

*pSrcRect* \[in\]
</dt> <dd>

Type: **const [**RECT**](gdi.rect)\***

Pointer to a [**RECT**](gdi.rect) structure. Specifies the dimensions of the source image in memory. This value cannot be **NULL**.

</dd> <dt>

*Filter* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Combination of one or more [D3DX\_FILTER](d3dx-filter.md) controlling how the image is filtered. Specifying D3DX\_DEFAULT for this parameter is the equivalent of specifying D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER.

</dd> <dt>

*ColorKey* \[in\]
</dt> <dd>

Type: **[**D3DCOLOR**](d3dcolor.md)**

[**D3DCOLOR**](d3dcolor.md) value to replace with transparent black, or 0 to disable the colorkey. This is always a 32-bit ARGB color, independent of the source image format. Alpha is significant and should usually be set to FF for opaque color keys. Thus, for opaque black, the value would be equal to 0xFF000000.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

This function handles conversion to and from compressed texture formats.

Writing to a non-level-zero surface will not cause the dirty rectangle to be updated. If **D3DXLoadSurfaceFromMemory** is called and the surface was not already dirty (this is unlikely under normal usage scenarios), the application needs to explicitly call [**AddDirtyRect**](/windows/win32/d3d9helper/nf-d3d9-idirect3dtexture9-adddirtyrect?branch=master) on the surface.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




