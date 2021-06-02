---
description: Troubleshooting Tips
ms.assetid: e87ad3bd-07ae-4b9d-b465-2ce4688bdd83
title: Troubleshooting Tips
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting Tips

This following tips will help you to avoid deadlocks or crashes in your DirectShow application.

**Global Objects**

A global C++ object should not create DirectShow objects in its constructor method or release them in its destructor method. Doing so can cause the application to block indefinitely, for the following reason:

Threads cannot exit while inside a DLL's entry-point function. Kernel 32 holds a global process lock during the entry-point function, and the lock prevents the thread from exiting. Because some DirectShow objects own threads, they can block if released from inside a DLL entry-point function. If an application has a global C++ object, the C runtime DLL calls the object's destructor when the DLL is unloaded. If the destructor releases DirectShow objects, it can block as a result.

For similar reasons, a DLL should not create or release DirectShow objects in its entry point routine.

**Releasing Interfaces**

You should release all DirectShow interface pointers while your application is still processing messages, before it exits the message loop. Otherwise, you might see various asserts, because some DirectShow objects send messages during their clean-up routines.

(As a corollary, if you are using the ATL **CWindowImpl** class, do not wait until **OnFinalMessage** to free the interfaces. Instead, free them when you handle the WM\_CLOSE message.)

**Reference Counts**

When the debug version of Quartz.dll unloads, it checks whether any DirectShow objects have reference counts that were not released. If so, it throws an assertion:


```C++
g_cFGObjects == 0 
```



When this assertion fails, it means your application has leaked a reference count. Review your code and make sure that you release all interface pointers.

## Related topics

<dl> <dt>

[Debugging in DirectShow](debugging-in-directshow.md)
</dt> </dl>

 

 



