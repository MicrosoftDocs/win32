---
description: Although this mechanism is sufficient for simple applications, it cannot support the complex message-dispatching requirements of more advanced applications such as those using the Multiple Document Interface (MDI) model.
ms.assetid: e4558e71-bbec-415a-a7c2-9025a4d6c474
title: Blocking Hook
ms.topic: article
ms.date: 05/31/2018
---

# Blocking Hook

Although this mechanism is sufficient for simple applications, it cannot support the complex message-dispatching requirements of more advanced applications such as those using the Multiple Document Interface (MDI) model. For such applications, a thread-specific blocking hook may be installed by the application. This will be called by the service provider instead of the default blocking hook described in the preceding. A service provider must retrieve a pointer to the per-thread blocking hook from the Ws2\_32.dll by calling [**WPUQueryBlockingCallback**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpuqueryblockingcallback). If the application has not installed its own blocking hook a pointer to the default blocking hook function will be returned.

A Windows Sockets service provider cannot assume that an application-supplied blocking hook allows message processing to continue as the default blocking hook does. Some applications cannot tolerate the possibility of reentrant messages while a blocking operation is outstanding. Such an application's blocking hook function would simply return **FALSE**. If a service provider depends on messages for its internal operation, it may execute **PeekMessage**(hMyWnd...) before executing the application's blocking hook so that it can get its own messages without affecting the rest of the system.

There is no default blocking hook installed in preemptive multithreaded versions of Windows. This is because other processes will not be blocked if a single application is waiting for an operation to complete (and hence not calling **PeekMessage** or **GetMessage** which causes the application to yield the processor in nonpreemptive Windows). When the service provider calls [**WPUQueryBlockingCallback**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpuqueryblockingcallback) a null pointer will be returned indicating that the provider is to use native operating system blocking functions. However, in order to preserve backward compatibility, an application-supplied blocking hook can still be installed on a per-thread basis in Windows.

The Winsock service provider calls the blocking hook only if all of the following are true: the routine is one which is defined as being able to block, the specified socket is a blocking socket, and the request cannot be completed immediately. If only nonblocking sockets and [**WSPAsyncSelect**](/previous-versions/windows/desktop/legacy/ms742267(v=vs.85))/[**WSPEventSelect**](/previous-versions/windows/hardware/network/ff566287(v=vs.85)) instead of [**WSPSelect**](/previous-versions/windows/desktop/legacy/ms742289(v=vs.85)) are used, then the blocking hook will never be called.

> [!Note]  
> If, during the time pseudoblocking is being used to block a thread, a Windows message is received for the thread, there is a risk that the thread will attempt to issue another Winsock call. Because of the difficulty of managing this condition safely, the Windows Sockets 1.1 specification disallowed this behavior. It is not permissible for a given thread to make multiple, nested Winsock function calls. Only one outstanding function call is allowed for a particular thread. Any nested Winsock function calls fail with the error WSAEINPROGRESS. It should be emphasized that this restriction applies to both blocking and nonblocking operations, but only in Windows Sockets 1.1 environments. There are a few exceptions to this rule, including two functions that allow an application to determine whether a pseudoblocking operation is in fact in progress, and to cancel such an operation if need be. These are described in the following.

 

 

 
