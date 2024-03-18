---
description: Retrieves the current value of a specified Desktop Window Manager (DWM) attribute applied to a window.
title: GetWindowCompositionAttribute function
ms.topic: reference
ms.date: 02/20/2024
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - user32.dll
api_name:
 - GetWindowCompositionAttribute
---

# GetWindowCompositionAttribute function

Retrieves the current value of a specified Desktop Window Manager (DWM) attribute applied to a window.

## Syntax

```C++
BOOL GetWindowCompositionAttribute(
  HWND hwnd,
  [INOUT] WINDOWCOMPOSITIONATTRIBDATA* pwcad
);
```

## Parameters

`hwnd`

An [**HWND**](/windows/desktop/winprog/windows-data-types) specifying the handle to the window for which the attribute value is to be retrieved.

`pwcad`

A pointer to a [WINDOWCOMPOSITIONATTRIBDATA](windowcompositionattribdata.md) structure describing which attribute to retrieve and a memory location to hold its value.



## Return value

**TRUE** if the function succeeds; otherwise, **FALSE**.


## Remarks

The use of this API is not recommended. Use [DwmGetWindowAttribute](/windows/win32/api/dwmapi/nf-dwmapi-dwmgetwindowattribute) instead.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from user32.dll.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 7 \[desktop apps only\] |
| Minimum supported server | None supported |
| End of client support | Windows 7 |
| Header | N/A |
| DLL | user32.dll |
