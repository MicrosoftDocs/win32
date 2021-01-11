---
description: The following example sets the last-write time for a file to the current system time using the SetFileTime function.
ms.assetid: b4a70c01-d5ce-47e8-9918-9c9176894240
title: Changing a File Time to the Current Time
ms.topic: article
ms.date: 05/31/2018
---

# Changing a File Time to the Current Time

The following example sets the last-write time for a file to the current system time using the [**SetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-setfiletime) function.

The NTFS file system stores time values in UTC format, so they are not affected by changes in time zone or daylight saving time. The FAT file system stores time values based on the local time of the computer.

The file must be opened with the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function using FILE\_WRITE\_ATTRIBUTES access.


```C++
#include <windows.h>

// SetFileToCurrentTime - sets last write time to current system time
// Return value - TRUE if successful, FALSE otherwise
// hFile  - must be a valid file handle

BOOL SetFileToCurrentTime(HANDLE hFile)
{
    FILETIME ft;
    SYSTEMTIME st;
    BOOL f;

    GetSystemTime(&st);              // Gets the current system time
    SystemTimeToFileTime(&st, &ft);  // Converts the current system time to file time format
    f = SetFileTime(hFile,           // Sets last-write time of the file 
        (LPFILETIME) NULL,           // to the converted current system time 
        (LPFILETIME) NULL, 
        &ft);    

    return f;
}
```



 

 
