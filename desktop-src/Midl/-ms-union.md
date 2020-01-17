---
title: /ms_union switch
description: The /ms\_union switch controls the NDR alignment of nonencapsulated unions.Note  This attribute is provided for backwards compatibility.
ms.assetid: 683d1498-6419-4600-ad5b-c0b6ea44a8e1
keywords:
- /ms_union switch MIDL
topic_type:
- apiref
api_name:
- /ms_union
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /ms\_union switch

The **/ms\_union** switch controls the NDR alignment of nonencapsulated unions.

> [!Note]  
> This attribute is provided for backwards compatibility. It is not recommended for use in a new interface.

 

``` syntax
midl /ms_union
```

## Switch Options

This switch has no parameters.

## Remarks

The MIDL compiler mirrors the behavior of the OSF-DCE IDL compiler for nonencapsulated unions. However, because earlier versions of the MIDL compiler did not do so, the **/ms\_union** switch provides compatibility with interfaces built on previous versions of the MIDL compiler.

The ms\_union feature can be used as a command-line switch (**/ms\_union**), an IDL interface attribute, or as an IDL-type attribute.

## Examples

**midl /ms\_union file.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> </dl>

 

 




