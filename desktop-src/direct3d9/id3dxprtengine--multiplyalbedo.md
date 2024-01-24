---
description: Multiplies each precomputed radiance transfer (PRT) vector by the per-vertex albedo.
ms.assetid: 2b3e4b19-7778-4240-ac79-3237fda2ed96
title: ID3DXPRTEngine::MultiplyAlbedo method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.MultiplyAlbedo
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::MultiplyAlbedo method

Multiplies each precomputed radiance transfer (PRT) vector by the per-vertex albedo.

## Syntax


```C++
HRESULT MultiplyAlbedo(
  [in, out] LPD3DXPRTBUFFER pDataOut
);
```



## Parameters

<dl> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an output [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that will contain PRT vectors multiplied by the per-vertex albedo. If this output buffer is a texture object, then care must be taken to store the albedo of the texture at the same resolution as the simulation buffer. You can set the proper resolution on the albedo with [**D3DXLoadSurfaceFromSurface**](d3dxloadsurfacefromsurface.md), applying texture gutter regions if appropriate.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

The ID3DXPRTEngine::Computexxx methods compute output buffers in which the light signal has not been multiplied by albedo. By not multiplying the albedo, you can model albedo variation at a finer scale than the source radiance, thereby yielding more accurate results from compression.

To include albedo in the rendered-light model, call this method after one of the Computexxx methods.

[**ID3DXPRTEngine::SetMeshMaterials**](id3dxprtengine--setmeshmaterials.md) should be called before calling this method.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> <dt>

[**ID3DXPRTEngine::ComputeDirectLightingSH**](id3dxprtengine--computedirectlightingsh.md)
</dt> </dl>

 

 




