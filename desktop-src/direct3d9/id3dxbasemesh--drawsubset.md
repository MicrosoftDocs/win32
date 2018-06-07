---
Description: Draws a subset of a mesh.
ms.assetid: 99eaa185-b681-47f2-aed8-5ca1697ff73c
title: ID3DXBaseMesh::DrawSubset method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXBaseMesh::DrawSubset method

Draws a subset of a mesh.

## Syntax


```C++
HRESULT DrawSubset(
  [in] DWORD AttribId
);
```



## Parameters

<dl> <dt>

*AttribId* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

DWORD that specifies which subset of the mesh to draw. This value is used to differentiate faces in a mesh as belonging to one or more attribute groups.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

The subset that is specified by AttribId will be rendered by the [**IDirect3DDevice9::DrawIndexedPrimitive**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-drawindexedprimitive) method, using the D3DPT\_TRIANGLELIST primitive type, so an index buffer must be properly initialized.

An attribute table is used to identify areas of the mesh that need to be drawn with different textures, render states, materials, and so on. In addition, the application can use the attribute table to hide portions of a mesh by not drawing a given attribute identifier (*AttribId*) when drawing the frame.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 




