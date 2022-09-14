---
title: C-Preprocessor Requirements for MIDL
description: This page applies only to developers who have specific reasons to replace the Microsoft C/C++ preprocessor as the preprocessor used by MIDL, or to developers who must specify customized preprocessor switches.
ms.assetid: 1dd5eef4-5ea4-4958-8f53-9a95c0ccbf3e
keywords:
- MIDL compiler MIDL , C-preprocessor, requirements
- C-preprocessor MIDL , requirements
ms.topic: article
ms.date: 05/31/2018
---

# C-Preprocessor Requirements for MIDL

This page applies only to developers who have specific reasons to replace the Microsoft C/C++ preprocessor as the preprocessor used by MIDL, or to developers who must specify customized preprocessor switches. The MIDL switches [**/cpp\_cmd**](-cpp-cmd.md), [**/cpp\_opt**](-cpp-opt.md), and [**/no\_cpp**](-no-cpp-nocpp.md) are used to override the default behavior of the compiler. There is typically no reason to replace the Microsoft C/C++ preprocessor, nor to specify customized preprocessor switches.

The MIDL compiler uses a C preprocessor during initial processing of the IDL file. The build environment used when compiling the IDL files is associated with a default C/C++ preprocessor. If a different preprocessor is to be used, the MIDL compiler switch [**/cpp\_cmd**](-cpp-cmd.md) enables an override of the default C/C++-preprocessor name:

``` syntax
midl /cpp_cmd preprocessor_name filename
```

<dl> <dt>

<span id="preprocessor_name"></span><span id="PREPROCESSOR_NAME"></span>*preprocessor\_name*
</dt> <dd>

Specifies the name of the preprocessor to be used by MIDL. May be specified with a path to the binary. The .exe extension is optional.

</dd> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

Specifies the name of the IDL file.

</dd> </dl>

-   The MIDL compiler expects any preprocessor to observe the following conventions:
-   The input file is specified as the last argument on the command line.
-   The preprocessor must redirect output to the standard output device, stdout.
-   In the output stream of the preprocessor, the **\#line** directives are present to enable better diagnostic messages.
-   The line directives are the only preprocessor directives in the output stream.

MIDL assumes that the spawned preprocessor has removed all preprocessor directives from the input stream of the compiler, with the exception of the occurrences of the line directive necessary for pinpointing source location in compiler messages. When indicating a preprocessor different from the Microsoft C/C++ preprocessor, or when specifying preprocessor options with the [**/cpp\_opt**](-cpp-opt.md) switch, specifying an appropriate preprocessor option that puts the line directives in the input stream of the compiler is required. For example, for the Microsoft C/C++ preprocessor the **/E** option would have to be used:

``` syntax
midl /cpp_cmd cl.exe /cpp_opt "/E" file.idl
```

The **\#line** directive is accepted by MIDL in one of the following forms:

``` syntax
#line digit-sequence "filename" new-line
 
# digit-sequence "filename" new-line
```

For a complete description of the line directive and other preprocessor directives, see the documentation for the C-compiler being used.

MIDL accepts only the line preprocessor directive. Therefore, if the [**/no\_cpp**](-no-cpp-nocpp.md) switch is used, the input file must not have other preprocessor directives, or the input file must have been processed prior to invoking MIDL.

For more information, see [Dealing with \#defines in IDL Files](dealing-with-defines-in-idl-files-2.md).

 

 




