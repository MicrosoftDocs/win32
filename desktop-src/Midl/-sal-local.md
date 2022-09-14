---
title: /sal_local switch
description: The /sal\_local switch directs MIDL to also generate SAL annotations for parameters of interface methods marked \ local\ . The /sal switch must also be present.
ms.assetid: 49AFC3F6-EAD5-45F6-8862-EFB3D9C479D1
keywords:
- /sal_local switch MIDL
topic_type:
- apiref
api_name:
- /sal_local
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /sal\_local switch

The **/sal\_local** switch directs MIDL to also generate SAL annotations for parameters of interface methods marked [**\[local\]**](local.md). The [**/sal**](-sal.md) switch must also be present.

``` syntax
midl /sal /sal_local
```

## Switch Options

This switch has no parameters.

## Remarks

Modifies the behavior of the [**/sal**](-sal.md) switch to also provide annotations on the parameters of interface methods marked with the [**\[local\]**](local.md) attribute. Use the [**\[annotate\]**](annotate.md)attribute to override the MIDL-generated annotation with a different annotation string.

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/sal**](-sal.md)
</dt> <dt>

[**\[annotate\]**](annotate.md)
</dt> </dl>

 

 




