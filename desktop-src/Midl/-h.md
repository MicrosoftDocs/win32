---
title: /h switch
description: The /h option is functionally equivalent to the /header option.
ms.assetid: 1b74d5f2-6624-4b71-832d-fb55a0e84c86
keywords:
- /h switch MIDL
topic_type:
- apiref
api_name:
- /h
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /h switch

The **/h** option is functionally equivalent to the [**/header**](-header.md) option.

``` syntax
midl /h filename
```

## Switch Options

<dl> <dt>

*filename* 
</dt> <dd>

Specifies a header file name that overrides the default header file name. File names can be explicitly quoted using double quotes (") to prevent the shell from interpreting special characters.

</dd> </dl>

## Remarks

The **/h** switch specifies *filename* as the name for a header file that contains all the definitions contained in the IDL file, without the IDL syntax. This file can be used as a C or C++ header file.

## Examples

**midl /h tlibhead.h filename.idl**

**midl /h "midl.h" filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/header**](-header.md)
</dt> </dl>

 

 




