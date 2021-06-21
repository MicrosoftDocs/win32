---
description: A combination of zero or more locking options that describe the type of lock to perform.
ms.assetid: 46a611bd-a1ec-4967-b68d-72661d1b5cad
title: D3DLOCK
ms.topic: article
ms.date: 05/31/2018
---

# D3DLOCK

A combination of zero or more locking options that describe the type of lock to perform.



| \#define                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DLOCK\_DISCARD           | The application discards all memory within the locked region. For vertex and index buffers, the entire buffer will be discarded. This option is only valid when the resource is created with dynamic usage (see [D3DUSAGE](d3dusage.md)).                                                                                                                                                                                                                                                                                                                                                           |
| D3DLOCK\_DONOTWAIT         | Allows an application to gain back CPU cycles if the driver cannot lock the surface immediately. If this flag is set and the driver cannot lock the surface immediately, the lock call will return D3DERR\_WASSTILLDRAWING. This flag can only be used when locking a surface created using [**CreateOffscreenPlainSurface**](/windows/desktop/api), [**CreateRenderTarget**](/windows/desktop/api), or [**CreateDepthStencilSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createdepthstencilsurface). This flag can also be used with a back buffer.            |
| D3DLOCK\_NO\_DIRTY\_UPDATE | By default, a lock on a resource adds a dirty region to that resource. This option prevents any changes to the dirty state of the resource. Applications should use this option when they have additional information about the set of regions changed during the lock operation.                                                                                                                                                                                                                                                                                                                    |
| D3DLOCK\_NOOVERWRITE       | Indicates that memory that was referred to in a drawing call since the last lock without this flag will not be modified during the lock. This can enable optimizations when the application is appending data to a resource. Specifying this flag enables the driver to return immediately if the resource is in use, otherwise, the driver must finish using the resource before returning from locking.                                                                                                                                                                                            |
| D3DLOCK\_NOSYSLOCK         | The default behavior of a video memory lock is to reserve a system-wide critical section, guaranteeing that no display mode changes will occur for the duration of the lock. This option causes the system-wide critical section not to be held for the duration of the lock.<br/> The lock operation is time consuming, but can enable the system to perform other duties, such as moving the mouse cursor. This option is useful for long-duration locks, such as the lock of the back buffer for software rendering that would otherwise adversely affect system responsiveness.<br/> |
| D3DLOCK\_READONLY          | The application will not write to the buffer. This enables resources stored in non-native formats to save the recompression step when unlocking.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |



 

## Constant Information



|  Requirement                        | Value            |
|--------------------------|-------------|
| Header                   | d3d9types.h |
| Minimum operating system | Windows 98  |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> <dt>

[**LockRect**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dcubetexture9-lockrect)
</dt> <dt>

[**Lock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dindexbuffer9-lock)
</dt> <dt>

[**LockRect**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dcubetexture9-lockrect)
</dt> <dt>

[**LockRect**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dcubetexture9-lockrect)
</dt> <dt>

[**Lock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dindexbuffer9-lock)
</dt> <dt>

[**LockBox**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dvolume9-lockbox)
</dt> <dt>

[**LockBox**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dvolume9-lockbox)
</dt> <dt>

[**LockIndexBuffer**](id3dxbasemesh--lockindexbuffer.md)
</dt> <dt>

[**LockVertexBuffer**](id3dxbasemesh--lockvertexbuffer.md)
</dt> <dt>

**LockVertexBuffer**
</dt> <dt>

[**LockAttributeBuffer**](id3dxmesh--lockattributebuffer.md)
</dt> <dt>

[**LockAttributeBuffer**](id3dxpatchmesh--lockattributebuffer.md)
</dt> <dt>

[**LockIndexBuffer**](id3dxpatchmesh--lockindexbuffer.md)
</dt> <dt>

[**LockVertexBuffer**](id3dxpatchmesh--lockvertexbuffer.md)
</dt> </dl>

 

 
