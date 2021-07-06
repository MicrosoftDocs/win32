---
title: Using descriptors directly in the root signature
description: Applications can put descriptors directly in the root signature to avoid having to go through a descriptor heap.
ms.assetid: 033E3D8F-3003-42F7-BF77-68A7D62802E5
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Using descriptors directly in the root signature

Applications can put descriptors directly in the root signature to avoid having to go through a descriptor heap. These descriptors take a lot of space in the root signature (see the root signature limits section), so applications have to use them sparingly.

An example usage would be to place a constant buffer views (CBV) that is changing per draw in the root layout so that descriptor heap space doesn't have to be allocated by the application per draw (and save pointing a descriptor table at the new location in the descriptor heap). By putting something in the root signature, the application is merely handing the versioning responsibility to the driver, but this is infrastructure that they already have.

For rendering that uses extremely few resources, descriptor table/heap use may not be needed at all if all the needed descriptors can be placed directly in the root signature.

The only types of descriptors supported in the root signature are:
- CBVs.
- Shader Resource Views (SRVs) / Unordered Access Views (UAVs) of buffer resources where format conversion is not required (Untyped Buffers). Some examples of Untyped Buffers that can be bound with root descriptors include `StructuredBuffer<type>`, `RWStructuredBuffer<type>`, `ByteAddressBuffer` and `RWByteAddressBuffer`. For the avoidance of doubt, Typed Buffers such as `Buffer<uint>` and `Buffer<float2>` cannot.
- SRVs of raytracing acceleration structures, in local or global root signatures. 

UAVs in the root cannot have counters associated with them. Descriptors in the root signature appear each as individual separate descriptors&mdash;they cannot be dynamically indexed.

``` syntax
struct SceneData
{
   uint foo;
   float bar[2];
   int moo;
};
ConstantBuffer<SceneData> mySceneData : register(b6);
```

In the above example, `mySceneData` cannot be declared as an array, as in `cbuffer mySceneData[2]` if it is going to be mapped onto a descriptor in the root signature, since indexing across descriptors is not supported in the root signature. The application can define separate individual constant buffers and define them each as a separate entry in the root signature if desired. Note that within `mySceneData` above, there is an array `bar[2]`. Dynamic indexing within the constant buffer is valid - a descriptor in the root signature behaves just like the same descriptor would behave if accessed through a descriptor heap. This is in contrast with inlining constants directly in the root signature, which also appears like a constant buffer except with the constraint that dynamic indexing within the inlined constants is not permitted, so `bar[2]` would not be allowed there.

The following APIs (from the [**ID3D12GraphicsCommandList**](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist) interface) are for setting descriptors directly on the root signature:

-   [**SetComputeRootConstantBufferView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootconstantbufferview)
-   [**SetGraphicsRootConstantBufferView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsrootconstantbufferview)
-   [**SetComputeRootShaderResourceView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootshaderresourceview)
-   [**SetGraphicsRootShaderResourceView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsrootshaderresourceview)
-   [**SetComputeRootUnorderedAccessView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootunorderedaccessview)
-   [**SetGraphicsRootUnorderedAccessView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsrootunorderedaccessview)

> [!Note]  
> There is no concept of a "root descriptor array" in Direct3D 12. Descriptor arrays are only supported in descriptor heaps.

## Related topics

[Root Signatures](root-signatures.md)
