---
title: /U switch
description: The /U switch removes any previous definition of a name by passing the name to the C preprocessor as if by a \ undefine directive.
ms.assetid: 3c253fb3-9448-4b55-bfd5-852e6feec280
keywords:
- /U switch MIDL
topic_type:
- apiref
api_name:
- /U
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /U switch

The **/U** switch removes any previous definition of a name by passing the name to the C preprocessor as if by a **\#undefine** directive.

``` syntax
midl /U name
```

## Switch Options

<dl> <dt>

*name* 
</dt> <dd>

Specifies a defined name to be passed to the C preprocessor as if by a **\#undefine** directive. The name is predefined by the C preprocessor or previously defined by the user.

</dd> </dl>

## Remarks

Multiple **/U** directives can be used in a command line. White space between the **/U** switch and the undefined name is optional.

When the [**/cpp\_cmd**](-cpp-cmd.md) switch is present and the [**/cpp\_opt**](-cpp-opt.md) switch is not, the MIDL compiler concatenates the string specified by the /cpp\_cmd switch with the [**/I**](-i.md), [**/D**](-d.md), and **/U** options and uses this concatenated string to invoke the C preprocessor for each IDL and ACF source file. The MIDL compiler switch **/U** is ignored when the MIDL compiler switch **/no\_cpp** or **/cpp\_opt** is specified.

## Examples

**midl /UUNICODE filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/cpp\_cmd**](-cpp-cmd.md)
</dt> <dt>

[**/cpp\_opt**](-cpp-opt.md)
</dt> <dt>

[**/D**](-d.md)
</dt> <dt>

[**/I**](-i.md)
</dt> <dt>

[**/no\_cpp**](-no-cpp-nocpp.md)
</dt> </dl>

 

 




