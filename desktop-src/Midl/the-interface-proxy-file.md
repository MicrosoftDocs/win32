---
title: The Interface Proxy File
description: The interface proxy file (U\_p.c) is a C file that contains routines equivalent to those in the client stub and server stub files of an object (COM) interface.
ms.assetid: f85f7384-a590-4146-9705-2e87f1a0a87a
keywords:
- MIDL and COM MIDL , interfaces, proxy files
ms.topic: article
ms.date: 05/31/2018
---

# The Interface Proxy File

The interface proxy file (U\_p.c) is a C file that contains routines equivalent to those in the client stub and server stub files of an object (COM) interface. This file contains implementations of the surrogate routines for client and server in the inline mode of the compiler or equivalent data and thunks in the interpreted modes, as well as other appropriate COM glue data, such as the proxy and stub Vtables.

The interface proxy file includes the supporting routines and data only for methods of the interfaces defined in the current IDL file. To clarify this behavior, an extended example is used throughout this section. When compiling an IDL file with an interface such as IFaceB that inherits from IFaceA, IFaceB related auxiliary data and routines are generated to the current proxy file, while the base interface IFaceA related auxiliary data and routines are found in the proxy generated from the IDL file containing the IFaceA definition. The compiler generates all data necessary to identify the surrogates of the base interface, and to delegate to them when needed to support the IFaceA methods used through IFaceB interface.

For every method in an interface in the current IDL file, the proxy file contains the following two surrogate methods when compiled in the mixed mode ([/Os](-os.md)), and equivalent interpreter data when compiled in the interpreter mode ([/Oi](-oi.md)).

-   The client-side surrogate, such as IFaceB\_Method\_Proxy in this example.

    This client-side surrogate is the virtual entry point to which the client, for example IFaceB::Method, dispatches. It marshals the input arguments into a transmittable form, transmits the marshaled arguments along with information that identifies the interface and the operation, and then unmarshals the return value and any output arguments when the invoked operation returns.

-   The server-side surrogate, for example, IFaceB\_Method\_Stub .

    This server-side surrogate is the virtual entry point that the underlying runtime dispatches to at the server to emulate the client. It unmarshals the input arguments to replicate the client data, invokes the server's implementation of the interface function, and then marshals and transmits the return value and any output arguments back to the client side.

The default name for a proxy file generated from a file.idl is file\_p.c.Use the [**/proxy**](-proxy.md) MIDL compiler switch to override the default name of the interface proxy file. The [**/env**](-env.md) and [**/out**](-out.md) switches affect this file.

 

 




