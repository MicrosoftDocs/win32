---
title: /lcid switch
description: The /lcid MIDL compiler option lets you use international characters in your input files, file names, and directory paths.
ms.assetid: 2ab4ba67-4414-4889-8ed7-83f4888caf8b
keywords:
- /lcid switch MIDL
topic_type:
- apiref
api_name:
- /lcid
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /lcid switch

The **/lcid** MIDL compiler option lets you use international characters in your input files, file names, and directory paths.

``` syntax
midl /lcid localeID
```

## Switch Options

<dl> <dt>

*localeID* 
</dt> <dd>

Specifies the 32-bit locale identifier used in Windows National Language Support. The locale identifier should be specified in decimal.

</dd> </dl>

## Remarks

Within the input files, you can use localized comments, strings, helpstrings and identifiers. In particular, the **/lcid** switch provides full DBCS support, to represent Asian languages such as Japanese, Chinese, and Korean.

> [!Note]  
> The **/lcid** switch is available with MIDL version 3.01.75 and later.

 

## Examples

**midl /lcid 1041 iface.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**lcid**](lcid.md)
</dt> </dl>

 

 




