---
description: Sets the minimum and maximum distances of intersection between 3D objects.
ms.assetid: da825c70-0c55-4303-b78a-a761ba037182
title: ID3DXPRTEngine::SetMinMaxIntersection method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.SetMinMaxIntersection
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::SetMinMaxIntersection method

Sets the minimum and maximum distances of intersection between 3D objects. These distance values can be used to control the minimum or maximum distance that objects can shadow or reflect light. For example, the method can be used to limit the shadowing of nearby features of a 3D model.

## Syntax


```C++
HRESULT SetMinMaxIntersection(
  [in] FLOAT fMin ,
  [in] FLOAT fMax
);
```



## Parameters

<dl> <dt>

*fMin* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Minimum intersection distance. Must be positive and less than fMax.

</dd> <dt>

*fMax* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Maximum intersection distance. If 0.0f, the previous value will be used; otherwise, must be greater than fMin.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This method cannot be used in precomputed radiance transfer (PRT) simulations that run in the GPU. See [**ID3DXPRTEngine::ComputeDirectLightingSHGPU**](id3dxprtengine--computedirectlightingshgpu.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 
