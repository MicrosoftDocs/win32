---
title: SRV behavior with non-mapped tiles
description: Behavior of shader resource view (SRV) reads that involve non-mapped tiles depends on the level of hardware support.
ms.assetid: 9B720BEE-AB0C-4B75-92AD-3F382A107D48
ms.topic: article
ms.date: 05/31/2018
---

# SRV behavior with non-mapped tiles

Behavior of shader resource view (SRV) reads that involve non-mapped tiles depends on the level of hardware support. For a breakdown of requirements, see read behavior for [Tiled resources features tiers](tiled-resources-features-tiers.md). This section summarizes the ideal behavior, which [Tier 2](tier-2.md) requires.

Consider a texture filter operation that reads from a set of texels in an SRV. Texels that fall on non-mapped tiles contribute 0 in all non-missing components of the format (and the default for missing components) into the overall filter operation alongside contributions from mapped texels. The texels are all weighted and combined together independent of whether the data came from mapped or non-mapped tiles.

Some first generation [Tier 2](tier-2.md) level hardware does not meet this spec requirement and returns the 0 with defaults described preceding as the overall filter result if any texels (with nonzero weight) fall on non-mapped tiles. No other hardware will be allowed to miss the requirement to include all (nonzero weight) texels in the filter.

## Related topics

<dl> <dt>

[Pipeline access to tiled resources](pipeline-access-to-tiled-resources.md)
</dt> </dl>

 

 




