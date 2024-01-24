---
title: /cpp_opt switch
description: The /cpp\_opt switch specifies options to pass to the C/C++ preprocessor.
ms.assetid: f0059caa-aff3-4e96-95f8-a0014d6a6556
keywords:
- /cpp_opt switch MIDL
topic_type:
- apiref
api_name:
- /cpp_opt
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /cpp\_opt switch

The **/cpp\_opt** switch specifies options to pass to the C/C++ preprocessor.

``` syntax
midl /cpp_opt "C_preprocessor_option" file.idl
```

## Switch Options

<dl> <dt>

*C\_preprocessor\_option* 
</dt> <dd>

Specifies command-line option associated with the invoked preprocessor. 

**Note**: For the Microsoft C/C++ preprocessors you must supply the `/E` switch as part of the *C\_preprocessor\_option* string. 

Quotes are required when more than one option is used, and for spaces.

</dd> </dl>

## Remarks

Do not use this switch unless there is a specific reason for doing so. Consult [C-Preprocessor Requirements for MIDL](c-preprocessor-requirements-for-midl.md) for important information regarding preprocessing.

The **/cpp\_opt** switch can be used with or without the [**/cpp\_cmd**](-cpp-cmd.md) switch. Consult **/cpp\_cmd** for details of how the preprocessor command line is constructed in either case.

The **/cpp\_opt** switch, if specified, must always include `/E` in order to function correctly.

## Examples

**midl /cpp\_cmd d:\\nt\\tools\\ia64\\cl.exe /DFLAG=TRUE /Ic:\\inc filename.idl**

**midl /cpp\_cmd "mycpp" /DFLAG=TRUE /Ic:\\inc filename.idl**

**midl /cpp\_opt "/E /DFLAG=TRUE /Ic:\\inc" filename.idl**

**midl /cpp\_cmd "cl" /cpp\_opt "/E /DFLAG=TRUE /Ic:\\inc" filename.idl**

## See also

<dl> <dt>

[**/savePP**](-savepp.md)
</dt> <dt>

[**/cpp\_cmd**](-cpp-cmd.md)
</dt> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/no\_cpp**](-no-cpp-nocpp.md)
</dt> <dt>

[C-Preprocessor Requirements for MIDL](c-preprocessor-requirements-for-midl.md)
</dt> </dl>

 

 




