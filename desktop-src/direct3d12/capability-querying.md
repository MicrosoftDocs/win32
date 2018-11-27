---
title: Capability querying
description: Your application can discover the level of support for resource binding, and many other features, with a call to ID3D12Device\:\:CheckFeatureSupport.
ms.assetid: ECBAF8EF-5D91-46D8-9D6E-A7FA4203B9F8
ms.topic: article
ms.date: 11/26/2018
---

# Capability querying

Your application can discover the level of support for resource binding (as well as the level of support for many other features), with a call to [**ID3D12Device::CheckFeatureSupport**](/windows/desktop/api/D3D12/nf-d3d12-id3d12device-checkfeaturesupport).

## How to query for the resource binding tier

This first example focuses on resource binding. Each resource binding tier is a superset of lower tiers in functionality, so code that works on a given tier works unchanged on any higher tier.

The resource binding tiers are constants in the [**D3D12_RESOURCE_BINDING_TIER**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_resource_binding_tier) enumeration.

To query for the resource binding tier, use code such as this. This code example demonstrates the general pattern for querying for any of the various kinds of feature support.

```cppwinrt
D3D12_RESOURCE_BINDING_TIER get_resource_binding_tier(::ID3D12Device* pIDevice)
{
    D3D12_FEATURE_DATA_D3D12_OPTIONS featureSupport{};
    winrt::check_hresult(
        pIDevice->CheckFeatureSupport(D3D12_FEATURE_D3D12_OPTIONS, &featureSupport, sizeof(featureSupport))
    );

    switch (featureSupport.ResourceBindingTier)
    {
    case D3D12_RESOURCE_BINDING_TIER_1:
        // Tier 1 is supported.
        break;

    case D3D12_RESOURCE_BINDING_TIER_2:
        // Tiers 1 and 2 are supported.
        break;

    case D3D12_RESOURCE_BINDING_TIER_3:
        // Tiers 1, 2, and 3 are supported.
        break;
    }

    return featureSupport.ResourceBindingTier;
}
```

Note that any enumerated constant that you pass ([**D3D12_FEATURE_D3D12_OPTIONS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_feature), in this case) has a corresponding data structure that receives info about that feature or set of features ([**D3D12_FEATURE_DATA_D3D12_OPTIONS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options), in this case). Always pass a pointer to the structure that matches the enumerated constant that you pass.

## How to query for any feature level

As well as the resource binding tier, there are many other features whose level of support you can query for using the same pattern shown in the code example above. You just pass a different constant from the [**D3D12_FEATURE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_feature) enumeration to [**ID3D12Device::CheckFeatureSupport**](/windows/desktop/api/D3D12/nf-d3d12-id3d12device-checkfeaturesupport) (to tell the API what feature to request support information on), and you pass a pointer to an instance of the matching structure (in which to receive the requested info).

- Pass **D3D12_FEATURE_ARCHITECTURE** and [**D3D12_FEATURE_DATA_ARCHITECTURE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_architecture).
- Pass **D3D12_FEATURE_ARCHITECTURE1** and [**D3D12_FEATURE_DATA_ARCHITECTURE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_architecture1).
- Pass **D3D12_FEATURE_COMMAND_QUEUE_PRIORITY** and [**D3D12_FEATURE_DATA_COMMAND_QUEUE_PRIORITY**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_command_queue_priority).
- Pass **D3D12_FEATURE_CROSS_NODE** and [**D3D12_FEATURE_DATA_CROSS_NODE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_cross_node).
- Pass **D3D12_FEATURE_D3D12_OPTIONS** and [**D3D12_FEATURE_DATA_D3D12_OPTIONS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options).
- Pass **D3D12_FEATURE_D3D12_OPTIONS1** and [**D3D12_FEATURE_DATA_D3D12_OPTIONS1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options1).
- Pass **D3D12_FEATURE_D3D12_OPTIONS2** and [**D3D12_FEATURE_DATA_D3D12_OPTIONS2**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options2).
- Pass **D3D12_FEATURE_D3D12_OPTIONS3** and [**D3D12_FEATURE_DATA_D3D12_OPTIONS3**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options3).
- Pass **D3D12_FEATURE_D3D12_OPTIONS4** and [**D3D12_FEATURE_DATA_D3D12_OPTIONS4**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options4).
- Pass **D3D12_FEATURE_D3D12_OPTIONS5** and [**D3D12_FEATURE_DATA_D3D12_OPTIONS5**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options5).
- Pass **D3D12_FEATURE_EXISTING_HEAPS** and [**D3D12_FEATURE_DATA_EXISTING_HEAPS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_existing_heaps).
- Pass **D3D12_FEATURE_FEATURE_LEVELS** and [**D3D12_FEATURE_DATA_FEATURE_LEVELS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_feature_levels).
- Pass **D3D12_FEATURE_FORMAT_INFO** and [**D3D12_FEATURE_DATA_FORMAT_INFO**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_format_info).
- Pass **D3D12_FEATURE_FORMAT_SUPPORT** and [**D3D12_FEATURE_DATA_FORMAT_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_format_support).
- Pass **D3D12_FEATURE_GPU_VIRTUAL_ADDRESS_SUPPORT** and [**D3D12_FEATURE_DATA_GPU_VIRTUAL_ADDRESS_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_gpu_virtual_address_support).
- Pass **D3D12_FEATURE_MULTISAMPLE_QUALITY_LEVELS** and [**D3D12_FEATURE_DATA_MULTISAMPLE_QUALITY_LEVELS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_multisample_quality_levels).
- Pass **D3D12_FEATURE_PROTECTED_RESOURCE_SESSION_SUPPORT** and [**D3D12_FEATURE_DATA_PROTECTED_RESOURCE_SESSION_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_protected_resource_session_support).
- Pass **D3D12_FEATURE_ROOT_SIGNATURE** and [**D3D12_FEATURE_DATA_ROOT_SIGNATURE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_root_signature).
- Pass **D3D12_FEATURE_SERIALIZATION** and [**D3D12_FEATURE_DATA_SERIALIZATION**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_serialization).
- Pass **D3D12_FEATURE_SHADER_CACHE** and [**D3D12_FEATURE_DATA_SHADER_CACHE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_shader_cache).
- Pass **D3D12_FEATURE_SHADER_MODEL** and [**D3D12_FEATURE_DATA_SHADER_MODEL**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_shader_model).

### D3D12_FEATURE_DATA_D3D12_OPTIONS

The [**D3D12_FEATURE_DATA_D3D12_OPTIONS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_d3d12_options) structure holds a range of supported feature data.

``` syntax
typedef struct D3D12_FEATURE_DATA_D3D12_OPTIONS  
    {  
    /* [annotation] */   
    _Out_  BOOL DoublePrecisionFloatShaderOps;  
    /* [annotation] */   
    _Out_  BOOL OutputMergerLogicOp;  
    /* [annotation] */   
    _Out_  D3D12_SHADER_MIN_PRECISION_SUPPORT MinPrecisionSupport;  
    /* [annotation] */   
    _Out_  D3D12_TILED_RESOURCES_TIER TiledResourcesTier;  
    /* [annotation] */   
    _Out_  D3D12_RESOURCE_BINDING_TIER ResourceBindingTier;  
    /* [annotation] */   
    _Out_  BOOL PSSpecifiedStencilRefSupported;  
    /* [annotation] */   
    _Out_  BOOL TypedUAVLoadAdditionalFormats;  
    /* [annotation] */   
    _Out_  BOOL ROVsSupported;  
    /* [annotation] */   
    _Out_  D3D12_CONSERVATIVE_RASTERIZATION_TIER ConservativeRasterizationTier;  
    /* [annotation] */   
    _Out_  UINT MaxGPUVirtualAddressBitsPerResource;  
    /* [annotation] */   
    _Out_  BOOL StandardSwizzle64KBSupported;  
    }   D3D12_FEATURE_DATA_D3D12_OPTIONS;
    
```

Refer to the following enumerations.

- [**D3D12_SHADER_MIN_PRECISION_SUPPORT**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_shader_min_precision_support)
- [**D3D12_TILED_RESOURCES_TIER**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_tiled_resources_tier)
- [**D3D12_RESOURCE_BINDING_TIER**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_resource_binding_tier)
- [**D3D12_CONSERVATIVE_RASTERIZATION_TIER**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_conservative_rasterization_tier)

### D3D12_FEATURE_DATA_ARCHITECTURE

The [**D3D12_FEATURE_DATA_ARCHITECTURE**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_architecture) structure holds three booleans referencing tile based rendering and UMA support.

### D3D12_FEATURE_DATA_FEATURE_LEVELS

The [**D3D12_FEATURE_DATA_FEATURE_LEVELS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_feature_levels) structure holds Direct3D feature level support information.

### D3D12_FEATURE_DATA_FORMAT_SUPPORT

The [**D3D12_FEATURE_DATA_FORMAT_SUPPORT**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_format_support) structure holds data format support details, and refer to the following enumerations.

- [**D3D12_FORMAT_SUPPORT1**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_format_support1)
- [**D3D12_FORMAT_SUPPORT2**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_format_support2)

Refer to [Typed Unordered Access View Loads](typed-unordered-access-view-loads.md) for an example use of this structure.

### D3D12_FEATURE_DATA_MULTISAMPLE_QUALITY_LEVELS

The [**D3D12_FEATURE_DATA_MULTISAMPLE_QUALITY_LEVELS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_multisample_quality_levels) structure holds multi-sampling quality level support information, and refer to the [**D3D12_MULTISAMPLE_QUALITY_LEVELS_FLAG**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_multisample_quality_level_flags) enumeration.

### D3D12_FEATURE_DATA_FORMAT_INFO

The [**D3D12_FEATURE_DATA_FORMAT_INFO**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_format_info) structure describes the supported [**DXGI_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) and plane count.

For example,


```C++
inline UINT8 D3D12GetFormatPlaneCount(
    _In_ ID3D12Device* pDevice,
    DXGI_FORMAT Format
    )
{
    D3D12_FEATURE_DATA_FORMAT_INFO formatInfo = {Format};
    if (FAILED(pDevice->CheckFeatureSupport(D3D12_FEATURE_FORMAT_INFO, &formatInfo, sizeof(formatInfo))))
    {
        return 0;
    }
    return formatInfo.PlaneCount;
}
```

### D3D12_FEATURE_DATA_GPU_VIRTUAL_ADDRESS_SUPPORT

The [**D3D12_FEATURE_DATA_GPU_VIRTUAL_ADDRESS_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_gpu_virtual_address_support) structure provides the maximum number of bits for a virtual GPU address for resources, and for processes.

## Hardware support for DXGI Formats

To view tables of DXGI formats and hardware features, refer to:

- [DXGI Format Support for Direct3D Feature Level 12.1 Hardware](https://msdn.microsoft.com/library/windows/desktop/mt426648)
- [DXGI Format Support for Direct3D Feature Level 12.0 Hardware](https://msdn.microsoft.com/library/windows/desktop/mt426647)
- [DXGI Format Support for Direct3D Feature Level 11.1 Hardware](https://msdn.microsoft.com/library/windows/desktop/mt427456)
- [DXGI Format Support for Direct3D Feature Level 11.0 Hardware](https://msdn.microsoft.com/library/windows/desktop/mt427455)
- [Hardware Support for Direct3D 10Level9 Formats](https://msdn.microsoft.com/library/windows/desktop/ff471324)
- [Hardware Support for Direct3D 10.1 Formats](https://msdn.microsoft.com/library/windows/desktop/cc627091)
- [Hardware Support for Direct3D 10 Formats](https://msdn.microsoft.com/library/windows/desktop/cc627090)

## Related topics

* [Resource Binding in Direct3D 12](resource-binding.md)
* [Hardware Feature Levels](hardware-feature-levels.md)
* [Root Signatures](root-signatures.md)
