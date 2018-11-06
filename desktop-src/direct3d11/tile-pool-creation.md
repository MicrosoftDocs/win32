---
title: Tile pool creation
description: A tile pool is created via the ID3D11Device CreateBuffer API by passing the D3D11\_RESOURCE\_MISC\_TILE\_POOL flag in the MiscFlags member of the D3D11\_BUFFER\_DESC structure that the pDesc parameter points to.
ms.assetid: 751A64A6-C9B6-4797-BA1C-B3BEF655DF32
ms.topic: article
ms.date: 05/31/2018
---

# Tile pool creation

A tile pool is created via the [**ID3D11Device::CreateBuffer**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createbuffer) API by passing the [**D3D11\_RESOURCE\_MISC\_TILE\_POOL**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag) flag in the **MiscFlags** member of the [**D3D11\_BUFFER\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_buffer_desc) structure that the *pDesc* parameter points to.

Applications can create one or more tile pools per Direct3D device. The total size of each tile pool is restricted to Direct3D 11's resource size limit, which is roughly 1/4 of graphics processing unit (GPU) RAM.

A tile pool is made of 64KB tiles, but the operating system (display driver) manages the entire pool as one or more allocations behind the scenes—the breakdown is not visible to applications. Tiled resources define content by pointing at tiles within a tile pool. Unmapping a tile from a tiled resource is done by pointing the tile to **NULL**. Such unmapped tiles have rules about the behavior of reads or writes. For info, see [Hazard tracking versus tile pool resources](hazard-tracking-versus-tile-pool-resources.md).

## Related topics

<dl> <dt>

[Mappings are into a tile pool](mappings-are-into-a-tile-pool.md)
</dt> </dl>

 

 




