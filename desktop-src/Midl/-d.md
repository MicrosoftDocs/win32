---
title: /D switch
description: The /D switch defines a name and an optional value to be passed to the C preprocessor as if by a \ define directive. Multiple /D directives can be used in a command line.
ms.assetid: 65642bf6-8e25-400b-8b1c-43513ab6b313
keywords:
- /D switch MIDL
topic_type:
- apiref
api_name:
- /D
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /D switch

The **/D** switch defines a name and an optional value to be passed to the C preprocessor as if by a **\#define** directive. Multiple **/D** directives can be used in a command line.

``` syntax
midl /Dname[=definition]
```

## Switch Options

<dl> <dt>

*name* 
</dt> <dd>

Specifies a defined name that is passed to the C preprocessor when the [**/cpp\_cmd**](-cpp-cmd.md) switch is present and the [**/cpp\_opt**](-cpp-opt.md) switch is not present.

</dd> <dt>

*definition* 
</dt> <dd>

Specifies a value associated with the defined name.

</dd> </dl>

## Remarks

White space between the **/D** switch and the defined name is optional.

When the [**/cpp\_cmd**](-cpp-cmd.md) switch is present and the [**/cpp\_opt**](-cpp-opt.md) switch is not, the MIDL compiler concatenates the string specified by the **/cpp\_cmd** switch with the [**/I**](-i.md), **/D**, and [**/U**](-u.md) options and uses this concatenated string to invoke the C preprocessor for each IDL and ACF source file.

The MIDL compiler switch **/D** is ignored when the MIDL compiler switch [/no\_cpp](-no-cpp-nocpp.md) or [**/cpp\_opt**](-cpp-opt.md) is specified.

## Examples

**midl -DUNICODE filename.idl**

## See also

<dl> <dt>

[**/cpp\_cmd**](-cpp-cmd.md)
</dt> <dt>

[**/cpp\_opt**](-cpp-opt.md)
</dt> <dt>

[**/I**](-i.md)
</dt> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/no\_cpp**](-no-cpp-nocpp.md)
</dt> <dt>

[**/U**](-u.md)
</dt> </dl>

 

 




