---
Description: Creates a texture from a resource.
ms.assetid: 7c841f21-5565-4923-a2fe-bbd618616f87
title: D3DXCreateTextureFromResource function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXCreateTextureFromResource function

Creates a texture from a resource.

## Syntax


```C++
HRESULT D3DXCreateTextureFromResource(
  _In_  LPDIRECT3DDEVICE9  pDevice,
  _In_  HMODULE            hSrcModule,
  _In_  LPCTSTR            pSrcResource,
  _Out_ LPDIRECT3DTEXTURE9 *ppTexture
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3ddevice9) interface, representing the device to be associated with the texture.

</dd> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Handle to the module where the resource is located, or **NULL** for module associated with the image the operating system used to create the current process.

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Pointer to a string that specifies the resource name. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dtexture9)\***

Address of a pointer to an [**IDirect3DTexture9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dtexture9) interface, representing the created texture object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_NOTAVAILABLE, D3DERR\_OUTOFVIDEOMEMORY, D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXCreateTextureFromResourceW. Otherwise, the function call resolves to D3DXCreateTextureFromResourceA because ANSI strings are being used.

The function is equivalent to D3DXCreateTextureFromResourceEx(pDevice, hSrcModule, pSrcResource, D3DX\_DEFAULT, D3DX\_DEFAULT, D3DX\_DEFAULT, 0, D3DFMT\_UNKNOWN, D3DPOOL\_MANAGED, D3DX\_DEFAULT, D3DX\_DEFAULT, 0, **NULL**, **NULL**, ppTexture).

The resource being loaded must be of type RT\_BITMAP or RT\_RCDATA. Resource type RT\_RCDATA is used to load formats other than bitmaps (such as .tga, .jpg, and .dds).

This function supports the following file formats: .bmp, .dds, .dib, .hdr, .jpg, .pfm, .png, .ppm, and .tga. See [**D3DXIMAGE\_FILEFORMAT**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dximage_fileformat.htm).

Note that a resource created with this function when called from a IDirect3DDevice9 object will be placed in the memory class denoted by D3DPOOL\_MANAGED. When this method is called from a IDirect3DDevice9Ex object the resource will be placed in the memory class denoted by D3DPOOL\_DEFAULT.

Filtering is automatically applied to a texture created using this method. The filtering is equivalent to D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER in [D3DX\_FILTER](d3dx-filter.md).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[**D3DXCreateTextureFromResourceEx**](d3dxcreatetexturefromresourceex.md)
</dt> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




