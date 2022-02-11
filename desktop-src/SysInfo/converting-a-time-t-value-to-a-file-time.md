---
description: The time functions included in the C run-time use the **time_t** type to represent the number of seconds elapsed since midnight, January 1, 1970. The following example converts a **time_t** value to a [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime).
ms.assetid: f626c0b2-a5a1-475d-9a24-64e7b0407278
title: Converting a time_t value to a FILETIME
ms.topic: article
ms.date: 12/03/2021
---

# Converting a time\_t value to a FILETIME

The time functions included in the C run-time use the **time_t** type to represent the number of seconds elapsed since midnight, January 1, 1970. The following example converts a **time_t** value to a [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime).

```cpp
#include <windows.h>
#include <time.h>

void TimetToFileTime(time_t t, LPFILETIME pft)
{
    ULARGE_INTEGER time_value;
    time_value.QuadPart = (t * 10000000LL) + 116444736000000000LL;
    pft->dwLowDateTime = time_value.LowPart;
    pft->dwHighDateTime = time_value.HighPart;
}
```

After you've obtained a [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime), you can convert the value to system time using the [**FileTimeToSystemTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-filetimetosystemtime) function.

## Legacy code example

The code example in the previous section is good for any architecture. But if you build for a 32-bit architecture and you define **_USE_32BIT_TIME_T**, then **time_t** is a 32-bit value. In that case you have the option to use the following code example instead.

```cpp
#include <windows.h>
#include <time.h>

void TimetToFileTime(time_t t, LPFILETIME pft)
{
    LONGLONG time_value = Int32x32To64(t, 10000000) + 116444736000000000;
    pft->dwLowDateTime = (DWORD) time_value;
    pft->dwHighDateTime = time_value >> 32;
}
```
