---
description: D3DXLoadMeshHierarchyFromX function - Loads the first frame hierarchy from a .x file.
ms.assetid: 1d446b23-9028-4187-b97c-a61edfe68e39
title: D3DXLoadMeshHierarchyFromX function (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXLoadMeshHierarchyFromX
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXLoadMeshHierarchyFromX function

Loads the first frame hierarchy from a .x file.

## Syntax


```C++
HRESULT D3DXLoadMeshHierarchyFromX(
  _In_  LPCTSTR                   Filename,
  _In_  DWORD                     MeshOptions,
  _In_  LPDIRECT3DDEVICE9         pDevice,
  _In_  LPD3DXALLOCATEHIERARCHY   pAlloc,
  _In_  LPD3DXLOADUSERDATA        pUserDataLoader,
  _Out_ LPD3DXFRAME               *ppFrameHierarchy,
  _Out_ LPD3DXANIMATIONCONTROLLER *ppAnimController
);
```



## Parameters

<dl> <dt>

*Filename* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Pointer to a string that specifies the filename. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*MeshOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of one or more flags from the [**D3DXMESH**](./d3dxmesh.md) enumeration that specify creation options for the mesh.

</dd> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) interface, the device object associated with the mesh.

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

*ppFrameHierarchy* \[out\]
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

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXLoadMeshHierarchyFromXW. Otherwise, the function call resolves to D3DXLoadMeshHierarchyFromXA.

All the meshes in the file will be collapsed into one output mesh. If the file contains a frame hierarchy, all the transformations will be applied to the mesh.

**D3DXLoadMeshHierarchyFromX** loads the animation data and frame hierarchy from a .x file. It scans the .x file and builds a frame hierarchy and animation controller according to the [**ID3DXAllocateHierarchy**](id3dxallocatehierarchy.md)-derived object passed to it through pAlloc. Loading the data requires several steps as follows:

1.  Derive [**ID3DXAllocateHierarchy**](id3dxallocatehierarchy.md), implementing each method. This controls how frames and meshes are allocated and freed.
2.  Derive [**ID3DXLoadUserData**](id3dxloaduserdata.md), implementing each method. If your .x file has no embedded user-defined data, or if you do not need it, you can skip this part.
3.  Create an object of your [**ID3DXAllocateHierarchy**](id3dxallocatehierarchy.md) class, and optionally of your LoadUserData class. You do not need to call any methods of these objects yourself.
4.  Call **D3DXLoadMeshHierarchyFromX**, passing in your [**ID3DXAllocateHierarchy**](id3dxallocatehierarchy.md) object and your [**ID3DXLoadUserData**](id3dxloaduserdata.md) object (or **NULL**) to create the frame hierarchy and animation controller. All the animation sets and frames are automatically registered to the animation controller.

During the load, [**CreateFrame**](id3dxallocatehierarchy--createframe.md) and [**LoadFrameChildData**](id3dxloaduserdata--loadframechilddata.md) are called back on each frame to control loading and allocation of the frame. The application defines these methods to control how frames are stored. [**CreateMeshContainer**](id3dxallocatehierarchy--createmeshcontainer.md) and [**LoadMeshChildData**](id3dxloaduserdata--loadmeshchilddata.md) are called back on each mesh object to control loading and allocation of mesh objects. [**LoadTopLevelData**](id3dxloaduserdata--loadtopleveldata.md) is called back for each top level object that doesn't get loaded by the other methods.

To free this data, call ID3DXAnimationController::Release to free the animation sets, and [**D3DXFRAMEDestroy**](d3dxframedestroy.md), passing in the root node of the frame hierarchy and an object of your derived [**ID3DXAllocateHierarchy**](id3dxallocatehierarchy.md) class. [**DestroyFrame**](id3dxallocatehierarchy--destroyframe.md) and [**DestroyMeshContainer**](id3dxallocatehierarchy--destroymeshcontainer.md) will each be called for every frame and mesh object in the frame hierarchy. Your implementation of **DestroyFrame** should release everything allocated by [**CreateFrame**](id3dxallocatehierarchy--createframe.md), and likewise for the mesh container methods.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Animation Functions](dx9-graphics-reference-d3dx-functions-animation.md)
</dt> </dl>

 

 
