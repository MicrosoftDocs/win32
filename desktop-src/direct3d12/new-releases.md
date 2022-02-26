---
title: What's new in Direct3D 12
description: This topic describes the most significant new Direct3D 12 documentation available for various releases.
ms.assetid: 38F41E05-FECB-41DE-8D30-09733FBEAC48
ms.topic: article
ms.date: 12/05/2019
---

# What's new in Direct3D 12

This topic describes the most significant new Direct3D 12 documentation available for various releases.

For info about obtaining and installing Direct3D, see [Direct3D 12 programming environment setup](./directx-12-programming-environment-set-up.md).

## Direct3D 12 on Windows 7

- [Direct3D 12 on Windows 7](https://devblogs.microsoft.com/directx/porting-directx-12-games-to-windows-7/) is now available for developers to use.

## Windows 10 May 2019 Update

These features and APIs were added or updated for Windows 10, version 1903 (10.0; Build 18362)&mdash;also known as Windows 10 May 2019 Update.

- [Variable-rate shading (VRS)](./vrs.md). Lets you allocate rendering performance/power at rates that vary across your rendered image.
- [HLSL shader model 6.4](../direct3dhlsl/hlsl-shader-model-6-4-features-for-direct3d-12.md). Describes the machine learning intrinsics added to HLSL Shader Model 6.4.
- [**D3D12_DRED_VERSION**](/windows/win32/api/d3d12/ne-d3d12-d3d12_dred_version) enumeration. Defines constants that specify a version of Device Removed Extended Data (DRED).
- [**D3D12_FEATURE_DATA_D3D12_OPTIONS6**](/windows/win32/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options6) structure. Indicates the level of support that the adapter provides for metacommands.
- [**D3D12_FEATURE_DATA_QUERY_META_COMMAND**](/windows/win32/api/d3d12/ns-d3d12-d3d12_feature_data_query_meta_command) structure. Indicates the level of support that the adapter provides for metacommands.
- [**D3D12_VARIABLE_SHADING_RATE_TIER**](/windows/win32/api/d3d12/ne-d3d12-d3d12_variable_shading_rate_tier) enumeration. Defines constants that specify a shading rate tier (for variable-rate shading, or VRS).
- [**ID3D12Device6**](/windows/win32/api/d3d12/nn-d3d12-id3d12device6) interface, and its methods. Used to set the mode for driver background processing optimizations. Also see [Background shader optimizations](https://devblogs.microsoft.com/directx/background-shader-optimizations/).
- [**ID3D12DeviceRemovedExtendedData**](/windows/win32/api/d3d12/nn-d3d12-id3d12deviceremovedextendeddata) interface, and its methods. Provides runtime access to Device Removed Extended Data (DRED) data.
- [**ID3D12DeviceRemovedExtendedDataSettings**](/windows/win32/api/d3d12/nn-d3d12-id3d12deviceremovedextendeddatasettings) interface, and its methods. Controls Device Removed Extended Data (DRED) settings.
- [**D3D12GraphicsCommandList5**](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist5) interface, and its methods. Support for variable-rate shading (VRS).

The [**D3D_SHADER_MODEL**](/windows/win32/api/d3d12/ne-d3d12-d3d_shader_model) enumeration has been updated with the addition of the **D3D_SHADER_MODEL_6_5** constant (an experimental-level feature).

The [**D3D12_COMMAND_LIST_TYPE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_command_list_type) enumeration has been updated with the addition of the **D3D12_COMMAND_LIST_TYPE_VIDEO_ENCODE** constant.

The [**D3D12_FEATURE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_feature) enumeration has been updated with the addition of the **D3D12_FEATURE_D3D12_OPTIONS6** and **D3D12_FEATURE_QUERY_META_COMMAND** constants.

The [**D3D12_RESOURCE_STATES**](/windows/win32/api/d3d12/ne-d3d12-d3d12_resource_states) enumeration has been updated with the addition of the **D3D12_RESOURCE_STATE_SHADING_RATE_SOURCE** constant.

## Windows 10, version 1809

These features and APIs were added or updated for Windows 10, version 1809 (10.0; Build 17763)&mdash;also known as Windows 10 October 2018 Update.

- [Direct3D 12 Raytracing](./direct3d-12-raytracing.md)
- [Direct3D 12 Render Passes](./direct3d-12-render-passes.md)

## Windows 10, version 1709

These interfaces have been added to the Direct3D documentation for Windows 10, version 1709.

-   [**ID3D12Fence1**](/windows/win32/api/d3d12/nn-d3d12-id3d12fence1) extends the functionality of creating fences by supporting the retrieval of flags passed in to create the fence.
-   [**ID3D12GraphicsCommandList2**](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist2) extends the list of available graphics commands by supporting writing immediate values directly to a buffer.
-   [**ID3D12Device3**](/windows/win32/api/d3d12/nn-d3d12-id3d12device3) extends the virtual adapter functionality by creating special-purpose diagnostic heaps in system memory that persist even in the event of a GPU-fault or device-removed scenario.

The [**D3D\_SHADER\_MODEL**](/windows/win32/api/d3d12/ne-d3d12-d3d_shader_model) enumeration has a new **D3D\_SHADER\_MODEL\_6\_1** value added to describe the shader model 6.1.

The [**D3D12\_FEATURE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_feature) enumeration also has the new **D3D12\_FEATURE\_D3D12\_OPTIONS3** and **D3D12\_FEATURE\_EXISTING\_HEAPS** values. As the names imply, these values allow you to check for additional Direct3D12 options, as well as checking for support of existing heaps.

## Windows 10, version 1703

These topics have been added to the Direct3D documentation for Windows 10, version 1703.

-   The [**ID3D12Device2::CreatePipelineState**](/windows/win32/api/d3d12/nf-d3d12-id3d12device2-createpipelinestate) method and [**D3D12\_Pipeline\_State\_Stream\_Desc**](/windows/win32/api/d3d12/ns-d3d12-d3d12_pipeline_state_stream_desc) struct represent new and more robust way to create PSOs, and unifies the inteface for creating graphics and compute pipelines.
-   The [**ID3D12Device1::CreatePipelineLibrary1**](https://www.bing.com/search?q=**ID3D12Device1::CreatePipelineLibrary1**) method expands the pipeline library interface to accept the PSOs created with the new, unified [**D3D12\_Pipeline\_State\_Stream\_Desc**](/windows/win32/api/d3d12/ns-d3d12-d3d12_pipeline_state_stream_desc) structure.
-   The [**D3D12EnableExperimentalFeatures**](/windows/win32/api/d3d12/nf-d3d12-d3d12enableexperimentalfeatures) function allows developers to experiment with certain in-development features using a machine in Developer Mode.
-   There are five new interfaces (refer to [Interface Hierarchy](interface-hierarchy.md)):
    -   [**ID3D12GraphicsCommandList1**](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist1)
    -   [**ID3D12PipelineLibrary1**](/windows/win32/api/d3d12/nn-d3d12-id3d12pipelinelibrary1)
    -   [**ID3D12Device2**](/windows/win32/api/d3d12/nn-d3d12-id3d12device2)
    -   [**ID3D12Debug2**](/windows/win32/api/D3D12sdklayers/nn-d3d12sdklayers-id3d12debug2)
    -   [**ID3D12Tools**](/windows/win32/api/d3d12/nn-d3d12-id3d12tools)
-   Refer to the [HLSL Shader Model 6.0 Overview](../direct3dhlsl/hlsl-shader-model-6-0-features-for-direct3d-12.md), which describes the wave intrinsic operations for multi-threaded pixel and compute shaders.
-   The use of [**ID3D12Device::SetStablePowerState**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-setstablepowerstate) has changed.
-   Some new features for Direct3D 11 are described in [Direct3D 11.4 Features](../direct3d11/direct3d-11-4-features.md).
-   [**AtomicCopyBufferUINT**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-atomiccopybufferuint) and [**AtomicCopyBufferUINT64**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-atomiccopybufferuint64) enable **late-latch** to reduce pervieved latency.
-   [**ID3D12Device2::CreatePipelineState**](/windows/win32/api/d3d12/nf-d3d12-id3d12device2-createpipelinestate) and [**OMSetDepthBounds**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-omsetdepthbounds) enable **depth-bounds testing** on supported hardware.
-   [**ResolveSubresourceRegion**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-resolvesubresourceregion) enables **partial resolution** of subresources to help optimize performance.
-   [**SetSamplePositions**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-setsamplepositions) enables **programable sample positions** on supported hardware.

## November 2016 documentation update

-   Revision of the remarks for [**ID3D12GraphicsCommandList::DiscardResource**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-discardresource).
-   Clarification of "State decay to common" (see [Using Resource Barriers to Synchronize Resource States in Direct3D 12](using-resource-barriers-to-synchronize-resource-states-in-direct3d-12.md)).
-   The D3dx12.h header file, referred to in [Helper Structures and Functions for D3D12](helper-structures-and-functions-for-d3d12.md), can be downloaded directly from [The D3D12 Helper Library](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h).

## August 2016 documentation update 2

-   A new guide section entitled [Understanding the D3D12 Debug Layer](understanding-the-d3d12-debug-layer.md).

    Three new debug layer interfaces (in Preview mode) are described: [**ID3D12Debug1**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debug1), [**ID3D12DebugCommandList1**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandlist1), [**ID3D12DebugDevice1**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugdevice1).

## August 2016 documentation update 1

-   Revision of [Using Resource Barriers to Synchronize Resource States in Direct3D 12](using-resource-barriers-to-synchronize-resource-states-in-direct3d-12.md).
-   Revision of [Multi-queue resource access](./user-mode-heap-synchronization.md#multi-queue-resource-access).

## Windows 10, version 1607

These topics have been added to the Direct3D documentation for Windows 10, version 1607.

-   [Root Signature Version 1.1](root-signature-version-1-1.md) : an overview of the updated root signatures, enabling apps to specify how static or volatile descriptors and data are, which can aid graphics driver optimizations.
-   The [**ID3D12Device1::CreatePipelineLibrary**](/windows/win32/api/d3d12/nf-d3d12-id3d12device1-createpipelinelibrary) method describes the advantages of creating a pipeline library.
-   There are three new interfaces (refer to [Interface Hierarchy](interface-hierarchy.md)):
    -   [**ID3D12PipelineLibrary**](/windows/win32/api/d3d12/nn-d3d12-id3d12pipelinelibrary)
    -   [**ID3D12Device1**](/windows/win32/api/d3d12/nn-d3d12-id3d12device1)
    -   [**ID3D12VersionedRootSignatureDeserializer**](/windows/win32/api/d3d12/nn-d3d12-id3d12versionedrootsignaturedeserializer)
-   Refer to the [HLSL Shader Model 6.0 Overview](../direct3dhlsl/hlsl-shader-model-6-0-features-for-direct3d-12.md), which describes the wave intrinsic operations for multi-threaded pixel and compute shaders.
-   The use of [**ID3D12Device::SetStablePowerState**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-setstablepowerstate) has changed.
-   Some new features for Direct3D 11 are described in [Direct3D 11.4 Features](../direct3d11/direct3d-11-4-features.md).
-   The range of supported libraries for Direct3D 12 has been updated, refer to the **Supported tools and libraries** section of [Direct3D 12 Programming Environment Setup](directx-12-programming-environment-set-up.md).
-   [Using DirectX with high dynamic range displays and advanced color](../direct3darticles/high-dynamic-range.md)
-   [Variable refresh rate displays](../direct3ddxgi/variable-refresh-rate-displays.md)
-   [DXGI 1.5 Improvements](../direct3ddxgi/dxgi-1-5-improvements.md)

## Related topics

* [Direct3D 12 Programming Guide](directx-12-programming-guide.md)
