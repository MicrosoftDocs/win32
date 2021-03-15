---
description: Converts a height map into a normal map. The (x,y,z) components of each normal are mapped to the (r,g,b) channels of the output texture.
ms.assetid: 535033dd-f078-4d56-8e5d-cdda80ef5992
title: D3DX10ComputeNormalMap function (D3DX10Tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10ComputeNormalMap
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DX10ComputeNormalMap function

Converts a height map into a normal map. The (x,y,z) components of each normal are mapped to the (r,g,b) channels of the output texture.

## Syntax


```C++
HRESULT D3DX10ComputeNormalMap(
  _In_ ID3D10Texture2D *pSrcTexture,
  _In_ UINT            Flags,
  _In_ UINT            Channel,
  _In_ FLOAT           Amplitude,
  _In_ ID3D10Texture2D *pDestTexture
);
```



## Parameters

<dl> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**ID3D10Texture2D**](/windows/desktop/api/D3D10/nn-d3d10-id3d10texture2d)\***

Pointer to an ID3D10Texture2D interface, representing the source height-map texture.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

One or more D3DX\_NORMALMAP flags that control generation of normal maps.

</dd> <dt>

*Channel* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

One D3DX\_CHANNEL flag specifying the source of height information.

</dd> <dt>

*Amplitude* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Constant value multiplier that increases (or decreases) the values in the normal map. Higher values usually make bumps more visible, lower values usually make bumps less visible.

</dd> <dt>

*pDestTexture* \[in\]
</dt> <dd>

Type: **[**ID3D10Texture2D**](/windows/desktop/api/D3D10/nn-d3d10-id3d10texture2d)\***

Pointer to an ID3D10Texture2D interface, representing the destination texture.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following value: D3DERR\_INVALIDCALL.

## Remarks

This method computes the normal by using the central difference with a kernel size of 3x3. RGB channels in the destination contain biased (x,y,z) components of the normal. The central differencing denominator is hardcoded to 2.0.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 10](d3d10-graphics-reference-d3dx10-functions-texturing.md)
</dt> </dl>

 

 
