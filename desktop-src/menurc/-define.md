---
title: ' define'
description: The \ define directive assigns the given value to the specified name. All subsequent occurrences of the name are replaced by the value.
ms.assetid: 2699d2dc-caf8-47d6-8b2e-526357962532
ms.topic: article
ms.date: 05/31/2018
---

# \#define

The **\#define** directive assigns the given value to the specified name. All subsequent occurrences of the name are replaced by the value.

``` syntax
#define name value
```

<dl> <dt>

<span id="name"></span><span id="NAME"></span>*name*
</dt> <dd>

Name to be defined. This value is any combination of letters, digits, and punctuation that is valid for the C/C++ preprocessor.

</dd> <dt>

<span id="value"></span><span id="VALUE"></span>*value*
</dt> <dd>

Integer, character string, or line of text.

</dd> </dl>

## Example

This example assigns values to the names NONZERO and USERCLASS:

``` syntax
#define     NONZERO     1
#define     USERCLASS   "MyControlClass"
```

## Related topics

<dl> <dt>

[Preprocessor Directives](preprocessor-directives.md)
</dt> </dl>

 

 




