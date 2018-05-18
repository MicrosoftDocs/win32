---
title: Tiled resources features tiers
description: Direct3D 11.2 exposes tiled resources support in two tiers with the D3D11\_TILED\_RESOURCES\_TIER values.
ms.assetid: 'E6A6565B-079B-47DB-A80C-CA5B5413BA32'
---

# Tiled resources features tiers

Direct3D 11.2 exposes tiled resources support in two tiers with the [**D3D11\_TILED\_RESOURCES\_TIER**](d3d11-tiled-resources-tier.md) values.

To query whether the hardware and driver support tiled resources and at what tier level, pass the [**D3D11\_FEATURE\_D3D11\_OPTIONS1**](d3d11-feature.md#d3d11-feature-d3d11-options1) value to the *Feature* parameter of [**ID3D11Device::CheckFeatureSupport**](id3d11device-checkfeaturesupport.md). Also, pass a pointer to the [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS1**](d3d11-feature-data-d3d11-options1.md) structure to the *pFeatureSupportData* parameter, and pass the size of the **D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS1** structure to the *FeatureSupportDataSize* parameter. **CheckFeatureSupport** returns the tier level as a [**D3D11\_TILED\_RESOURCES\_TIER**](d3d11-tiled-resources-tier.md) value in the **TiledResourcesTier** member of **D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS1**.

This section describes these two tiers.

## In this section



| Topic                           | Description                                       |
|---------------------------------|---------------------------------------------------|
| [Tier 1](tier-1.md)<br/> | This section describes tier 1 support.<br/> |
| [Tier 2](tier-2.md)<br/> | This section describes tier 2 support.<br/> |



 

## Related topics

<dl> <dt>

[Tiled resources](tiled-resources.md)
</dt> </dl>

 

 





