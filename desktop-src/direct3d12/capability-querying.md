---
title: Capability Querying
description: Applications can discover the level of support for resource binding, and many other features, via the ID3D12Device CheckFeatureSupport call.
ms.assetid: 'ECBAF8EF-5D91-46D8-9D6E-A7FA4203B9F8'
---

# Capability Querying

Applications can discover the level of support for resource binding, and many other features, via the [**ID3D12Device::CheckFeatureSupport**](id3d12device-checkfeaturesupport.md) call.

-   [Resource binding tiers](#resource-binding-tiers)
-   [Check feature support](#check-feature-support)
    -   [D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS](#d3d12-feature-data-d3d12-options)
    -   [D3D12\_FEATURE\_DATA\_ARCHITECTURE](#d3d12-feature-data-architecture)
    -   [D3D12\_FEATURE\_DATA\_FEATURE\_LEVELS](#d3d12-feature-data-feature-levels)
    -   [D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT](#d3d12-feature-data-format-support)
    -   [D3D12\_FEATURE\_DATA\_MULTISAMPLE\_QUALITY\_LEVELS](#d3d12-feature-data-multisample-quality-levels)
    -   [D3D12\_FEATURE\_DATA\_FORMAT\_INFO](#d3d12-feature-data-format-info)
    -   [D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT](#d3d12-feature-data-gpu-virtual-address-support)
-   [Hardware support for DXGI Formats](#hardware-support-for-dxgi-formats)
-   [Related topics](#related-topics)

## Resource binding tiers

For resource binding, each tier is a superset of lower tiers in functionality, so code that works on a given tier works on any higher tier unchanged.

The number of resource binding tiers is stored in the [**D3D12\_RESOURCE\_BINDING\_TIER**](d3d12-resource-binding-tier.md) enum.

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

Select one member of the enum [**D3D12\_FEATURE**](d3d12-feature.md) as input to [**CheckFeatureSupport**](id3d12device-checkfeaturesupport.md) to determine what features to request support information on. It can be one of the following.

-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS**](d3d12-feature-data-d3d12-options.md)
-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS1**](d3d12-feature-data-d3d12-options1.md)
-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS2**](d3d12-feature-data-d3d12-options2.md)
-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS3**](d3d12-feature-data-d3d12-options3.md)
-   [**D3D12\_FEATURE\_DATA\_ROOT\_SIGNATURE**](d3d12-feature-data-root-signature.md)
-   [**D3D12\_FEATURE\_DATA\_ARCHITECTURE**](d3d12-feature-data-architecture.md)
-   [**D3D12\_FEATURE\_DATA\_ARCHITECTURE1**](d3d12-feature-data-architecture1.md)
-   [**D3D12\_FEATURE\_DATA\_FEATURE\_LEVELS**](d3d12-feature-data-feature-levels.md)
-   [**D3D12\_FEATURE\_DATA\_SHADER\_MODEL**](d3d12-feature-data-shader-model.md)
-   [**D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT**](d3d12-feature-data-format-support.md)
-   [**D3D12\_FEATURE\_DATA\_MULTISAMPLE\_QUALITY\_LEVELS**](d3d12-feature-data-multisample-quality-levels.md)
-   [**D3D12\_FEATURE\_DATA\_FORMAT\_INFO**](d3d12-feature-data-format-info.md)
-   [**D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT**](d3d12-feature-data-gpu-virtual-address-support.md)
-   [**D3D12\_FEATURE\_DATA\_SHADER\_CACHE**](d3d12-feature-data-shader-cache.md)
-   [**D3D12\_FEATURE\_DATA\_COMMAND\_QUEUE\_PRIORITY**](d3d12-feature-data-command-queue-priority.md)
-   [**D3D12\_FEATURE\_DATA\_EXISTING\_HEAPS**](d3d12-feature-data-existing-heaps.md)

### D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS

The [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS**](d3d12-feature-data-d3d12-options.md) structure holds a range of supported feature data.

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

-   [**D3D12\_SHADER\_MIN\_PRECISION\_SUPPORT**](d3d12-shader-min-precision-support.md)
-   [**D3D12\_TILED\_RESOURCES\_TIER**](d3d12-tiled-resources-tier.md)
-   [**D3D12\_RESOURCE\_BINDING\_TIER**](d3d12-resource-binding-tier.md)
-   [**D3D12\_CONSERVATIVE\_RASTERIZATION\_TIER**](d3d12-conservative-rasterization-tier.md)

### D3D12\_FEATURE\_DATA\_ARCHITECTURE

The [**D3D12\_FEATURE\_DATA\_ARCHITECTURE**](d3d12-feature-data-architecture.md) structure holds three booleans referencing tile based rendering and UMA support.

### D3D12\_FEATURE\_DATA\_FEATURE\_LEVELS

The [**D3D12\_FEATURE\_DATA\_FEATURE\_LEVELS**](d3d12-feature-data-feature-levels.md) structure holds Direct3D feature level support information.

### D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT

The [**D3D12\_FEATURE\_DATA\_FORMAT\_SUPPORT**](d3d12-feature-data-format-support.md) structure holds data format support details, and refer to the following enums.

-   [**D3D12\_FORMAT\_SUPPORT1**](d3d12-format-support1.md)
-   [**D3D12\_FORMAT\_SUPPORT2**](d3d12-format-support2.md)

Refer to [Typed Unordered Access View Loads](typed-unordered-access-view-loads.md) for an example use of this structure.

### D3D12\_FEATURE\_DATA\_MULTISAMPLE\_QUALITY\_LEVELS

The [**D3D12\_FEATURE\_DATA\_MULTISAMPLE\_QUALITY\_LEVELS**](d3d12-feature-data-multisample-quality-levels.md) structure holds multi-sampling quality level support information, and refer to the [**D3D12\_MULTISAMPLE\_QUALITY\_LEVELS\_FLAG**](d3d12-multisample-quality-level-flags.md) enum.

### D3D12\_FEATURE\_DATA\_FORMAT\_INFO

The [**D3D12\_FEATURE\_DATA\_FORMAT\_INFO**](d3d12-feature-data-format-info.md) structure describes the supported [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) and plane count.

For example,


```C++
inline UINT8 D3D12GetFormatPlaneCount(
    _In_ ID3D12Device* pDevice,
    DXGI_FORMAT Format
    )
{
    D3D12_FEATURE_DATA_FORMAT_INFO formatInfo = {Format};
    if (FAILED(pDevice->CheckFeatureSupport(D3D12_FEATURE_FORMAT_INFO, &amp;formatInfo, sizeof(formatInfo))))
    {
        return 0;
    }
    return formatInfo.PlaneCount;
}
```



### D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT

The [**D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT**](d3d12-feature-data-gpu-virtual-address-support.md) structure provides the maximum number of bits for a virtual GPU address for resources, and for processes.

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

 

 




