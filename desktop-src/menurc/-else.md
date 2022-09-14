---
title: ' else'
description: The \ else directive marks an optional clause of a conditional-compilation block defined by a \ ifdef, \ ifndef, or \ if directive. The \ else directive must be the last directive before the \ endif directive.
ms.assetid: 982466d9-ae77-4e1c-89f3-511335165da7
ms.topic: article
ms.date: 05/31/2018
---

# \#else

The **\#else** directive marks an optional clause of a conditional-compilation block defined by a **\#ifdef**, **\#ifndef**, or **\#if** directive. The **\#else** directive must be the last directive before the **\#endif** directive.

``` syntax
#else
```

This directive has no parameters.

## Example

This example compiles the second [**BITMAP**](bitmap-resource.md) statement only if DEBUG is not defined:

``` syntax
#ifdef DEBUG
    BITMAP 1 errbox.bmp
#else
    BITMAP 1 userbox.bmp
#endif
```

## Related topics

<dl> <dt>

[Preprocessor Directives](preprocessor-directives.md)
</dt> </dl>

 

 




