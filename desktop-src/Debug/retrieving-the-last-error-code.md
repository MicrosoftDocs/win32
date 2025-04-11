---
description: When many system functions fail, they set the last-error code.
ms.assetid: 4cc626ac-7574-44ce-8377-e0bdd8e74b7e
title: Retrieving the Last-Error Code
ms.topic: concept-article
ms.date: 05/31/2018
---

# Retrieving the Last-Error Code

When many system functions fail, they set the last-error code. If your application needs more details about an error, it can retrieve the last-error code using the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function and get a description of the error using the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function.

The following example includes an error-handling function that prints the error message and terminates the process.


```C++
#include <windows.h>

void ErrorExit() 
{ 
    // Retrieve the system error message for the last-error code

    LPVOID lpMsgBuf;
    DWORD dw = GetLastError(); 

    if (FormatMessage(
        FORMAT_MESSAGE_ALLOCATE_BUFFER | 
        FORMAT_MESSAGE_FROM_SYSTEM |
        FORMAT_MESSAGE_IGNORE_INSERTS,
        NULL,
        dw,
        MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
        (LPTSTR) &lpMsgBuf,
        0, NULL) == 0) {
        MessageBox(NULL, TEXT("FormatMessage failed"), TEXT("Error"), MB_OK);
        ExitProcess(dw);
    }

    MessageBox(NULL, (LPCTSTR)lpMsgBuf, TEXT("Error"), MB_OK);

    LocalFree(lpMsgBuf);
    ExitProcess(dw); 
}

void main()
{
    // Generate an error

    if (!GetProcessId(NULL))
        ErrorExit();
}
```
