---
Description: Creates a volume texture from a resource.
ms.assetid: 82a0b7aa-69fa-450d-b0d2-769f05fd75ea
title: D3DXCreateVolumeTextureFromResource function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCreateVolumeTextureFromResource function

Creates a volume texture from a resource.

## Syntax


```C++
HRESULT D3DXCreateVolumeTextureFromResource(
  _In_  LPDIRECT3DDEVICE9        pDevice,
  _In_  HMODULE                  hSrcModule,
  _In_  LPCTSTR                  pSrcResource,
  _Out_ LPDIRECT3DVOLUMETEXTURE9 *ppVolumeTexture
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface, representing the device to be associated with the volume texture.

</dd> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](winprog.windows_data_types)**

Handle to the module where the resource is located, or **NULL** for the module associated with the image the operating system used to create the current process.

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

Pointer to a string that specifies the resource name. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*ppVolumeTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DVOLUMETEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvolumetexture9?branch=master)\***

Address of a pointer to an [**IDirect3DVolumeTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvolumetexture9?branch=master) interface representing the created texture object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_NOTAVAILABLE, D3DERR\_OUTOFVIDEOMEMORY, D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXCreateVolumeTextureFromResourceW. Otherwise, the function call resolves to D3DXCreateVolumeTextureFromResourceA because ANSI strings are being used.

The function is equivalent to D3DXCreateVolumeTextureFromResourceEx(pDevice, hSrcModule, pSrcResource, D3DX\_DEFAULT, D3DX\_DEFAULT, D3DX\_DEFAULT, D3DX\_DEFAULT, 0, D3DFMT\_UNKNOWN, D3DPOOL\_MANAGED, D3DX\_DEFAULT, D3DX\_DEFAULT, 0, **NULL**, **NULL**, ppVolumeTexture).

The resource being loaded must be an application-defined resource (RT\_RCDATA).

This function supports the following file formats: .bmp, .dds, .dib, .hdr, .jpg, .pfm, .png, .ppm, and .tga. See [**D3DXIMAGE\_FILEFORMAT**](direct3d9.d3dximage_fileformat).

Note that a resource created with this function when called from a IDirect3DDevice9 object will be placed in the memory class denoted by D3DPOOL\_MANAGED. When this method is called from a IDirect3DDevice9Ex object the resource will be placed in the memory class denoted by D3DPOOL\_DEFAULT.

Filtering is automatically applied to a texture created using this method. The filtering is equivalent to D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER in [D3DX\_FILTER](d3dx-filter.md).

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

[**D3DXCreateVolumeTextureFromResourceEx**](d3dxcreatevolumetexturefromresourceex.md)
</dt> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




