---
title: Using descriptors directly in the root signature
description: To avoid the need to go through a descriptor heap, you can put a descriptor directly into the root signature.
ms.assetid: 033E3D8F-3003-42F7-BF77-68A7D62802E5
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Using descriptors directly in the root signature

To avoid the need to go through a descriptor heap, you can put a descriptor directly into the root signature. These descriptors take up a lot of space in the root signature (see [Root signature limits](./root-signature-limits.md)), so we recommend that you use them sparingly.

An example usage would be to place in the root layout a constant buffer view (CBV) that is changing per draw. That's so that descriptor heap space doesn't have to be allocated by the application per draw (and saves pointing a descriptor table at the new location in the descriptor heap). By putting something in the root signature, the application is merely handing the versioning responsibility to the driver; but that's infrastructure that drivers already have.

For rendering that uses extremely few resources, descriptor table/heap use may not be needed at all if all of the needed descriptors can be placed directly in the root signature.

These are the only types of descriptors supported in the root signature.

- Constant buffer view (CBVs).
- Shader resource views (SRVs) / unordered access views (UAVs) of buffer resources where format conversion is not required (untyped buffers). Some examples of untyped buffers that can be bound with root descriptors include `StructuredBuffer<type>`, `RWStructuredBuffer<type>`, `ByteAddressBuffer` and `RWByteAddressBuffer`. Typed buffers such as `Buffer<uint>` and `Buffer<float2>` can't.
- SRVs of raytracing acceleration structures, in local or global root signatures. 

A UAV in the root cannot have counters associated with it. Descriptors in the root signature appear each as individual separate descriptors&mdash;they cannot be dynamically indexed.

``` syntax
struct SceneData
{
   uint foo;
   float bar[2];
   int moo;
};
ConstantBuffer<SceneData> mySceneData : register(b6);
```

In the above example, `mySceneData` can't be declared as an array, as in `cbuffer mySceneData[2]` if it is going to be mapped onto a descriptor in the root signature. That's because indexing across descriptors isn't supported in the root signature. If desired, you can define separate individual constant buffers, and define them each as a separate entry in the root signature. Note that within `mySceneData` above, there is an array `bar[2]`. Dynamic indexing within the constant buffer is valid&mdash;a descriptor in the root signature behaves just like the same descriptor would behave if it were accessed through a descriptor heap. This is in contrast with inlining constants directly in the root signature, which also appears like a constant buffer, except with the constraint that dynamic indexing within the inlined constants is not permitted, so `bar[2]` wouldn't be allowed there.

These APIs (from the [**ID3D12GraphicsCommandList**](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist) interface) are for setting descriptors directly on the root signature.

-   [**SetComputeRootConstantBufferView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootconstantbufferview)
-   [**SetGraphicsRootConstantBufferView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsrootconstantbufferview)
-   [**SetComputeRootShaderResourceView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootshaderresourceview)
-   [**SetGraphicsRootShaderResourceView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsrootshaderresourceview)
-   [**SetComputeRootUnorderedAccessView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootunorderedaccessview)
-   [**SetGraphicsRootUnorderedAccessView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsrootunorderedaccessview)

> [!NOTE]  
> There's no concept of a *root descriptor array* in Direct3D 12. Descriptor arrays are supported only in descriptor heaps.

## Related topics

* [Root signatures](root-signatures.md)