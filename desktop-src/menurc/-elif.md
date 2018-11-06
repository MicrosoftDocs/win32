---
title: ' elif'
description: The \ elif directive marks an optional clause of a conditional-compilation block defined by a \ ifdef, \ ifndef, or \ if directive.
ms.assetid: 432b8543-7e1a-411a-8191-cc0f0e4a2e86
ms.topic: article
ms.date: 05/31/2018
---

# \#elif

The **\#elif** directive marks an optional clause of a conditional-compilation block defined by a **\#ifdef**, **\#ifndef**, or **\#if** directive. The directive controls conditional compilation of the resource file by checking the specified constant expression. If the constant expression is nonzero, **\#elif** directs the compiler to continue processing statements up to the next **\#endif**, **\#else**, or **\#elif** directive and then skip to the statement after **\#endif**. If the constant expression is zero, **\#elif** directs the compiler to skip to the next **\#endif**, **\#else**, or **\#elif** directive. You can use any number of **\#elif** directives in a conditional block.

``` syntax
#elif constant-expression
```

<dl> <dt>

<span id="constant-expression"></span><span id="CONSTANT-EXPRESSION"></span>*constant-expression*
</dt> <dd>

Expression to be checked. This value is a defined name, an integer constant, or an expression consisting of names, integers, and arithmetic and relational operators.

</dd> </dl>

## Example

In this example, **\#elif** directs the compiler to process the second [**BITMAP**](bitmap-resource.md) statement only if the value assigned to the name Version is less than 7. The **\#elif** directive itself is processed only if Version is greater than or equal to 3.

``` syntax
#if Version < 3
BITMAP 1 errbox.bmp
#elif Version < 7
BITMAP 1 userbox.bmp
#endif
```

## Related topics

<dl> <dt>

[Preprocessor Directives](preprocessor-directives.md)
</dt> </dl>

 

 




