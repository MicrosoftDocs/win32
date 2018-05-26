---
Description: Saves a texture to an image file.
ms.assetid: 8dcfd58a-ae1e-43c3-8ff1-94e3fa398b0f
title: D3DXSaveTextureToFileInMemory function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXSaveTextureToFileInMemory function

Saves a texture to an image file.

## Syntax


```C++
HRESULT D3DXSaveTextureToFileInMemory(
  _Out_       LPD3DXBUFFER           *ppDestBuf,
  _In_        D3DXIMAGE_FILEFORMAT   DestFormat,
  _In_        LPDIRECT3DBASETEXTURE9 pSrcTexture,
  _In_  const PALETTEENTRY           *pSrcPalette
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

Type: **[**D3DXIMAGE\_FILEFORMAT**](direct3d9.d3dximage_fileformat)**

[**D3DXIMAGE\_FILEFORMAT**](direct3d9.d3dximage_fileformat) specifying the file format to use when saving. This function supports saving to all **D3DXIMAGE\_FILEFORMAT** formats except Portable Pixmap (.ppm) and Targa/Truevision Graphics Adapter (.tga).

</dd> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DBASETEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dbasetexture9?branch=master)**

Pointer to [**IDirect3DBaseTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dbasetexture9?branch=master) interface containing the image to be saved.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master) structure containing a palette of 256 colors. This parameter can be **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

[**D3DXSaveSurfaceToFileInMemory**](d3dxsavesurfacetofileinmemory.md)
</dt> <dt>

[**D3DXSaveVolumeToFileInMemory**](d3dxsavevolumetofileinmemory.md)
</dt> </dl>

 

 




