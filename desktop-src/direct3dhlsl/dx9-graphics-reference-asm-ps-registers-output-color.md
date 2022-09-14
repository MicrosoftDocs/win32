---
title: Output Color Register
description: The pixel shader color output registers (oC\ ) are write-only registers that output results to multiple render targets.
ms.assetid: 88e69189-3956-47de-a336-921f1e62c025
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Output Color Register

The pixel shader color output registers (oC#) are write-only registers that output results to multiple render targets.

Syntax



| oC# |
|------|



 

Where:



| Name | Description       |
|------|-------------------|
| oC0  | render target \#0 |
| oC1  | render target \#1 |
| oC2  | render target \#2 |
| oC3  | render target \#3 |



 

## Remarks

-   If oCn is written but there is no corresponding render target, then this write to oCn is ignored.
-   The render states D3DRS\_COLORWRITEENABLE, D3DRS\_COLORWRITEENABLE1, D3DRS\_COLORWRITEENABLE2 and D3DRS\_COLORWRITEENABLE3 determine which components of oCn ultimately get written to the render target (after blend, if applicable). If the shader writes some but not all of the components defined by the D3DRS\_COLORWRITEENABLE\* render states for a given oCn register, then the unwritten channels produce undefined values in the corresponding render target. If none of the components of an oCn are written, the corresponding render target must not be updated at all (as stated above), so the D3DRS\_COLORWRITEENABLE\* render states do not apply.

### Shader Model 2 Restrictions

-   oCn can only be written with the [mov - ps](mov---ps.md) instruction.
-   oC0 must be always written in the shader.
-   No source swizzle (except .xyzw = default swizzle) or source modifier is allowed when writing to any oCn.
-   No destination write mask (except .xyzw = default mask) or instruction modifier is allowed when writing to any oCn.
-   If oCn is written, then oC0 - oCn-1 must also be written. For example, to write to oC2, you must also write to oC0 and oC1.
-   At most one write to any oC# per shader is allowed.
-   For ps\_2\_x and ps\_3\_0, you cannot write to oC# and oD\# registers within dynamic flow control or predication (writes to oC# inside static flow control is fine).

### Shader Model 3 Restrictions

-   For ps\_3\_0, output registers oC# and oD\# can be written any number of times. The output of the pixel shader comes from the contents of the output registers at the end of shader execution. If a write to an output register does not happen, perhaps due to flow control or if the shader just did not write it, the corresponding rendertarget is also not updated. If a subset of the channels in an output register are written, then undefined values will be written to the remaining channels.
-   For ps\_3\_0, the oC# registers can be written with any writemasks.
-   For ps\_2\_x and ps\_3\_0, you cannot write to oC# and oD\# registers within dynamic flow control or predication (writes to oC# inside static flow control is fine).
-   You may not perform any gradient calculations (or operations that implicitly invoke gradient calculations such as [texld - ps\_2\_0 and up](texld---ps-2-0.md), [texldb - ps](texldb---ps.md), [texldp - ps](texldp---ps.md)) inside of flow control statements whose branching conditions vary on a per-primitive basis (ie: dynamic flow control instructions). Instruction predication is not considered dynamic flow control.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> <dt>

[Multiple Render Targets (Direct3D 9)](/windows/desktop/direct3d9/multiple-render-targets)
</dt> </dl>

 

 