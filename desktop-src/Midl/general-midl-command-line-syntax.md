---
title: General MIDL Command-line Syntax
description: The MIDL compiler processes an IDL file and an optional application configuration file (ACF) to generate a set of output files.
ms.assetid: 1906b374-d0d1-4ec8-9a00-c5228b4c29ca
keywords:
- command-line reference MIDL , general syntax
ms.topic: article
ms.date: 05/31/2018
---

# General MIDL Command-line Syntax

The MIDL compiler processes an IDL file and an optional application configuration file (ACF) to generate a set of output files. The attributes specified in the IDL file's interface attribute list determine whether the compiler generates source files for an RPC interface or for a custom OLE interface.

## Switch Options

``` syntax
     midl [command-line-switch [switch-options]] filename
    
```

<dl> <dt>

<span id="command-line-switch"></span><span id="COMMAND-LINE-SWITCH"></span>*command-line-switch*
</dt> <dd>

Specifies MIDL compiler command-line switches. Switches can appear in any sequence.

</dd> <dt>

<span id="switch-options"></span><span id="SWITCH-OPTIONS"></span>*switch-options*
</dt> <dd>

Specifies options associated with each switch. Valid options are described in the reference entry for each MIDL compiler switch.

</dd> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

Specifies the name of the IDL file. This file usually has the extension .idl, but it can have another or none.

</dd> </dl>

## Remarks

The following lists show the default names of the files generated for an IDL file named Name.idl. You can use command-line switches to override these default names. Note that the name of the IDL file can have an extension other than .idl, or no extension at all.

By default (that is, if the interface attribute list does not contain the [**object**](object.md) or [**local**](local.md) attribute), the compiler generates the following files for an [RPC interface](files-generated-for-an-rpc-interface.md):

-   Client stub (name\_c.c)
-   Server stub (name\_s.c)
-   Header file (name.h)

When the [**object**](object.md) attribute appears in the interface attribute list, the compiler generates the following files for a COM interface:

-   Interface proxy file (name\_p.c)
-   Interface header file (name.h)
-   Interface UUID file (name\_I.c)

When the [**local**](local.md) attribute appears in the interface attribute list, the compiler generates only the interface header file, Name.h.

The MIDL compiler provided with Microsoft RPC invokes the C preprocessor as needed to process the IDL file. It does not automatically invoke the C compiler to compile generated files.

> [!Note]  
> The MIDL compiler provided with Microsoft RPC uses a different command-line syntax than the DCE IDL compiler.

 

The MIDL compiler switches [**/env**](-env.md), [**/server**](-server.md), [**/sstub**](-sstub.md), and [**/out**](-out.md) affect the server stub file.

Starting with MIDL version 6.0.359, the default command line option for the MIDL compiler is [**/Oicf**](-oi.md)Â [**/robust**](-robust.md). To disable /robust, specify the [**/no\_robust**](-no-robust.md) option.

## The Header File

The header file contains definitions of all the data types and operations declared in the IDL file. The header file must be included by all application modules that call the defined operations, implement the defined operations, or manipulate the defined types.

The MIDL compiler switches [**/header**](-header.md) and [**/out**](-out.md) affect the header file.

 

 




