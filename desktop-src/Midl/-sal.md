---
title: /sal switch
description: The /sal switch directs MIDL to generate SAL annotations in the generated stub files.
ms.assetid: 452A19CA-6F72-416F-8059-77937412DA88
keywords:
- /sal switch MIDL
topic_type:
- apiref
api_name:
- /sal
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /sal switch

The **/sal** switch directs MIDL to generate SAL annotations in the generated stub files.

``` syntax
midl /sal
```

## Switch Options

This switch has no parameters.

## Remarks

MIDL will mark pointer and array parameters with annotations that reflect the parameter description in the IDL file as enforced by RPC and the NDR marshaling engine. MIDL does not create annotations for parameters in interface methods marked with the [**\[local\]**](local.md)attribute unless [**/sal\_local**](-sal-local.md) is also present on the command line. To override the MIDL-generated annotation, use the [**\[annotate\]**](annotate.md) attribute.

MIDL-generated annotations are always prefixed with \_\_RPC\_, and require use of the **rpcsal.h** header to translate the annotation into standard SAL annotations.

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/sal\_local**](-sal-local.md)
</dt> <dt>

[**\[annotate\]**](annotate.md)
</dt> </dl>

 

 




