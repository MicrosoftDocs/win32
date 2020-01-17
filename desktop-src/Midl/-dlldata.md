---
title: /dlldata switch
description: The /dlldata switch is used to specify the file name for the generated dlldata file for a proxy DLL. The default file name Dlldata.c is used if the /dlldata switch is not specified.
ms.assetid: 5211498b-c641-447f-9514-a98766e26ea9
keywords:
- /dlldata switch MIDL
topic_type:
- apiref
api_name:
- /dlldata
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /dlldata switch

The **/dlldata** switch is used to specify the file name for the generated dlldata file for a proxy DLL. The default file name Dlldata.c is used if the **/dlldata** switch is not specified.

``` syntax
midl /dlldata file-name
```

## Switch Options

<dl> <dt>

*file-name* 
</dt> <dd>

The name of the C source file the MIDL compiler will generate for the proxy DLL.

</dd> </dl>

## Remarks

The file specified by *file-name* must be linked to the proxy DLL. The dlldata file contains entry points and data structures required by the class factory for the proxy DLL. These data structures specify the object interfaces contained in the proxy DLL. The dlldata file also specifies the class identifier of the class factory for the proxy DLL. This is always the UUID (IID) of the first interface of the first proxy file (by alphabetical order).

The same dlldata file should be specified when invoking MIDL on all the IDL files that will go into a particular proxy DLL. The dlldata file is created or updated during each MIDL compilation, incrementally building a list of the interfaces that will go into the proxy DLL.

## Examples

**midl /dlldata data.c**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 




