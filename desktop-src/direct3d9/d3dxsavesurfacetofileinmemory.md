---
Description: Saves a surface to an image file.
ms.assetid: 6320e5ed-e43d-43bf-a746-5478df42941d
title: D3DXSaveSurfaceToFileInMemory function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXSaveSurfaceToFileInMemory function

Saves a surface to an image file.

## Syntax


```C++
HRESULT D3DXSaveSurfaceToFileInMemory(
  _Out_       LPD3DXBUFFER         *ppDestBuf,
  _In_        D3DXIMAGE_FILEFORMAT DestFormat,
  _In_        LPDIRECT3DSURFACE9   pSrcSurface,
  _In_  const PALETTEENTRY         *pSrcPalette,
  _In_  const RECT                 *pSrcRect
);
```



## Parameters

<dl> <dt>

*ppDestBuf* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to an [**ID3DXBuffer**](id3dxbuffer.md) that will store the image.

</dd> <dt>

*DestFormat* \[in\]
</dt> <dd>

Type: **[**D3DXIMAGE\_FILEFORMAT**](https://msdn.microsoft.com/windows/desktop/245a0052-f156-44ad-ab46-3677a818167e)**

[**D3DXIMAGE\_FILEFORMAT**](https://msdn.microsoft.com/windows/desktop/245a0052-f156-44ad-ab46-3677a818167e) specifying the file format to use when saving. This function supports saving to all **D3DXIMAGE\_FILEFORMAT** formats except Portable Pixmap (.ppm) and Targa/Truevision Graphics Adapter (.tga).

</dd> <dt>

*pSrcSurface* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DSURFACE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dsurface9)**

Pointer to [**IDirect3DSurface9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dsurface9) interface containing the image to be saved.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/desktop/api/Wingdi/ns-wingdi-tagpaletteentry)\***

Pointer to a [**PALETTEENTRY**](/windows/desktop/api/Wingdi/ns-wingdi-tagpaletteentry) structure containing a palette of 256 colors. This parameter can be **NULL**.

</dd> <dt>

*pSrcRect* \[in\]
</dt> <dd>

Type: **const [**RECT**](https://msdn.microsoft.com/windows/desktop/9439cb6c-f2f7-4c27-b1d7-8ddf16d81fe8)\***

Pointer to a [**RECT**](https://msdn.microsoft.com/windows/desktop/9439cb6c-f2f7-4c27-b1d7-8ddf16d81fe8) structure. Specifies the source rectangle. Set this parameter to **NULL** to specify the entire image.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following: D3DERR\_INVALIDCALL.

## Remarks

This function handles conversion to and from compressed texture formats.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> <dt>

[**D3DXSaveVolumeToFileInMemory**](d3dxsavevolumetofileinmemory.md)
</dt> </dl>

 

 




