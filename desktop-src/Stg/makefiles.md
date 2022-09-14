---
title: Makefiles
description: The makefiles for each of the code samples in this series are generic Microsoft Win32 makefiles and are meant to be built from the Command Prompt window.
ms.assetid: f9944069-b536-4ae2-8411-f02c3a78978c
keywords:
- Makefiles Structured Storage
ms.topic: article
ms.date: 05/31/2018
---

# Makefiles

The makefiles for each of the code samples in this series are generic Microsoft Win32 makefiles and are meant to be built from the Command Prompt window. They assume Microsoft compiler and linker tools and will probably require some modification to work with other tools. Most compiler/linker command line switches are specified by macros defined in the Win32.mak makefile include file included with the Platform Software Development Kit (SDK).

The Makeall.bat file, and each respective code sample makefile, support common options, listed in the following table, for invocation from the Command Prompt window to control the nature of the build.



| Nmake invocation        | Makeall invocation          | Effect                       |
|-------------------------|-----------------------------|------------------------------|
| **nmake**               | **makeall**                 | Compile with debug info.     |
| **nmake** **nodebug=1** | **makeall** **"nodebug=1"** | Compile without debug info.  |
| **nmake** **profile=1** | **makeall** **"profile=1"** | Compile with profiling info. |
| **nmake** **tune=1**    | **makeall** **"tune=1"**    | With working set tuner info. |
| **nmake** **unicode=1** | **makeall** **"unicode=1"** | Compile for Unicode.         |
| **nmake** **clean**     | **makeall** **clean**       | Delete temporary binaries.   |
| **nmake** **cleanall**  | **makeall** **cleanall**    | Delete all generated files.  |



 

For the Makeall.bat invocations you must have the quotes as shown. The **nodebug**, **profile**, and **tune** options are mutually exclusive: you may use only one of them, or none, for a given compilation/link. To compile the samples to run with Unicode strings, use the **"unicode=1"** option. The default is to compile for the traditional ANSI string support, because you can then run on any 32-bit Windows operating system. You can freely compile and run with or without Unicode on Windows Server 2003 and later, and Windows 2000 and later. Be aware that APPUTIL is always compiled with the same options as the other code samples you may be separately compiling. This is especially true for the **"unicode=1"** option.

You may use an installed 32-bit C++ integrated development environment (IDE) to build the samples using the generic makefiles provided. To do so requires that within your IDE you handle the generic makefiles as 'external' makefiles. The makefiles provided require a Microsoft NMAKE-compatible make utility.

Most C++ IDEs can recognize these makefiles as external and yet still provide many edit-build-debug benefits of the IDE. For example, in Microsoft Visual Studio 97 or later, you can use the File menu Open Workspace choice to produce a workspace by opening an appropriately named copy (for example, Exeskel.mak) of the code sample Win32 makefile.

 

 




