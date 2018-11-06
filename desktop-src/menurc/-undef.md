---
title: ' undef'
description: The \ undef directive removes the current definition of the specified name. All subsequent occurrences of the name are processed without replacement.
ms.assetid: c9a0b538-3030-4d39-bfc2-d158061967b6
ms.topic: article
ms.date: 05/31/2018
---

# \#undef

The **\#undef** directive removes the current definition of the specified name. All subsequent occurrences of the name are processed without replacement.

``` syntax
#undef name
```

<dl> <dt>

<span id="name"></span><span id="NAME"></span>*name*
</dt> <dd>

Name to be removed. This value is any combination of letters, digits, and punctuation that is valid for the C/C++ preprocessor.

</dd> </dl>

## Example

This example removes the definitions for the names nonzero and USERCLASS:

``` syntax
#undef     nonzero
#undef     USERCLASS
```

## Related topics

<dl> <dt>

[Preprocessor Directives](preprocessor-directives.md)
</dt> </dl>

 

 




