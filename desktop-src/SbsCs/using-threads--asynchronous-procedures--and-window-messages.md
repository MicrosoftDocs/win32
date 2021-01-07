---
description: Activation contexts are visible throughout the entire process.
ms.assetid: 6eda00d5-9dac-4267-bf61-b481814201f8
title: Threads, Asynchronous Procedures, and Window Messages
ms.topic: article
ms.date: 05/31/2018
---

# Using Threads, Asynchronous Procedures, and Window Messages

Activation contexts are visible throughout the entire process. The activation context stacks are however per-thread, and two threads in the same process can have different activation stacks. [**CreateThread**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createthread) automatically puts the current activation context at the top of the new thread's activation stack. This can facilitate upgrading existing code to use side-by-side components because the new thread can run immediately in the current activation context.

Asynchronous procedure calls, completion port callbacks, and any other callbacks on other threads automatically get the activation context of the source. When the callback is called, the activation stack is cleaned up. This means that your application can use asynchronous procedure calls and callbacks without explicitly activating any contexts because context management will be done by the underlying side-by-side infrastructure. To make other contexts active during a callback or new thread, your application can do its own context management. In this case your program must use the proper sequence of activation context activate functions and deactivate functions.

Activation contexts are thread-neutral. Activating a context only changes the current thread's stack, and you cannot activate a context across threads. Thread A cannot force a context onto thread B. The functions of the activation context API are also threading-aware.

When you use [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) or [**PostMessage**](/windows/win32/api/winuser/nf-winuser-postmessagea) to send a window message to another window procedure in your process, the current activation context is activated before the message is passed on to the target procedure. The current activation context goes along with the message. This ensures that messages that refer to COM objects, DLL names, or other side-by-side resources retain their correct context information.

 

 
