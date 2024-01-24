---
description: Notifies the DWM of an incoming update to a window shared surface.
ms.assetid: 8357D977-E501-47D7-85BC-7C8954C6D166
title: DwmDxUpdateWindowSharedSurface function
ms.topic: reference
ms.date: 11/27/2018
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - Dwmapi.dll
api_name:
 - DwmDxUpdateWindowSharedSurface
---

# DwmDxUpdateWindowSharedSurface function

Notifies the DWM of an incoming update to a window shared surface.

## Syntax

```C++
HRESULT WINAPI DwmDxUpdateWindowSharedSurface(
  _In_     HWND     hwnd,
  _In_     UINT64   uiUpdateId,
  _In_     DWORD    dwFlags,
  _In_opt_ HMONITOR hmonitorAssociation,
  _In_     RECT     *prc
);
```

## Parameters

`hwnd`

An [**HWND**](/windows/desktop/winprog/windows-data-types) specifying the window being updated.

`uiUpdateId`

The update ID retrieved from [**DwmDxGetWindowSharedSurface**](dwmdxgetwindowsharedsurface.md).

`dwFlags`

Reserved.

`hmonitorAssociation`

Reserved.

`prc`

The rect of the window being updated, in window coordinate space. A NULL rectangle indicates that no region was updated.

## Return value

**S\_OK** if successful, otherwise a FAILED **HRESULT.**

## Remarks

This API is intended for implementing a graphics driver or runtime. An application may not call this method. This documentation is only valid for Windows 7, and this API is not guaranteed to exist nor behave in a similar manner on other versions of Windows. This function is not present in any header or static-link library, and it is located at ordinal 101 in dwmapi.dll.

This method should only ever be called after [**DwmDxGetWindowSharedSurface**](dwmdxgetwindowsharedsurface.md) returns **S\_OK**, and must be called in that scenario, regardless of whether the surface is updated or not.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 7 \[desktop apps only\] |
| Minimum supported server | None supported |
| End of client support | Windows 7 |
| Header | N/A |
| DLL | Dwmapi.dll |
