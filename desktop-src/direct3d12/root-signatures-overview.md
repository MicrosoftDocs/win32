---
title: Root Signatures Overview
description: A root signature is configured by the app and links command lists to the resources the shaders require.
ms.assetid: 2E649DA2-6CAC-4C2A-A420-D4EC0DD6EA73
ms.topic: article
ms.date: 05/31/2018
---

# Root Signatures Overview

A root signature is configured by the app and links command lists to the resources the shaders require. The graphics command list has both a graphics and compute root signature. A compute command list will simply have one compute root signature. These root signatures are independent of each other.

-   [Root parameters and arguments](#root-parameters-and-arguments)
-   [Root constants, descriptors and tables](#root-constants-descriptors-and-tables)
-   [Related topics](#related-topics)

## Root parameters and arguments

A **root signature** is similar to an API function signature, it determines the types of data the shaders should expect, but does not define the actual memory or data. A **root parameter** is one entry in the root signature. The actual values of root parameters set and changed at runtime are called **root arguments**. Changing the root arguments changes the data that the shaders read.

## Root constants, descriptors and tables

The root signature can contain three types of parameters; root constants (constants inlined in the root arguments), root descriptors (descriptors inlined in the root arguments), and descriptor tables (pointers to a range of descriptors in the descriptor heap).

The root constants are inline 32-bit values that show up in the shader as a constant buffer.

The inlined root descriptors should contain descriptors that are accessed most often, though is limited to CBVs, and raw or structured UAV or SRV buffers. A more complex type, such as a 2D texture SRV, cannot be used as a root descriptor. Root descriptors do not include a size limit, so there can be no out-of-bounds checking, unlike descriptors in descriptor heaps, which do include a size.

Descriptor table entries within root signatures contain the descriptor, HLSL shader bind name and visibility flag. Refer to [Shader Model 5.1](/windows/desktop/direct3dhlsl/shader-model-5-1) for details of shader names. On some hardware, there can be a performance gain from only making descriptors visible to the shader stages that require them (refer to [**D3D12\_SHADER\_VISIBILITY**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_shader_visibility)).

![root descriptor table entry](images/root-descriptor-table.png)

The layout of the root signature is quite flexible, with some constraints imposed on less capable hardware. Regardless of the level of hardware, applications should always try to make the root signature as small as needed for maximum efficiency. Applications can trade off having more descriptor tables in the root signature but less room for root constants, or vice versa.

The contents of the root signature (the descriptor tables, root constants and root descriptors) that the application has bound automatically get versioned by the D3D12 driver whenever any part of the contents change between draw (graphics)/dispatch (compute) calls. So each draw/dispatch gets a unique full set of root signature state.

Ideally, there are groups of Pipeline State Objects (PSOs) that share the same root signature. After a root signature is set on the pipeline, all the bindings that it defines (descriptor tables, descriptors, constants) can each be individually set or changed, including inheritance into bundles.

An app can make its own tradeoff between how many descriptor tables it wants versus inline descriptors (which take more space but remove an indirection) versus inline constants (which have no indirection) they want in the root signature. Applications should use the root signature as sparingly as possible, relying on application controlled memory such as heaps and descriptor heaps pointing into them to represent bulk data.

## Related topics

<dl> <dt>

[Root Signatures](root-signatures.md)
</dt> </dl>

 

 
