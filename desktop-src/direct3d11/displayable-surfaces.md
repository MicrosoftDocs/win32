---
title: Displayable surfaces
description: The displayable surfaces feature means that buffers that are presented may have varying properties, and you may present them in any order.
ms.topic: article
ms.date: 07/05/2022
---

# Displayable surfaces

Before displayable surfaces, presentation was generally done by creating a swap chain of buffers with identical properties, which were then cycled (flipped) through repeatedly, in order, to be presented to the screen. If you wanted to change the properties of a buffer to be presented, then you had to destroy that swap chain, and create a new one with all the buffers updated to the same new properties.

The displayable surfaces feature adds new operating system (OS) behavior that eliminates those restrictions (but it requires driver support in order to behave properly). Specifically, the feature means that buffers that are presented may have varying properties, and you may present them in any order.

The displayable surfaces (and flexible presentation) features, and their APIs, were introduced in Windows 11 (Build 10.0.22000.194). The functionality is enabled on supported drivers, beginning with WDDM 3.0 drivers, enabling enhanced presentation scenarios for Direct3D 11.

## Check for support, and use displayable surfaces

To determine whether the displayable surfaces feature is available on a system, call [**ID3D11Device::CheckFeatureSupport**](/windows/win32/api/d3d11/nf-d3d11-id3d11device-checkfeaturesupport). Pass [**D3D11_FEATURE::D3D11_FEATURE_DISPLAYABLE**](/windows/win32/api/d3d11/ne-d3d11-d3d11_feature), and receive a [**D3D11_FEATURE_DATA_DISPLAYABLE**](/windows/win32/api/d3d11/ns-d3d11-d3d11_feature_data_displayable) structure.

The [**ID3D11Device::CreateTexture2D**](/windows/win32/api/d3d11/nf-d3d11-id3d11device-createtexture2d) API supports [**D3D11_RESOURCE_MISC_FLAG::D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE**](/windows/win32/api/d3d11/ne-d3d11-d3d11_resource_misc_flag), which you can use in the [D3D11_TEXTURE2D_DESC::MiscFlags](/windows/win32/api/d3d11/ns-d3d11-d3d11_texture2d_desc) member of the structure that you pass to **CreateTexture2D** in the *pDesc* parameter.

Textures with **D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE** are restricted to an array size of 1, and to 1 mip level.

When you use the [**D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE**](/windows/win32/api/d3d11/ne-d3d11-d3d11_resource_misc_flag) flag on the texture, you can show the texture on any active output (including multiple outputs simultaneously). Depending on the scenario, the texture might end up being consumed by the compositor (DWM), scanned out, or bound to various parts of the pipeline&mdash;potentially all simultaneously. For example, a capture texture from a camera might be shown on two displays, and a thumbnail of it shown on a third display, all at the same time&mdash;and all from the same allocation with no additional copies. In the case where a displayable surface is to be scanned out on multiple displays, the OS will coordinate the collection of flip completes from the involved outputs before alerting your application that the surface is released back to it&mdash;no coordination of flip completion is required from the driver.

Such textures as described above must be displayable for flexible presentation use. These textures are not required to have the same properties&mdash;for example, formats and sizes can differ, and these textures must be able to be displayed in arbitrary order ("out-of-order presentation"). Presentation will occur using the existing **Present1** DDI, with its existing calling patterns. For example, consider a pool of six buffers, three that are 720p (A, B, and C) and three that are 4K (D, E, and F): a valid presentation order could be A-\>E-\>C-\>B-\>F-\>E-\>D-\>C.

## Formats

The [**D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE**](/windows/win32/api/d3d11/ne-d3d11-d3d11_resource_misc_flag) flag  is supported for the following formats in Direct3D 11:

- [**DXGI_FORMAT::DXGI_FORMAT_B8G8R8A8_UNORM**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)
- **DXGI_FORMAT_R8G8B8A8_UNORM**
- **DXGI_FORMAT_R16G16B16A16_FLOAT**
- **DXGI_FORMAT_R10G10B10A2_UNORM**
- **DXGI_FORMAT_NV12**
- **DXGI_FORMAT_YUY2**

## Flags

Shareable formats already generally support the following bind flags: [**D3D11_BIND_FLAG::D3D11_BIND_SHADER_RESOURCE**](/windows/win32/api/d3d11/ne-d3d11-d3d11_bind_flag), **D3D11_BIND_UNORDERED_ACCESS**, **D3D11_BIND_RENDER_TARGET**, and **D3D11_BIND_DECODER**.

Existing supported usages of shared resources with the **D3D11_BIND_VIDEO_ENCODER** flag are extended to also support the **D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE** flag being added in these cases. Existing restrictions related to use of shared resources with **D3D11_BIND_VIDEO_ENCODER** are maintained.

**D3D11_BIND_VIDEO_ENCODER** and **D3D11_BIND_SHADER_RESOURCE** were previously mutually exclusive, except when combined with certain other bind flags. The exception has been extended to allow **D3D11_BIND_VIDEO_ENCODER** and **D3D11_BIND_SHADER_RESOURCE** to be used together when **D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE** is used.

The **D3D11_RESOURCE_MISC_HW_PROTECTED** flag is supported with the **D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE** flag.
