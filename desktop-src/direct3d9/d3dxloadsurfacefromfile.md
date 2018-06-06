---
Description: Loads a surface from a file.
ms.assetid: cbd360b6-6cee-418b-8c45-506e190eb2f6
title: D3DXLoadSurfaceFromFile function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXLoadSurfaceFromFile function

Loads a surface from a file.

## Syntax


```C++
HRESULT D3DXLoadSurfaceFromFile(
  _In_          LPDIRECT3DSURFACE9 pDestSurface,
  _In_    const PALETTEENTRY       *pDestPalette,
  _In_    const RECT               *pDestRect,
  _In_          LPCTSTR            pSrcFile,
  _In_    const RECT               *pSrcRect,
  _In_          DWORD              Filter,
  _In_          D3DCOLOR           ColorKey,
  _Inout_       D3DXIMAGE_INFO     *pSrcInfo
);
```



## Parameters

<dl> <dt>

*pDestSurface* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DSURFACE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dsurface9)**

Pointer to an [**IDirect3DSurface9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dsurface9) interface. Specifies the destination surface, which receives the image.

</dd> <dt>

*pDestPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/desktop/api/Wingdi/ns-wingdi-tagpaletteentry)\***

Pointer to a [**PALETTEENTRY**](/windows/desktop/api/Wingdi/ns-wingdi-tagpaletteentry) structure, the destination palette of 256 colors or **NULL**.

</dd> <dt>

*pDestRect* \[in\]
</dt> <dd>

Type: **const [**RECT**](https://msdn.microsoft.com/9439cb6c-f2f7-4c27-b1d7-8ddf16d81fe8)\***

Pointer to a [**RECT**](https://msdn.microsoft.com/9439cb6c-f2f7-4c27-b1d7-8ddf16d81fe8) structure. Specifies the destination rectangle. Set this parameter to **NULL** to specify the entire surface.

</dd> <dt>

*pSrcFile* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Pointer to a string that specifies the filename. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*pSrcRect* \[in\]
</dt> <dd>

Type: **const [**RECT**](https://msdn.microsoft.com/9439cb6c-f2f7-4c27-b1d7-8ddf16d81fe8)\***

Pointer to a [**RECT**](https://msdn.microsoft.com/9439cb6c-f2f7-4c27-b1d7-8ddf16d81fe8) structure. Specifies the source rectangle. Set this parameter to **NULL** to specify the entire image.

</dd> <dt>

*Filter* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Combination of one or more [D3DX\_FILTER](d3dx-filter.md) controlling how the image is filtered. Specifying D3DX\_DEFAULT for this parameter is the equivalent of specifying D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER.

</dd> <dt>

*ColorKey* \[in\]
</dt> <dd>

Type: **[**D3DCOLOR**](d3dcolor.md)**

[**D3DCOLOR**](d3dcolor.md) value to replace with transparent black, or 0 to disable the colorkey. This is always a 32-bit ARGB color, independent of the source image format. Alpha is significant and should usually be set to FF for opaque color keys Thus, for opaque black, the value would be equal to 0xFF000000.

</dd> <dt>

*pSrcInfo* \[in, out\]
</dt> <dd>

Type: **[**D3DXIMAGE\_INFO**](d3dximage-info.md)\***

Pointer to a [**D3DXIMAGE\_INFO**](d3dximage-info.md) structure to be filled with a description of the data in the source image file, or **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXLoadSurfaceFromFileW. Otherwise, the function call resolves to D3DXLoadSurfaceFromFileA because ANSI strings are being used.

This function handles conversion to and from compressed texture formats and supports the following file formats: .bmp, .dds, .dib, .hdr, .jpg, .pfm, .png, .ppm, and .tga. See [**D3DXIMAGE\_FILEFORMAT**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dximage_fileformat.htm).

Writing to a non-level-zero surface will not cause the dirty rectangle to be updated. If **D3DXLoadSurfaceFromFile** is called and the surface was not already dirty (this is unlikely under normal usage scenarios), the application needs to explicitly call [**AddDirtyRect**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dtexture9-adddirtyrect) on the surface.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




