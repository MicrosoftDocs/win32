---
Description: Creates a volume texture from a resource specified by a string. This is a more advanced function than D3DXCreateVolumeTextureFromResource.
ms.assetid: 02f2cb9e-4750-4854-aa74-202426427af5
title: D3DXCreateVolumeTextureFromResourceEx function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCreateVolumeTextureFromResourceEx function

Creates a volume texture from a resource specified by a string. This is a more advanced function than [**D3DXCreateVolumeTextureFromResource**](d3dxcreatevolumetexturefromresource.md).

## Syntax


```C++
HRESULT D3DXCreateVolumeTextureFromResourceEx(
  _In_    LPDIRECT3DDEVICE9        pDevice,
  _In_    HMODULE                  hSrcModule,
  _In_    LPCTSTR                  pSrcResource,
  _In_    UINT                     Width,
  _In_    UINT                     Height,
  _In_    UINT                     Depth,
  _In_    UINT                     MipLevels,
  _In_    DWORD                    Usage,
  _In_    D3DFORMAT                Format,
  _In_    D3DPOOL                  Pool,
  _In_    DWORD                    Filter,
  _In_    DWORD                    MipFilter,
  _In_    D3DCOLOR                 ColorKey,
  _Inout_ D3DXIMAGE_INFO           *pSrcInfo,
  _Out_   PALETTEENTRY             *pPalette,
  _Out_   LPDIRECT3DVOLUMETEXTURE9 *ppVolumeTexture
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface, representing the device to be associated with the texture.

</dd> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](winprog.windows_data_types)**

Handle to the module where the resource is located, or **NULL** for module associated with the image the operating system used to create the current process.

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

Pointer to a string that specifies the resource name. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*Width* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Width in pixels. If this value is zero or D3DX\_DEFAULT, the dimensions are taken from the file. The maximum dimension that a driver supports (for width, height, and depth) can be found in MaxVolumeExtent in [**D3DCAPS9**](/windows/win32/D3D9Caps/ns-d3d9caps-_d3dcaps9?branch=master).

</dd> <dt>

*Height* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Height, in pixels. If this value is zero or D3DX\_DEFAULT, the dimensions are taken from the file. The maximum dimension that a driver supports (for width, height, and depth) can be found in MaxVolumeExtent in [**D3DCAPS9**](/windows/win32/D3D9Caps/ns-d3d9caps-_d3dcaps9?branch=master).

</dd> <dt>

*Depth* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Depth, in pixels. If this value is zero or D3DX\_DEFAULT, the dimensions are taken from the file. The maximum dimension that a driver supports (for width, height, and depth) can be found in MaxVolumeExtent in [**D3DCAPS9**](/windows/win32/D3D9Caps/ns-d3d9caps-_d3dcaps9?branch=master).

</dd> <dt>

*MipLevels* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of mip levels requested. If this value is zero or D3DX\_DEFAULT, a complete mipmap chain is created.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

0, D3DUSAGE\_RENDERTARGET, or D3DUSAGE\_DYNAMIC. Setting this flag to D3DUSAGE\_RENDERTARGET indicates that the surface is to be used as a render target. The resource can then be passed to the *pNewRenderTarget* parameter of the [**SetRenderTarget**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setrendertarget?branch=master) method. If either D3DUSAGE\_RENDERTARGET or D3DUSAGE\_DYNAMIC is specified, *Pool* must be set to D3DPOOL\_DEFAULT, and the application should check that the device supports this operation by calling [**CheckDeviceFormat**](/windows/win32/d3d9helper/nf-d3d9-idirect3d9-checkdeviceformat?branch=master). D3DUSAGE\_DYNAMIC indicates that the surface should be handled dynamically. For more information about using dynamic textures, see [Using Dynamic Textures](performance-optimizations.md).

</dd> <dt>

*Format* \[in\]
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

Member of the [D3DFORMAT](d3dformat.md) enumerated type, describing the requested pixel format for the texture. The returned texture might have a different format from that specified by *Format*. Applications should check the format of the returned texture. If [D3DFMT\_UNKNOWN](other-d3dx-constants.md), the format is taken from the file. If D3DFMT\_FROM\_FILE, the format is taken exactly as it is in the file, and the call will fail if this violates device capabilities.

</dd> <dt>

*Pool* \[in\]
</dt> <dd>

Type: **[**D3DPOOL**](direct3d9.d3dpool)**

Member of the [**D3DPOOL**](direct3d9.d3dpool) enumerated type, describing the memory class into which the texture should be placed.

</dd> <dt>

*Filter* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

A combination of one or more [D3DX\_FILTER](d3dx-filter.md) controlling how the image is filtered. Specifying D3DX\_DEFAULT for this parameter is the equivalent of specifying D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER.

</dd> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

A combination of one or more [D3DX\_FILTER](d3dx-filter.md) controlling how the image is filtered. Specifying D3DX\_DEFAULT for this parameter is the equivalent of specifying D3DX\_FILTER\_BOX.

</dd> <dt>

*ColorKey* \[in\]
</dt> <dd>

Type: **[**D3DCOLOR**](d3dcolor.md)**

[**D3DCOLOR**](d3dcolor.md) value to replace with transparent black, or 0 to disable the colorkey. This is always a 32-bit ARGB color, independent of the source image format. Alpha is significant and should usually be set to FF for opaque color keys. Thus, for opaque black, the value would be equal to 0xFF000000.

</dd> <dt>

*pSrcInfo* \[in, out\]
</dt> <dd>

Type: **[**D3DXIMAGE\_INFO**](d3dximage-info.md)\***

Pointer to a [**D3DXIMAGE\_INFO**](d3dximage-info.md) structure to be filled in with a description of the data in the source image file, or **NULL**.

</dd> <dt>

*pPalette* \[out\]
</dt> <dd>

Type: **[**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master) structure, representing a 256-color palette to fill in, or **NULL**.

</dd> <dt>

*ppVolumeTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DVOLUMETEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvolumetexture9?branch=master)\***

Address of a pointer to an [**IDirect3DVolumeTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvolumetexture9?branch=master) interface, representing the created texture object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_NOTAVAILABLE, D3DERR\_OUTOFVIDEOMEMORY, D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXCreateVolumeTextureFromResourceExW. Otherwise, the function call resolves to D3DXCreateVolumeTextureFromResourceExA because ANSI strings are being used.

The resource being loaded must be an application-defined resource (RT\_RCDATA).

This function supports the following file formats: .bmp, .dds, .dib, .hdr, .jpg, .pfm, .png, .ppm, and .tga. See [**D3DXIMAGE\_FILEFORMAT**](direct3d9.d3dximage_fileformat).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[**D3DXCreateVolumeTextureFromFile**](d3dxcreatevolumetexturefromfile.md)
</dt> <dt>

[**D3DXCreateVolumeTextureFromFileEx**](d3dxcreatevolumetexturefromfileex.md)
</dt> <dt>

[**D3DXCreateVolumeTextureFromFileInMemory**](d3dxcreatevolumetexturefromfileinmemory.md)
</dt> <dt>

[**D3DXCreateVolumeTextureFromFileInMemoryEx**](d3dxcreatevolumetexturefromfileinmemoryex.md)
</dt> <dt>

[**D3DXCreateVolumeTextureFromResource**](d3dxcreatevolumetexturefromresource.md)
</dt> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




