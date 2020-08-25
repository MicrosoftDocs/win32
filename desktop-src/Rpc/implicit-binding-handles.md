---
title: Implicit Binding Handles
description: Implicit binding handles allow your application to select a specific server to execute its remote procedure calls.
ms.assetid: cf4e179b-8d97-4597-89e6-c8967b9db6c7
ms.topic: article
ms.date: 05/31/2018
---

# Implicit Binding Handles

Implicit binding handles allow your application to select a specific server to execute its remote procedure calls. For details, see [Client-Side Binding](client-side-binding.md). They also enable your client/server program to use authenticated bindings. That is, the client can specify authentication information in an implicit binding handle. The RPC run-time library uses the authentication information to establish an authenticated RPC session between the client and the server. For more information, see [Security](security.md).

> [!Note]  
> Implicit binding handles are not thread safe. Multi-threaded applications therefore should avoid using implicit binding handles.

 

When your application uses implicit bindings, the client must set the binding information so that it can create the binding. After the client creates an implicit binding, it does not need to pass any binding handles to remote procedures. The RPC library handles the rest of the mechanics of the communication session.

The client stores the binding information for an implicit handle in a global variable. When the MIDL compiler generates the client stub and header file from the interface specification in your MIDL file, it also generates code for a global binding handle variable. Your client program initializes the handle and then does not refer to it again until it destroys the binding.

You create an implicit handle by specifying the \[[**implicit\_handle**](/windows/desktop/Midl/implicit-handle)\] attribute in the ACF for an interface as follows:

``` syntax
/* ACF file (complete) */
 
[
  implicit_handle(handle_t hHello)
]
interface hello
{
}
```

The **handle\_t** type, which is used in the preceding example, is a MIDL data type used for defining binding handles.

After creating the implicit handle, the application needs to use it as a parameter to the RPC run-time library functions. Do not use the implicit handle as a parameter to remote procedure calls. The following code sample demonstrates the use of implicit binding handles.

``` syntax
RPC_STATUS status;
status = RpcBindingFromStringBinding(
            pszStringBinding,
            &hHello);
 
status = MyRemoteProcedure();
 
status = RpcBindingFree(hHello);
...
```

In the preceding example, the RPC run-time library functions [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding) and [**RpcBindingFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfree) both required the implicit binding handle to be passed in their parameter lists. However, the remote procedure MyRemoteProcedure did not, since it is not an RPC run-time library function.

 

 