---
Description: Converts a height map into a normal map. The (x,y,z) components of each normal are mapped to the (r,g,b) channels of the output texture.
ms.assetid: ed9053c0-b1df-4f74-bdee-627c0f60d942
title: D3DXComputeNormalMap function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXComputeNormalMap function

Converts a height map into a normal map. The (x,y,z) components of each normal are mapped to the (r,g,b) channels of the output texture.

## Syntax


```C++
HRESULT D3DXComputeNormalMap(
  _Out_       LPDIRECT3DTEXTURE9 pTexture,
  _In_        LPDIRECT3DTEXTURE9 pSrcTexture,
  _In_  const PALETTEENTRY       *pSrcPalette,
  _In_        DWORD              Flags,
  _In_        DWORD              Channel,
  _In_        FLOAT              Amplitude
);
```



## Parameters

<dl> <dt>

*pTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master)**

Pointer to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) interface, representing the destination texture.

</dd> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master)**

Pointer to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) interface, representing the source height-map texture.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/Wingdi/ns-wingdi-tagpaletteentry?branch=master) type that contains the source palette of 256 colors or **NULL**.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

One or more [D3DX\_NORMALMAP](d3dx-normalmap.md) flags that control generation of normal maps.

</dd> <dt>

*Channel* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

One [D3DX\_CHANNEL](d3dx-channel.md) flag specifying the source of height information.

</dd> <dt>

*Amplitude* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Constant value multiplier that increases (or decreases) the values in the normal map. Higher values usually make bumps more visible, lower values usually make bumps less visible.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following value: D3DERR\_INVALIDCALL.

## Remarks

This method computes the normal by using the central difference with a kernel size of 3x3. The central differencing denominator used is 2.0. RGB channels in the destination contain biased (x,y,z) components of the normal.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 




