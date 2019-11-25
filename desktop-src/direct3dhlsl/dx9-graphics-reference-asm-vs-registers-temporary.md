---
title: Temporary Register (HLSL VS reference)
description: A vertex shader temporary register is used to hold intermediate results.
ms.assetid: 186adff6-0641-4507-9adc-e02cf1cc3ea9
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Temporary Register (HLSL VS reference)

A vertex shader temporary register is used to hold intermediate results.

A temporary register must be initialized before it is used. Each temporary register has single-write and triple-read access. This means that a single shader instruction can use as many as three temporary registers as inputs.

Values in a temporary register that remain from preceding invocations of the vertex shader cannot be used.

A register consists of properties that determine how each register behaves.



| Property        | Description                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name            | r\[n\]. n is an optional register number. The default is 0, and is the value used if no value is specified.                                                                                 |
| Count           | A maximum of 12 registers.                                                                                                                                                                  |
| I/O permissions | Read/write. This register can be read or written by the API or by the shader.                                                                                                               |
| Read ports      | The number of times a register can be read within a single instruction is 3. A temporary register is the only register that can be read and written more than once in a single instruction. |



 

Each temporary register has single-write and triple-read access. Therefore, an instruction can have as many as three temporary registers in its set of input source operands.

No values in a temporary register that remain from preceding invocations of the vertex shader can be used. Vertex shaders that read a value from a temporary register before writing to it will fail the Direct3D API call to create the vertex shader.

## Example

Here is an example using a temporary register:


```
def c4, 0,0,0,1
...
// Decompress position
mov r0.x, v0.x
mov r0.y, c4.w       // 1
mov r0.z, v0.y
mov r0.w, c4.w       // 1

// Compute theta from distance and time
mov r4.xz, r0        // xz
```





| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Temporary Register     | x    | x    | x     | x    | x    | x     |



 

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




