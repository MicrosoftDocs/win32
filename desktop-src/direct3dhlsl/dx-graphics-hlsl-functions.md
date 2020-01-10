---
title: Functions (HLSL reference)
description: Functions encapsulate HLSL statements.
ms.assetid: b6f934e5-eac7-4859-b1d0-698632011e1d
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Functions (HLSL reference)

Functions encapsulate HLSL statements. This enables you to debug a set of functions and then reuse them across shaders or effects. You may want to create a function that encapsulates the functionality of a vertex shader, pixel shader or texture shader. Other times, you may want to write a helper function that performs some commonly used task, and then call that helper function from your shader function. The rules for writing shader functions for HLSL are very similar to writing C functions.

-   [Syntax](dx-graphics-hlsl-function-syntax.md)
-   [Parameters](dx-graphics-hlsl-function-parameters.md)
-   [Return Statement](dx-graphics-hlsl-return.md)
-   [Signatures](dx-graphics-hlsl-signatures.md)

HLSL also has a number of built-in [**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md). Because all intrinsic functions are tested and performance optimized, it is good practice to use an intrinsic function where possible instead of creating your own function.

## Related topics

<dl> <dt>

[Language Syntax (DirectX HLSL)](dx-graphics-hlsl-language-syntax.md)
</dt> </dl>

 

 




