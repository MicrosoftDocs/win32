---
title: The Header Files
description: The interface header file (Name.h) contains type definitions and function declarations based on the interface definition in the current IDL file, as well as all the data types and operations declared in the files included with the \ include directive.
ms.assetid: 81fac1fa-6bd7-4a3e-8aa6-5104d4b25b55
keywords:
- header files MIDL
ms.topic: article
ms.date: 05/31/2018
---

# The Header Files

The interface header file (Name.h) contains type definitions and function declarations based on the interface definition in the current IDL file, as well as all the data types and operations declared in the files included with the \#include directive. Data types from the files imported with the import directive are not replicated to the header file; instead, the generated header file contains an include line to the H file generated from the imported file.

Include this file in the source files for the proxy DLL and for client applications that use the interface.

The default name for a header file generated from a file.idl is File.h. The [**/header**](-header.md) MIDL compiler switch overrides the default name of the interface header file.

 

 




