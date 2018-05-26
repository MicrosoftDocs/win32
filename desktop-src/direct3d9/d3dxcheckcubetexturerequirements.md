---
Description: Checks cube-texture-creation parameters.
ms.assetid: 56ced947-1142-4d05-95e3-ca6a26b147d4
title: D3DXCheckCubeTextureRequirements function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCheckCubeTextureRequirements function

Checks cube-texture-creation parameters.

## Syntax


```C++
HRESULT D3DXCheckCubeTextureRequirements(
  _In_    LPDIRECT3DDEVICE9 pDevice,
  _Inout_ UINT              *pSize,
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

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface, representing the device to be associated with the cube texture.

</dd> <dt>

*pSize* \[in, out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

Pointer to the requested width and height in pixels, or **NULL**. Returns the corrected size.

</dd> <dt>

*pNumMipLevels* \[in, out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

Pointer to the number of requested mipmap levels, or **NULL**. Returns the corrected number of mipmap levels.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

0 or D3DUSAGE\_RENDERTARGET. Setting this flag to D3DUSAGE\_RENDERTARGET indicates that the surface is to be used as a render target. The resource can then be passed to the pNewRenderTarget parameter of the [**SetRenderTarget**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setrendertarget?branch=master) method. If D3DUSAGE\_RENDERTARGET is specified, the application should check that the device supports this operation by calling [**CheckDeviceFormat**](/windows/win32/d3d9helper/nf-d3d9-idirect3d9-checkdeviceformat?branch=master).

</dd> <dt>

*pFormat* \[in, out\]
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)\***

Pointer to a member of the [D3DFORMAT](d3dformat.md) enumerated type. Specifies the desired pixel format, or **NULL**. Returns the corrected format.

</dd> <dt>

*Pool* \[in\]
</dt> <dd>

Type: **[**D3DPOOL**](direct3d9.d3dpool)**

Member of the [**D3DPOOL**](direct3d9.d3dpool) enumerated type, describing the memory class into which the texture should be placed.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_NOTAVAILABLE, D3DERR\_INVALIDCALL.

## Remarks

If parameters to this function are invalid, this function returns corrected parameters.

Cube textures differ from other surfaces in that they are collections of surfaces. To call [**SetRenderTarget**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setrendertarget?branch=master) with a cube texture, you must select an individual face using [**GetCubeMapSurface**](/windows/win32/d3d9helper/nf-d3d9-idirect3dcubetexture9-getcubemapsurface?branch=master) and pass the resulting surface to **SetRenderTarget**.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




