---
title: Stream Output Counters
description: Stream output is the ability of the GPU to write vertices to a buffer. The stream output counters monitor progress.
ms.assetid: 7342DA09-25E9-4154-83BA-B03ADBB8B671
ms.topic: article
ms.date: 05/31/2018
---

# Stream Output Counters

Stream output is the ability of the GPU to write vertices to a buffer. The stream output counters monitor progress.

-   [Differences in Stream Counters from Direct3D 11 to Direct3D 12](#differences-in-stream-counters-from-direct3d-11-to-direct3d-12)
-   [BufferFilledSize](#bufferfilledsize)
-   [Related topics](#related-topics)

## Differences in Stream Counters from Direct3D 11 to Direct3D 12

As a part of the stream output process, the GPU has to know the current location in the buffer that it is writing to. In Direct3D 11, memory to store this location is allocated by the driver and the only way for applications to manipulate this value is via the **SOSetTargets** method. In Direct3D 12, apps allocate memory to store this current location. There are no special ways to manipulate this value, and apps are free to read/write the value with the CPU or GPU.

## BufferFilledSize

The application is responsible for allocating storage for a 32-bit quantity called the *BufferFilledSize*. This contains the number of bytes of data in the stream-output buffer. This storage can be placed in the same, or a different, resource as the one that contains the stream-output data. This value is accessed by the GPU in the stream-output stage to determine where to append new vertex data in the buffer. Additionally, this value is accessed by the GPU to determine when overflow has occurred.

Refer to the structure [**D3D12\_STREAM\_OUTPUT\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_stream_output_desc).

The debug layer will validate the following in [**ID3D12GraphicsCommandList::SOSetTargets**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-sosettargets):

-   *BufferFilledSize* falls in the range implied by {*OffsetInBytes*, *SizeInBytes*}, if a non-NULL resource is specified.
-   *BufferFilledSizeOffsetInBytes* is a multiple of 4.
-   *BufferFilledSizeOffsetInBytes* is within the range of the containing resource.
-   The specified resource is a buffer.

The runtime will not validate the heap type associated with the stream output buffer, as stream output is supported in all heap types.

Root signatures must specify if stream output will be used, by using the [**D3D12\_ROOT\_SIGNATURE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_signature_flags) flags.

D3D12\_ROOT\_SIGNATURE\_FLAG\_ALLOW\_STREAM\_OUTPUT can be specified for root signatures authored in HLSL, in a manner similar to how the other flags are specified.

[**CreateGraphicsPipelineState**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-creategraphicspipelinestate) will fail if the geometry shader contains stream-output but the root signature does not have the D3D12\_ROOT\_SIGNATURE\_FLAG\_ALLOW\_STREAM\_OUTPUT flag set.

When a resource is used as a stream-output target, the resources used must be in the D3D12\_RESOURCE\_STATE\_STREAM\_OUT state. This applies to both the vertex data and the *BufferFilledSize* (which can be in the same or separate resources).

There are no special APIs to set stream-output buffer offsets because applications can write to the *BufferFilledSize* with the CPU or GPU directly.

## Related topics

<dl> <dt>

[Counters and Queries](counters-and-queries.md)
</dt> </dl>

 

 




