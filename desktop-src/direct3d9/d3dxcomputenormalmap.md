---
Description: Converts a height map into a normal map. The (x,y,z) components of each normal are mapped to the (r,g,b) channels of the output texture.
ms.assetid: ed9053c0-b1df-4f74-bdee-627c0f60d942
title: D3DXComputeNormalMap function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXComputeNormalMap
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
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

Type: **[**LPDIRECT3DTEXTURE9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx)**

Pointer to an [**IDirect3DTexture9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx) interface, representing the destination texture.

</dd> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx)**

Pointer to an [**IDirect3DTexture9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx) interface, representing the source height-map texture.

</dd> <dt>

*pSrcPalette* \[in\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/desktop/api/Wingdi/ns-wingdi-tagpaletteentry)\***

Pointer to a [**PALETTEENTRY**](/windows/desktop/api/Wingdi/ns-wingdi-tagpaletteentry) type that contains the source palette of 256 colors or **NULL**.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

One or more [D3DX\_NORMALMAP](d3dx-normalmap.md) flags that control generation of normal maps.

</dd> <dt>

*Channel* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

One [D3DX\_CHANNEL](d3dx-channel.md) flag specifying the source of height information.

</dd> <dt>

*Amplitude* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Constant value multiplier that increases (or decreases) the values in the normal map. Higher values usually make bumps more visible, lower values usually make bumps less visible.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




