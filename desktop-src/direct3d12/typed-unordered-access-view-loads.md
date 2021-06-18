---
title: Typed unordered access view (UAV) loads
description: Learn about Unordered Access View (UAV) Typed Load in Direct3D 12. UAV Typed Load is the ability for a shader to read from a UAV with a specific DXGI_FORMAT.
ms.assetid: 6106D15E-EAF6-4583-B4F2-7CC7EE30DE15
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Typed unordered access view (UAV) loads

Unordered Access View (UAV) Typed Load is the ability for a shader to read from a UAV with a specific [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format).

-   [Overview](#overview)
-   [Supported formats and API calls](#supported-formats-and-api-calls)
-   [Using typed UAV loads from HLSL](#using-typed-uav-loads-from-hlsl)
-   [Using UNORM and SNORM typed UAV loads from HLSL](#using-unorm-and-snorm-typed-uav-loads-from-hlsl)
-   [Related topics](#related-topics)

## Overview

An unordered access view (UAV) is a view of an unordered access resource (which can include buffers, textures, and texture arrays, though without multi-sampling). A UAV allows temporally unordered read/write access from multiple threads. This means that this resource type can be read/written simultaneously by multiple threads without generating memory conflicts. This simultaneous access is handled through the use of [Atomic Functions](/windows/desktop/direct3d11/direct3d-11-advanced-stages-cs-atomic-functions).

D3D12 (and D3D11.3) expands on the list of formats that can be used with typed UAV loads.

## Supported formats and API calls

Previously, the following three formats supported typed UAV loads, and were required for D3D11.0 hardware. They are supported for all D3D11.3 and D3D12 hardware.

-   R32\_FLOAT
-   R32\_UINT
-   R32\_SINT

The following formats are supported as a set on D3D12 or D3D11.3 hardware, so if any one is supported, all are supported.

-   R32G32B32A32\_FLOAT
-   R32G32B32A32\_UINT
-   R32G32B32A32\_SINT
-   R16G16B16A16\_FLOAT
-   R16G16B16A16\_UINT
-   R16G16B16A16\_SINT
-   R8G8B8A8\_UNORM
-   R8G8B8A8\_UINT
-   R8G8B8A8\_SINT
-   R16\_FLOAT
-   R16\_UINT
-   R16\_SINT
-   R8\_UNORM
-   R8\_UINT
-   R8\_SINT

The following formats are optionally and individually supported on D3D12 and D3D11.3 hardware, so a single query would need to be made on each format to test for support.

-   R16G16B16A16\_UNORM
-   R16G16B16A16\_SNORM
-   R32G32\_FLOAT
-   R32G32\_UINT
-   R32G32\_SINT
-   R10G10B10A2\_UNORM
-   R10G10B10A2\_UINT
-   R11G11B10\_FLOAT
-   R8G8B8A8\_SNORM
-   R16G16\_FLOAT
-   R16G16\_UNORM
-   R16G16\_UINT
-   R16G16\_SNORM
-   R16G16\_SINT
-   R8G8\_UNORM
-   R8G8\_UINT
-   R8G8\_SNORM
-   R8G8\_SINT
-   R16\_UNORM
-   R16\_SNORM
-   R8\_SNORM
-   A8\_UNORM
-   B5G6R5\_UNORM
-   B5G5R5A1\_UNORM
-   B4G4R4A4\_UNORM

To determine the support for any additional formats, call [**CheckFeatureSupport**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport) with the [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options) structure as the first parameter (refer to [Capability Querying](capability-querying.md)). The *TypedUAVLoadAdditionalFormats* field will be set if the "supported as a set" list above is supported. Make a second call to **CheckFeatureSupport**, using a [**D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_format_support) structure (checking the returned structure against the D3D12\_FORMAT\_SUPPORT2\_UAV\_TYPED\_LOAD member of the [**D3D12\_FORMAT\_SUPPORT2**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_format_support2) enum) to determine support in the list of optionally supported formats listed above, for example:

``` syntax
D3D12_FEATURE_DATA_D3D12_OPTIONS FeatureData;
ZeroMemory(&FeatureData, sizeof(FeatureData));
HRESULT hr = pDevice->CheckFeatureSupport(D3D12_FEATURE_D3D12_OPTIONS, &FeatureData, sizeof(FeatureData));
if (SUCCEEDED(hr))
{
    // TypedUAVLoadAdditionalFormats contains a Boolean that tells you whether the feature is supported or not
    if (FeatureData.TypedUAVLoadAdditionalFormats)
    {
        // Can assume “all-or-nothing” subset is supported (e.g. R32G32B32A32_FLOAT)
        // Cannot assume other formats are supported, so we check:
        D3D12_FEATURE_DATA_FORMAT_SUPPORT FormatSupport = {DXGI_FORMAT_R32G32_FLOAT, D3D12_FORMAT_SUPPORT1_NONE, D3D12_FORMAT_SUPPORT2_NONE};
        hr = pDevice->CheckFeatureSupport(D3D12_FEATURE_FORMAT_SUPPORT, &FormatSupport, sizeof(FormatSupport));
        if (SUCCEEDED(hr) && (FormatSupport.Support2 & D3D12_FORMAT_SUPPORT2_UAV_TYPED_LOAD) != 0)
        {
            // DXGI_FORMAT_R32G32_FLOAT supports UAV Typed Load!
        }
    }
}
```

## Using typed UAV loads from HLSL

For typed UAVs, the HLSL flag is D3D\_SHADER\_REQUIRES\_TYPED\_UAV\_LOAD\_ADDITIONAL\_FORMATS.

Here is example shader code to process a typed UAV load:

``` syntax
RWTexture2D<float4> uav1;
uint2 coord;
float4 main() : SV_Target
{
  return uav1.Load(coord);
}
```

## Using UNORM and SNORM typed UAV loads from HLSL

When using typed UAV loads to read from a UNORM or SNORM resource, you must properly declare the element type of the HLSL object to be `unorm` or `snorm`. It is specified as undefined behavior to mismatch the element type declared in HLSL with the underlying resource data type. For example, if you are using typed UAV loads on a buffer resource with R8\_UNORM data, then you must declare the element type as `unorm float`:

``` syntax
RWBuffer<unorm float> uav;
```

## Related topics

<dl> <dt>

[Rendering](rendering.md)
</dt> <dt>

[Resource Binding](resource-binding.md)
</dt> <dt>

[Resource Binding in HLSL](resource-binding-in-hlsl.md)
</dt> <dt>

[Shader Model 5.1](/windows/desktop/direct3dhlsl/shader-model-5-1)
</dt> <dt>

[Specifying Root Signatures in HLSL](specifying-root-signatures-in-hlsl.md)
</dt> </dl>

 

 