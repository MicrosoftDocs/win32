---
title: /align switch
description: The /align switch is functionally the same as the MIDL /Zp option and is recognized by the MIDL compiler solely for backward compatibility with MkTypLib.
ms.assetid: 7f303c49-a6b5-4e3c-95e5-5c49e338c766
keywords:
- /align switch MIDL
topic_type:
- apiref
api_name:
- /align
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /align switch

The **/align** switch is functionally the same as the MIDL [**/Zp**](-zp.md) option and is recognized by the MIDL compiler solely for backward compatibility with MkTypLib.

> [!Note]  
> The Mktyplib.exe tool is obsolete. Use the MIDL compiler instead.

 

``` syntax
midl /align:alignment
```

## Switch Options

<dl> <dt>

*alignment* 
</dt> <dd>

Specifies the alignment for types in the library. The *alignment* value can be 1, 2, 4, or 8. The value 1 indicates natural alignment; *n* indicates alignment on byte *n*. When you do not specify the **/align** switch, the default is 8.

</dd> </dl>

## Remarks

If you are generating a new makefile, use the [**/Zp**](-zp.md) switch.

The alignment value corresponds to the [**/Zp**](-zp.md) option value used by the Microsoft C/C++ compiler. Be sure that you specify the same alignment when you invoke the C compiler as when you invoke the MIDL compiler.

For more information, see your Microsoft C/C++ programming documentation. For a discussion of the potential dangers in using nonstandard packing levels, see the [**/Zp**](-zp.md) help topic.

## Examples

**midl /align:4 filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/Zp**](-zp.md)
</dt> </dl>

 

 




