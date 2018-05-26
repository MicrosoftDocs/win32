---
Description: Saves a volume to a file on disk.
ms.assetid: 4d33fba5-e003-4385-b683-aff6723af2a5
title: D3DXSaveVolumeToFile function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXSaveVolumeToFile function

Saves a volume to a file on disk.

## Syntax


```C++
HRESULT D3DXSaveVolumeToFile(
  _In_       LPCTSTR              pDestFile,
  _In_       D3DXIMAGE_FILEFORMAT DestFormat,
  _In_       LPDIRECT3DVOLUME9    pSrcVolume,
  _In_ const PALETTEENTRY         *pSrcPalette,
  _In_ const D3DBOX               *pSrcBox
);
```



## Parameters

<dl> <dt>

*pDestFile* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

Pointer to a string that specifies the file name of the destination image. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*DestFormat* \[in\]
</dt> <dd>

Type: **[**D3DXIMAGE\_FILEFORMAT**](direct3d9.d3dximage_fileformat)**

[**D3DXIMAGE\_FILEFORMAT**](direct3d9.d3dximage_fileformat) specifying the file format to use when saving. This function supports saving to all **D3DXIMAGE\_FILEFORMAT** formats except Portable Pixmap (.ppm) and Targa/Truevision Graphics Adapter (.tga).

</dd> <dt>

*pSrcVolume* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DVOLUME9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvolume9?branch=master)**

Pointer to [**IDirect3DVolume9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvolume9?branch=master) interface containing the image to be saved.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master) structure containing a palette of 256 colors. This parameter can be **NULL**.

</dd> <dt>

*pSrcBox* \[in\]
</dt> <dd>

Type: **const [**D3DBOX**](d3dbox.md)\***

Pointer to a [**D3DBOX**](d3dbox.md) structure. Specifies the source box. Set this parameter to **NULL** to specify the entire volume.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following: D3DERR\_INVALIDCALL

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXSaveVolumeToFileW. Otherwise, the function call resolves to &gt;D3DXSaveVolumeToFileA because ANSI strings are being used.

This function handles conversion to and from compressed texture formats.

If the volume is nondynamic (because of a usage parameter set to 0 at the creation) and located in video memory (the memory pool set to D3DPOOL\_DEFAULT), [**D3DXSaveTextureToFile**](d3dxsavetexturetofile.md) will fail because D3DX cannot lock nondynamic volumes located in video memory.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> <dt>

[**D3DXSaveSurfaceToFile**](d3dxsavesurfacetofile.md)
</dt> <dt>

[**D3DXSaveTextureToFile**](d3dxsavetexturetofile.md)
</dt> <dt>

[**D3DXSaveVolumeToFileInMemory**](d3dxsavevolumetofileinmemory.md)
</dt> </dl>

 

 




