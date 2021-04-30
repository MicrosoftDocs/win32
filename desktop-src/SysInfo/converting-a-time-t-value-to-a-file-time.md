---
description: The time functions included in the C run-time use the time\_t type to represent the number of seconds elapsed since midnight, January 1, 1970. The following example converts a time\_t value to a file time, using the Int32x32To64 function.
ms.assetid: f626c0b2-a5a1-475d-9a24-64e7b0407278
title: Converting a time_t Value to a File Time
ms.topic: article
ms.date: 05/31/2018
---

# Converting a time\_t Value to a File Time

The time functions included in the C run-time use the time\_t type to represent the number of seconds elapsed since midnight, January 1, 1970. The following example converts a time\_t value to a file time, using the [**Int32x32To64**](/windows/desktop/api/winnt/nf-winnt-int32x32to64) function.


```C++
#include <windows.h>
#include <time.h>

void TimetToFileTime( time_t t, LPFILETIME pft )
{
    LONGLONG ll = Int32x32To64(t, 10000000) + 116444736000000000;
    pft->dwLowDateTime = (DWORD) ll;
    pft->dwHighDateTime = ll >>32;
}
```



After you have obtained a file time, you can convert this value to system time using the [**FileTimeToSystemTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-filetimetosystemtime) function.

 

 
