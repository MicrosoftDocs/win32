---
title: COM Handlers
description: The purpose of COM handlers is to provide some \ 0034;smart \ 0034; code in the client address space that can optimize calls between a client and server. Handlers can override some interfaces while delegating others directly to the server (through the proxy).
ms.assetid: 390b0228-4c52-453c-82d8-466600d23a04
ms.topic: article
ms.date: 05/31/2018
---

# COM Handlers

The purpose of COM handlers is to provide some "smart" code in the client address space that can optimize calls between a client and server. Handlers can override some interfaces while delegating others directly to the server (through the proxy).

There are two types of COM handlers:

-   [The OLE handler](the-ole-handler.md) is a heavyweight DLL that provides important services for linking and embedding. It is usually created before the server is launched and is initialized so that the server is activated when the embedded object enters the running state.
-   [The lightweight client-side handler](the-lightweight-client-side-handler.md) can be created for any purpose, can be very small, and cannot be created before the server.

 

 




