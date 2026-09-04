---
description: Describes how to detect whether a specific API set is available on the current device.
title: Detect API set availability
ms.topic: reference
ms.date: 09/03/2026
---

# Detect API set availability

In some cases, a given API set contract name might be intentionally mapped to an empty module name on some Windows devices. The reasons for this vary, but a common example is that an expensive feature in terms of system resources might be removed from the Windows OS when configured for a resource-constrained device. This poses a challenge for applications to gracefully handle optional features at the API level.

The traditional approach for testing whether a Win32 API is available is to use [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw) or [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress). However, these are not a reliable means for testing API sets, because of [reverse forwarding](api-set-loader-operation.md#reverse-forwarding). Where reverse forwarding is applied to a given API, **LoadLibrary** or **GetProcAddress** might resolve to a valid function pointer even in cases where the internal implementation has been removed. In this case, the function pointer will be pointing to a stub function that simply returns an error.

In order to detect this case, you can use the [IsApiSetImplemented](/windows/win32/api/apiquery2/nf-apiquery2-isapisetimplemented) function to query the underlying availability of a given API implementation. This test reports whether the API set is present in the composed API set schema on the running device, and whether it is mapped to an implementation module.

> [!IMPORTANT]
> A successful availability query is not a guarantee that a particular call will succeed. Continue to handle module-loading errors, missing exports, and the API's own documented failure results.

The following code example demonstrates how to use **IsApiSetImplemented** to determine whether the API set that contains [WTSEnumerateSessionsW](/windows/win32/api/wtsapi32/nf-wtsapi32-wtsenumeratesessionsw) is available on the current device before calling it.

```cpp
#include <windows.h>
#include <apiquery2.h>
#include <stdio.h>
#include <wtsapi32.h>

#pragma comment(lib, "OneCore.lib")
#pragma comment(lib, "Wtsapi32.lib")

int __cdecl wmain(int /* argc */, PCWSTR /* argv */ [])
{
    PWTS_SESSION_INFOW pInfo = nullptr;
    DWORD count = 0;

    if (!IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0"))
    {
        wprintf(L"ext-ms-win-session-wtsapi32-l1-1-0 is not available.\n");
        return 0;
    }

    if (WTSEnumerateSessionsW(WTS_CURRENT_SERVER_HANDLE, 0, 1, &pInfo, &count))
    {
        wprintf(L"SessionCount = %lu\n", count);

        for (DWORD i = 0; i < count; i++)
        {
            PWTS_SESSION_INFOW pCurInfo = &pInfo[i];
            wprintf(L"    %ls: ID = %lu, state = %d\n", pCurInfo->pWinStationName,
                pCurInfo->SessionId, static_cast<int>(pCurInfo->State));
        }

        WTSFreeMemory(pInfo);
    }
    else
    {
        wprintf(L"WTSEnumerateSessionsW failure : %lu\n", GetLastError());
    }

    return 0;
}
```

`IsApiSetImplemented` is declared in *apiquery2.h*, and the normal public SDK link path supplies it from *OneCore.lib*. That library is separate from any import library needed to call the optional target API itself.

The example above links *Wtsapi32.lib* for a static import, which keeps the example short. A production application that must run where the API set is absent should also apply the guidance in [Keep the optional code path reachable](#keep-the-optional-code-path-reachable).

## Choose the query name

Pass the name of the API set you are testing, without a `.dll` suffix. Add the suffix only when the name is used with a loader operation such as **LoadLibrary**.

To find the name to pass, see the **Requirements** table on the reference page for the API you want to call. When the API is delivered through an API set, the DLL row names the API set rather than a physical module.

The form of the name depends on how the API is addressed.

| API surface | Query form | Example |
|---|---|---|
| Named group | `<contract>~<group>` | `api-win-core-samplefeature~AdvancedOperations` |
| Default group | Contract alias, without `~Default` | `api-win-core-samplefeature` |
| Versioned contract | Complete versioned contract name | `ext-ms-win-core-samplefeature-l1-1-0` |

The `samplefeature` names are illustrative names for a fictional Windows component. The name prefix (`api-` or `ext-`) doesn't play a role in availability behavior.

For a named group, a successful query means that the group exists, its contract is mapped to an implementation module, that host is usable in the current execution environment, the group isn't disabled, and any system feature associated with the group is enabled. A query that uses a contract alias applies the contract and host checks.

If the API's public header supplies an `Is<APIName>Present` helper, prefer that helper. It already contains the correct name for the API set or group that carries the API.

The result of a query is contract- or group-granular, not function-granular. Two helpers backed by the same named group always return the same result, even though each helper is named for a different API.

## Keep the optional code path reachable

An availability check can't protect process startup if the optional API is linked as a static import. The loader resolves static imports before your code runs, so a missing module fails the process before execution reaches the check.

Use one of these approaches:

- Configure the module that carries the optional API for [delay loading](/cpp/build/reference/linker-support-for-delay-loaded-dlls). Delay loading is a linker setting: specify `/DELAYLOAD:<module>` and link *delayimp.lib*. Specify the module name that appears in your binary's import table, which might be the classic DLL name rather than the API set contract name. For the preceding example, that name is *WTSAPI32.dll*.
- Or resolve the target dynamically with **LoadLibrary** and [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) after the availability query succeeds.

Don't use **LoadLibrary** or **GetProcAddress** as a substitute for the availability query. They answer module and export questions, they don't evaluate named group state, and they can resolve to a reverse-forwarding stub as described earlier. Use them after the query, to handle the separate module and export checks.

## Behavior on earlier versions of Windows

The implementation supplied by *OneCore.lib* selects an available query mechanism at run time, so an application that calls **IsApiSetImplemented** can still run on a system that predates the underlying query support.

On a system where no query mechanism is available:

- A group-qualified name that contains `~` returns **FALSE**. A system that can't evaluate named groups can't report that a group is available.
- A name that isn't group-qualified can return **TRUE**. This preserves compatibility with applications that supplied their own forwarder DLLs on early versions of Windows, where the contract was in fact satisfied by that forwarder.

Don't use an API set availability query as a security or authorization check.

## See also

- [IsApiSetImplemented function](/windows/win32/api/apiquery2/nf-apiquery2-isapisetimplemented)
- [Windows API sets](windows-apisets.md)
- [API set loader operation](api-set-loader-operation.md)
- [LoadLibrary function](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw)
- [GetProcAddress function](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress)
