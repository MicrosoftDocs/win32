---
title: /no_format_opt switch
description: The /no\_format\_opt switch changes the way MIDL optimizes type and procedure descriptors.
ms.assetid: 721ac828-7b47-4991-8bce-f9babf6c77a8
keywords:
- /no_format_opt switch MIDL
topic_type:
- apiref
api_name:
- /no_format_opt
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /no\_format\_opt switch

The **/no\_format\_opt** switch changes the way MIDL optimizes type and procedure descriptors.

``` syntax
midl /no_format_opt
```

## Switch Options

This switch has no parameters.

## Remarks

By default, MIDL eliminates duplicate type and procedure descriptors in order to reduce the size of the generated stub code. Using the **/no\_format\_opt** switch turns off this optimizing behavior.

## Examples

**midl /no\_format\_opt mylean.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/Oi**](-oi.md)
</dt> </dl>

 

 




