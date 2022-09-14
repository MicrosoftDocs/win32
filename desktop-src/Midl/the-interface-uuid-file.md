---
title: The Interface UUID File
description: The interface UUID file collects the definitions of the interface identifiers from all interfaces in the processed IDL file.
ms.assetid: 8e7198e9-8166-426d-a6cc-e9a0a798811b
keywords:
- MIDL and COM MIDL , interfaces, proxy UUID files
- interface UUID file MIDL
ms.topic: article
ms.date: 05/31/2018
---

# The Interface UUID File

The interface UUID file collects the definitions of the interface identifiers from all interfaces in the processed IDL file. Similar to the stub file and the header file, the input stream closure is defined by the current IDL file and the included files. For example, for Interface IFace, the compiler generates a constant IID\_IFace and initializes it to the interface's UUID specified in the IDL file. Client applications and the proxy DLL use this constant to identify the interface.

The default name for an interface IID file generated from a file.idl is File\_i.c. The [**/iid**](-iid.md) MIDL compiler switch overrides the default name of the interface UUID file.

 

 




