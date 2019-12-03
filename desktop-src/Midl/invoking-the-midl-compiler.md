---
title: Invoking the MIDL Compiler
description: The MIDL compiler can generate code for different platforms and system releases. Consult the /target switch to learn more about suggested switches and how to generate code optimized for a particular release.
ms.assetid: 57730efa-71c3-4746-83f4-c7e327888efc
keywords:
- MIDL compiler MIDL , invoking
ms.topic: article
ms.date: 05/31/2018
---

# Invoking the MIDL Compiler

The MIDL compiler can generate code for different platforms and system releases. Consult the [**/target**](-target.md) switch to learn more about suggested switches and how to generate code optimized for a particular release.

Run the MIDL compiler from the command line using the following command:

**midl** *<***options***>* **filename.idl**

where *<***options***>* represents the command-line options you want to use, and Filename.idl is the name of the MIDL file to compile.

A complete listing of MIDL compiler switches and options is available when you use the MIDL compiler [**/help**](-help-.md) and /? switches. The switches are organized by categories. For details, see the [MIDL Command-Line Reference](midl-command-line-reference.md).

> [!NOTE]
> The new global flag **$(MIDL\_OPTIMIZATION)** exists in win32.mak. When an .idl file is compiled using this flag, the generated stub can utilize the latest RPC features available on the specified platform, and potentially improve the application's performance and stability. It's recommended that applications use this flag when using MIDL.
>
> **midl** **$(MIDL\_OPTIMIZATION)** **...**