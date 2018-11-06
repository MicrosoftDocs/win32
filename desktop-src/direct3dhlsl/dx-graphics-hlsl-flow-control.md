---
title: Flow Control
description: Most hardware is designed to run shader code line by line, executing each HLSL statement once.
ms.assetid: 94f22e39-8e71-424b-8ca1-bafc843f843f
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Flow Control

Most hardware is designed to run shader code line by line, executing each HLSL statement once. A flow-control statement determines at run time which block of HLSL statements to execute next. Using a flow-control statement, a shader can loop through a set of statements, or jump (branch) to an instruction other than the one on the next line. Some flow-control statements support static control that is specified at compile time; others offer predicated control which is a per-component decision made at runtime, and still others support dynamic control which is a decision made at run time based on the contents of a variable.

HLSL supports the following flow-control statements.

-   [break](dx-graphics-hlsl-break.md)
-   [continue](dx-graphics-hlsl-continue.md)
-   [discard](dx-graphics-hlsl-discard.md)
-   [do](dx-graphics-hlsl-do.md)
-   [for](dx-graphics-hlsl-for.md)
-   [if](dx-graphics-hlsl-if.md)
-   [switch](dx-graphics-hlsl-switch.md)
-   [while](dx-graphics-hlsl-while.md)

## Related topics

<dl> <dt>

[Language Syntax (DirectX HLSL)](dx-graphics-hlsl-language-syntax.md)
</dt> </dl>

 

 




