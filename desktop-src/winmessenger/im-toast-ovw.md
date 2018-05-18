---
title: Coordinating Toast Pop-ups Between Multiple Clients
description: This topic provides basic information about coordinating Toast Pop-ups between multiple clients.
ms.assetid: '356da025-c7e7-422e-b290-4109ac1bbe6b'
keywords: ["Windows Messenger,toast pop-ups", "Messenger client,toasts", "Messenger service,toasts", "toasts", "Messenger toasts", "toast collision", "mutex", "ToastSemaphore mutex", "Messenger toast"]
---

# Coordinating Toast Pop-ups Between Multiple Clients

This topic provides basic information about coordinating Toast Pop-ups between multiple clients.Windows Messenger provides a feature that displays small pop-up messages on the user's desktop, along with an accompanying audio cue. A pop-up message displayed by the Messenger client is referred to as a *toast*.

The topic contains the following sections.

-   [Introduction](#introduction)
-   [Functionality and Use of the ToastSemaphore Mutex](#functionality-and-use-of-the-toastsemaphore-mutex)
-   [Related topics](#related-topics)

## Introduction

An example of a Messenger toast is the message that appears on a user's desktop when one of the user's contacts signs in. Another example of Messenger toasts is the messages displayed when a user receives an alert from the .NET Alerts service. The following are examples of typical toasts:

![sign-in toast](graphics/sign-in-toast.png)

![alert toast](graphics/alert-toast.png)

In certain situations, different applications might attempt to draw toasts on the desktop simultaneously. If there is no control over how this happens, toasts might inadvertently overlap or hide each other, resulting in a poor and confusing user experience. Undesirable and unintended overlapping of toasts is referred to as a *toast collision*. Toast collisions can happen when a non-Microsoft application that renders toast-like messages on the user's desktop is running at the same time as the Messenger client.

To avoid toast collisions, current versions of the Messenger clients make use of a mutex to ensure that only one client is drawing toasts at a time. A *mutex* is a shared synchronization object, provided by the operating system, that can be used to avoid collisions when different threads or processes need to access a single shared resource. No more than one thread can be in possession of the mutex at a time. For more information, see the MSDN topic [Mutex Objects](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/mutex_objects.asp). The mutex that is used by the Messenger clients is referred to as the *ToastSemaphore mutex*.

If you are a developer who implements toast-like functionality in one of your products, you are encouraged to use the ToastSemaphore mutex to avoid toast collisions.

## Functionality and Use of the ToastSemaphore Mutex

Before the Messenger client displays a toast, the client attempts to acquire the ToastSemaphore mutex from the operating system. If the mutex is successfully acquired, the client draws the toast on the desktop. After the toast disappears (which usually takes about 10 seconds, but can be longer if the toast has the input focus), the client releases the mutex.

If the Messenger client is unable to acquire the mutex because it is being held by another application, the client will wait for up to 60 seconds for the mutex to become available. If the client is unable to acquire the toast within 60 seconds, it will proceed with its toast drawing operation.

**To use the ToastSemaphore mutex in your own application:**

1.  **Get a handle to the mutex.** When your application needs to draw a toast on the desktop, first acquire a handle to the ToastSemaphore mutex by calling the Windows Software Development Kit (SDK) function, [CreateMutex](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/createmutex.asp). The [CreateMutex](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/createmutex.asp) function takes three parameters. The first parameter specifies a security descriptor for the mutex: set this parameter to **NULL** to use the default security descriptor. The second parameter controls ownership of the mutex: set this parameter to **FALSE** so that the calling thread does not maintain ownership of the mutex. The third parameter is a string that specifies the name of the mutex: the full name of the ToastSemaphore mutex is **Microsoft.Messenger.ToastSemaphore**. So, the call to [CreateMutex](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/createmutex.asp) should be as follows:
    ```
    HANDLE hToastSemaphore = CreateMutex(NULL, FALSE, "Microsoft.Messenger.ToastSemaphore");
    ```

    

    If the mutex does not exist, the call to [CreateMutex](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/createmutex.asp) will create it. Whether the mutex existed previously or not, a successful call will also return a handle to the mutex, which can be used to acquire the mutex. If the call to [CreateMutex](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/createmutex.asp) fails, **NULL** is returned. The [GetLastError](http://msdn.microsoft.com/library/default.asp?url=/library/debug/base/getlasterror.asp) function can be used to get information about the error.
2.  **Attempt to acquire the mutex.** Call one of the synchronization wait functions, such as [WaitForSingleObject](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/waitforsingleobject.asp), and wait for a specified period of time to acquire the mutex. The recommended wait time is 60 seconds.
3.  **Draw your toast.** After either acquiring the mutex or timing out, your application should draw the toast on the desktop.
4.  **Release the mutex.** After your toast disappears from the desktop, release the mutex by calling the [ReleaseMutex](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/releasemutex.asp) function.

**Remarks**

Avoid holding the mutex for periods of more than 60 seconds. If you hold the mutex for longer than 60 seconds while a Messenger client is waiting to draw a toast, the Messenger client will give up on waiting for the mutex and draw its toast, potentially resulting in a toast collision with your application's toast. If for some reason you need to hold the mutex for longer than 60 seconds, you should release and reacquire the mutex near 60-second intervals, when feasible. This will give other clients that may be waiting for the mutex a chance to draw toasts and will help avoid toast collisions that may occur when a client gives up on waiting for the mutex.

The Messenger ToastSemaphore mutex is not a feature of Windows Messenger. Rather, mutex services are provided by the operating system, and the Messenger client makes use of these services to avoid toast collisions.

If you are producing a non-Microsoft application that draws toasts on the desktop, you must implement your own mechanism for drawing the toasts. The Messenger APIs do not supply toast rendering functionality.

## Related topics

<dl> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Windows Messenger](im-messenger-entry.md)
</dt> <dt>

[Synchronization](http://msdn.microsoft.com/library/default.asp?url=/library/dllproc/base/synchronization.asp)
</dt> </dl>

 

 




