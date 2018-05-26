---
Description: Creates an empty texture, adjusting the calling parameters as needed.
ms.assetid: ea028aa9-4f37-4625-9e07-9072ec1a61d0
title: D3DXCreateTexture function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCreateTexture function

Creates an empty texture, adjusting the calling parameters as needed.

## Syntax


```C++
HRESULT D3DXCreateTexture(
  _In_  LPDIRECT3DDEVICE9  pDevice,
  _In_  UINT               Width,
  _In_  UINT               Height,
  _In_  UINT               MipLevels,
  _In_  DWORD              Usage,
  _In_  D3DFORMAT          Format,
  _In_  D3DPOOL            Pool,
  _Out_ LPDIRECT3DTEXTURE9 *ppTexture
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface, representing the device to be associated with the texture.

</dd> <dt>

*Width* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Width in pixels. If this value is 0, a value of 1 is used. See Remarks.

</dd> <dt>

*Height* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Height in pixels. If this value is 0, a value of 1 is used. See Remarks.

</dd> <dt>

*MipLevels* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of mip levels requested. If this value is zero or D3DX\_DEFAULT, a complete mipmap chain is created.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

0, [**D3DUSAGE\_RENDERTARGET**](d3dusage.md), or **D3DUSAGE\_DYNAMIC**. Setting this flag to **D3DUSAGE\_RENDERTARGET** indicates that the surface is to be used as a render target by calling the [**SetRenderTarget**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setrendertarget?branch=master) method. If either **D3DUSAGE\_RENDERTARGET** or **D3DUSAGE\_DYNAMIC** is specified, the application should check that the device supports this operation by calling [**CheckDeviceFormat**](/windows/win32/d3d9helper/nf-d3d9-idirect3d9-checkdeviceformat?branch=master). For more information about using dynamic textures, see [Using Dynamic Textures](performance-optimizations.md).

</dd> <dt>

*Format* \[in\]
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

Member of the [D3DFORMAT](d3dformat.md) enumerated type, describing the requested pixel format for the texture. The returned texture may be of a different format from that specified, if the device does not support the requested format. Applications should check the format of the returned texture to see if it matches the format requested.

</dd> <dt>

*Pool* \[in\]
</dt> <dd>

Type: **[**D3DPOOL**](direct3d9.d3dpool)**

Member of the [**D3DPOOL**](direct3d9.d3dpool) enumerated type, describing the memory class into which the texture should be placed.

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master)\***

Address of a pointer to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) interface, representing the created texture object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DERR\_NOTAVAILABLE, D3DERR\_OUTOFVIDEOMEMORY, E\_OUTOFMEMORY.

## Remarks

Internally, D3DXCreateTexture uses [**D3DXCheckTextureRequirements**](d3dxchecktexturerequirements.md) to adjust the calling parameters. Therefore, calls to D3DXCreateTexture will often succeed where calls to [**CreateTexture**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-createtexture?branch=master) would fail.

If both Height and Width are set to [D3DX\_DEFAULT](other-d3dx-constants.md), a value of 256 is used for both parameters. If either Height or Width is set to D3DX\_DEFAULT And the other parameter is set to a numeric value, the texture will be square with both the height and width equal to the numeric value.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




