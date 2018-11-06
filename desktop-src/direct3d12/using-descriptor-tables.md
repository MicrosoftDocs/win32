---
title: Using Descriptor Tables
description: Descriptor tables, each identifying a range in a descriptor heap, are bound at slots defined by the current root signature on a command list.
ms.assetid: 4ECEC07A-7ABC-4C5F-B23C-36F0D92643FE
ms.topic: article
ms.date: 05/31/2018
---

# Using Descriptor Tables

Descriptor tables, each identifying a range in a descriptor heap, are bound at slots defined by the current root signature on a command list.

-   [Indexing Descriptor Tables](#indexing-descriptor-tables)
-   [Related topics](#related-topics)

Shaders can locate resources referenced by the descriptors that make up the descriptor table. Other resource bindings - Index Buffers, Vertex Buffer, Stream Output Buffers, Render Targets, and Depth Stencil are done directly on a command list rather than via descriptors. To summarize:

The following resource references can share the same descriptor table and heap:

-   Shader resource views
-   Unordered access views
-   Constant buffer views

The following resource references must be in their own descriptor heap:

-   Samplers

The following resources are not placed in descriptor tables or heaps, but are bound directly using command lists:

-   Index buffers
-   Vertex buffers
-   Stream output buffers
-   Render targets
-   Depth stencil views

## Indexing Descriptor Tables

Shaders cannot dynamically index across descriptor table boundaries from a given call-site in the shader. However, the selection of a descriptor within a descriptor table is allowed to be dynamically indexed in shader code within ranges of the same descriptor type (such as indexing across a contiguous region of SRVs).

## Related topics

<dl> <dt>

[Descriptor Tables](descriptor-tables.md)
</dt> </dl>

 

 




