---
title: Source Register Swizzling (HLSL VS reference)
description: Before an instruction runs, the data in a source register is copied to a temporary register. Swizzling refers to the ability to copy any source register component to any temporary register component. Swizzling does not affect the source register data.
ms.assetid: 6271d846-c68d-467c-a110-be3279e0c11a
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Source Register Swizzling (HLSL VS reference)

Before an instruction runs, the data in a source register is copied to a temporary register. Swizzling refers to the ability to copy any source register component to any temporary register component. Swizzling does not affect the source register data.

## Component Swizzling

As shown in the following table, swizzling can be applied to the individual components of the source register data (where r is one of the valid vertex shader input [Registers - vs\_1\_1](dx9-graphics-reference-asm-vs-registers-vs-1-1.md)).



| Component modifier                 | Description    |
|------------------------------------|----------------|
| r.\[xyzw\]\[xyzw\]\[xyzw\]\[xyzw\] | Source swizzle |



 

-   All four components are always copied. If fewer than four components are specified, the last component is repeated (xy means .xyyy). If no components are specified, x is repeated (.xxxx).
-   The components can appear in any order. v0.ywx results in v0.ywxx.
-   The rgba components can be used respectively for xyzw (r for x, g for b, etc.).
-   These instructions implement source-register single component swizzles: exp, expp, log, logp, pow, rcp, rsq. The result of these instructions is copied to all four destination register components.

Swizzling cannot be used on the [m3x2 - vs](m3x2---vs.md), [m3x3 - vs](m3x3---vs.md), [m4x3 - vs](m4x3---vs.md), and [m4x4 - vs](m4x4---vs.md) instructions.

## Related topics

<dl> <dt>

[Vertex Shader Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers.md)
</dt> </dl>

 

 




