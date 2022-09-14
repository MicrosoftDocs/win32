---
description: Uses a user-provided function to fill each texel of each mip level of a given volume texture.
ms.assetid: cc9eb051-8a62-4e35-87df-c255f10e94d8
title: D3DXFillVolumeTexture function (D3dx9tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXFillVolumeTexture
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXFillVolumeTexture function

Uses a user-provided function to fill each texel of each mip level of a given volume texture.

## Syntax


```C++
HRESULT D3DXFillVolumeTexture(
  _Out_ LPDIRECT3DVOLUMETEXTURE9 pTexture,
  _In_  LPD3DXFILL3D             pFunction,
  _In_  LPVOID                   pData
);
```



## Parameters

<dl> <dt>

*pTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DVOLUMETEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dvolumetexture9)**

Pointer to an [**IDirect3DVolumeTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dvolumetexture9) interface, representing the filled texture.

</dd> <dt>

*pFunction* \[in\]
</dt> <dd>

Type: **[LPD3DXFILL3D](lpd3dxfill3d.md)**

Pointer to a user-provided evaluator function, which will be used to compute the value of each texel. The function follows the prototype of [LPD3DXFILL3D](lpd3dxfill3d.md).

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

Pointer to an arbitrary block of user-defined data. This pointer will be passed to the function provided in *pFunction*.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL.

## Remarks

If the volume is non-dynamic (because usage is set to 0 when it is created), and located in video memory (the memory pool set to D3DPOOL\_DEFAULT), **D3DXFillVolumeTexture** will fail because the volume cannot be locked.

This example creates a function called ColorVolumeFill, which relies on D3DXFillVolumeTexture.


```
// Define a function that matches the prototype of LPD3DXFILL3D
VOID WINAPI ColorVolumeFill (D3DXVECTOR4* pOut, const D3DXVECTOR3* pTexCoord, 
const D3DXVECTOR3* pTexelSize, LPVOID pData)
{
   *pOut = D3DXVECTOR4(pTexCoord->x, pTexCoord->y, pTexCoord->z, 0.0f);
}
    
    
// Fill volume texture
if (FAILED (hr = D3DXFillVolumeTexture (m_pTexture, ColorVolumeFill, NULL)))
{
       return hr;
}
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 
