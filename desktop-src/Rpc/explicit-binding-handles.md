---
title: Explicit Binding Handles
description: For maximum control over the binding process, client/server applications may use explicit binding handles.
ms.assetid: e711ce37-92f0-4e60-a126-148c27662c26
ms.topic: article
ms.date: 05/31/2018
---

# Explicit Binding Handles

For maximum control over the binding process, client/server applications may use explicit binding handles. Like implicit handles, explicit binding handles enable your client application to select a server to execute its calls. In addition, explicit binding handles enable your client/server application to create an authenticated RPC communication session. With explicit handles, your client can connect to more than one server and execute remote procedures on multiple servers. Multithreaded and asynchronous client applications can even connect to multiple servers and execute multiple remote procedures at the same time.

Your client application must pass the explicit handle as a parameter to each remote procedure call. To conform to the OSF standard, the handle should be specified as the first parameter on each remote procedure. However, the Microsoft extensions to RPC enable you to specify the binding handle in other positions. For more information, see [Microsoft RPC Binding-Handle Extensions](microsoft-rpc-binding-handle-extensions.md).

To create an explicit handle, declare the handle as a parameter to the remote operations in the IDL file. The [Hello, World example](tutorial.md) can be redefined to use an explicit handle as shown:

``` syntax
/* IDL file for explicit handles */
 
[ 
  uuid(20B309B1-015C-101A-B308-02608C4C9B53),
  version(1.0) 
]
interface hello
{
  void HelloProc([in] handle_t h1,
                 [in, string] char *  pszString); 
}
```

You can combine explicit and implicit handles in a single interface. If a function has an explicit handle in its parameter list, that handle will be used. If a function in an interface using implicit handles does not specify an explicit handle, then the default implicit handle will be used.

 

 




