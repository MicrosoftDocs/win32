---
title: Tutorial
description: This tutorial takes you through the steps required to create a simple, single-client, single-server distributed application from an existing standalone application.
ms.assetid: afdfa037-58c0-4dcf-aa27-6839db0515e6
keywords:
- Remote Procedure Call RPC , tutorial
ms.topic: article
ms.date: 05/31/2018
---

# Tutorial

This tutorial takes you through the steps required to create a simple, single-client, single-server distributed application from an existing standalone application. These steps are:

-   Create interface definition and application configuration files.
-   Use the MIDL compiler to generate C-language client and server stubs and headers from those files.
-   Write a client application that manages its connection to the server.
-   Write a server application that contains the actual remote procedures.
-   Compile and link these files to the RPC run-time library to produce the distributed application.

The client application passes a character string to the server in a remote procedure call, and the server prints the string "Hello, World" to its standard output.

The complete source files for this example application, with additional code to handle command-line input and to output various status messages to the user, are in the RPC\\Hello directory of the Platform Software Development Kit (SDK).

This section presents its discussion in the following topics:

-   [The Standalone Application](the-standalone-application.md)
-   [Defining the Interface](defining-the-interface.md)
-   [Generating the UUID](generating-the-uuid.md)
-   [The IDL File](the-idl-file.md)
-   [The ACF File](the-acf-file.md)
-   [Generating the Stub Files](generating-the-stub-files.md)
-   [The Client Application](the-client-application.md)
-   [The Server Application](the-server-application.md)
-   [Stopping the Server Application](stopping-the-server-application.md)
-   [Compiling and Linking](compiling-and-linking.md)
-   [Running the Application](running-the-application.md)

 

 




