---
title: Advanced use of Descriptor Tables
description: The following sections provide information about the advanced use of descriptor tables.
ms.assetid: BB0CA29C-65CB-48B1-8351-EE13CC470B54
ms.date: 05/31/2018
ms.topic: article
---

# Advanced use of Descriptor Tables

The following sections provide information about the advanced use of descriptor tables.

-   [Changing Descriptor Table Entries between Rendering Calls](#changing-descriptor-table-entries-between-rendering-calls)
-   [Out of Bounds Indexing](#out-of-bounds-indexing)
-   [Shader Derivatives and Divergent Indexing](#shader-derivatives-and-divergent-indexing)
-   [Related topics](#related-topics)

## Changing Descriptor Table Entries between Rendering Calls

After command lists that set descriptor tables have been submitted to a queue for execution, the application must not edit from the CPU the portions of descriptor heaps that the GPU might reference until the application knows that the GPU has finished using the references.

Work completion can be determined at a tight bound using API fences for tracking GPU progress, or more coarse mechanisms like waiting to see that rendering has been sent to display - whatever suits the application. If an application knows that only a subset of the region a descriptor table points to will be accessed (say due to flow control in the shader), the other unreferenced descriptors are still free to be changed. If an application needs to switch between different descriptor tables between rendering calls, there are a few approaches the application can choose from:

-   Descriptor Table Versioning: Create (or reuse) a separate descriptor table for every unique collection of descriptors that is to be referenced by a command list. When editing and reusing previously populated areas on descriptor heaps, applications must first ensure that the GPU has finished using any portion of a descriptor heap that will be recycled.
-   Dynamic Indexing: Applications can arrange objects that vary across draw/dispatch (or even vary within a draw) in a range of a descriptor heap, define a descriptor table that spans all of them, and from the shader, use dynamic indexing of the table during shader execution to select which object to use.
-   Putting descriptors in the root signature directly. Only a very small number of descriptors can be managed this way because root signature space is limited.

The implication of using descriptor table versioning is that descriptor memory out of a descriptor heap must be burned through for every unique set of descriptors referenced by the graphics pipeline for every command list that could be either executing, queued for execution, or being recorded at any given time.

D3D12 leaves the responsibility of managing versioning to the application for the object types managed via descriptor heaps and descriptor tables. One benefit of this is that applications can choose to reuse descriptor table contents as much as possible rather than always defining a new descriptor table version for every command list submission. The root signature is a space that the D3D12 driver automatically versions.

The ability to bind multiple descriptor tables to the root signature (and thus to the pipeline) at a time allows applications to group and switch sets of descriptor references at different frequencies if desired. For example, an application could use a small number (perhaps just one) of large static descriptor tables that rarely change, or in which regions in the underlying descriptor heap memory are being populated as needed, with the use of dynamic indexing from the shader to select textures. At the same time, the application could maintain another class of resources where the set referenced by each draw call is switched from the CPU using the descriptor table versioning technique.

## Out of Bounds Indexing

Out of bounds indexing of any descriptor table from the shader results in a largely undefined memory access, including the possibility of reading arbitrary in-process memory as if it is a hardware state descriptor and living with the consequence of what the hardware does with that. This could produce a device reset, but will not crash Windows.

## Shader Derivatives and Divergent Indexing

If pixel shader invocations that are executing in a 2x2 stamp (to support derivative calculations) choose different texture indices to sample from out of a descriptor table, and if the selected sampler configuration and texture for any given pixel requires an LOD calculation from texture coordinate derivatives, then the LOD calculation and texture sampling process is done by the hardware independently for each texture lookup in the 2x2 stamp, which will impact performance.

## Related topics

<dl> <dt>

[Descriptor Tables](descriptor-tables.md)
</dt> </dl>

 

 




