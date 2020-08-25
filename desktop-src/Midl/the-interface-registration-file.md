---
title: The Interface Registration File
description: The interface registration file collects information that helps in the registration of COM interfaces packaged into a DLL or EXE file.
ms.assetid: 203303dc-121e-4bf4-b648-a35b956a56ee
keywords:
- interface registration file MIDL
ms.topic: article
ms.date: 05/31/2018
---

# The Interface Registration File

The interface registration file collects information that helps in the registration of COM interfaces packaged into a DLL or EXE file. The interface registration file is different from other generated files because it can gather information from compiling several different IDL files. Each MIDL compiler run for COM interfaces looks for an existing dlldata.c file first, and if the file is not found, a new dlldata.c file is created. If a dlldata.c file is found, information about the current IDL is added (if absent) or replaced.

The interface registration file is safely generated or updated in a multiprocessor environment because parallel MIDL compiles are prevented from writing to the file at the same time. Because any dlldata.c file can be marked as read-only by either the build environment or the user, the MIDL compiler implements a timeout approach to waiting on a file it cannot open, and issues an appropriate error message if the timeout expires.

The default name for the interface registration file generated from an input file is dlldata.c. The [**/dlldata**](-dlldata.md) MIDL compiler switch can be used to override the default name of the file. Overriding the default name of the interface registration file is especially useful when some IDL files packaged to a common binary reside in different directories.

## Related topics

<dl> <dt>

[Building and Registering a Proxy DLL](../com/building-and-registering-a-proxy-dll.md)
</dt> </dl>

 

 