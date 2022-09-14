---
title: Files Generated for a COM Interface
description: For COM interfaces, the MIDL compiler combines all client and object server auxiliary routines and data into a single interface proxy file.
ms.assetid: 13063ee8-cb41-48a7-b90b-ea08c19c5230
keywords:
- MIDL compiler MIDL , MIDL and COM
- COM MIDL
ms.topic: article
ms.date: 05/31/2018
---

# Files Generated for a COM Interface

For COM interfaces, the MIDL compiler combines all client and object server auxiliary routines and data into a single interface proxy file. This file includes the surrogate entry points for both clients and servers. In addition, the MIDL compiler generates an interface header file, an interface UUID file and an interface registration file. You will use all these files when creating a proxy DLL that contains the code to support the use of the interface by both client applications and object servers. You will also use the interface header file and the interface UUID file when creating the executable file for a client application that uses the interface.

The following topics describe each of the files generated for a custom COM interface, which you identify by including the **\[**[**object**](object.md)**\]** attribute in the interface attribute list of the IDL file:

-   [The Interface Proxy File](the-interface-proxy-file.md)
-   [The Header Files](the-header-files.md)
-   [The Interface UUID File](the-interface-uuid-file.md)
-   [The Interface Registration File](the-interface-registration-file.md)

For more information, see [Application Configuration File (ACF)](application-configuration-file-acf-.md), [**/app\_config**](-app-config.md), [Interface Definition (IDL) File](interface-definition-idl-file.md), and [Building and Registering a Proxy DLL](../com/building-and-registering-a-proxy-dll.md).

 

 