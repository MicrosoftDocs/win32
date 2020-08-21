---
title: The IDL File
description: The IDL file consists of one or more interface definitions, each of which has a header and a body.
ms.assetid: 64a30a12-a53e-4c53-b8cf-7af85ffd0a94
ms.topic: article
ms.date: 05/31/2018
---

# The IDL File

The IDL file consists of one or more interface definitions, each of which has a header and a body. The header contains information that applies to the entire interface, such as the UUID. This information is enclosed in square brackets and is followed by the keyword **interface** and the interface name. The body contains C-style data type definitions and function prototypes, augmented with attributes that describe how the data is transmitted over the network.

In this example, the interface header contains only the UUID and the version number. The version number ensures that when there are multiple versions of an RPC interface, only compatible versions of the client and server will be connected.

The interface body contains the function prototype for **HelloProc**. In this prototype, the function parameter pszString has the attributes **\[**[**in**](/windows/desktop/Midl/in)**\]** and **\[**[**string**](/windows/desktop/Midl/string)**\]**. The **\[in\]** attribute tells the run-time library that the parameter is passed only from the client to the server. The **\[string\]** attribute specifies that the stub should treat the parameter as a C-style character string.

The client application should be able to shut down the server application, so the interface contains a prototype for another remote function,**Shutdown** , that will be implemented later in this tutorial.

``` syntax
//file hello.idl
[
    uuid(7a98c250-6808-11cf-b73b-00aa00b677a7),
    version(1.0)
]
interface hello
{
    void HelloProc([in, string] unsigned char * pszString);
    void Shutdown(void);
}
```

 

 