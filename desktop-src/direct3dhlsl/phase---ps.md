---
title: phase - ps
description: The phase instruction marks the transition between phase 1 and phase 2. If no phase instruction is present, the entire shader runs as if it is a phase 2 shader.
ms.assetid: e0e89425-dc8e-489f-a0d1-3eefbfd09178
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# phase - ps

The phase instruction marks the transition between phase 1 and phase 2. If no phase instruction is present, the entire shader runs as if it is a phase 2 shader.

This instruction applies to version 1\_4 only.

## Syntax


```
phase
```



## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| phase                 |      |      |      | x    |      |      |       |      |       |



 

Shader instructions that occur before the phase instruction are phase 1 instructions. All other instructions are phase 2 instructions. By having two phases for instructions, the maximum number of instructions per shader is increased.

The unfortunate side-effect of the phase transition is that the alpha component of [temporary registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md) do not persist across the transition. In other words, the alpha component must be reinitialized after the phase instruction.

## Example

This example shows how to group instructions as phase 1 or phase 2 instructions within a shader.

The phase instruction is also commonly called the phase marker because it marks the transition between phase 1 and 2 instructions. In a version 1\_4 pixel shader, if the phase marker is not present, the shader is run as if it is running in phase 2. This is important because there are differences between phase 1 and 2 instructions and register availability. The differences are noted throughout the reference section.


```
ps_1_4
  // Add phase 1 instructions here

phase
  // Add phase 2 instructions here
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




