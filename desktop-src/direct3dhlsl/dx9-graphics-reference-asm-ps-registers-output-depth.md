---
title: Output Depth Register
description: The pixel shader output depth register (oDepth) is a write-only scalar register with the range \ 0..1\ that returns a new depth value for a depth test against the depth-stencil buffer.
ms.assetid: 47b9afd9-4520-480d-b4a2-3d9a5569defb
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Output Depth Register

The pixel shader output depth register (oDepth) is a write-only scalar register with the range \[0..1\] that returns a new depth value for a depth test against the depth-stencil buffer.

Syntax



| oDepth |
|--------|



 

Where:



| Name   | Description                                                       |
|--------|-------------------------------------------------------------------|
| oDepth | New depth value for a depth test against the depth-stencil buffer |



 

It is important to be aware that writing to oDepth causes the loss of any hardware-specific depth buffer optimization algorithms (i.e. hierarchical Z) which accelerate depth test performance.

Replicate source swizzle (.x \| .y \| .z \| .w) is required when writing to oDepth. Explicit write masks are not allowed.

Writing to the oDepth register replaces the interpolated depth value (and ignores any depth bias/slopescale renderstates). If no depth buffer has been created or attached to the device, then write to oDepth is ignored.

If you are multisampling and write to oDepth, since the pixel shader only runs once per pixel, your depth value is replicated for all covered sub-sample locations. The depth test still happens per-sample, but you don't have a per-sample depth value going into the comparison from the pixel shader like you would have if you didn't write oDepth.

If an application has a w-buffer set as its depth buffer, then it needs to take that into account while writing to oDepth. It potentially needs to send w-range information to the pixel shader and compute the w-range to scale the w-values written out to oDepth.

### ps\_2\_0 and ps\_2\_x Restrictions

-   oDepth can only be written with the [mov - ps](mov---ps.md) instruction and can only be done once.
-   No source modifier is allowed when writing to oDepth.
-   No instruction modifier is allowed when writing to oDepth.
-   No writing to oDepth from within a flow control construct, or when using predication.

### ps\_3\_0 Restrictions

-   For ps\_3\_0, output registers oC# and oD\# can be written any number of times. The output of the pixel shader comes from the contents of the output registers at the end of shader execution. If a write to an output register does not happen, perhaps due to flow control or if the shader just did not write it, the corresponding render target is also not updated. If a subset of the channels in an output register are written, then undefined values will be written to the remaining channels.
-   You can write to oDepth within flow control or predication as long as all possible paths eventually write into the register.
-   You may not perform any gradient calculations (or operations that implicitly invoke gradient calculations such as [texld - ps\_2\_0 and up](texld---ps-2-0.md), [texldb - ps](texldb---ps.md), [texldp - ps](texldp---ps.md)) inside of flow control statements whose branching conditions vary on a per-primitive basis (ie: dynamic flow control instructions). Instruction predication is not considered dynamic flow control.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 




