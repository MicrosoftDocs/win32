---
description: When a method call produces an error, many functions return an error code.
ms.assetid: 9d60277a-5ee8-471e-bfcd-d104064030a8
title: Retrieving Error Messages
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Error Messages

When a method call produces an error, many functions return an error code. For most Certificate Services interfaces and API elements that return an error code, the error message text can be retrieved by calling [**FormatMessage**](/windows/win32/api/winbase/nf-winbase-formatmessage) with a **NULL** module handle. If **FormatMessage** does not succeed, the error code most likely resulted from a backup API element or database related error; calling **FormatMessage** with a module handle corresponding to the Ntdsbmsg.dll library should retrieve the error message text. The following example shows how to retrieve error message text in a Certificate Services application.


```C++
#include <windows.h>
#include <stdio.h>
// Display error message text, given an error code.
// Typically, the parameter passed to this function is retrieved
// from GetLastError().
void PrintCSBackupAPIErrorMessage(DWORD dwErr)
{

    WCHAR   wszMsgBuff[512];  // Buffer for text.

    DWORD   dwChars;  // Number of chars returned.

    // Try to get the message from the system errors.
    dwChars = FormatMessage( FORMAT_MESSAGE_FROM_SYSTEM |
                             FORMAT_MESSAGE_IGNORE_INSERTS,
                             NULL,
                             dwErr,
                             0,
                             wszMsgBuff,
                             512,
                             NULL );

    if (0 == dwChars)
    {
        // The error code did not exist in the system errors.
        // Try Ntdsbmsg.dll for the error code.

        HINSTANCE hInst;

        // Load the library.
        hInst = LoadLibrary(L"Ntdsbmsg.dll");
        if ( NULL == hInst )
        {
            printf("cannot load Ntdsbmsg.dll\n");
            exit(1);  // Could 'return' instead of 'exit'.
        }

        // Try getting message text from ntdsbmsg.
        dwChars = FormatMessage( FORMAT_MESSAGE_FROM_HMODULE |
                                 FORMAT_MESSAGE_IGNORE_INSERTS,
                                 hInst,
                                 dwErr,
                                 0,
                                 wszMsgBuff,
                                 512,
                                 NULL );

        // Free the library.
        FreeLibrary( hInst );

    }

    // Display the error message, or generic text if not found.
    printf("Error value: %d Message: %ws\n",
            dwErr,
            dwChars ? wszMsgBuff : L"Error message not found." );

}
```



 

 
