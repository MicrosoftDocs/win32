---
title: Rasterizer behavior with non-mapped tiles
description: This section describes rasterizer behavior with non-mapped tiles.
ms.assetid: 3477A621-7051-4585-AB58-523EE64CDC5C
ms.topic: article
ms.date: 05/31/2018
---

# Rasterizer behavior with non-mapped tiles

This section describes rasterizer behavior with non-mapped tiles.

## DepthStencilView

Behavior of depth stencil view (DSV) reads and writes depends on the level of hardware support. For a breakdown of requirements, see overall read and write behavior for [Tiled resources features tiers](tiled-resources-features-tiers.md).

Here is the ideal behavior:

If a tile isn't mapped in the DepthStencilView, the return value from reading depth is 0, which is then fed into whatever operations are configured for the depth read value. Writes to the missing depth tile are dropped. This ideal definition for write handling is not required by [Tier 2](tier-2.md); writes to non-mapped tiles can end up in a cache that subsequent reads could pick up.

## RenderTargetView

Behavior of render target view (RTV) reads and writes depends on the level of hardware support. For a breakdown of requirements, see overall read and write behavior for [Tiled resources features tiers](tiled-resources-features-tiers.md).

On all implementations, different RTVs (and DSV) bound simultaneously can have different areas mapped versus non-mapped and can have different sized surface formats (which means different tile shapes).

Here is the ideal behavior:

Reads from RTVs return 0 in missing tiles and writes are dropped. This ideal definition for write handling is not required by [Tier 2](tier-2.md); writes to non-mapped tiles can end up in a cache that subsequent reads could pick up.

## Related topics

<dl> <dt>

[Pipeline access to tiled resources](pipeline-access-to-tiled-resources.md)
</dt> </dl>

 

 




