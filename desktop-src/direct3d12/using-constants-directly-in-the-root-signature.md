---
title: Using Constants Directly in the Root Signature
description: Applications can define root constants in the root signature, each as a set of 32-bit values. They appear in High Level Shading Language (HLSL) as a constant buffer. Note that constant buffers for historical reasons are viewed as sets of 4x32-bit values.
ms.assetid: F9A2640F-D1FA-481C-BDF1-B15372E3C512
ms.topic: article
ms.date: 05/31/2018
---

# Using Constants Directly in the Root Signature

Applications can define root constants in the root signature, each as a set of 32-bit values. They appear in High Level Shading Language (HLSL) as a constant buffer. Note that constant buffers for historical reasons are viewed as sets of 4x32-bit values.

Each set of user constants is treated as a scalar array of 32 -bit values, dynamically indexable and read-only from the shader. Out of bounds indexing a given set of root constants produces undefined results. In HLSL, data structure definitions can be provided for the user constants to give them types. For example, if the root signature defines a set of 4 root constants, HLSL can overlay the following structure on them.

``` syntax
struct DrawConstants
{
    uint foo;
    float2 bar;
    int moo;
};
ConstantBuffer<DrawConstants> myDrawConstants : register(b1, space0);
```

Arrays are not permitted in constant buffers that get mapped onto root constants since dynamic indexing in the root signature space is not supported. For example, it is invalid to have an entry in the constant buffer like `float myArray[2];`. A constant buffer that is mapped to root constants cannot itself be an array; therefore, it is invalid to map `cbuffer myCBArray[2]` into root constants.

Constants can be partially set. For example, if the root signature defines four 32-bit values at *RootTableBindSlot* 2, then any subset of the four constants can be set at a time (the others remain unchanged). This can be useful in bundles that inherit root signature state and can partially change it.

When setting constants be careful of the constant buffer layout expected by the shader. It is possible that constants are padded to `vec4` boundaries, for example. To verify the layout expected, check the reflection information from the HLSL shader.

The following APIs (from the [**ID3D12GraphicsCommandList**](/windows/desktop/api/d3d12/nn-d3d12-id3d12graphicscommandlist) interface) are for setting constants directly on the root signature:

-   [**SetGraphicsRoot32BitConstant**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsroot32bitconstant)
-   [**SetGraphicsRoot32BitConstants**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsroot32bitconstants)
-   [**SetComputeRoot32BitConstant**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputeroot32bitconstant)
-   [**SetComputeRoot32BitConstants**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputeroot32bitconstants)

Also, refer to the [**D3D12\_ROOT\_CONSTANTS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_constants) structure.

## Related topics

<dl> <dt>

[Root Signatures](root-signatures.md)
</dt> </dl>

 

 




