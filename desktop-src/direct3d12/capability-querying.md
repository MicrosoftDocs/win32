---
title: Capability Querying
description: Applications can discover the level of support for resource binding, and many other features, via the ID3D12Device CheckFeatureSupport call.
ms.assetid: ECBAF8EF-5D91-46D8-9D6E-A7FA4203B9F8
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Capability Querying

Applications can discover the level of support for resource binding, and many other features, via the [**ID3D12Device::CheckFeatureSupport**](/windows/desktop/api/D3D12/nf-d3d12-id3d12device-checkfeaturesupport) call.

-   [Resource binding tiers](#resource-binding-tiers)
-   [Check feature support](#check-feature-support)
    -   [D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS](https://docs.microsoft.com/windows)
    -   [D3D12\_FEATURE\_DATA\_ARCHITECTURE](https://docs.microsoft.com/windows)
    -   [D3D12\_FEATURE\_DATA\_FEATURE\_LEVELS](https://docs.microsoft.com/windows)
    -   [D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT](https://docs.microsoft.com/windows)
    -   [D3D12\_FEATURE\_DATA\_MULTISAMPLE\_QUALITY\_LEVELS](https://docs.microsoft.com/windows)
    -   [D3D12\_FEATURE\_DATA\_FORMAT\_INFO](https://docs.microsoft.com/windows)
    -   [D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT](https://docs.microsoft.com/windows)
-   [Hardware support for DXGI Formats](#hardware-support-for-dxgi-formats)
-   [Related topics](#related-topics)

## Resource binding tiers

For resource binding, each tier is a superset of lower tiers in functionality, so code that works on a given tier works on any higher tier unchanged.

The number of resource binding tiers is stored in the [**D3D12\_RESOURCE\_BINDING\_TIER**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_resource_binding_tier) enum.

To check the resource binding tier, use code such as

``` syntax
D3D12_FEATURE_DATA_D3D12_OPTIONS options;
mDevice->CheckFeatureSupport(D3D12_FEATURE_D3D12_OPTIONS,&options, sizeof(options));
switch (options.ResourceBindingTier)
{
    case D3D12_RESOURCE_BINDING_TIER_1:
     // Tier 1 is supported
    break;
    
    case D3D12_RESOURCE_BINDING_TIER_2:
     // Tier 1 and 2 are supported
    break;
            
    case D3D12_RESOURCE_BINDING_TIER_3:
     // Tier 1,2 and 3 are supported
    break;
  }
```

The following section shows the full range of options for checking feature support.

## Check feature support

Select one member of the enum [**D3D12\_FEATURE**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_feature) as input to [**CheckFeatureSupport**](/windows/desktop/api/D3D12/nf-d3d12-id3d12device-checkfeaturesupport) to determine what features to request support information on. It can be one of the following.

-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_d3d12_options)
-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options1)
-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS2**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options2)
-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS3**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options3)
-   [**D3D12\_FEATURE\_DATA\_ROOT\_SIGNATURE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_root_signature)
-   [**D3D12\_FEATURE\_DATA\_ARCHITECTURE**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_architecture)
-   [**D3D12\_FEATURE\_DATA\_ARCHITECTURE1**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_architecture1)
-   [**D3D12\_FEATURE\_DATA\_FEATURE\_LEVELS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_feature_levels)
-   [**D3D12\_FEATURE\_DATA\_SHADER\_MODEL**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_shader_model)
-   [**D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_format_support)
-   [**D3D12\_FEATURE\_DATA\_MULTISAMPLE\_QUALITY\_LEVELS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_multisample_quality_levels)
-   [**D3D12\_FEATURE\_DATA\_FORMAT\_INFO**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_format_info)
-   [**D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_gpu_virtual_address_support)
-   [**D3D12\_FEATURE\_DATA\_SHADER\_CACHE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_shader_cache)
-   [**D3D12\_FEATURE\_DATA\_COMMAND\_QUEUE\_PRIORITY**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_command_queue_priority)
-   [**D3D12\_FEATURE\_DATA\_EXISTING\_HEAPS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_existing_heaps)

### D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS

The [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_d3d12_options) structure holds a range of supported feature data.

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

Refer to the following enums.

-   [**D3D12\_SHADER\_MIN\_PRECISION\_SUPPORT**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_shader_min_precision_support)
-   [**D3D12\_TILED\_RESOURCES\_TIER**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_tiled_resources_tier)
-   [**D3D12\_RESOURCE\_BINDING\_TIER**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_resource_binding_tier)
-   [**D3D12\_CONSERVATIVE\_RASTERIZATION\_TIER**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_conservative_rasterization_tier)

### D3D12\_FEATURE\_DATA\_ARCHITECTURE

The [**D3D12\_FEATURE\_DATA\_ARCHITECTURE**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_architecture) structure holds three booleans referencing tile based rendering and UMA support.

### D3D12\_FEATURE\_DATA\_FEATURE\_LEVELS

The [**D3D12\_FEATURE\_DATA\_FEATURE\_LEVELS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_feature_levels) structure holds Direct3D feature level support information.

### D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT

The [**D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_format_support) structure holds data format support details, and refer to the following enums.

-   [**D3D12\_FORMAT\_SUPPORT1**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_format_support1)
-   [**D3D12\_FORMAT\_SUPPORT2**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_format_support2)

Refer to [Typed Unordered Access View Loads](typed-unordered-access-view-loads.md) for an example use of this structure.

### D3D12\_FEATURE\_DATA\_MULTISAMPLE\_QUALITY\_LEVELS

The [**D3D12\_FEATURE\_DATA\_MULTISAMPLE\_QUALITY\_LEVELS**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_feature_data_multisample_quality_levels) structure holds multi-sampling quality level support information, and refer to the [**D3D12\_MULTISAMPLE\_QUALITY\_LEVELS\_FLAG**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_multisample_quality_level_flags) enum.

### D3D12\_FEATURE\_DATA\_FORMAT\_INFO

The [**D3D12\_FEATURE\_DATA\_FORMAT\_INFO**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_format_info) structure describes the supported [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) and plane count.

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



### D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT

The [**D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_gpu_virtual_address_support) structure provides the maximum number of bits for a virtual GPU address for resources, and for processes.

## Hardware support for DXGI Formats

To view tables of DXGI formats and hardware features, refer to:

-   [DXGI Format Support for Direct3D Feature Level 12.1 Hardware](https://msdn.microsoft.com/library/windows/desktop/mt426648)
-   [DXGI Format Support for Direct3D Feature Level 12.0 Hardware](https://msdn.microsoft.com/library/windows/desktop/mt426647)
-   [DXGI Format Support for Direct3D Feature Level 11.1 Hardware](https://msdn.microsoft.com/library/windows/desktop/mt427456)
-   [DXGI Format Support for Direct3D Feature Level 11.0 Hardware](https://msdn.microsoft.com/library/windows/desktop/mt427455)
-   [Hardware Support for Direct3D 10Level9 Formats](https://msdn.microsoft.com/library/windows/desktop/ff471324)
-   [Hardware Support for Direct3D 10.1 Formats](https://msdn.microsoft.com/library/windows/desktop/cc627091)
-   [Hardware Support for Direct3D 10 Formats](https://msdn.microsoft.com/library/windows/desktop/cc627090)

## Related topics

<dl> <dt>

[Resource Binding in Direct3D 12](resource-binding.md)
</dt> <dt>

[Hardware Feature Levels](hardware-feature-levels.md)
</dt> <dt>

[Root Signatures](root-signatures.md)
</dt> </dl>

 

 




