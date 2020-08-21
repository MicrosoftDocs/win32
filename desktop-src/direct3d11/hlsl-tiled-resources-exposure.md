---
title: HLSL tiled resources exposure
description: New Microsoft High Level Shader Language (HLSL) syntax is required to support tiled resources in Shader Model 5.
ms.assetid: B6CE51E6-1BA9-4D15-9654-86FE9BAAF585
ms.topic: article
ms.date: 05/31/2018
---

# HLSL tiled resources exposure

New Microsoft High Level Shader Language (HLSL) syntax is required to support tiled resources in [Shader Model 5](/windows/desktop/direct3dhlsl/d3d11-graphics-reference-sm5).

The new HLSL syntax is allowed only on devices with tiled resources support. Each relevant HLSL method for tiled resources in the following table accepts either one (feedback) or two (clamp and feedback in this order) additional optional parameters. For example, a **Sample** method is:

**Sample(sampler, location \[, offset \[, clamp \[, feedback\] \] \])**

An example of a **Sample** method is [**Texture2D.Sample(S,float,int,float,uint)**](/windows/desktop/direct3dhlsl/t2darray-sample-s-float-int-float-uint-).

The offset, clamp and feedback parameters are optional. You must specify all optional parameters up to the one you need, which is consistent with the C++ rules for default function arguments. For example, if the feedback status is needed, both offset and clamp parameters need to be explicitly supplied to **Sample**, even though they may not be logically needed.

The clamp parameter is a scalar float value. The literal value of clamp=0.0f indicates that the clamp operation isn't performed.

The feedback parameter is a **uint** variable that you can supply to the memory-access querying intrinsic [**CheckAccessFullyMapped**](/windows/desktop/direct3dhlsl/checkaccessfullymapped) function. You must not modify or interpret the value of the feedback parameter; but, the compiler doesn't provide any advanced analysis and diagnostics to detect whether you modified the value.

Here is the syntax of [**CheckAccessFullyMapped**](/windows/desktop/direct3dhlsl/checkaccessfullymapped):

**bool CheckAccessFullyMapped(in uint FeedbackVar);**

[**CheckAccessFullyMapped**](/windows/desktop/direct3dhlsl/checkaccessfullymapped) interprets the value of *FeedbackVar* and returns true if all data being accessed was mapped in the resource; otherwise, **CheckAccessFullyMapped** returns false.

If either the clamp or feedback parameter is present, the compiler emits a variant of the basic instruction. For example, sample of a tiled resource generates the `sample_cl_s` instruction. If neither clamp nor feedback is specified, the compiler emits the basic instruction, so that there is no change from the current behavior. The clamp value of 0.0f indicates that no clamp is performed; thus, the driver compiler can further tailor the instruction to the target hardware. If feedback is a NULL register in an instruction, the feedback is unused; thus, the driver compiler can further tailor the instruction to the target architecture.

If the HLSL compiler infers that clamp is 0.0f and feedback is unused, the compiler emits the corresponding basic instruction (for example, `sample` rather than `sample_cl_s`).

If a tiled resource access consists of several constituent byte code instructions, for example, for structured resources, the compiler aggregates individual feedback values via the OR operation to produce the final feedback value. Therefore, you see a single feedback value for such a complex access.

This is the summary table of HLSL methods that are changed to support feedback and/or clamp. These all work on tiled and non-tiled resources of all dimensions. Non-tiled resources always appear to be fully mapped.



| [HLSL objects](/windows/desktop/direct3dhlsl/d3d11-graphics-reference-sm5-objects)                                                                                                                                                                                                                                | Intrinsic methods with feedback option (\*) - also has clamp option                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \[RW\]Texture2D<br/> \[RW\]Texture2DArray<br/> TextureCUBE<br/> TextureCUBEArray<br/>                                                                                                                                                                                    | Gather<br/> GatherRed<br/> GatherGreen<br/> GatherBlue<br/> GatherAlpha<br/> GatherCmp<br/> GatherCmpRed<br/> GatherCmpGreen<br/> GatherCmpBlue<br/> GatherCmpAlpha<br/> |
| \[RW\]Texture1D<br/> \[RW\]Texture1DArray<br/> \[RW\]Texture2D<br/> \[RW\]Texture2DArray<br/> \[RW\]Texture3D<br/> TextureCUBE<br/> TextureCUBEArray<br/>                                                                                              | Sample\*<br/> SampleBias\*<br/> SampleCmp\*<br/> SampleCmpLevelZero<br/> SampleGrad\*<br/> SampleLevel<br/>                                                                                      |
| \[RW\]Texture1D<br/> \[RW\]Texture1DArray<br/> \[RW\]Texture2D<br/> Texture2DMS<br/> \[RW\]Texture2DArray<br/> Texture2DArrayMS<br/> \[RW\]Texture3D<br/> \[RW\]Buffer<br/> \[RW\]ByteAddressBuffer<br/> \[RW\]StructuredBuffer<br/> | Load                                                                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Pipeline access to tiled resources](pipeline-access-to-tiled-resources.md)
</dt> </dl>

 

