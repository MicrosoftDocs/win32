---
title: /syntax_check switch
description: The /syntax\_check switch indicates that the compiler checks only syntax and does not generate output files.
ms.assetid: 8d9139d3-6018-48a7-bea5-0c843b6273d3
keywords:
- /syntax_check switch MIDL
topic_type:
- apiref
api_name:
- /syntax_check
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /syntax\_check switch

The **/syntax\_check** switch indicates that the compiler checks only syntax and does not generate output files.

``` syntax
midl /syntax_check
midl /Zs
```

## Switch Options

This switch has no parameters.

## Remarks

This switch overrides all other switches that specify information about output files.

You can also specify syntax-checking mode with the MIDL compiler option [**/Zs**](-zs.md).

## Examples

**midl /Zs filename.idl**

**midl /syntax\_check filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/Zs**](-zs.md)
</dt> </dl>

 

 




