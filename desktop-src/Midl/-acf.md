---
title: /acf switch
description: The /acf switch allows the user to supply an explicit ACF file name. The switch also allows the use of different interface names in the IDL and ACF files.
ms.assetid: 8f0833ec-1dbc-4c8a-af7e-3de42169af8d
keywords:
- /acf switch MIDL
topic_type:
- apiref
api_name:
- /acf
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /acf switch

The **/acf** switch allows the user to supply an explicit ACF file name. The switch also allows the use of different interface names in the IDL and ACF files.

``` syntax
midl /acf acf_filename
```

## Switch Options

<dl> <dt>

*acf\_filename* 
</dt> <dd>

Specifies the name of the ACF. White space may or may not be present between the **/acf** switch and the file name.

</dd> </dl>

## Remarks

By default, the MIDL compiler constructs the name of the ACF by replacing the IDL file name extension (usually .idl) with .acf. When the **/acf** switch is present, the ACF takes its name from the specified file name. The **/acf** switch applies only to the IDL file specified on the MIDL compiler command line. It does not apply to imported files.

When the **/acf** switch is used, the interface name in the ACF need not match the MIDL interface name. This feature allows interfaces to share an ACF specification.

When an absolute path to an ACF is not specified, the MIDL compiler searches in the current directory, directories supplied by the [**/I**](-i.md) option, and directories in the INCLUDE path.

If the ACF is not found, the MIDL compiler assumes there is no ACF for this interface. For more information about the sequence of directories, see the reference entries for the [**/I**](-i.md) and [**/no\_def\_idir**](-no-def-idir.md) switches. For more information relating to **/acf**, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

## Examples

**midl /acf bar.acf filename.idl**

## See also

<dl> <dt>

[**/I**](-i.md)
</dt> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/no\_def\_idir**](-no-def-idir.md)
</dt> </dl>

 

 




