---
title: Rendering Contexts
description: An OpenGL rendering context is a port through which all OpenGL commands pass. Every thread that makes OpenGL calls must have a current rendering context. Rendering contexts link OpenGL to the Windows windowing systems.
ms.assetid: '9fbbb0be-2db4-4bfc-9a5c-a43d71554abc'
keywords:
- OpenGL on Windows,rendering contexts
- rendering contexts OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Rendering Contexts

An OpenGL *rendering context* is a port through which all OpenGL commands pass. Every thread that makes OpenGL calls must have a current rendering context. Rendering contexts link OpenGL to the Windows windowing systems.

An application specifies a Windows device context when it creates a rendering context. This rendering context is suitable for drawing on the device that the specified device context references. In particular, the rendering context has the same pixel format as the device context. For more information, see [Rendering Context Functions](rendering-context-functions.md).

Despite this relationship, a rendering context is not the same as a device context. A device context contains information pertinent to the graphics component (GDI) of Windows. A rendering context contains information pertinent to OpenGL. A device context must be explicitly specified in a GDI call. A rendering context is implicit in an OpenGL call. You should set a device context's pixel format before creating a rendering context.

A thread that makes OpenGL calls must have a current rendering context. If an application makes OpenGL calls from a thread that lacks a current rendering context, nothing happens; the call has no effect. An application commonly creates a rendering context, sets it as a thread's current rendering context, and then calls OpenGL functions. When it finishes calling OpenGL functions, the application uncouples the rendering context from the thread, and then deletes the rendering context. A window can have multiple rendering contexts drawing to it at one time, but a thread can have only one current, active rendering context.

A current rendering context has an associated device context. That device context need not be the same device context as that used when the rendering context was created, but it must reference the same device and have the same pixel format.

A thread can have only one current rendering context. A rendering context can be current to only one thread.

 

 




