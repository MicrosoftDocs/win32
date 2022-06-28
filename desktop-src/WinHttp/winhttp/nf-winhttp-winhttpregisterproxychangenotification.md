---
title: WinHttpRegisterProxyChangeNotification
description: TBD
ms.topic: reference
ms.date: 06/28/2022
req.lib: Winhttp.lib
req.dll: Winhttp.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
 - Winhttp.dll
api_name:
 - WinHttpRegisterProxyChangeNotification
targetos: Windows
---

# WinHttpRegisterProxyChangeNotification function

TBD

## Syntax

```cpp
DWORD WINAPI WinHttpRegisterProxyChangeNotification(
  _In_ ULONGLONG ullFlags,
  _In_ WINHTTP_PROXY_CHANGE_CALLBACK pfnCallback,
  _In_ PVOID pvContext,
  _Out_ WINHTTP_PROXY_CHANGE_REGISTRATION_HANDLE *hRegistration
);
```

## Parameters

TBD

## Return value

TBD

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | Winhttp.h |
| **Library** | Winhttp.lib |
| **DLL** | Winhttp.dll |
