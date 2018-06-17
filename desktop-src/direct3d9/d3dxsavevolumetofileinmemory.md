---
Description: Saves a volume to a buffer. The method creates an ID3DXBuffer buffer to store the data, and returns that object.
ms.assetid: 4887ff1f-7904-4764-b284-b2c8e037f806
title: D3DXSaveVolumeToFileInMemory function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXSaveVolumeToFileInMemory function

Saves a volume to a buffer. The method creates an [**ID3DXBuffer**](id3dxbuffer.md) buffer to store the data, and returns that object.

## Syntax


```C++
HRESULT D3DXSaveVolumeToFileInMemory(
  _Out_       LPD3DXBUFFER         *ppDestBuf,
  _In_        D3DXIMAGE_FILEFORMAT DestFormat,
  _In_        LPDIRECT3DVOLUME9    pSrcVolume,
  _In_  const PALETTEENTRY         *pSrcPalette,
  _In_  const D3DBOX               *pSrcBox
);
```



## Parameters

<dl> <dt>

*ppDestBuf* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to an [**ID3DXBuffer**](id3dxbuffer.md) buffer that will store the image.

</dd> <dt>

*DestFormat* \[in\]
</dt> <dd>

Type: **[**D3DXIMAGE\_FILEFORMAT**](https://msdn.microsoft.com/en-us/library/Bb172878(v=VS.85).aspx)**

[**D3DXIMAGE\_FILEFORMAT**](https://msdn.microsoft.com/en-us/library/Bb172878(v=VS.85).aspx) specifying the file format to use when saving. This function supports saving to all **D3DXIMAGE\_FILEFORMAT** formats except Portable Pixmap (.ppm) and Targa/Truevision Graphics Adapter (.tga).

</dd> <dt>

*pSrcVolume* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DVOLUME9**](/windows/desktop/api)**

Pointer to [**IDirect3DVolume9**](/windows/desktop/api) interface containing the image to be saved.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/desktop/api/Wingdi/ns-wingdi-tagpaletteentry)\***

Pointer to a [**PALETTEENTRY**](/windows/desktop/api/Wingdi/ns-wingdi-tagpaletteentry) structure containing a palette of 256 colors. This parameter can be **NULL**.

</dd> <dt>

*pSrcBox* \[in\]
</dt> <dd>

Type: **const [**D3DBOX**](d3dbox.md)\***

Pointer to a [**D3DBOX**](d3dbox.md) structure. Specifies the source box. Set this parameter to **NULL** to specify the entire volume.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following: D3DERR\_INVALIDCALL

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> <dt>

[**D3DXSaveVolumeToFile**](d3dxsavevolumetofile.md)
</dt> </dl>

 

 




