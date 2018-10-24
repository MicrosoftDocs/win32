---
Description: This article contains information about the management of thread references using functions from the Shell lightweight utility functions.
ms.assetid: d8d479fd-c45a-4dfa-b496-76abc7c09a42
title: Managing Thread References
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing Thread References

This article contains information about the management of thread references using functions from the Shell lightweight utility functions.

## 

Situations arise when a parent thread must be kept active for the lifetime of a child thread. For instance, if a Component Object Model (COM) object is created on the parent thread and marshaled to the child thread, that parent thread cannot terminate before the child thread. To accomplish this, the Shell provides these functions.

-   [**SHCreateThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethreadref)
-   [**SHSetThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shsetthreadref)
-   [**SHGetThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shgetthreadref)

Use these functions in your parent thread as outlined here.

1.  Declare an application-defined thread procedure following the form of the [*ThreadProc*](https://msdn.microsoft.com/en-us/library/ms686736(v=VS.85).aspx) function.

    ``` syntax
    DWORD WINAPI ThreadProc(LPVOID lpParameter);
    ```

2.  In your [*ThreadProc*](https://msdn.microsoft.com/en-us/library/ms686736(v=VS.85).aspx), call [**SHCreateThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethreadref) to create a reference to the thread. This provides a pointer to an instance of [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx). This **IUnknown** uses the value pointed to by *pcRef* to maintain a reference count. As long as this count is greater than 0, the thread remains active.
3.  Using that pointer to [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx), call [**SHSetThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shsetthreadref) in your [*ThreadProc*](https://msdn.microsoft.com/en-us/library/ms686736(v=VS.85).aspx). This sets the reference so that subsequent calls to [**SHGetThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shgetthreadref) have something to retrieve.
4.  If your [*ThreadProc*](https://msdn.microsoft.com/en-us/library/ms686736(v=VS.85).aspx) creates another thread, that thread's *ThreadProc* can call [**SHGetThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shgetthreadref) with the pointer to [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) obtained by [**SHCreateThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethreadref). This increments the reference count pointed to by the *pcRef* parameter in **SHCreateThreadRef**.
5.  Create the thread. This is usually done by calling [**SHCreateThread**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethread), passing a pointer to your [*ThreadProc*](https://msdn.microsoft.com/en-us/library/ms686736(v=VS.85).aspx) in the *pfnThreadProc* parameter. Also pass the CTF\_THREAD\_REF flag in the *dwFlags* parameter. The thread is active as long as *ThreadProc* is executing.
6.  When a child thread is created, pass the **CTF\_REF\_COUNTED** flag in the *dwFlags* parameter in the call to its [**SHCreateThread**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethread).
7.  As child threads complete and are released, the value pointed to by the parent thread's *pcRef* decreases. Once all child threads are complete, the original [*ThreadProc*](https://msdn.microsoft.com/en-us/library/ms686736(v=VS.85).aspx) can complete and release the final thread reference, dropping the reference count to 0. At that point, the reference to the original thread opened by [**SHCreateThread**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethread) is released and the thread completed.

Another related function is [**SHReleaseThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shreleasethreadref). This function is called by the [*ThreadProc*](https://msdn.microsoft.com/en-us/library/ms686736(v=VS.85).aspx) if the thread has been created using [**SHCreateThread**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethread) with the **CTF\_THREAD\_REF** flag. However, the *ThreadProc* is not required to do so implicitly. Calling [**IUnknown::Release**](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx) on the pointer to [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) obtained through [**SHCreateThreadRef**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethreadref) is all that needs to be done.

 

 



