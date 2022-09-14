---
title: DLL Surrogates
description: DLL Surrogates
ms.assetid: fe30c0ae-1d19-4a5f-8ee3-8a5337c79c44
ms.topic: article
ms.date: 05/31/2018
---

# DLL Surrogates

COM makes it possible to create DLL servers that can be loaded into a surrogate EXE process. This combines the ease of writing DLL servers with the benefits of executable implementation. Development tools like Microsoft Visual Studio facilitate the writing of DLL servers, but a DLL server in itself has limits. Running the DLL server in a surrogate process offers several possible benefits:

-   Fault isolation and the ability to service multiple clients simultaneously.
-   In a distributed environment, a DLL server implementation could be used to service remote clients.
-   It could permit clients to help protect themselves from untrusted server code while allowing them access to the services the DLL server provides.
-   Running a DLL server in a surrogate provides the DLL with the surrogate's security.

COM provides a default surrogate process, or you can write a custom surrogate if you have special needs.

The following topics provide more information on DLL surrogates:

-   [DLL Server Requirements](dll-server-requirements.md)
-   [Using the System-Supplied Surrogate](using-the-system-supplied-surrogate.md)
-   [Writing a Custom Surrogate](writing-a-custom-surrogate.md)

 

 




