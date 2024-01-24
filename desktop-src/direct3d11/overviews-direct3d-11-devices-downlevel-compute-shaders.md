---
title: Compute Shaders on Downlevel Hardware
description: This topic discusses how to make use of compute shaders in a Direct3D 11 app on Direct3D 10 hardware.
ms.assetid: b864269f-c1f7-4253-888d-04d1ed3e6587
ms.topic: article
ms.date: 05/31/2018
---

# Compute Shaders on Downlevel Hardware

Direct3D 11 provides the ability to use [compute shaders](direct3d-11-advanced-stages-compute-shader.md) that operate on most Direct3D 10.x hardware, with some limitations to operation. The compute shader technology is also known as the DirectCompute technology. This topic discusses how to make use of [compute shaders](direct3d-11-advanced-stages-compute-shader.md) in a Direct3D 11 app on Direct3D 10 hardware.

Support for compute shaders on downlevel hardware is only for devices compatible with Direct3D 10.x. Compute shaders cannot be used on Direct3D 9.x hardware.

To check if Direct3D 10.x hardware supports compute shaders, call [**ID3D11Device::CheckFeatureSupport**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport). In the **CheckFeatureSupport** call, pass the D3D11\_FEATURE\_D3D10\_X\_HARDWARE\_OPTIONS value to the *Feature* parameter, pass a pointer to the [**D3D11\_FEATURE\_DATA\_D3D10\_X\_HARDWARE\_OPTIONS**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d10_x_hardware_options) structure to the *pFeatureSupportData* parameter, and pass the size of the **D3D11\_FEATURE\_DATA\_D3D10\_X\_HARDWARE\_OPTIONS** structure to the *FeatureSupportDataSize* parameter. **CheckFeatureSupport** returns **TRUE** in the **ComputeShaders\_Plus\_RawAndStructuredBuffers\_Via\_Shader\_4\_x** member of **D3D11\_FEATURE\_DATA\_D3D10\_X\_HARDWARE\_OPTIONS** if the Direct3D 10.x hardware supports compute shaders.

The [10Level9 Reference](d3d11-graphics-reference-10level9.md) section lists the differences between how various [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) and [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) methods behave at various 10Level9 feature levels.

-   [Unordered Access Views (UAVs)](#unordered-access-views-uavs)
-   [Shader Resource Views (SRVs)](#shader-resource-views-srvs)
-   [Thread Groups](#thread-groups)
    -   [Thread Group Dimensions](#thread-group-dimensions)
    -   [Two-Dimensional Thread Indices](#two-dimensional-thread-indices)
    -   [Thread Group Shared Memory (TGSM)](#thread-group-shared-memory-tgsm)
-   [D3DCompile with D3DCOMPILE\_SKIP\_OPTIMIZATION](/windows)
-   [Related topics](#related-topics)

## Unordered Access Views (UAVs)

Raw ([RWByteAddressBuffer](/windows/desktop/direct3dhlsl/sm5-object-rwbyteaddressbuffer)) and Structured ([RWStructuredBuffer](/windows/desktop/direct3dhlsl/sm5-object-rwstructuredbuffer)) Unordered Access Views are supported on downlevel hardware, with the following limitations:

-   Only a single UAV may be bound to a pipeline at a time through [**ID3D11DeviceContext::CSSetUnorderedAccessViews**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-cssetunorderedaccessviews).
-   The base offset for a Raw UAV must be aligned on a 256-byte boundary (instead of 16-byte alignment required for Direct3D 11 hardware).

Typed UAVs are not supported on downlevel hardware. This includes [Texture1D](/windows/desktop/direct3dhlsl/sm5-object-rwtexture1d), [Texture2D](/windows/desktop/direct3dhlsl/sm5-object-rwtexture2d), and [Texture3D](/windows/desktop/direct3dhlsl/sm5-object-rwtexture3d) UAVs.

Pixel Shaders on downlevel hardware do not support unordered access.

## Shader Resource Views (SRVs)

Raw and Structured Buffers as Shader Resource Views are supported on downlevel hardware for read-only access, as they are on Direct3D 11 hardware. These resource types are supported for Vertex Shaders, Geometry Shaders, Pixel Shaders as well as Compute Shaders.

## Thread Groups

A compute shader can execute on many threads in parallel, within a thread group.

Thread groups are supported on downlevel hardware, with the following limitations:

### Thread Group Dimensions

Thread groups defined for downlevel hardware are limited to X and Y dimensions of 768. This is less than the maximum values of 1024 for Direct3D 11 hardware. The maximum Z dimension of 64 is unchanged.

The total number of threads in the group (X × Y × Z) is limited to 768. This is less than the limit of 1024 for Direct3D 11 hardware.

If these numbers are exceeded, shader compilation will fail.

### Two-Dimensional Thread Indices

A particular thread within a thread group is indexed using a 3D vector given by (x,y,z).

For compute shaders operating on downlevel hardware, thread groups only support two dimensions. This means that the Z value in the 3D vector must always be 1.

This limitation specifically applies to the following:

-   [**ID3D11DeviceContext::Dispatch**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-dispatch)— The *ThreadGroupCountZ* argument must be 1.
-   [**ID3D11DeviceContext::DispatchIndirect**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-dispatchindirect)— This function is not supported on downlevel hardware.
-   [numthreads](/windows/desktop/direct3dhlsl/sm5-attributes-numthreads)— The Z value must be 1.

### Thread Group Shared Memory (TGSM)

Thread Group Shared Memory is limited to 16Kb on downlevel hardware. This is less than the 32Kb that is available to Direct3D 11 hardware.

A Compute Shader thread may only write to its own region of TGSM. This write-only region has a maximum size of 256 bytes or less, with the maximum decreasing as the number of threads declared for the group increases.

The following table defines the per-thread maximum size of a TGSM region for the number of threads in the group:



| Number of Threads in Group | Maximum TGSM Size Per Thread |
|----------------------------|------------------------------|
| 0-64                       | 256                          |
| 65-68                      | 240                          |
| 69-72                      | 224                          |
| 73-76                      | 208                          |
| 77-84                      | 192                          |
| 85-92                      | 176                          |
| 93-100                     | 160                          |
| 101-112                    | 144                          |
| 113-128                    | 128                          |
| 129-144                    | 112                          |
| 145-168                    | 96                           |
| 169-204                    | 80                           |
| 205-256                    | 64                           |
| 257-340                    | 48                           |
| 341-512                    | 32                           |
| 513-768                    | 16                           |



 

A Compute Shader thread may read the TGSM from any location.

## D3DCompile with D3DCOMPILE\_SKIP\_OPTIMIZATION

[**D3DCompile**](/windows/desktop/direct3dhlsl/d3dcompile) returns **E\_NOTIMPL** when you pass cs\_4\_0 as the shader target along with the [**D3DCOMPILE\_SKIP\_OPTIMIZATION**](/windows/desktop/direct3dhlsl/d3dcompile-constants) compile option. The cs\_5\_0 shader target works with **D3DCOMPILE\_SKIP\_OPTIMIZATION**.

## Related topics

<dl> <dt>

[Direct3D 11 on Downlevel Hardware](overviews-direct3d-11-devices-downlevel.md)
</dt> </dl>

 

 