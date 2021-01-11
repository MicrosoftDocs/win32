---
description: Resource management is the process where resources are promoted from system-memory storage to device-accessible storage and discarded from device-accessible storage.
ms.assetid: 4aa55313-b86c-48e7-829a-a0917c2ebae7
title: Managing Resources (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Managing Resources (Direct3D 9)

Resource management is the process where resources are promoted from system-memory storage to device-accessible storage and discarded from device-accessible storage. The Direct3D run time has its own management algorithm based on a least-recently-used priority technique. Direct3D switches to a most-recently-used priority technique when it detects that more resources than can coexist in device-accessible memory are used in a single frame - between [**IDirect3DDevice9::BeginScene**](/windows/desktop/api) and [**IDirect3DDevice9::EndScene**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-endscene) calls.

Use the [**D3DPOOL\_DEFAULT**](./d3dpool.md) flag at creation time to specify that a resource are placed in the memory pool most appropriate for the set of usages requested for the given resource. This is usually video memory, including both local video memory and accelerated graphics port (AGP) memory. Resources in the default pool do not persist through transitions between the lost and operational states of the device. These resources must be released before calling reset and must then be re-created.

Use the [**D3DPOOL\_MANAGED**](./d3dpool.md) flag at creation time to specify a managed resource. Managed resources persist through transitions between the lost and operational states of the device. These resources exist both in video and system memory. A managed resource will be copied into video memory when it is needed during rendering. The device can be restored with a call to [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset), and such resources continue to function normally without being reloaded with data. However, if the device must be destroyed and re-created, all resources must be re-created.

Resource management is not recommended for resources which change with high frequency. For example, vertex and index buffers which are used to traverse a scene graph every frame rendering only geometry visible to the user changes every frame. Since managed resources are backed by system memory, the constant changes must be updated in system memory, which can cause a severe degradation in performance. For this particular scenario, [**D3DPOOL\_DEFAULT**](./d3dpool.md) along with [**D3DUSAGE\_DYNAMIC**](d3dusage.md) should be used.

Another example for which resource management is not recommended (and explicitly not allowed by the runtime) is management of a texture created with [**D3DUSAGE\_RENDERTARGET**](d3dusage.md). If the memory used by render targets were managed by the runtime, it's contents would have to constantly be copied to system memory during rendering, causing large performance penalties. For this reason, render targets must be created in the default pool. If CPU access of the data contained in a render target is needed, the data must be copied to a resource created in [**D3DPOOL\_SYSTEMMEM**](./d3dpool.md) using [**IDirect3DDevice9::UpdateTexture**](/windows/desktop/api), or [**IDirect3DDevice9::UpdateSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-updatesurface)

For more information about the lost state of a device, see [Lost Devices (Direct3D 9)](lost-devices.md).

## Related topics

<dl> <dt>

[Direct3D Resources](direct3d-resources.md)
</dt> </dl>

 

 
