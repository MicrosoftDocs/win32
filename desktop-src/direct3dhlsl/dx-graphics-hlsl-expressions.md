---
title: Expressions
description: An expression is a sequence of variables and literals, punctuated by operators. A literal is an explicit data value, such as 1 for an integer or 2.1 for a floating-point number. Literals are often used to assign a value to a variable.
ms.assetid: b9ba1c1f-3338-45f3-9901-38eaf00278cc
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Expressions

An expression is a sequence of [variables](dx-graphics-hlsl-variable-syntax.md) and literals, punctuated by [operators](dx-graphics-hlsl-statement-blocks.md). A literal is an explicit data value, such as 1 for an integer or 2.1 for a floating-point number. Literals are often used to assign a value to a variable.

An expression followed by a semicolon (;) is called a statement. Statements range in complexity from simple expressions to blocks of statements that accomplish a sequence of actions. Flow-control statements determine the order statements are executed.

A statement block also indicates subscope. Variables declared within a statement block are only recognized within the block. HLSL statements determine the order in which expressions are evaluated. Each expression can be one of the following.

-   An expression
-   A [statement block](dx-graphics-hlsl-statement-blocks.md)
-   A [return statement](dx-graphics-hlsl-return.md)
-   A [flow-control statement](dx-graphics-hlsl-flow-control.md)

## Related topics

<dl> <dt>

[Statements (DirectX HLSL)](dx-graphics-hlsl-statements.md)
</dt> </dl>

 

 




