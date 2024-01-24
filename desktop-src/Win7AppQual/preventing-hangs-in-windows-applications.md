---
description: Learn how to prevent hangs in Windows applications for Windows 7 and Windows Server 2008 R2 platforms.
ms.assetid: 698a046b-1934-49cd-a717-d61e7e1ec534
title: Preventing Hangs in Windows Applications
ms.topic: article
ms.date: 05/31/2018
---

# Preventing Hangs in Windows Applications

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Description

**Hangs - User Perspective**

Users like responsive applications. When they click a menu, they want the application to react instantly, even if it is currently printing their work. When they save a lengthy document in their favorite word processor, they want to continue typing while the disk is still spinning. Users get impatient rather quickly when the application does not react in a timely fashion to their input.

A programmer might recognize many legitimate reasons for an application not to instantly respond to user input. The application might be busy recalculating some data, or simply waiting for its disk I/O to complete. However, from user research, we know that users get annoyed and frustrated after just a couple of seconds of unresponsiveness. After 5 seconds, they will try to terminate a hung application. Next to crashes, application hangs are the most common source of user disruption when working with Win32 applications.

There are many different root causes for application hangs, and not all of them manifest themselves in an unresponsive UI. However, an unresponsive UI is one of the most common hang experiences, and this scenario currently receives the most operating system support for both detection as well as recovery. Windows automatically detects, collects debug information, and optionally terminates or restarts hung applications. Otherwise, the user might have to restart the machine in order to recover a hung application.

**Hangs - Operating System Perspective**

When an application (or more accurately, a thread) creates a window on the desktop, it enters into an implicit contract with the Desktop Window Manager (DWM) to process window messages in a timely fashion. The DWM posts messages (keyboard/mouse input and messages from other windows, as well as itself) into the thread-specific message queue. The thread retrieves and dispatches those messages via its message queue. If the thread does not service the queue by calling GetMessage(), messages are not processed, and the window hangs: it can neither redraw nor can it accept input from the user. The operating system detects this state by attaching a timer to pending messages in the message queue. If a message has not been retrieved within 5 seconds, the DWM declares the window to be hung. You can query this particular window state via the IsHungAppWindow() API.

Detection is only the first step. At this point, the user still cannot even terminate the application - clicking the X (Close) button would result in a WM\_CLOSE message, which would be stuck in the message queue just like any other message. The Desktop Window Manager assists by seamlessly hiding and then replacing the hung window with a 'ghost' copy displaying a bitmap of the original window's previous client area (and adding "Not Responding" to the title bar). As long as the original window's thread does not retrieve messages, the DWM manages both windows simultaneously, but allows the user to interact only with the ghost copy. Using this ghost window, the user can only move, minimize, and - most importantly - close the unresponsive application, but not change its internal state.

The whole ghost experience looks like this:

![Screenshot that shows the 'Notepad is not responding' dialog.](images/preventinghangs-ghostwindow.gif)

The Desktop Window Manager does one last thing; it integrates with Windows Error Reporting, allowing the user to not only close and optionally restart the application, but also send valuable debugging data back to Microsoft. You can get this hang data for your own applications by signing up at the Winqual website.

Windows 7 added one new feature to this experience. The operating system analyzes the hung application and, under certain circumstances, gives the user the option to cancel a blocking operation and make the application responsive again. The current implementation supports cancellation of blocking Socket calls; more operations will be user-cancelable in future releases.

To integrate your application with the hang recovery experience and to make the most out of the available data, follow these steps:

-   Ensure that your application registers for restart and recovery, making a hang as pain-free as possible to the user. A properly registered application can automatically restart with most of its unsaved data intact. This works for both application hangs and crashes.
-   Get frequency information as well as debugging data for your hung and crashed applications from the Winqual website. You can use this information even during your Beta to improve your code. See "Introducing Windows Error Reporting" for a brief overview.
-   You can disable the ghosting feature in your application via a call to DisableProcessWindowsGhosting (). However, this prevents the average user from closing and restarting a hung application and often ends in a reboot.

**Hangs - Developer Perspective**

The operating system defines an application hang as a UI thread that has not processed messages for at least 5 seconds. Obvious bugs cause some hangs, for example, a thread waiting for an event that is never signaled, and two threads each holding a lock and trying to acquire the others. You can fix those bugs without too much effort. However, many hangs are not so clear. Yes, the UI thread is not retrieving messages - but it is equally busy doing other 'important' work and will eventually come back to processing messages.

However, the user perceives this as a bug. The design should match the user's expectations. If the application's design leads to an unresponsive application, the design will have to change. Finally, and this is important, unresponsiveness cannot be fixed like a code bug; it requires upfront work during the design phase. Trying to retrofit an application's existing code base to make the UI more responsive is often too expensive. The following design guidelines might help.

-   Make UI responsiveness a top-level requirement; the user should always feel in control of your application
-   Ensure that users can cancel operations that take longer than one second to complete and/or that operations can complete in the background; provide appropriate progress UI if necessary

![Screenshot that shows the 'Copying items' dialog.](images/preventinghangs-progressbar.gif)

-   Queue long-running or blocking operations as background tasks (this requires a well-thought out messaging mechanism to inform the UI thread when work has been completed)
-   Keep the code for UI threads simple; remove as many blocking API calls as possible
-   Show windows and dialogs only when they are ready and fully operational. If the dialog needs to display information that is too resource-intensive to calculate, show some generic information first and update it on the fly when more data becomes available. A good example is the folder properties dialog from Windows Explorer. It needs to display the folder's total size, information that is not readily available from the file system. The dialog shows up right away and the "size" field is updated from a worker thread:

![Screenshot that shows the 'General' page of Windows Properties with the 'Size', 'Size on disk', and 'Contains' text circled.](images/preventinghangs-updatingdialog.gif)

Unfortunately, there is no simple way to design and write a responsive application. Windows does not provide a simple asynchronous framework that would allow for easy scheduling of blocking or long-running operations. The following sections introduce some of the best practices in preventing hangs and highlight some of the common pitfalls.

## Best Practices

**Keep the UI Thread Simple**

The UI thread's primary responsibility is to retrieve and dispatch messages. Any other kind of work introduces the risk of hanging the windows owned by this thread.

**Do:**

-   Move resource-intensive or unbounded algorithms that result in long-running operations to worker threads
-   Identify as many blocking function calls as possible and try to move them to worker threads; any function calling into another DLL should be suspicious
-   Make an extra effort to remove all file I/O and networking API calls from your worker thread. These functions can block for many seconds if not minutes. If you need to do any kind of I/O in the UI thread, consider using asynchronous I/O
-   Be aware that your UI thread is also servicing all single-threaded apartment (STA) COM servers hosted by your process; if you make a blocking call, these COM servers will be unresponsive until you service the message queue again

**Do not:**

-   Wait on any kernel object (like Event or Mutex) for more than a very short amount of time; if you have to wait at all, consider using MsgWaitForMultipleObjects(), which will unblock when a new message arrives
-   Share a thread's window message queue with another thread by using the AttachThreadInput() function. It is not only extremely difficult to properly synchronize access to the queue, it also can prevent the Windows operating system from properly detecting a hung window
-   Use TerminateThread() on any of your worker threads. Terminating a thread in this way will not allow it to release locks or signal events and can easily result in orphaned synchronization objects
-   Call into any 'unknown' code from your UI thread. This is especially true if your application has an extensibility model; there is no guarantee that 3rd-party code follows your responsiveness guidelines
-   Make any kind of blocking broadcast call; SendMessage(HWND\_BROADCAST) puts you at the mercy of every ill-written application currently running

**Implement Asynchronous Patterns**

Removing long-running or blocking operations from the UI thread requires implementing an asynchronous framework that allows offloading those operations to worker threads.

**Do:**

-   Use asynchronous window message APIs in your UI thread, especially by replacing SendMessage with one of its non-blocking peers: PostMessage, SendNotifyMessage, or SendMessageCallback
-   Use background threads to execute long-running or blocking tasks. Use the new thread pool API to implement your worker threads
-   Provide cancellation support for long-running background tasks. For blocking I/O operations, use I/O cancellation, but only as a last resort; it's not easy to cancel the 'right' operation
-   Implement an asynchronous design for managed code by using the IAsyncResult pattern or by using Events

**Use Locks Wisely**

Your application or DLL needs locks to synchronize access to its internal data structures. Using multiple locks increases parallelism and makes your application more responsive. However, using multiple locks also increases the chance of acquiring those locks in different orders and causing your threads to deadlock. If two threads each hold a lock and then try to acquire the other thread's lock, their operations will form a circular wait that blocks any forward progress for these threads. You can avoid this deadlock only by ensuring that all threads in the application always acquire all locks in the same order. However, it isn't always easy to acquire locks in the 'right' order. Software components can be composed, but lock acquisitions cannot. If your code calls some other component, that component's locks now become part of your implicit lock order - even if you have no visibility into those locks.

Things get even harder because locking operations include far more than the usual functions for Critical Sections, Mutexes, and other traditional locks. Any blocking call that crosses thread boundaries has synchronization properties that can result in a deadlock. The calling thread performs an operation with 'acquire' semantics and cannot unblock until the target thread 'releases' that call. Quite a few User32 functions (for example SendMessage), as well as many blocking COM calls fall into this category.

Worse yet, the operating system has its own internal process-specific lock that sometimes is held while your code executes. This lock is acquired when DLLs are loaded into the process, and is therefore called the 'loader lock.' The DllMain function always executes under the loader lock; if you acquire any locks in DllMain (and you should not), you need to make the loader lock part of your lock order. Calling certain Win32 APIs might also acquire the loader lock on your behalf - functions like LoadLibraryEx, GetModuleHandle, and especially CoCreateInstance.

To tie all of this together, look at the sample code below. This function acquires multiple synchronization objects and implicitly defines a lock order, something that is not necessarily obvious on cursory inspection. On function entry, the code acquires a Critical Section and does not release it until function exit, thereby making it the top node in our lock hierarchy. The code then calls the Win32 function LoadIcon(), which under the covers might call into the Operating System Loader to load this binary. This operation would acquire the loader lock, which now also becomes part of this lock hierarchy (make sure the DllMain function does not acquire the g\_cs lock). Next the code calls SendMessage(), a blocking cross-thread operation, which will not return unless the UI thread responds. Again, make sure that the UI thread never acquires g\_cs.

```
bool foo::bar (char* buffer)  
{  
      EnterCriticalSection(&g_cs);  
      // Get 'new data' icon  
      this.m_Icon = LoadIcon(hInst, MAKEINTRESOURCE(5));  
      // Let UI thread know to update icon SendMessage(hWnd,WM_COMMAND,IDM_ICON,NULL);  
      this.m_Params = GetParams(buffer);  
      LeaveCriticalSection(&g_cs);
      return true;  
}  
```

Looking at this code it seems clear that we implicitly made g\_cs the top-level lock in our lock hierarchy, even if we only wanted to synchronize access to the class member variables.

**Do:**

-   Design a lock hierarchy and obey it. Add all the necessary locks. There are many more synchronization primitives than just Mutex and CriticalSections; they all need to be included. Include the loader lock in your hierarchy if you take any locks in DllMain()
-   Agree on locking protocol with your dependencies. Any code your application calls or that might call your application needs to share the same lock hierarchy
-   Lock data structures not functions. Move lock acquisitions away from function entry points and guard only data access with locks. If less code operates under a lock, there is less of a chance for deadlocks
-   Analyze lock acquisitions and releases in your error handling code. Often the lock hierarchy if forgotten when trying to recover from an error condition
-   Replace nested locks with reference counters - they cannot deadlock. Individually locked elements in lists and tables are good candidates
-   Be careful when waiting on a thread handle from a DLL. Always assume that your code could be called under the loader lock. It's better to reference-count your resources and let the worker thread do its own cleanup (and then use FreeLibraryAndExitThread to terminate cleanly)
-   Use the Wait Chain Traversal API if you want to diagnose your own deadlocks

**Do not:**

-   Do anything other than very simple initialization work in your DllMain() function. See DllMain Callback Function for more details. Especially do not call LoadLibraryEx or CoCreateInstance
-   Write your own locking primitives. Custom synchronization code can easily introduce subtle bugs into your code base. Use the rich selection of operating system synchronization objects instead
-   Do any work in the constructors and destructors for global variables, they are executed under the loader lock

**Be Careful with Exceptions**

Exceptions allow the separation of normal program flow and error handling. Because of this separation, it can be difficult to know the precise state of the program prior to the exception and the exception handler might miss crucial steps in restoring a valid state. This is especially true for lock acquisitions that need to be released in the handler to prevent future deadlocks.

The sample code below illustrates this issue. The unbounded access to the "buffer" variable will occasionally result in an access violation (AV). This AV is caught by the native exception handler, but it has no easy way of determining if the critical section was already acquired at the time of the exception (the AV could even have taken place somewhere in the EnterCriticalSection code).

```
 BOOL bar (char* buffer)  
{  
   BOOL rc = FALSE;  
   __try {  
      EnterCriticalSection(&cs);  
      while (*buffer++ != '&') ;  
      rc = GetParams(buffer);  
      LeaveCriticalSection(&cs);  
   } __except (EXCEPTION_EXECUTE_HANDLER)  
   {  
      return FALSE;  
   } 
   return rc;  
}  
```

**Do:**

-   Remove \_\_try/\_\_except whenever possible; do not use SetUnhandledExceptionFilter
-   Wrap your locks in custom auto\_ptr-like templates if you use C++ exceptions. The lock should be released in the destructor. For native exceptions release the locks in your \_\_finally statement
-   Be careful with the code executing in a native exception handler; the exception might have leaked many locks, so your handler should not acquire any

**Do not:**

-   Handle native exceptions if not necessary or required by the Win32 APIs. If you use native exception handlers for reporting or data recovery after catastrophic failures, consider using the default operating system mechanism of Windows Error Reporting instead
-   Use C++ exceptions with any kind of UI (user32) code; an exception thrown in a callback will travel through layers of C code provided by the operating system. That code does not know about C++ unroll semantics

## Links to Resources

-   [Windows Error Reporting](../wer/windows-error-reporting.md)
-   [Asynchronous Design](https://msdn.microsoft.com/library/ms228969(v=VS.80).aspx)
-   [Asynchronous I/O](../fileio/synchronous-and-asynchronous-i-o.md)
-   [**AttachThreadInput Function**](/windows/win32/api/winuser/nf-winuser-attachthreadinput)
-   [**auto\_ptr Class**](https://msdn.microsoft.com/library/ew3fk483(v=VS.71).aspx)
-   [**DisableProcessWindowsGhosting Function**](/windows/win32/api/winuser/nf-winuser-disableprocesswindowsghosting)
-   [**DllMain Callback Function**](../dlls/dllmain.md)
-   [Events](https://msdn.microsoft.com/library/wewwczdw(v=VS.80).aspx)
-   [**GetMessage Function**](/windows/win32/api/winuser/nf-winuser-getmessage)
-   [I/O cancellation](../fileio/canceling-pending-i-o-operations.md)
-   [**IsHungAppWindow Function**](/windows/win32/api/winuser/nf-winuser-ishungappwindow)
-   [Message Queue](../winmsg/using-messages-and-message-queues.md)
-   [**MsgWaitForMultipleObjects Function**](/windows/win32/api/winuser/nf-winuser-msgwaitformultipleobjects)
-   [New Thread Pool API](../procthread/thread-pool-api.md)
-   [**PostMessage Function**](/windows/win32/api/winuser/nf-winuser-postmessagea)
-   [Restart and Recovery](../recovery/registering-for-application-restart.md)
-   [**SendMessageCallback Function**](/windows/win32/api/winuser/nf-winuser-sendmessagecallbacka)
-   [**SendNotifyMessage Function**](/windows/win32/api/winuser/nf-winuser-sendnotifymessagea)
-   [Synchronization Objects](../sync/about-synchronization.md)
-   [**TerminateThread Function**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminatethread)
-   [Windows Error Reporting](../wer/windows-error-reporting.md)
-   [Winqual](/windows-hardware/drivers/dashboard/hardware-submission-wlk)

 

 
