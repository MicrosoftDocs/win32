---
Description: Creates an empty texture, adjusting the calling parameters as needed.
ms.assetid: ea028aa9-4f37-4625-9e07-9072ec1a61d0
title: D3DXCreateTexture function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXCreateTexture
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
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

Type: **[**LPDIRECT3DDEVICE9**](https://msdn.microsoft.com/library/Bb174336(v=VS.85).aspx)**

Pointer to an [**IDirect3DDevice9**](https://msdn.microsoft.com/library/Bb174336(v=VS.85).aspx) interface, representing the device to be associated with the texture.

</dd> <dt>

*Width* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Width in pixels. If this value is 0, a value of 1 is used. See Remarks.

</dd> <dt>

*Height* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Height in pixels. If this value is 0, a value of 1 is used. See Remarks.

</dd> <dt>

*MipLevels* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Number of mip levels requested. If this value is zero or D3DX\_DEFAULT, a complete mipmap chain is created.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

0, [**D3DUSAGE\_RENDERTARGET**](d3dusage.md), or **D3DUSAGE\_DYNAMIC**. Setting this flag to **D3DUSAGE\_RENDERTARGET** indicates that the surface is to be used as a render target by calling the [**SetRenderTarget**](/windows/desktop/api) method. If either **D3DUSAGE\_RENDERTARGET** or **D3DUSAGE\_DYNAMIC** is specified, the application should check that the device supports this operation by calling [**CheckDeviceFormat**](/windows/desktop/api). For more information about using dynamic textures, see [Using Dynamic Textures](performance-optimizations.md).

</dd> <dt>

*Format* \[in\]
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

Member of the [D3DFORMAT](d3dformat.md) enumerated type, describing the requested pixel format for the texture. The returned texture may be of a different format from that specified, if the device does not support the requested format. Applications should check the format of the returned texture to see if it matches the format requested.

</dd> <dt>

*Pool* \[in\]
</dt> <dd>

Type: **[**D3DPOOL**](https://msdn.microsoft.com/en-us/library/Bb172584(v=VS.85).aspx)**

Member of the [**D3DPOOL**](https://msdn.microsoft.com/en-us/library/Bb172584(v=VS.85).aspx) enumerated type, describing the memory class into which the texture should be placed.

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx)\***

Address of a pointer to an [**IDirect3DTexture9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx) interface, representing the created texture object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DERR\_NOTAVAILABLE, D3DERR\_OUTOFVIDEOMEMORY, E\_OUTOFMEMORY.

## Remarks

Internally, D3DXCreateTexture uses [**D3DXCheckTextureRequirements**](d3dxchecktexturerequirements.md) to adjust the calling parameters. Therefore, calls to D3DXCreateTexture will often succeed where calls to [**CreateTexture**](https://msdn.microsoft.com/library/Bb174363(v=VS.85).aspx) would fail.

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

 

 




