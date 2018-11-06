---
title: Optimizing HLSL Shaders
description: This section describes general-purpose strategies that you can use to optimize your shaders. You can apply these strategies to shaders that are written in any language, on any platform.
ms.assetid: 014b9cb3-a489-48d7-8174-b97de168bf3a
keywords:
- high-level shader language
- HLSL, performance
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Optimizing HLSL Shaders

This section describes general-purpose strategies that you can use to optimize your shaders. You can apply these strategies to shaders that are written in any language, on any platform.

-   [Know Where To Perform Shader Calculations](#know-where-to-perform-shader-calculations)
-   [Skip Unnecessary Instructions](#skip-unnecessary-instructions)
-   [Pack Variables and Interpolants](#pack-variables-and-interpolants)
-   [Reduce Shader Complexity](#reduce-shader-complexity)
-   [Related Topics](#related-topics)
-   [Related topics](#related-topics)

## Know Where To Perform Shader Calculations

Vertex shaders perform operations that include fetching vertices and performing matrix transformation of vertex data. Typically, vertex shaders are executed once per vertex.

Pixel Shaders perform operations that include fetching texture data and performing lighting calculations. Typically, pixel shaders are executed once per pixel for a given piece of geometry.

Typically, pixels outnumber vertices in a scene, so pixel shaders execute more often than vertex shaders.

When you design shader algorithms, keep the following in mind:

-   Perform calculations on the vertex shader if possible. A calculation that is performed on a pixel shader is much more expensive than a calculation that is performed on a vertex shader.
-   Consider using per-vertex calculations to improve performance in situations such as dense meshes. For dense meshes, per-vertex calculations may produce results that are visually indistinguishable from results produced with per-pixel calculations.

## Skip Unnecessary Instructions

In HLSL, dynamic branching provides the ability to limit the number of instructions that are executed. Therefore, dynamic branching can help speed up shader execution time. If geometry or pixels are not displayed, use dynamic branching to exit the shader or to limit instructions. For example, if a pixel is not lit, there is no point in executing the lighting algorithm.

The following table lists some cases where you can test conditions in your shader and use dynamic branching to skip unnecessary instructions. The table not comprehensive. Rather, it is intended to give you ideas for optimizing your code.



| Condition to Check                                    | Response in the Shader       |
|-------------------------------------------------------|------------------------------|
| Alpha check determines that a pixel will not be seen. | Skip the rest of the shader. |
| The pixel or geometry is fully fogged.                | Skip the rest of the shader. |
| Skin weights are zero.                                | Skip bones.                  |
| Light attenuation is zero.                            | Skip lighting.               |
| Non-positive Lambertian term.                         | Skip lighting.               |



 

## Pack Variables and Interpolants

Be mindful of the space required for shader data. Pack as much information into a variable or interpolant as possible. Sometimes, the information from two variables can be packed into the memory space of a single variable.

## Reduce Shader Complexity

Keep your shaders small and simple. In general, shaders with fewer instructions execute more quickly than shaders with more instructions. It is also easier to debug and optimize smaller, less complex shaders.

## Related Topics

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)


## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

 




