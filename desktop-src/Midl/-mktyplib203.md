---
title: /mktyplib203 switch
description: The /mktyplib203 switch forces the MIDL compiler to parse the input file.
ms.assetid: e1eddf03-db42-426e-bdf1-b7122b862756
keywords:
- /mktyplib203 switch MIDL
topic_type:
- apiref
api_name:
- /mktyplib203
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /mktyplib203 switch

The **/mktyplib203** switch forces the MIDL compiler to parse the input file.

``` syntax
midl /mktyplib203
```

## Switch Options

This switch has no parameters.

## Remarks

In order to use the **/mktyplib203** switch, the input file must follow the ODL syntax exactly, which means you cannot place any statements outside of the library block. Examples

**midl /mktyplib203 myoldodl.odl**

**midl /mktyplib203 oldhabit.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 




