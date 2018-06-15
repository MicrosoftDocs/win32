---
Description: Checks texture-creation parameters.
ms.assetid: f8e788f3-02a9-4ee7-b74d-9e781a2fb39f
title: D3DXCheckTextureRequirements function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXCheckTextureRequirements function

Checks texture-creation parameters.

## Syntax


```C++
HRESULT D3DXCheckTextureRequirements(
  _In_    LPDIRECT3DDEVICE9 pDevice,
  _Inout_ UINT              *pWidth,
  _Inout_ UINT              *pHeight,
  _Inout_ UINT              *pNumMipLevels,
  _In_    DWORD             Usage,
  _Inout_ D3DFORMAT         *pFormat,
  _In_    D3DPOOL           Pool
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3ddevice9) interface, representing the device to be associated with the texture.

</dd> <dt>

*pWidth* \[in, out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to the requested width in pixels, or **NULL**. Returns the corrected size.

</dd> <dt>

*pHeight* \[in, out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to the requested height in pixels, or **NULL**. Returns the corrected size.

</dd> <dt>

*pNumMipLevels* \[in, out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to number of requested mipmap levels, or **NULL**. Returns the corrected number of mipmap levels.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

0 or [**D3DUSAGE\_RENDERTARGET**](d3dusage.md). Setting this flag to D3DUSAGE\_RENDERTARGET indicates that the surface is to be used as a render target. The resource can then be passed to the pNewRenderTarget parameter of the [**SetRenderTarget**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-setrendertarget) method. If **D3DUSAGE\_RENDERTARGET** is specified, the application should check that the device supports this operation by calling [**CheckDeviceFormat**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3d9-checkdeviceformat).

</dd> <dt>

*pFormat* \[in, out\]
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)\***

Pointer to a member of the [D3DFORMAT](d3dformat.md) enumerated type. Specifies the desired pixel format, or **NULL**. Returns the corrected format.

</dd> <dt>

*Pool* \[in\]
</dt> <dd>

Type: **[**D3DPOOL**](https://msdn.microsoft.com/en-us/library/Bb172584(v=VS.85).aspx)**

Member of the [**D3DPOOL**](https://msdn.microsoft.com/en-us/library/Bb172584(v=VS.85).aspx) enumerated type, describing the memory class into which the texture should be placed.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DERR\_NOTAVAILABLE.

## Remarks

If parameters to this function are invalid, this function returns corrected parameters.

This function uses the following heuristics when comparing the requested requirements against available formats:

-   Do not choose a format that has fewer channels.
-   Avoid [FOURCC](d3dformat.md) And 24-bit formats unless explicitly requested.
-   Try not to add new channels.
-   Try not to change the number of bits per channel.
-   Try to avoid converting between types of formats. For instance, avoid converting an ARGB format to a depth format.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




