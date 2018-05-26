---
Description: This article contains information about the management of thread references using functions from the Shell lightweight utility functions.
ms.assetid: d8d479fd-c45a-4dfa-b496-76abc7c09a42
title: Managing Thread References
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Thread References

This article contains information about the management of thread references using functions from the Shell lightweight utility functions.

## 

Situations arise when a parent thread must be kept active for the lifetime of a child thread. For instance, if a Component Object Model (COM) object is created on the parent thread and marshaled to the child thread, that parent thread cannot terminate before the child thread. To accomplish this, the Shell provides these functions.

-   [**SHCreateThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shcreatethreadref?branch=master)
-   [**SHSetThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shsetthreadref?branch=master)
-   [**SHGetThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shgetthreadref?branch=master)

Use these functions in your parent thread as outlined here.

1.  Declare an application-defined thread procedure following the form of the [*ThreadProc*](base.threadproc) function.

    ``` syntax
    DWORD WINAPI ThreadProc(LPVOID lpParameter);
    ```

2.  In your [*ThreadProc*](base.threadproc), call [**SHCreateThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shcreatethreadref?branch=master) to create a reference to the thread. This provides a pointer to an instance of [**IUnknown**](com.iunknown). This **IUnknown** uses the value pointed to by *pcRef* to maintain a reference count. As long as this count is greater than 0, the thread remains active.
3.  Using that pointer to [**IUnknown**](com.iunknown), call [**SHSetThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shsetthreadref?branch=master) in your [*ThreadProc*](base.threadproc). This sets the reference so that subsequent calls to [**SHGetThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shgetthreadref?branch=master) have something to retrieve.
4.  If your [*ThreadProc*](base.threadproc) creates another thread, that thread's *ThreadProc* can call [**SHGetThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shgetthreadref?branch=master) with the pointer to [**IUnknown**](com.iunknown) obtained by [**SHCreateThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shcreatethreadref?branch=master). This increments the reference count pointed to by the *pcRef* parameter in **SHCreateThreadRef**.
5.  Create the thread. This is usually done by calling [**SHCreateThread**](/windows/win32/Shlwapi/nf-shlwapi-shcreatethread?branch=master), passing a pointer to your [*ThreadProc*](base.threadproc) in the *pfnThreadProc* parameter. Also pass the CTF\_THREAD\_REF flag in the *dwFlags* parameter. The thread is active as long as *ThreadProc* is executing.
6.  When a child thread is created, pass the **CTF\_REF\_COUNTED** flag in the *dwFlags* parameter in the call to its [**SHCreateThread**](/windows/win32/Shlwapi/nf-shlwapi-shcreatethread?branch=master).
7.  As child threads complete and are released, the value pointed to by the parent thread's *pcRef* decreases. Once all child threads are complete, the original [*ThreadProc*](base.threadproc) can complete and release the final thread reference, dropping the reference count to 0. At that point, the reference to the original thread opened by [**SHCreateThread**](/windows/win32/Shlwapi/nf-shlwapi-shcreatethread?branch=master) is released and the thread completed.

Another related function is [**SHReleaseThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shreleasethreadref?branch=master). This function is called by the [*ThreadProc*](base.threadproc) if the thread has been created using [**SHCreateThread**](/windows/win32/Shlwapi/nf-shlwapi-shcreatethread?branch=master) with the **CTF\_THREAD\_REF** flag. However, the *ThreadProc* is not required to do so implicitly. Calling [**IUnknown::Release**](com.iunknown_release) on the pointer to [**IUnknown**](com.iunknown) obtained through [**SHCreateThreadRef**](/windows/win32/Shlwapi/nf-shlwapi-shcreatethreadref?branch=master) is all that needs to be done.

 

 



