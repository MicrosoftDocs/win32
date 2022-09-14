---
title: Using a Root Signature
description: The root signature is the definition of an arbitrarily arranged collection of descriptor tables (including their layout), root constants and root descriptors.
ms.assetid: 0131CDE4-02DB-440A-92B8-B0933C6414B0
ms.topic: article
ms.date: 05/31/2018
---

# Using a Root Signature

The root signature is the definition of an arbitrarily arranged collection of descriptor tables (including their layout), root constants and root descriptors. Each entry has a cost towards a maximum limit, so the application can trade off the balance between how many of each type of entry the root signature will contain.

-   [Command List Semantic](#command-list-semantic)
-   [Bundle Semantics](#bundle-semantics)
-   [Related topics](#related-topics)

The root signature is an object that can be created by manual specification at the API. All shaders in a PSO must be compatible with the root layout specified with the PSO, or else the individual shaders must include embedded root layouts that match each other; otherwise, PSO creation will fail. One property of the root signature is that shaders don't have to know about it when authored, although root signatures can also be authored directly in shaders if desired. Existing shader assets do not require any changes to be compatible with root signatures. Shader Model 5.1 is introduced to provide some extra flexibility (dynamic indexing of descriptors from within shaders), and can be incrementally adopted starting from existing shader assets as desired.

## Command List Semantic

At the beginning of a command list, the root signature is undefined. Graphics shaders have a separate root signature from the compute shader, each independently assigned on a command list. The root signature set on a command list or bundle must also match the currently set PSO at Draw/Dispatch; otherwise, the behavior is undefined. Transient root signature mismatches before Draw/Dispatch are fine - such as setting an incompatible PSO before switching to a compatible root signature (as long as these are compatible by the time Draw/Dispatch is called). Setting a PSO does not change the root signature. The application must call a dedicated API for setting the root signature.

Once a root signature has been set on a command list, the layout defines the set of bindings that the application is expected to provide, and which PSOs can be used (those compiled with the same layout) for the next draw/dispatch calls. For example, a root signature could be defined by the application to have the following entries. Each entry is referred to as a "slot".

-   \[0\] A CBV descriptor inline (root descriptors)
-   \[1\] A descriptor table containing 2 SRVs, 1 CBVs, and 1 UAV
-   \[2\] A descriptor table containing 1 sampler
-   \[3\] A 4x32-bit collection of root constants
-   \[4\] A descriptor table containing an unspecified number of SRVs

In this case, before being able to issue a Draw/Dispatch, the application is expected to set the appropriate binding to each of the slots \[0..4\] that the application defined with its current root signature. For instance, at slot \[1\], a descriptor table must be bound, which is a contiguous region in a descriptor heap that contains (or will contain at execution) 2 SRVs, 1 CBVs, and 1 UAV. Similarly, descriptor tables must be set at slots \[2\] and \[4\].

The application can change part of the root signature bindings at a time (the rest remain unchanged). For example, if the only thing that needs to change between draws is one of the constants at slot \[2\], that is all the application needs to rebind. As discussed previously, the driver/hardware versions all root signature bind state as it is modified automatically. If a root signature is changed on a command list, all previous root signature bindings become stale and all newly expected bindings must be set before Draw/Dispatch; otherwise, the behavior is undefined. If the root signature is redundantly set to the same one currently set, existing root signature bindings do not become stale.

## Bundle Semantics

Bundles inherit the command list's root signature bindings (the bindings to the various slots in the Command List example above). If a bundle needs to change some of the inherited root signature bindings, it must first set the root signature to be the same as the calling command list (the inherited bindings do not become stale). If the bundle sets the root signature to be different than the calling command list, that has the same effect as changing the root signature on the command list described above: all previous root signature bindings are stale and newly expected bindings must be set before Draw/Dispatch; otherwise, the behavior is undefined. If a bundle does not need to change any root signature bindings, it does not need to set the root signature.

The following code shows an example call flow into a bundle.

``` syntax
// Command List
...
pCmdList->SetGraphicsRootSignature(pRootSig); // new parameter space
MyEngine_SetTextures(); // bundle inherits descriptor table setting
MyEngine_SetAnimationFactor(fTime); // bundle inherits root constant
pCmdList->ExecuteBundle(...);
...
// Bundle
pBundle->SetGraphicsRootSignature(pRootSig); // same as caller, in order to inherits bindings
pBundle->SetPipelineState(pPS); 
pBundle->SetGraphicsRoot32BitConstant(drawConstantsSlot,0,drawIDOffset);
pBundle->Draw(...); // using inherited textures / animation factor
pBundle->SetGraphicsRoot32BitConstant(drawConstantsSlot,1,drawIDOffset);
pBundle->Draw(...);
...
```

Coming out of a bundle, any root layout changes and/or binding changes a bundle makes are inherited back to the calling command list when a bundle finishes executing.

For more information on inheritance, refer to the **Graphics pipeline state inheritance** section of [Managing Graphics Pipeline State in Direct3D 12](managing-graphics-pipeline-state-in-direct3d-12.md).

## Related topics

<dl> <dt>

[Root Signatures](root-signatures.md)
</dt> </dl>

 

 




