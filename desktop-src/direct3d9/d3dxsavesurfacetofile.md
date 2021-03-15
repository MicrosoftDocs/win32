---
description: Saves a surface to a file.
ms.assetid: 28bbf728-afde-4d25-8562-9d6a957aab2d
title: D3DXSaveSurfaceToFile function (D3dx9tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXSaveSurfaceToFile
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXSaveSurfaceToFile function

Saves a surface to a file.

## Syntax


```C++
HRESULT D3DXSaveSurfaceToFile(
  _In_       LPCTSTR              pDestFile,
  _In_       D3DXIMAGE_FILEFORMAT DestFormat,
  _In_       LPDIRECT3DSURFACE9   pSrcSurface,
  _In_ const PALETTEENTRY         *pSrcPalette,
  _In_ const RECT                 *pSrcRect
);
```



## Parameters

<dl> <dt>

*pDestFile* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Pointer to a string that specifies the file name of the destination image. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*DestFormat* \[in\]
</dt> <dd>

Type: **[**D3DXIMAGE\_FILEFORMAT**](./d3dximage-fileformat.md)**

[**D3DXIMAGE\_FILEFORMAT**](./d3dximage-fileformat.md) specifying the file format to use when saving. This function supports saving to all **D3DXIMAGE\_FILEFORMAT** formats except Portable Pixmap (.ppm) and Targa/Truevision Graphics Adapter (.tga).

</dd> <dt>

*pSrcSurface* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DSURFACE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dsurface9)**

Pointer to [**IDirect3DSurface9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dsurface9) interface, containing the image to be saved.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry) structure containing a palette of 256 colors. This parameter can be **NULL**.

</dd> <dt>

*pSrcRect* \[in\]
</dt> <dd>

Type: **const [**RECT**](/previous-versions//dd162897(v=vs.85))\***

Pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure. Specifies the source rectangle. Set this parameter to **NULL** to specify the entire image.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following: D3DERR\_INVALIDCALL

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXSaveSurfaceToFileW. Otherwise, the function call resolves to D3DXSaveSurfaceToFileA because ANSI strings are being used.

This function handles conversion to and from compressed texture formats.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> <dt>

[**D3DXSaveTextureToFile**](d3dxsavetexturetofile.md)
</dt> <dt>

[**D3DXSaveVolumeToFile**](d3dxsavevolumetofile.md)
</dt> </dl>

 

 
