---
description: Expressions are mathematical or logical statements that are used on the right hand side of an equals sign. There are many types of expressions.
ms.assetid: 642aa188-5dd7-49fc-b6cc-845f8fc22530
title: Expressions (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Expressions (Direct3D 9)

Expressions are mathematical or logical statements that are used on the right hand side of an equals sign. There are many types of expressions.

## Expressions

1.  Variable Reference
    ```
    ( variable ) or<variable >
    ```

    

2.  Numeric Scalar
    ```
    scalar 
    ```

    

3.  Numeric Expression

    ```
    ( numeric expression )
    ```

    

    All standard numeric HLL expressions are supported here.

4.  Constructor
    ```
    type ( constructor arguments )
    ```

    

5.  List of Initializers

    ```
    { scalar value [, scalar value ...  ] }
    
    ```

    

    The scalars must be literal scalar values.

    The number of initializers must be compatible with the variable (state) on the left hand side of the equals sign.

6.  OR Expression

    ```
    token [ | token ... ]
    ```

    

    The tokens must be compatible with the variable (state) on the left hand side of the equals sign.

    The tokens are not case sensitive.

7.  NULL

    ```
    NULL
    ```

    

    NULL can only be assigned to a shader, sampler, or a texture object.

8.  Assembly Block

    ```
    asm { code }
    ```

    

    PS Assembly Blocks must be assigned to the PIXELSHADER state.

    VS Assembly Blocks must be assigned to the VERTEXSHADER state.

9.  Sampler State Block

    ```
    sampler_state { [ state = expression ; [ state = ... ] ] }
    ```

    

    Sampler state blocks are sequences of un-indexed sampler stage state or texture assignments.

    Sampler state blocks must be assigned to the SAMPLER effect state.

10. Effect State State Block

    ```
    stateblock_state { [ state [ [index] ] = expression; 
        [ state [ [index] ] = ... ] ] }
    ```

    

    State blocks are sequences of general state. State blocks can be nested, but cannot contain circular references.

    State blocks must be assigned to the STATEBLOCK effect state.

11. HLSL Compile

    ```
    compile target entrypoint ( [ arguments ] )
    ```

    

    The vertex shader vs\_m\_n target indicates D3DVS\_VERSION(m, n) vertex shader version. The pixel shader ps\_m\_n target indicates D3DPS\_VERSION(m, n) pixel shader version.

    Vertex shader high-level language compile expressions can only be assigned to the VERTEXSHADER effect state. Pixel shader high-level language compile expressions can only be assigned to the PIXELSHADER effect state.

## Related topics

<dl> <dt>

[Effect Format](dx9-graphics-reference-effects-file-format.md)
</dt> </dl>

 

 



