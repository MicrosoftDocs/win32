---
title: /no_robust switch
description: The /no\_robust switch directs the MIDL compiler to explicitly disable the /robust command line feature. The /robust command line switch and its associated features is the default compiler setting for MIDL version 6.0.359 and later.
ms.assetid: 17ece05a-d39d-4465-8553-199a45c8c073
keywords:
- /no_robust switch MIDL
topic_type:
- apiref
api_name:
- /no_robust
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /no\_robust switch

The **/no\_robust** switch directs the MIDL compiler to explicitly disable the [**/robust**](-robust.md) command line feature. The **/robust** command line switch and its associated features is the default compiler setting for MIDL version 6.0.359 and later.

``` syntax
midl /no_robust
```

## Switch Options

This switch has no parameters.

## Remarks

With MIDL version 6.0.359 and later, the MIDL compiler sets [**/robust**](-robust.md) by default. The **/no\_robust** command line switch must be used to disable the **/robust** feature if generated stubs need to run on Microsoft WindowsÂ NT, WindowsÂ 95/98, or WindowsÂ Me.

## Examples

**midl /no\_robust filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/robust**](-robust.md)
</dt> </dl>

 

 




