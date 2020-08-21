---
title: Using New Data Types in Your IDL File
description: The Basetsd.h header file defines the new data types needed for writing applications that run on both 32- and 64-bit Windows.
ms.assetid: 99a3904b-9120-4d1d-bd8c-1eb299bd6b27
keywords:
- Basetsd.h header file 64-bit Windows Programming
- data types in IDL file 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Using New Data Types in Your IDL File

The Basetsd.h header file defines the new data types needed for writing applications that run on both 32- and 64-bit Windows. To use these data types in your interfaces, import Basetsd.h into your IDL file. Do not \#include the file or you will end up with multiple definitions at compile time.

Alternatively, you can include or import the Basetsd.idl file into your IDL file.

For more information on adding system header files to your IDL file, see [Importing Files and Type Libraries](/windows/desktop/Midl/importing-files-and-type-libraries) and [Importing System Header Files](/windows/desktop/Midl/importing-system-header-files).

 

 