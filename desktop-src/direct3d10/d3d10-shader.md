---
description: HLSL compile options.
ms.assetid: 'vs|directx_sdk|~\d3d10_shader.htm'
title: D3D10_SHADER Constants
ms.topic: article
ms.date: 05/31/2018
---

# D3D10\_SHADER Constants

HLSL compile options.



| \#define                                        | Description                                                                                                                                                                                                                                    |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D10\_SHADER\_AVOID\_FLOW\_CONTROL             | Tell compiler to not allow flow-control (when possible).                                                                                                                                                                                       |
| D3D10\_SHADER\_DEBUG                            | Insert debug file/line/type/symbol information.                                                                                                                                                                                                |
| D3D10\_SHADER\_ENABLE\_STRICTNESS               | By default, the HLSL compiler disables strictness on deprecated syntax. Specifying this flag enables strictness which may not allow for legacy syntax.                                                                                         |
| D3D10\_SHADER\_ENABLE\_BACKWARDS\_COMPATIBILITY | This enables older shaders to compile to 4\_0 targets.                                                                                                                                                                                         |
| D3D10\_SHADER\_FORCE\_VS\_SOFTWARE\_NO\_OPT     | Compile a vertex shader for the next highest shader profile. This option turns debugging on (and optimizations off).                                                                                                                           |
| D3D10\_SHADER\_FORCE\_PS\_SOFTWARE\_NO\_OPT     | Compile a pixel shader for the next highest shader profile. This option turns debugging on (and optimizations off).                                                                                                                            |
| D3D10\_SHADER\_IEEE\_STRICTNESS                 | Enables IEEE strictness.                                                                                                                                                                                                                       |
| D3D10\_SHADER\_NO\_PRESHADER                    | Disables Preshaders. Using this flag will cause the compiler to not pull out static expression for evaluation.                                                                                                                                 |
| D3D10\_SHADER\_OPTIMIZATION\_LEVEL0             | Lowest optimization level. May produce slower code but will do so more quickly. This may be useful in a highly iterative shader development cycle.                                                                                             |
| D3D10\_SHADER\_OPTIMIZATION\_LEVEL1             | Second lowest optimization level.                                                                                                                                                                                                              |
| D3D10\_SHADER\_OPTIMIZATION\_LEVEL2             | Second highest optimization level.                                                                                                                                                                                                             |
| D3D10\_SHADER\_OPTIMIZATION\_LEVEL3             | Highest optimization level. Will produce best possible code but may take significantly longer to do so. This will be useful for final builds of an application where performance is the most important factor.                                 |
| D3D10\_SHADER\_PACK\_MATRIX\_ROW\_MAJOR         | Unless explicitly specified, matrices will be packed in row-major order on input and output from the shader.                                                                                                                                   |
| D3D10\_SHADER\_PACK\_MATRIX\_COLUMN\_MAJOR      | Unless explicitly specified, matrices will be packed in column-major order on input and output from the shader. This is generally more efficient, since it allows vector-matrix multiplication to be performed using a series of dot-products. |
| D3D10\_SHADER\_PARTIAL\_PRECISION               | Force all computations to be done with partial precision; this may run faster on some hardware.                                                                                                                                                |
| D3D10\_SHADER\_PREFER\_FLOW\_CONTROL            | Tell compiler to use flow-control (when possible).                                                                                                                                                                                             |
| D3D10\_SHADER\_SKIP\_OPTIMIZATION               | Skip optimization during code generation; generally recommended for debug only.                                                                                                                                                                |
| D3D10\_SHADER\_SKIP\_VALIDATION                 | Do not validate the generated code against known capabilities and constraints. Only use this with shaders that have been successfully compiled in the past. Shaders are always validated by DirectX before they are set to the device.         |
| D3D10\_SHADER\_WARNINGS\_ARE\_ERRORS            | Inform the HLSL compiler to treat all warnings as errors when compiling the shader code. For new shader code, you should use this option so you can resolve all warnings and ensure the fewest possible hard-to-find code defects.             |



 

These constants are defined as macros in d3d10shader.h.

## Related topics

<dl> <dt>

[Shader Constants](d3d10-graphics-reference-d3d10-shader-constants.md)
</dt> </dl>

 

 



