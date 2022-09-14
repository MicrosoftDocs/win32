---
title: Hazard tracking versus tile pool resources
description: For non-tiled resources, Direct3D can prevent certain hazard conditions during rendering, but because hazard tracking would be at a tile level for tiled resources, tracking hazard conditions during rendering of tiled resources might be too expensive.
ms.assetid: 4106BAB9-3E0C-48F1-B7E2-565A65DBC78F
ms.topic: article
ms.date: 05/31/2018
---

# Hazard tracking versus tile pool resources

For non-tiled resources, Direct3D can prevent certain hazard conditions during rendering, but because hazard tracking would be at a tile level for tiled resources, tracking hazard conditions during rendering of tiled resources might be too expensive.

For example, for non-tiled resources, the runtime doesn't allow any given SubResource to be bound as an input (such as a ShaderResourceView) and as an output (such as a RenderTargetView) at the same time. If such a case is encountered, the runtime unbinds the input. This tracking overhead in the runtime is cheap and is done at the SubResource level. One of the benefits of this tracking overhead is to minimize the chances of applications accidentally depending on hardware shader execution order. Hardware shader execution order can vary if not on a given graphics processing unit (GPU), then certainly across different GPUs.

Tracking how resources are bound might be too expensive for tiled resources because tracking is at a tile level. New issues arise such as possibly validating away attempts to render to an RenderTargetView with one tile mapped to multiple areas in the surface simultaneously. If it turns out this per-tile hazard tracking is too expensive for the runtime, ideally this would at least be an option in the debug layer.

An application must inform the display driver when it has issued a write or read operation to a tiled resource that references tile pool memory that will also be referenced by separate tiled resources in upcoming read or write operations that it is expecting the first operation to complete before the following operations can begin. For more info about this condition, see [**ID3D11DeviceContext2::TiledResourceBarrier**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-tiledresourcebarrier) remarks.

## Related topics

<dl> <dt>

[Mappings are into a tile pool](mappings-are-into-a-tile-pool.md)
</dt> </dl>

 

 




