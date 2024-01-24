---
title: Hardware Tiers
description: The levels of hardware from Tier 1 to Tier 3 have increasing resources available to the pipeline.
ms.assetid: 5A640BA9-3914-4481-9A0C-E18B52BD8AFE
ms.topic: article
ms.date: 05/31/2018
---

# Hardware Tiers

The levels of hardware from Tier 1 to Tier 3 have increasing resources available to the pipeline.

-   [Limits dependant on hardware](#limits-dependant-on-hardware)
-   [Invariable limits](#invariable-limits)
-   [Related topics](#related-topics)

## Limits dependant on hardware



| Resources Available to the Pipeline                                                                                                              | Tier 1                                                                   | Tier 2        | Tier 3        |
|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------|---------------|
| Feature levels                                                                                                                                   | 11.0+                                                                    | 11.0+         | 11.1+         |
| Maximum number of descriptors in a Constant Buffer View (CBV), Shader Resource View (SRV), or Unordered Access View(UAV) heap used for rendering | 1,000,000                                                                | 1,000,000     | 1,000,000+    |
| Maximum number of Constant Buffer Views in all descriptor tables per shader stage                                                                | 14                                                                       | 14            | **full heap** |
| Maximum number of Shader Resource Views in all descriptor tables per shader stage                                                                | 128                                                                      | **full heap** | full heap     |
| Maximum number of Unordered Access Views in all descriptor tables across all stages                                                              | 64 for feature levels 11.1+<br/> 8 for feature level 11<br/> | 64            | **full heap** |
| Maximum number of Samplers in all descriptor tables per shader stage                                                                             | 16                                                                       | **2048** | 2048     |



 

**Bold** entries highlight significant improvements over the previous tier.

There is an additional restriction for Tier 1 hardware that applies to all heaps, and to Tier 2 hardware that applies to CBV and UAV heaps, that all descriptor heap entries covered by descriptor tables in the root signature *must* be populated with descriptors by the time the shader executes, even if the shader (perhaps due to branching) does not need the descriptor. There is no such restriction for Tier 3 hardware. One mitigation for this restriction is the diligent use of [Null descriptors](descriptors.md).

## Invariable limits

The maximum number of samplers in a shader visible descriptor heap is 2048.

The maximum number of unique static samplers across live root signatures is 2032 (which leaves 16 for drivers that need their own samplers).

## Related topics

<dl> <dt>

[Descriptor Heaps](descriptor-heaps.md)
</dt> <dt>

[Hardware Feature Levels](hardware-feature-levels.md)
</dt> </dl>

 

 





