---
description: Describes how to detect whether a specific API set is available on the current device.
title: Detect API set availability
ms.topic: article
ms.date: 10/14/2020
---

# Detect API set availability

In some cases, a given API set contract name may be intentionally mapped to an empty module name on some Windows 10 devices. The reasons for this vary, but a common example is that an expensive feature in terms of system resources may be removed from the Windows OS when configured for a resource-constrained device. This poses a challenge for applications to gracefully handle optional features at the API level.

The traditional approach for testing whether a Win32 API is available is to use [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress). However, these are not a reliable means for testing API sets because of the [reverse forwarding](api-set-loader-operation.md#reverse-forwarding) support in Windows 10. When reverse forwarding is applied to a given API, **LoadLibrary** or **GetProcAddress** may resolve to a valid function pointer even in cases where the internal implementation has been removed. In this case, the function pointer will be pointing to a stub function that simply returns an error.

In order to detect this case, you can use the [IsApiSetImplemented](/windows/win32/api/apiquery2/nf-apiquery2-isapisetimplemented) function to query the underlying availability of a given API implementation. This test validates that calling this function will result in executing a functional implementation of the API.

The following code example demonstrates how to use **IsApiSetImplemented** to determine whether the [WTSEnumerateSessions](/windows/win32/api/wtsapi32/nf-wtsapi32-wtsenumeratesessionsa) function is available on the current device before calling it. 

```c++
#include <windows.h>
#include <stdio.h>
#include <Wtsapi32.h>

int __cdecl wmain(int /* argc */, PCWSTR /* argv */ [])
{
    PWTS_SESSION_INFO pInfo = {};
    DWORD count = 0;

    if (!IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0"))
    {
        wprintf(L"IsApiSetImplemented on ext-ms-win-session-wtsapi32-l1-1-0 returns FALSE\n");
    }
    else
    {
        if (WTSEnumerateSessionsW(WTS_CURRENT_SERVER_HANDLE, 0, 1, &pInfo, &count))
        {
            wprintf(L"SessionCount = %d\n", count);

            for (ULONG i = 0; i < count; i++)
            {
                PWTS_SESSION_INFO pCurInfo = &pInfo[i];
                wprintf(L"    %s: ID = %d, state = %d\n", pCurInfo->pWinStationName, 
                    pCurInfo->SessionId, pCurInfo->State);
            }

            WTSFreeMemory(pInfo);
        }
        else
        {
            wprintf(L"WTSEnumerateSessions failure : %x\n", GetLastError());
        }
    }

    return 0;
}
```