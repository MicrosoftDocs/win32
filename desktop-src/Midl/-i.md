---
title: /I switch
description: The /I switch specifies directories to be searched for imported IDL files, included header files, and ACF files.
ms.assetid: cdb0a1c2-ff99-4060-be72-a54dd20dbf93
keywords:
- /I switch MIDL
topic_type:
- apiref
api_name:
- /I
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /I switch

The **/I** switch specifies directories to be searched for imported IDL files, included header files, and ACF files.

``` syntax
midl /I include_path
```

## Switch Options

<dl> <dt>

*include\_path* 
</dt> <dd>

Specifies one or more directories that contain import, include, and ACF files. White space between the **/I** switch and *include\_path* is optional. Separate multiple directories with a semicolon character (;).

</dd> </dl>

## Remarks

More than one directory can appear with each **/I** switch, and more than one **/I** switch can appear with each MIDL compiler invocation. Directories are searched in the order they are specified.

The **/I** switch setting is also passed by the MIDL compiler to the C compiler's C preprocessor. When the [**/cpp\_cmd**](-cpp-cmd.md) switch is present and the [**/cpp\_opt**](-cpp-opt.md) switch is not, the MIDL compiler concatenates the string specified by the **/cpp\_cmd** switch with the **/I**, [**/D**](-d.md), and [**/U**](-u.md) options and uses this concatenated string to invoke the C preprocessor for each IDL and ACF source file. The MIDL compiler switch **/I** is not passed to the preprocessor when the MIDL compiler switch **/no\_cpp** or **/cpp\_opt** is specified.

In Microsoft operating-system environments (64-bit Windows, 32-bit Windows, 16-bit Windows, and MS-DOS), directories are searched in the following sequence:

1.  Current directory
2.  Directories specified by the **/I** switch (in the order they follow the switch)
3.  Directories specified by the INCLUDE environment variable

When directories are specified with the **/I** switch, the [**/no\_def\_idir**](-no-def-idir.md) switch instructs the MIDL compiler to ignore the current directory, ignore the directories specified by the INCLUDE environment variable, and search only the specified directories.

When no directories are specified with the **/I** switch, the [**/no\_def\_idir**](-no-def-idir.md) switch instructs the MIDL compiler to search only the current directory.

## Examples

**midl /I c:\\include;c:\\include\\h /I\\include2 filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/acf**](-acf.md)
</dt> <dt>

[**/cpp\_cmd**](-cpp-cmd.md)
</dt> <dt>

[**/cpp\_opt**](-cpp-opt.md)
</dt> <dt>

[**/no\_def\_idir**](-no-def-idir.md)
</dt> </dl>

 

 




