---
title: Using Direct3D 11 feature data to supplement Direct3D feature levels
description: Find out how to check device support for optional features, including features that were added in recent versions of Windows.
ms.assetid: 91D9706A-47C5-4220-8AC7-167095E74F74
ms.topic: article
ms.date: 05/31/2018
---

# Using Direct3D 11 feature data to supplement Direct3D feature levels

Find out how to check device support for optional features, including features that were added in recent versions of Windows.

[Direct3D feature levels](overviews-direct3d-11-devices-downlevel-intro.md) indicate well-defined sets of GPU functionality that roughly correspond to different generations of graphics hardware. This greatly simplifies the task of checking hardware capaibilities, and also provides a consistent experience across a wide array of different devices.

To account for some of the variance across different hardware implementations - including legacy hardware, mobile hardware, and modern hardware - some features are considered optional. Support for these features can be determined by calling [**ID3D11Device::CheckFeatureSupport**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport) and supplying the relevant D3D11\_FEATURE\_DATA\_\* structure. This topic describes the various optional Direct3D 11 features, how some of them work together, and how you can avoid checking for every single optional feature.

## How to check for optional feature support

Call [**ID3D11Device::CheckFeatureSupport**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport), providing the structure that represents the optional feature you'd like to use. If the method returns **S\_OK**, that means you're on a version of the Direct3D runtime that supports the optional feature. If it returns **E\_INVALIDARG**, that means you're on a version of the Direct3D 11 runtime from before the optional feature was added - this means the optional feature is not available, along with any other optional features introduced in the same version of Direct3D 11 or later.

## Can I minimize the work required for feature support checks?

In addition to having the right Direct3D 11 runtime (usually associated with a Windows version) the graphics driver must also be recent enough to support the optional feature. The WDDM specifications require optional features to be supported if the hardware can support it. So when a graphics driver supports one of the optional features that were added in a particular version of Windows, it usually means that the graphics driver supports the other features added in that version of Windows. For example, if a device driver supports shadows on feature level 9, then you know the device driver is at least WDDM 1.2.

**Note**  If a Microsoft Direct3D device supports [feature level](overviews-direct3d-11-devices-downlevel-intro.md) 11.1, all of the optional features indicated by [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options) are automatically supported except **SAD4ShaderInstructions** and **ExtendedDoublesShaderInstructions**.

The runtime always sets the following groupings of members identically. That is, all the values in a grouping are **TRUE** or **FALSE** together:

-   **DiscardAPIsSeenByDriver** and **FlagsForUpdateAndCopySeenByDriver**
-   **ClearView**, **CopyWithOverlap**, **ConstantBufferPartialUpdate**, **ConstantBufferOffsetting**, and **MapNoOverwriteOnDynamicConstantBuffer**
-   **MapNoOverwriteOnDynamicBufferSRV** and **MultisampleRTVWithForcedSampleCountOne**

**Feature level 11.2 options ([**D3D11\_FEATURE\_D3D11\_OPTIONS1**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_feature)):** The optional features indicated by this field are independent and must be checked individually.

### Feature support on Windows RT 8.1 and Windows Phone 8.1 devices

Windows RT tablet devices can support a variety of feature levels and optional features, are optimized for reduced power consumption, and use integrated graphics instead of discrete GPUs. Windows Store apps for ARM devices must support feature level 9.1. DirectX apps for Windows RT should take advantage of optional features that can save power and cycles - such as simple instancing - when they are available.

Windows Phone 8 mobile devices support feature level 9.3 with specific optional features. See [Direct3D feature level 9\_3 for Windows Phone 8](/previous-versions/windows/apps/jj714085(v=vs.105)).

## What are the Direct3D 11 optional features?

The rest of this article describes the optional features available in Direct3D 11.2. Features are described in chronological order by when they were added so you can get a sense for what features are in different versions of Direct3D 11.

## Optional compute shader support for feature level 10

The following feature is always available for feature level 10 devices:

**[**D3D11\_FEATURE\_DATA\_D3D10\_X\_HARDWARE\_OPTIONS**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d10_x_hardware_options):** If this is **TRUE**, the device supports compute shaders. This includes support for raw and structured buffers.

When the feature level 10\_0 or 10\_1 device supports this feature, the device is not guaranteed to support compute shader 4.1. Apps should be prepared to fall back to a compute shader 4.0 if [**ID3D11Device::CreateComputeShader**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createcomputeshader) throws an exception with a compute shader 4.1 program.

## Optional capabilities for feature level 9

The following features are added for feature level 9 starting in Windows 8:

**[**D3D11\_FEATURE\_DATA\_D3D9\_OPTIONS**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d9_options):** Indicates support for wrap texture addressing with non-power-of-2 textures. If this is supported, D3D11\_TEXTURE\_ADDRESS\_MODE\_WRAP can be used with such textures.

**[**D3D11\_FEATURE\_DATA\_D3D9\_SHADOW\_SUPPORT**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d9_shadow_support):** Indicates support for comparison samplers in shader model 4.0 feature level 9\_x shaders. This is used for depth testing in pixel shaders, enabling support for common techniques such as shadow mapping and stencils.

The following feature was added for feature level 9 devices starting in Windows 8.1:

**[**D3D11\_FEATURE\_DATA\_D3D9\_SIMPLE\_INSTANCING\_SUPPORT**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d9_simple_instancing_support):** Indicates support for simple instancing features that might be available on DirectX 9-level hardware. Simple instancing means that all **InstanceDataStepRate** members of the [**D3D11\_INPUT\_ELEMENT\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_input_element_desc) structures used to define the input layout must be equal to 1. Devices that support feature level 9.3 or higher already include full support for instancing.

## Optional floating-point precision support for shader programs

**[**D3D11\_FEATURE\_DATA\_SHADER\_MIN\_PRECISION\_SUPPORT**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_shader_min_precision_support):** The fields in this struct indicate the length of floating-point numbers when minimum precision is enabled, or 0 if only full 32-bit floating point precision is supported.

For feature level 9 devices, the minimum precision for the vertex shader can be different from the pixel shader. The precision for the vertex shader is indicated in the **AllOtherShaderStagesMinPrecision** field.

**[**D3D11\_FEATURE\_DATA\_DOUBLES**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_doubles):** Feature level 11 devices can support double precision calculations within shader model 5.0 programs. Support for double precision calculations within the shader means that floats can be converted to doubles within the compute shader program, providing the benefit of higher precision computation within each shader pass. The double-precision numbers must be converted back to floats before being written to the output buffer. Note that double-precision division is not necessarily supported.

## Additional capabilities for Direct3D 11.2

Direct3D 11.2 adds four new optional features that can be supported by Direct3D 11 devices. These features are in the [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS1**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options1) structure:

**TiledResourcesTier:** Indicates support for tiled resources, and indicates the tier level supported.

**MinMaxFiltering:** Indicates support for D3D11\_FILTER\_MINIMUM\_\* and D3D11\_FILTER\_MAXIMUM\_\* filtering options, which compare the filtering result to the minimum (or maximum) value. See [**D3D11\_FILTER**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_filter).

**ClearViewAlsoSupportsDepthOnlyFormats:** Indicates support for clearing depth buffer resource views.

**MapOnDefaultBuffers:** Indicates support for mapping render target buffers created with the **D3D11\_USAGE\_DEFAULT** flag.

## Tile based rendering

**[**D3D11\_FEATURE\_DATA\_ARCHITECTURE\_INFO**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_architecture_info):** Indicates whether the graphics device batches rendering commands, and performs tile-based rendering by default. This can be used as a hint for graphics engine optimization.

## Optional features for development and debugging

**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS::DiscardAPIsSeenByDriver:** You can monitor this member during development to rule out legacy drivers on hardware where [**DiscardView**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardview) and [**DiscardResource**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardresource) might have otherwise been beneficial.

**[**D3D11\_FEATURE\_DATA\_MARKER\_SUPPORT**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_marker_support):** This is supported if the hardware and driver support data marking for GPU profiling.

## Related topics

<dl> <dt>

[Devices](overviews-direct3d-11-devices.md)
</dt> </dl>

 

 