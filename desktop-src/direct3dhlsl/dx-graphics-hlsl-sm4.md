---
title: Shader Model 4
description: Shader Model 4 is a superset of the capabilities in Shader Model 3, except that Shader Model 4 doesn't support the features in Shader Model 1.
ms.assetid: 76155749-11e9-41ff-881d-8f77f2729364
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Shader Model 4

Shader Model 4 is a superset of the capabilities in [Shader Model 3](dx-graphics-hlsl-sm3.md), except that Shader Model 4 doesn't support the features in Shader Model 1. It has been designed using a common-shader core that gives a common set of features to all programmable shaders, which are only programmable using HLSL.




| Feature | Capability | 
|---------|------------|
| Instruction Set | <a href="dx-graphics-hlsl-intrinsic-functions.md"><strong>HLSL functions</strong></a> | 
| Register Set | The register set is accessible through members in constant and texture buffers using HLSL semantics for things like component packing.<ul><li>Pixel shader registers (see <a href="dx-graphics-hlsl-sm4-registers-ps-4-0.md">Registers - ps_4_0</a> and <a href="dx-graphics-hlsl-sm4-registers-ps-4-1.md">Registers - ps_4_1</a>)</li><li>Vertex shader registers (see <a href="dx-graphics-hlsl-sm4-registers-vs-4-0.md">Registers - vs_4_0</a> and <a href="dx-graphics-hlsl-sm4-registers-vs-4-1.md">Registers - vs_4_1</a>)</li><li>Geometry shader registers (see <a href="dx-graphics-hlsl-sm4-registers-gs-4-0.md">Registers - gs_4_0</a> and <a href="dx-graphics-hlsl-sm4-registers-gs-4-1.md">Registers - gs_4_1</a>)</li></ul> | 
| Vertex Shader Max | No restriction | 
| Pixel Shader Max | No restriction | 
| New Shader Profiles Added | gs_4_0, ps_4_0, vs_4_0, gs_4_1*, ps_4_1*, gs_4_1* | 
| New Effect-Framework Profile Added | fx_4_0, fx_4_1* | 




 

\* - gs\_4\_1, ps\_4\_1, vs\_4\_1 and fx\_4\_1 are supported on Direct3D 10.1 or higher.

Shader Model 4 supports a new pipeline stage—the geometry-shader stage—which can be used to create or modify existing geometry. It also includes two new object types: a stream-output object designed for streaming data out of the geometry stage, and a templated texture object that implements texture sampling functions.

-   [Common-Shader Core](dx-graphics-hlsl-common-core.md)
-   [Constants](dx-graphics-hlsl-constants.md)
-   [Geometry-Shader Object](dx-graphics-hlsl-geometry-shader.md)
-   [Stream-Output Object](dx-graphics-hlsl-so-type.md)
-   [Texture Object](dx-graphics-hlsl-to-type.md)

Shader Model 4 supports packing rules that dictate how tightly data can be arranged when it is stored. These rules are described in [Packing Rules for Constant Variables](dx-graphics-hlsl-packing-rules.md)

The [Shader Model 4 Assembly](dx-graphics-hlsl-sm4-asm.md) section describes the assembly instructions that the Shader Model 4 and Shader Model 4.1 support.

## Related topics

<dl> <dt>

[Shader Models vs Shader Profiles](dx-graphics-hlsl-models.md)
</dt> </dl>

 

 




