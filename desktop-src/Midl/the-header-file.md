---
title: The Header File
description: The header file contains definitions of all data types and operations declared in the IDL file, as well as all data types and operations declared in the files included with the \ include directive.
ms.assetid: 51789b42-e01c-4233-97da-5e0a044f596f
keywords:
- MIDL and RPC MIDL , interfaces, header file
ms.topic: article
ms.date: 05/31/2018
---

# The Header File

The header file contains definitions of all data types and operations declared in the IDL file, as well as all data types and operations declared in the files included with the \#include directive. Data types from the files imported with the import directive are not replicated to the header file; instead the generated header file contains an include line to the H file generated from the imported file. The header file must be included by all application modules that call the defined operations, implement the defined operations, or manipulate the defined types.

The MIDL compiler switches [**/header**](-header.md) and [**/out**](-out.md) affect the header file.

 

 




