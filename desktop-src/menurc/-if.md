---
title: ' if'
description: The \ if directive controls conditional compilation of the resource file by checking the specified constant expression.
ms.assetid: 4d0f26a0-1a2d-4fad-b5ce-b9441397d2c3
ms.topic: article
ms.date: 05/31/2018
---

# \#if

The **\#if** directive controls conditional compilation of the resource file by checking the specified constant expression. If the constant expression is nonzero, **\#if** directs the compiler to continue processing statements up to the next **\#endif**, **\#else**, or **\#elif** directive and then skip to the statement after the **\#endif** directive. If the constant expression is zero, **\#if** directs the compiler to skip to the next **\#endif**, **\#else**, or **\#elif** directive.

``` syntax
#if constant-expression
```

<dl> <dt>

<span id="constant-expression"></span><span id="CONSTANT-EXPRESSION"></span>*constant-expression*
</dt> <dd>

Expression to be checked. This value is a defined name, an integer constant, or an expression consisting of names, integers, and arithmetic and relational operators.

</dd> </dl>

## Example

This example compiles the [**BITMAP**](bitmap-resource.md) statement only if the value assigned Version is less than 3:

``` syntax
#if Version < 3
BITMAP 1 errbox.bmp
#endif
```

## Related topics

<dl> <dt>

[Preprocessor Directives](preprocessor-directives.md)
</dt> </dl>

 

 




