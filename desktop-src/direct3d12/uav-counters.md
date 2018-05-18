---
title: UAV Counters
description: UAV counters can be used to associate a 32-bit atomic counter with an unordered-access-view (UAV).
ms.assetid: '0B77E238-E8CF-466B-9188-3DE96AF97F42'
---

# UAV Counters

UAV counters can be used to associate a 32-bit atomic counter with an unordered-access-view (UAV).

-   [Differences in UAV Counters from Direct3D 11 to Direct3D 12](#differences-in-uav-counters-from-direct3d-11-to-direct3d-12)
-   [Using UAV Counters](#using-uav-counters)
-   [Related topics](#related-topics)

## Differences in UAV Counters from Direct3D 11 to Direct3D 12

In Direct3D 12 apps use the same HLSL shader functions as Direct3D 11 to access the UAV counters:

-   **IncrementCounter**
-   **DecrementCounter**
-   **Append**
-   **Consume**

Outside of the shaders Direct3D 11 uses API methods to access the counters, in Direct3D 12 the 32-bit values are allocated by the app so the 32-bit values can be read and written to by the CPU or GPU just like any other Direct3D 12 resource.

## Using UAV Counters

The app is responsible for allocating 32-bits of storage for UAV counters. This storage can be allocated in a different resource as the one that contains data accessible via the UAV.

Refer to [**CreateUnorderedAccessView**](id3d12device-createunorderedaccessview.md), [**D3D12\_BUFFER\_UAV\_FLAGS**](d3d12-buffer-uav-flags.md) and [**D3D12\_BUFFER\_UAV**](d3d12-buffer-uav.md).

If *pCounterResource* is specified in the call to [**CreateUnorderedAccessView**](id3d12device-createunorderedaccessview.md), then there is a counter associated with the UAV. In this case:

-   *StructureByteStride* must be greater than zero
-   Format must be DXGI\_FORMAT\_UNKNOWN
-   The RAW flag must not be set
-   Both of the resources must be buffers
-   *CounterOffsetInBytes* must be a multiple of 4 bytes
-   *CounterOffsetInBytes* must be within the range of the counter resource
-   *pDesc* cannot be NULL
-   *pResource* cannot be NULL

And note the following use cases:

-   If *pCounterResource* is not specified, then *CounterOffsetInBytes* must be 0.
-   If the RAW flag is set then the format must be DXGI\_FORMAT\_R32\_TYPELESS and the UAV resource must be a buffer.
-   If *pCounterResource* is not set, then *CounterOffsetInBytes* must be 0.
-   If the RAW flag is not set and *StructureByteStride* = 0, then the format must be a valid UAV format.

Direct3D 12 removes the distinction between append and counter UAVs (although the distinction still exists in HLSL bytecode).

The core runtime will validate these restrictions inside of [**CreateUnorderedAccessView**](id3d12device-createunorderedaccessview.md).

During Draw/Dispatch, the counter resource must be in the state [**D3D12\_RESOURCE\_STATE\_UNORDERED\_ACCESS**](d3d12-resource-states.md). Also, within a single Draw/Dispatch call, it is invalid for an application to access the same 32-bit memory location via two separate UAV counters. The debug layer will issue errors if either of these is detected.

There are no "SetUnorderedAccessViewCounterValue" or "CopyStructureCount" methods because apps can simply copy data to and from the counter value directly.

Dynamic indexing of UAVs with counters is supported.

If a shader attempts to access the counter of a UAV that does not have an associated counter, then the debug layer will issue a warning, and a GPU page fault will occur causing the apps’s device to be removed.

UAV counters are supported in all heap types (default, upload, readback).

## Related topics

<dl> <dt>

[Counters and Queries](counters-and-queries.md)
</dt> </dl>

 

 




