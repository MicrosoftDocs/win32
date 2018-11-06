---
title: ' ifndef'
description: The \ ifndef directive controls conditional compilation of the resource file by checking the specified name.
ms.assetid: b83d7b0e-1a37-47a8-b495-0eab05ed3a9a
ms.topic: article
ms.date: 05/31/2018
---

# \#ifndef

The **\#ifndef** directive controls conditional compilation of the resource file by checking the specified name. If the name has not been defined or if its definition has been removed by using the **\#undef** directive, **\#ifndef** directs the compiler to continue processing statements up to the next **\#endif**, **\#else**, or **\#elif** directive and then skip to the statement after the **\#endif** directive. If the name is defined, **\#ifndef** directs the compiler to skip to the next **\#endif**, **\#else**, or **\#elif** directive.

``` syntax
#ifndef name
```

<dl> <dt>

<span id="name"></span><span id="NAME"></span>*name*
</dt> <dd>

Name to be checked by the directive.

</dd> </dl>

## Example

This example compiles the [**BITMAP**](bitmap-resource.md) statement only if Optimize is not defined:

``` syntax
#ifndef Optimize
BITMAP 1 errbox.bmp
#endif
```

## Related topics

<dl> <dt>

[Preprocessor Directives](preprocessor-directives.md)
</dt> </dl>

 

 




