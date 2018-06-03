---
Description: Loads the first frame hierarchy from a .x file.
ms.assetid: 428e5cfb-d6a5-4a7f-b082-2d8898e65490
title: D3DXLoadMeshHierarchyFromXInMemory function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXLoadMeshHierarchyFromXInMemory function

Loads the first frame hierarchy from a .x file.

## Syntax


```C++
HRESULT D3DXLoadMeshHierarchyFromXInMemory(
  _In_  LPCVOID                   pMemory,
  _In_  DWORD                     SizeOfMemory,
  _In_  DWORD                     MeshOptions,
  _In_  LPDIRECT3DDEVICE9         pDevice,
  _In_  LPD3DXALLOCATEHIERARCHY   pAlloc,
  _In_  LPD3DXLOADUSERDATA        pUserDataLoader,
  _Out_ LPD3DXFRAME               *ppFrameHeirarchy,
  _Out_ LPD3DXANIMATIONCONTROLLER *ppAnimController
);
```



## Parameters

<dl> <dt>

*pMemory* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Pointer to a buffer that contains the mesh hierarchy.

</dd> <dt>

*SizeOfMemory* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Size of the pMemory buffer, in bytes.

</dd> <dt>

*MeshOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Combination of one or more flags from the [**D3DXMESH**](https://msdn.microsoft.com/windows/desktop/c94e19ab-8024-4a28-9d1a-6d57707c3a52) enumeration that specify creation options for the mesh.

</dd> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3ddevice9) interface, the device object associated with the mesh.

</dd> <dt>

*pAlloc* \[in\]
</dt> <dd>

Type: **[**LPD3DXALLOCATEHIERARCHY**](id3dxallocatehierarchy.md)**

Pointer to an [**ID3DXAllocateHierarchy**](id3dxallocatehierarchy.md) interface.

</dd> <dt>

*pUserDataLoader* \[in\]
</dt> <dd>

Type: **[**LPD3DXLOADUSERDATA**](id3dxloaduserdata.md)**

Application provided interface that allows loading of user data. See [**ID3DXLoadUserData**](id3dxloaduserdata.md).

</dd> <dt>

*ppFrameHeirarchy* \[out\]
</dt> <dd>

Type: **[**LPD3DXFRAME**](d3dxframe.md)\***

Returns a pointer to the loaded frame hierarchy. See [**D3DXFRAME**](d3dxframe.md).

</dd> <dt>

*ppAnimController* \[out\]
</dt> <dd>

Type: **[**LPD3DXANIMATIONCONTROLLER**](id3dxanimationcontroller.md)\***

Returns a pointer to the animation controller corresponding to animation in the .x file. This is created with default tracks and events. See [**ID3DXAnimationController**](id3dxanimationcontroller.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

All the meshes in the file will be collapsed into one output mesh. If the file contains a frame hierarchy, all the transformations will be applied to the mesh.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Animation Functions](dx9-graphics-reference-d3dx-functions-animation.md)
</dt> </dl>

 

 




