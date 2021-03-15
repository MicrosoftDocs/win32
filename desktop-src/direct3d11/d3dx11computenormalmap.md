---
title: D3DX11ComputeNormalMap function (D3DX11tex.h)
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Note Instead of using this function, we recommend that you use the DirectXTex library, ComputeNormalMap.
ms.assetid: 3ccdbd9a-669e-48ff-97d5-e5a6c7d2fb26
keywords:
- D3DX11ComputeNormalMap function Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11ComputeNormalMap
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX11ComputeNormalMap function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

> [!Note]  
> Instead of using this function, we recommend that you use the [DirectXTex](https://github.com/Microsoft/DirectXTex) library, **ComputeNormalMap**.

 

Converts a height map into a normal map. The (x,y,z) components of each normal are mapped to the (r,g,b) channels of the output texture.

## Syntax


```C++
HRESULT D3DX11ComputeNormalMap(
  _In_ ID3D11DeviceContext *pContext,
  _In_ ID3D11Texture2D     *pSrcTexture,
  _In_ UINT                Flags,
  _In_ UINT                Channel,
  _In_ FLOAT               Amplitude,
  _In_ ID3D11Texture2D     *pDestTexture
);
```



## Parameters

<dl> <dt>

*pContext* \[in\]
</dt> <dd>

Type: **[**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext)\***

Pointer to an [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) interface, representing the source height-map texture.

</dd> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**ID3D11Texture2D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture2d)\***

Pointer to an [**ID3D11Texture2D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture2d) interface, representing the source height-map texture.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

One or more D3DX\_NORMALMAP flags that control generation of normal maps.

</dd> <dt>

*Channel* \[in\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

One D3DX\_CHANNEL flag specifying the source of height information.

</dd> <dt>

*Amplitude* \[in\]
</dt> <dd>

Type: **[**FLOAT**](/windows/desktop/WinProg/windows-data-types)**

Constant value multiplier that increases (or decreases) the values in the normal map. Higher values usually make bumps more visible, lower values usually make bumps less visible.

</dd> <dt>

*pDestTexture* \[in\]
</dt> <dd>

Type: **[**ID3D11Texture2D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture2d)\***

Pointer to an [**ID3D11Texture2D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture2d) interface, representing the destination texture.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following value: D3DERR\_INVALIDCALL.

## Remarks

This method computes the normal by using the central difference with a kernel size of 3x3. RGB channels in the destination contain biased (x,y,z) components of the normal. The central differencing denominator is hardcoded to 2.0.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>  |



## See also

<dl> <dt>

[D3DX Functions](d3d11-graphics-reference-d3dx11-functions.md)
</dt> </dl>

 

