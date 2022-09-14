---
title: Tiled resources
description: Tiled resources can be thought of as large logical resources that use small amounts of physical memory.
ms.assetid: '03083460-192b-40cb-8ee1-76df6d95f72b'
ms.topic: article
ms.date: 05/31/2018
---

# Tiled resources

Tiled resources can be thought of as large logical resources that use small amounts of physical memory.

This section describes why tiled resources are needed and how you create and use tiled resources.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Why are tiled resources needed?](why-are-tiled-resources-needed-.md)<br/>       | Tiled resources are needed so less graphics processing unit (GPU) memory is wasted storing regions of surfaces that the application knows will not be accessed, and the hardware can understand how to filter across adjacent tiles.<br/>     |
| [Creating tiled resources](creating-tiled-resources.md)<br/>                     | Tiled resources are created by specifying the [**D3D11\_RESOURCE\_MISC\_TILED**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag) flag when you create a resource.<br/>                                                                                          |
| [Tiled Resource APIs](tiled-resource-apis.md)<br/>                               | The APIs described in this section work with tiled resources and tile pool.<br/>                                                                                                                                                              |
| [Pipeline access to tiled resources](pipeline-access-to-tiled-resources.md)<br/> | Tiled resources can be used in shader resource views (SRV), render target views (RTV), depth stencil views (DSV) and unordered access views (UAV), as well as some bind points where views aren't used, such as vertex buffer bindings. <br/> |
| [Tiled resources features tiers](tiled-resources-features-tiers.md)<br/>         | Direct3D 11.2 exposes tiled resources support in two tiers with the [**D3D11\_TILED\_RESOURCES\_TIER**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_tiled_resources_tier) values. <br/>                                                                                         |



 

## Related topics

<dl> <dt>

[Resources](overviews-direct3d-11-resources.md)
</dt> </dl>

 

 





