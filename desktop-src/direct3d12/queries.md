---
title: Queries
description: In Direct3D 12, queries are grouped into arrays of queries called a query heap. A query heap has a type which defines the valid types of queries that can be used with that heap.
ms.assetid: 'd7403b5d-7e1b-4dd2-ae45-52e1153233c6'
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Queries

In Direct3D 12, queries are grouped into arrays of queries called a query heap. A query heap has a type which defines the valid types of queries that can be used with that heap.

-   [Differences in Queries from Direct3D 11 to Direct3D 12](#differences-in-queries-from-direct3d-11-to-direct3d-12)
-   [Query Heaps](#query-heaps)
-   [Creating Query heaps](#creating-query-heaps)
-   [Extracting data from a query](#extracting-data-from-a-query)
-   [Related topics](#related-topics)

## Differences in Queries from Direct3D 11 to Direct3D 12

The following query types are no longer present in Direct3D 12, their functionality being incorporated into other processes:

-   **Event queries** - event functionally is now handled by fences.
-   **Disjoint timestamp queries** - GPU clocks can be set to a stable state in Direct3D 12 (see the [Timing](timing.md) section). GPU clock comparisons are not meaningful if the GPU idled at all between the timestamps (known as a disjoint query). With stable power two timestamp queries issued from different command lists are reliably comparable. Two timestamps within the same command list are always reliably comparable.
-   **Stream output statistics queries** - in Direct3D 12 there is no single stream output (SO) overflow query for all the output streams. Apps need to issue multiple single-stream queries, and then correlate the results.
-   **Stream output statistics predicate and occlusion predicate queries** - queries (which write to memory) and [Predication](predication.md) (which reads from memory) are no longer coupled, and so these query types are not needed.

A new binary occlusion query type has been added to Direct3D 12. This allows predication strategies that care only whether an object was fully occluded or not (rather than how many pixels were occluded) to indicate this to the device, which might be able to more efficiently perform the queries.

## Query Heaps

Queries can be one from a number of types ([**D3D12\_QUERY\_HEAP\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_query_heap_type)), and are grouped into query heaps before being submitted to the GPU.

A new query type D3D12\_QUERY\_TYPE\_BINARY\_OCCLUSION is available and acts like D3D12\_QUERY\_TYPE\_OCCLUSION except that it returns a binary 0/1 result: 0 indicates that no samples passed depth and stencil testing, 1 indicates that at least one sample passed depth and stencil testing. This enables occlusion queries to not interfere with any GPU performance optimization associated with depth/stencil testing.

## Creating Query heaps

The APIs relevant to creating query heaps are the enum [**D3D12\_QUERY\_HEAP\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_query_heap_type), the struct [**D3D12\_QUERY\_HEAP\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_query_heap_desc), and the method [**CreateQueryHeap**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createqueryheap).

The core runtime will validate that the query heap type is a valid member of the [**D3D12\_HEAP\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_type) enumeration, and that the count is greater than 0.

Each individual query element within a query heap can be started and stopped separately.

The APIs for using the query heaps are the enum [**D3D12\_QUERY\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_query_type), and the methods [**BeginQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-beginquery) and [**EndQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-endquery).

D3D12\_QUERY\_TYPE\_TIMESTAMP is the only query that supports [**EndQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-endquery) only. All other query types require [**BeginQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-beginquery) and **EndQuery**.

The debug layer will validate the following:

-   It is illegal to begin a timestamp query&mdash;you can only end it
-   It is illegal to begin a query twice without ending it (for a given element). For queries that require both begin and end, it is illegal to end a query before the corresponding begin (for a given element).
-   The query type passed to [**BeginQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-beginquery) must match the query type passed to [**EndQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-endquery).

The core runtime will validate the following:

-   [**BeginQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-beginquery) cannot be called on a timestamp query.
-   For the query types which support both [**BeginQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-beginquery) and [**EndQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-endquery) (all except for timestamp), a query for a given element must not span command list boundaries.
-   *ElementIndex* must be within range.
-   The query type is a valid member of the [**D3D12\_QUERY\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_query_type) enum.
-   The query type must be compatible with the query heap. The following table shows the query heap type required for each query type:

    

    | Query Type                                  | Query Heap type                                |
    |---------------------------------------------|------------------------------------------------|
    | D3D12\_QUERY\_TYPE\_OCCLUSION               | D3D12\_QUERY\_HEAP\_TYPE\_OCCLUSION            |
    | D3D12\_QUERY\_TYPE\_BINARY\_OCCLUSION       | D3D12\_QUERY\_HEAP\_TYPE\_OCCLUSION            |
    | D3D12\_QUERY\_TYPE\_TIMESTAMP               | D3D12\_QUERY\_HEAP\_TYPE\_TIMESTAMP            |
    | D3D12\_QUERY\_TYPE\_PIPELINE\_STATISTICS    | D3D12\_QUERY\_HEAP\_TYPE\_PIPELINE\_STATISTICS |
    | D3D12\_QUERY\_TYPE\_SO\_STATISTICS\_STREAM0 | D3D12\_QUERY\_HEAP\_TYPE\_SO\_STATISTICS       |
    | D3D12\_QUERY\_TYPE\_SO\_STATISTICS\_STREAM1 | D3D12\_QUERY\_HEAP\_TYPE\_SO\_STATISTICS       |
    | D3D12\_QUERY\_TYPE\_SO\_STATISTICS\_STREAM2 | D3D12\_QUERY\_HEAP\_TYPE\_SO\_STATISTICS       |
    | D3D12\_QUERY\_TYPE\_SO\_STATISTICS\_STREAM3 | D3D12\_QUERY\_HEAP\_TYPE\_SO\_STATISTICS       |

    

     

-   The query type is supported by the command list type. The following table shows which queries are supported on which command list types.

    

    | Query Type                                  | Supported Command List Types         |
    |---------------------------------------------|--------------------------------------|
    | D3D12\_QUERY\_TYPE\_OCCLUSION               | Direct                               |
    | D3D12\_QUERY\_TYPE\_BINARY\_OCCLUSION       | Direct                               |
    | D3D12\_QUERY\_TYPE\_TIMESTAMP               | Direct, Compute, and optionally Copy |
    | D3D12\_QUERY\_TYPE\_PIPELINE\_STATISTICS    | Direct                               |
    | D3D12\_QUERY\_TYPE\_SO\_STATISTICS\_STREAM0 | Direct                               |
    | D3D12\_QUERY\_TYPE\_SO\_STATISTICS\_STREAM1 | Direct                               |
    | D3D12\_QUERY\_TYPE\_SO\_STATISTICS\_STREAM2 | Direct                               |
    | D3D12\_QUERY\_TYPE\_SO\_STATISTICS\_STREAM3 | Direct                               |

    

     

## Extracting data from a query

The way to extract data from a query is to use the [**ResolveQueryData**](/windows/win32p/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resolvequerydata) method. **ResolveQueryData** works with all memory types (whether they are system memory or device local memory), but requires the destination resource to be in [**D3D12_RESOURCE_STATE_COPY_DEST**](/windows/win32/api/d3d12/ne-d3d12-d3d12_resource_states). 

## Related topics

* [Counters and Queries](counters-and-queries.md)
* [Predication queries walk-through](predication-queries.md)
