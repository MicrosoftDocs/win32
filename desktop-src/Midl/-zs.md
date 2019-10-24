---
title: /Zs switch
description: The /Zs switch indicates that the compiler only checks syntax and does not generate output files.
ms.assetid: 5ff44607-12c3-4a2d-8a7f-2056504990e2
keywords:
- /Zs switch MIDL
topic_type:
- apiref
api_name:
- /Zs
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /Zs switch

The **/Zs** switch indicates that the compiler only checks syntax and does not generate output files.

``` syntax
midl /Zs
midl /syntax_check
```

## Switch Options

This switch has no parameters.

## Remarks

This switch overrides all other switches that specify information about output files.

You can also specify syntax-checking mode with the MIDL compiler switch [**/syntax\_check**](-syntax-check.md).

## Examples

**midl /Zs filename.idl**

**midl /syntax\_check filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/syntax\_check**](-syntax-check.md)
</dt> </dl>

 

 




