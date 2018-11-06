---
title: Multithread OpenGL Drawing Strategies
description: The GDI does not support multiple threads.
ms.assetid: 3930029d-b2d9-4beb-bad6-4962f952d7ee
keywords:
- OpenGL on Windows,multithread drawing
- multithread OpenGL drawing OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Multithread OpenGL Drawing Strategies

The GDI does not support multiple threads. You must use a distinct device context and a distinct rendering context for each thread. This tends to limit the performance advantages of using multiple threads with single-processor systems running OpenGL applications. However, there are ways to use threads with a single processor system to greatly increase performance. For example, you can use a separate thread to pass OpenGL rendering calls to dedicated 3-D hardware.

Symmetric multiprocessing (SMP) systems can greatly benefit from using multiple threads. An obvious strategy is to use a separate thread for each processor to handle OpenGL rendering in separate windows. For example, in a flight-simulation application you could use separate processors and threads to render the front, back, and side views.

A thread can have only one current, active rendering context. When you use multiple threads and multiple rendering contexts, you must be careful to synchronize their use. For example, use one thread only to call [**SwapBuffers**](/windows/desktop/api/wingdi/nf-wingdi-swapbuffers) after all threads finish drawing.

 

 




