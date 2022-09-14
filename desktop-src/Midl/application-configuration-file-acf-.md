---
title: Application Configuration File (ACF)
description: There may be aspects of your distributed application that affect one component, but have nothing to do with another.
ms.assetid: 017d93fd-1701-4713-a786-752a7695b5a6
keywords:
- ACF MIDL
- Microsoft Interface Definition Language MIDL , described, application configuration file
- application configuration file MIDL
ms.topic: article
ms.date: 05/31/2018
---

# Application Configuration File (ACF)

There may be aspects of your distributed application that affect one component, but have nothing to do with another. For example, an object may contain a large, complex data structure and pass the contents of this data structure to another object. The exact layout of this data structure may be meaningless to the receiving application. Also, the structure may contain data types that the MIDL compiler does not recognize and cannot generate marshaling and unmarshaling code.

Client applications may share the same interface but run on different platforms; they may each need their own set of marshaling routines. Finally, individual clients may not always need the same set of functions. It is inefficient to generate stub code for functions that will never be implemented in a particular client application.

By defining these local aspects of your interface in an application configuration file (ACF), you can separate the differences between the client interfaces from their network representation, allowing the server to send and receive data in a consistent format, and making your stub code more compact and efficient.

The structure and syntax of an ACF interface definition are identical to the IDL definition:

``` syntax
[ interface-attribute-list] interface interface-name {. . .}
```

By default, the ACF interface name must match its name in the IDL definition. However, when you use the MIDL compiler option / [**acf**](-acf.md) to explicitly specify an ACF file name, the interface names do not have to match. This feature allows several interfaces to share a single ACF specification.

 

 




