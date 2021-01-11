---
description: Any thread can create a window.
ms.assetid: 27f04f9f-52d9-46d6-8e06-9b032682b7c7
title: Creating Windows in Threads
ms.topic: article
ms.date: 05/31/2018
---

# Creating Windows in Threads

Any thread can create a window. The thread that creates the window owns the window and its associated message queue. Therefore, the thread must provide a message loop to process the messages in its message queue. In addition, you must use [**MsgWaitForMultipleObjects**](/windows/desktop/api/winuser/nf-winuser-msgwaitformultipleobjects) or [**MsgWaitForMultipleObjectsEx**](/windows/desktop/api/winuser/nf-winuser-msgwaitformultipleobjectsex) in that thread, rather than the other [wait functions](/windows/desktop/Sync/wait-functions), so that it can process messages. Otherwise, the system can become deadlocked when the thread is sent a message while it is waiting.

The [**AttachThreadInput**](/windows/desktop/api/Winuser/nf-winuser-attachthreadinput) function can be used to allow a set of threads to share the same input state. By sharing input state, the threads share their concept of the active window. By doing this, one thread can always activate another thread's window. This function is also useful for sharing focus state, mouse capture state, keyboard state, and window Z-order state among windows created by different threads whose input state is shared.

For information about creating windows, see [Windows Classes](../winmsg/window-classes.md).

 

 
