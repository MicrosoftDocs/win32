---
title: Execution Model
description: Execution Model
ms.assetid: 1947eb24-3a55-4d30-924e-93f2eed2c7b6
keywords:
- OpenGL,execution model
- execution model OpenGL
- OpenGL,client/server model
- client/server model OpenGL
- OpenGL,network-transparent
- framebuffers,execution model
ms.topic: article
ms.date: 05/31/2018
---

# Execution Model

The model for interpretation of OpenGL commands is client/server. Application code (the client) issues commands, which are interpreted and processed by OpenGL (the server). The server may or may not operate on the same computer as the client. In this sense, OpenGL is network-transparent. A server can maintain several OpenGL contexts, each of which is an encapsulated OpenGL state. A client can connect to any one of these contexts. The required network protocol can be implemented by augmenting an already existing protocol (such as that of the X Window System) or by using an independent protocol. No OpenGL commands are provided for obtaining user input.

The window system that allocates framebuffer resources ultimately controls the effects of OpenGL commands on the framebuffer. The window system:

-   Determines which portions of the framebuffer OpenGL may access at any given time.
-   Communicates to OpenGL how those portions are structured.

Therefore, there are no OpenGL commands to configure the framebuffer or initialize OpenGL. Frame buffer configuration is done outside of OpenGL in conjunction with the window system; OpenGL initialization takes place when the window system allocates a window for OpenGL rendering.

 

 




