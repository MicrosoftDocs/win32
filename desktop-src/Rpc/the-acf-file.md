---
title: The ACF File
description: The ACF file enables you to customize your client and/or server applications' RPC interface without affecting the network characteristics of the interface.
ms.assetid: 7d3fef5c-b645-4e10-b08d-b339025718b4
ms.topic: article
ms.date: 05/31/2018
---

# The ACF File

The ACF file enables you to customize your client and/or server applications' RPC interface without affecting the network characteristics of the interface. For example, if your client application contains a complex data structure that only has meaning on the local machine, you can specify in the ACF file how the data in that structure can be represented in a machine-independent form for remote procedure calls.

This tutorial demonstrates another use of the ACF file—specifying the type of binding handle that represents the connection between client and server. The **\[**[**implicit\_handle**](/windows/desktop/Midl/implicit-handle)**\]** attribute in the ACF header allows the client application to select a server for its remote procedure call. The ACF defines the handle to be of the type [**handle\_t**](/windows/desktop/Midl/handle-t) (a MIDL primitive data type). The MIDL compiler will put the binding handle name that the ACF specified, hello\_IfHandle into the header file it generates. Notice that this particular ACF file has an empty body.

``` syntax
//file: hello.acf
[
    implicit_handle (handle_t hello_IfHandle)
] 
interface hello
{
}
```

The MIDL compiler has an option, [**/app\_config**](/windows/desktop/Midl/-app-config), that lets you include certain ACF attributes, such as **implicit\_handle**, in the IDL file, rather than creating a separate ACF file. Consider using this option if your application doesn't require a lot of special configuration and if strict OSF compatibility is not an issue.

 

 