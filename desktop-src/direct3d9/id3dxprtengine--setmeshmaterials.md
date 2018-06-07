---
Description: Sets mesh material properties in the 3D scene. Use this method to specify subsurface scattering parameters.
ms.assetid: 830d73be-bba6-454d-8476-341d291a5b2e
title: ID3DXPRTEngine::SetMeshMaterials method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXPRTEngine::SetMeshMaterials method

Sets mesh material properties in the 3D scene. Use this method to specify subsurface scattering parameters.

## Syntax


```C++
HRESULT SetMeshMaterials(
  [in] const D3DXSHMATERIAL **ppMaterials,
  [in]       UINT           NumMeshes,
  [in]       UINT           NumChannels,
  [in]       BOOL           bSetAlbedo,
  [in]       FLOAT          fLengthScale
);
```



## Parameters

<dl> <dt>

*ppMaterials* \[in\]
</dt> <dd>

Type: **const [**D3DXSHMATERIAL**](d3dxshmaterial.md)\*\***

Address of a pointer to desired mesh material properties. See [**D3DXSHMATERIAL**](d3dxshmaterial.md).

</dd> <dt>

*NumMeshes* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Index of the mesh on which to set material properties.

</dd> <dt>

*NumChannels* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of color channels to set in the mesh. Set to 1 to specify gray materials (R = G = B), or 3 to enable color bleeding effects. If you intend to change this parameter, first set the albedo using another method such as [**ID3DXPRTEngine::SetPerTexelAlbedo**](id3dxprtengine--setpertexelalbedo.md) or [**ID3DXPRTEngine::SetPerVertexAlbedo**](id3dxprtengine--setpervertexalbedo.md).

</dd> <dt>

*bSetAlbedo* \[in\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

If **TRUE**, sets the albedo of the mesh to ppMaterials, overwriting all existing texel and vertex albedo values. If **FALSE**, preserves all existing texel and vertex albedo values set by other methods; NumChannels must match the NumChannels parameter used to create the buffer in [**D3DXCreatePRTBuffer**](d3dxcreateprtbuffer.md) or [**D3DXCreatePRTBufferTex**](d3dxcreateprtbuffertex.md).

</dd> <dt>

*fLengthScale* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Scale of the 3D scene relative to a 1-mm cube. Used for subsurface scattering computations.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 




