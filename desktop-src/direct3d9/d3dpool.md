---
description: Defines the memory class that holds the buffers for a resource.
ms.assetid: 29720b5f-16d7-4bd9-a7bd-e4dbfb00070b
title: D3DPOOL enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DPOOL
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DPOOL enumeration

Defines the memory class that holds the buffers for a resource.

## Syntax


```C++
typedef enum D3DPOOL { 
  D3DPOOL_DEFAULT      = 0,
  D3DPOOL_MANAGED      = 1,
  D3DPOOL_SYSTEMMEM    = 2,
  D3DPOOL_SCRATCH      = 3,
  D3DPOOL_FORCE_DWORD  = 0x7fffffff
} D3DPOOL, *LPD3DPOOL;
```



## Constants

<dl> <dt>

<span id="D3DPOOL_DEFAULT"></span><span id="d3dpool_default"></span>**D3DPOOL\_DEFAULT**
</dt> <dd>

Resources are placed in the memory pool most appropriate for the set of usages requested for the given resource. This is usually video memory, including both local video memory and AGP memory. The D3DPOOL\_DEFAULT pool is separate from D3DPOOL\_MANAGED and D3DPOOL\_SYSTEMMEM, and it specifies that the resource is placed in the preferred memory for device access. Note that D3DPOOL\_DEFAULT never indicates that either D3DPOOL\_MANAGED or D3DPOOL\_SYSTEMMEM should be chosen as the memory pool type for this resource. Textures placed in the D3DPOOL\_DEFAULT pool cannot be locked unless they are dynamic textures or they are private, FOURCC, driver formats. To access unlockable textures, you must use functions such as [**IDirect3DDevice9::UpdateSurface**](/windows/desktop/api), [**IDirect3DDevice9::UpdateTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-updatetexture), [**IDirect3DDevice9::GetFrontBufferData**](/windows/desktop/api), and [**IDirect3DDevice9::GetRenderTargetData**](/windows/desktop/api). D3DPOOL\_MANAGED is probably a better choice than D3DPOOL\_DEFAULT for most applications. Note that some textures created in driver-proprietary pixel formats, unknown to the Direct3D runtime, can be locked. Also note that - unlike textures - swap chain back buffers, render targets, vertex buffers, and index buffers can be locked. When a device is lost, resources created using D3DPOOL\_DEFAULT must be released before calling [**IDirect3DDevice9::Reset**](/windows/desktop/api). For more information, see [Lost Devices (Direct3D 9)](lost-devices.md).

When creating resources with D3DPOOL\_DEFAULT, if video card memory is already committed, managed resources will be evicted to free enough memory to satisfy the request.

</dd> <dt>

<span id="D3DPOOL_MANAGED"></span><span id="d3dpool_managed"></span>**D3DPOOL\_MANAGED**
</dt> <dd>

Resources are copied automatically to device-accessible memory as needed. Managed resources are backed by system memory and do not need to be recreated when a device is lost. See [Managing Resources (Direct3D 9)](managing-resources.md) for more information. Managed resources can be locked. Only the system-memory copy is directly modified. Direct3D copies your changes to driver-accessible memory as needed.



|                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Differences between Direct3D 9 and Direct3D 9Ex:<br/> D3DPOOL\_MANAGED is valid with [**IDirect3DDevice9**](/windows/desktop/api); however, it is not valid with [**IDirect3DDevice9Ex**](/windows/desktop/api/d3d9/nn-d3d9-idirect3ddevice9ex).<br/> |



 

</dd> <dt>

<span id="D3DPOOL_SYSTEMMEM"></span><span id="d3dpool_systemmem"></span>**D3DPOOL\_SYSTEMMEM**
</dt> <dd>

Resources are placed in memory that is not typically accessible by the Direct3D device. This memory allocation consumes system RAM but does not reduce pageable RAM. These resources do not need to be recreated when a device is lost. Resources in this pool can be locked and can be used as the source for a [**IDirect3DDevice9::UpdateSurface**](/windows/desktop/api) or [**IDirect3DDevice9::UpdateTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-updatetexture) operation to a memory resource created with D3DPOOL\_DEFAULT.

</dd> <dt>

<span id="D3DPOOL_SCRATCH"></span><span id="d3dpool_scratch"></span>**D3DPOOL\_SCRATCH**
</dt> <dd>

Resources are placed in system RAM and do not need to be recreated when a device is lost. These resources are not bound by device size or format restrictions. Because of this, these resources cannot be accessed by the Direct3D device nor set as textures or render targets. However, these resources can always be created, locked, and copied.

</dd> <dt>

<span id="D3DPOOL_FORCE_DWORD"></span><span id="d3dpool_force_dword"></span>**D3DPOOL\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

All pool types are valid with all resources including: vertex buffers, index buffers, textures, and surfaces.

The following tables indicate restrictions on pool types for render targets, depth stencils, and dynamic and mipmap usages. An x indicates a compatible combination; lack of an x indicates incompatibility.



| Pool               | D3DUSAGE\_RENDERTARGET | D3DUSAGE\_DEPTHSTENCIL |
|--------------------|------------------------|------------------------|
| D3DPOOL\_DEFAULT   | x                      | x                      |
| D3DPOOL\_MANAGED   |                        |                        |
| D3DPOOL\_SCRATCH   |                        |                        |
| D3DPOOL\_SYSTEMMEM |                        |                        |



 



| Pool               | D3DUSAGE\_DYNAMIC | D3DUSAGE\_AUTOGENMIPMAP |
|--------------------|-------------------|-------------------------|
| D3DPOOL\_DEFAULT   | x                 | x                       |
| D3DPOOL\_MANAGED   |                   | x                       |
| D3DPOOL\_SCRATCH   |                   |                         |
| D3DPOOL\_SYSTEMMEM | x                 |                         |



 

For more information about usage types, see [**D3DUSAGE**](d3dusage.md).

Pools cannot be mixed for different objects contained within one resource (mip levels in a mipmap) and, when a pool is chosen, it cannot be changed.

Applications should use D3DPOOL\_MANAGED for most static resources because this saves the application from having to deal with lost devices. (Managed resources are restored by the runtime.) This is especially beneficial for unified memory architecture (UMA) systems. Other dynamic resources are not a good match for D3DPOOL\_MANAGED. In fact, index buffers and vertex buffers cannot be created using D3DPOOL\_MANAGED together with D3DUSAGE\_DYNAMIC.

For dynamic textures, it is sometimes desirable to use a pair of video memory and system memory textures, allocating the video memory using D3DPOOL\_DEFAULT and the system memory using D3DPOOL\_SYSTEMMEM. You can lock and modify the bits of the system memory texture using a locking method. Then you can update the video memory texture using [**IDirect3DDevice9::UpdateTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-updatetexture).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**D3DUSAGE**](d3dusage.md)
</dt> <dt>

[**IDirect3DDevice9::CreateCubeTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createcubetexture)
</dt> <dt>

[**IDirect3DDevice9::CreateIndexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createindexbuffer)
</dt> <dt>

[**IDirect3DDevice9::CreateTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createtexture)
</dt> <dt>

[**IDirect3DDevice9::CreateVolumeTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createvolumetexture)
</dt> <dt>

[**IDirect3DDevice9::CreateVertexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createvertexbuffer)
</dt> <dt>

[**D3DINDEXBUFFER\_DESC**](d3dindexbuffer-desc.md)
</dt> <dt>

[**D3DSURFACE\_DESC**](d3dsurface-desc.md)
</dt> <dt>

[**D3DVERTEXBUFFER\_DESC**](d3dvertexbuffer-desc.md)
</dt> <dt>

[**D3DVOLUME\_DESC**](d3dvolume-desc.md)
</dt> </dl>

 

 
