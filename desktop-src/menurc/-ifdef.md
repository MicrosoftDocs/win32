---
title: ' ifdef'
description: The \ ifdef directive controls conditional compilation of the resource file by checking the specified name.
ms.assetid: 877c6b58-d8a1-4e68-8b69-29fe106d6cbd
ms.topic: article
ms.date: 05/31/2018
---

# \#ifdef

The **\#ifdef** directive controls conditional compilation of the resource file by checking the specified name. If the name has been defined by using a **\#define** directive or by using the **/d** command-line option with the resource compiler, **\#ifdef** directs the compiler to continue with the statement immediately after the **\#ifdef** directive. If the name has not been defined, **\#ifdef** directs the compiler to skip all statements up to the next **\#endif** directive.

``` syntax
#ifdef name
```

<dl> <dt>

<span id="name"></span><span id="NAME"></span>*name*
</dt> <dd>

Name to be checked by the directive.

</dd> </dl>

## Example

This example compiles the [**BITMAP**](bitmap-resource.md) statement only if Debug is defined:

``` syntax
#ifdef Debug
BITMAP 1 errbox.bmp
#endif
```

## Related topics

<dl> <dt>

[Preprocessor Directives](preprocessor-directives.md)
</dt> </dl>

 

 




