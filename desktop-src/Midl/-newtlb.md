---
title: /newtlb switch
description: This is the default setting for choosing a type library format.
ms.assetid: 460bc6bc-0958-42bd-92e0-838b019ec79d
keywords:
- /newtlb switch MIDL
topic_type:
- apiref
api_name:
- /newtlb
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /newtlb switch

This is the default setting for choosing a type library format.

``` syntax
midl /newtlb filename
```

## Switch Options

This switch has no parameters.

## Remarks

On recent versions of Windows, this switch does nothing. On unsupported versions of Windows, specifying this switch in the MIDL command line will generate an error.

## Examples

**midl /newtlb filename.idl**

**midl filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/oldtlb**](-oldtlb.md)
</dt> </dl>

 

 




