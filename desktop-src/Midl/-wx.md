---
title: /WX switch
description: The /WX switch instructs the MIDL compiler to handle all errors at the given warning level as errors.
ms.assetid: 1dd9791c-0488-4ca3-8a29-082ae03c3cd4
keywords:
- /WX switch MIDL
topic_type:
- apiref
api_name:
- /WX
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /WX switch

The **/WX** switch instructs the MIDL compiler to handle all errors at the given warning level as errors.

``` syntax
midl /WX
```

## Switch Options

This switch has no parameters.

## Remarks

If the **/WX** switch is specified and the [**/W**](-w.md)*n* switch is not specified, all warnings at the default level, level 1, are treated as errors.

The [**/W**](-w.md)*n* switch directs the compiler to display all warnings at level *n* and **/WX** directs the compiler to handle all warnings as errors. The combination of these two switches directs the compiler to handle all warnings at level *n* as errors.

Errors are different from warnings. Errors cause the MIDL compiler to halt processing of the IDL file. Warnings cause the MIDL compiler to emit an informational message and continue processing the IDL file.

Warning-level zero (0) directs the MIDL compiler to suppress warning information. When the **/W0** and **/WX** switches are combined, the MIDL compiler suppresses all warning information. In this case, the **/WX** switch has no effect.

## Examples

**midl /WX filename.idl**

**midl /W3 /WX filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/W**](-w.md)
</dt> </dl>

 

 




