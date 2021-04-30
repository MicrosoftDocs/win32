---
description: Managed vertex-buffer or index-buffer resources cannot be declared dynamic by specifying D3DUSAGE\_DYNAMIC at creation time.
ms.assetid: 440d9d94-3a56-4b34-a5e3-1b4712b078fc
title: Application-Managed Resources and Allocation Strategies (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Application-Managed Resources and Allocation Strategies (Direct3D 9)

Managed vertex-buffer or index-buffer resources cannot be declared dynamic by specifying D3DUSAGE\_DYNAMIC at creation time. This would require an additional copy for every modification to the vertex buffer contents. Dynamic vertex buffers are intended for rendering dynamic geometry and data pulled in from binary space partitioned trees or other visibility data structures. This can be accomplished by pre-allocating buffers of the desired format. These resources are then parceled out to support application needs by a resource manager within the application. The total number of dynamic vertex buffers is small because an application will use simultaneously only a few different vertex strides and because a different vertex buffer is required only for unique strides. When managing dynamic resources in this way, ensure that high-frequency demands on the resources do not significantly decrease the application's performance.

When using resources managed by both Direct3D and applications, allocate application-managed resources in D3DPOOL\_DEFAULT memory prior to creating Direct3D-managed resources. This enables the memory manager to maintain an accurate count of available memory.

## Related topics

<dl> <dt>

[Direct3D Resources](direct3d-resources.md)
</dt> </dl>

 

 



