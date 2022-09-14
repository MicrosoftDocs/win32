---
title: RPC Components
description: Remote Procedure Call (RPC) components.
ms.assetid: 7caaf01a-7f20-470f-afcf-478146cae5eb
keywords:
- Remote Procedure Call RPC , described, components
ms.topic: article
ms.date: 05/31/2018
---

# RPC Components

RPC includes the following major components:

-   MIDL compiler
-   Run-time libraries and header files
-   Name service provider (sometimes referred to as the Locator)
-   Endpoint mapper (sometimes referred to as the port mapper)

In the RPC model, you can formally specify an interface to the remote procedures using a language designed for this purpose. This language is called the Interface Definition Language, or IDL. The Microsoft implementation of this language is called the Microsoft Interface Definition Language, or MIDL.

After you create an interface, you must pass it through the MIDL compiler. This compiler generates the stubs that translate local procedure calls into remote procedure calls. Stubs are placeholder functions that make the calls to the run-time library functions, which manage the remote procedure call. The advantage of this approach is that the network becomes almost completely transparent to your distributed application. Your client program calls what appear to be local procedures; the work of turning them into remote calls is done for you automatically. All the code that translates data, accesses the network, and retrieves results is generated for you by the MIDL compiler and is invisible to your application.

 

 




