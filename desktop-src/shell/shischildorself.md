---
UID: 
title: SHIsChildOrSelf function
description: Compares whether a window is equal to, a child of, or a descendant of, a second window.
old-location: 
ms.assetid: na
ms.date: 04/10/2019
ms.keywords: IsChild
ms.topic: reference
req.header: Shlwapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 Professional, Windows XP [desktop apps only]
req.target-min-winversvr: Windows 2000 Server, Windows Server 2003 [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: api-ms-win-shlwapi-winrt-storage-l1-1-1.dll
req.irql: 
topic_type:
- APIRef
api_type: 
api_location:
- api-ms-win-shlwapi-winrt-storage-l1-1-1.dll
api_name:
- SHIsChildOrSelf
targetos: Windows
req.typenames: 
req.redist: 
---

# SHIsChildOrSelf function

## Description

\[This function is available through Windows XP and Windows Server 2003.
It might be altered or unavailable in subsequent versions of Windows.\]

Compares whether a window is equal to, a child of, or a descendant of, a second window.

```cpp
HRESULT SHIsChildOrSelf(
  _In_ HWND hwndParent,
  _In_ HWND hwnd
);
```

## Parameters

### hwndParent [in]

Type: **HWND**

A handle to the first window.

### hwnd [in]

Type: **HWND**

A handle to a window to be tested against *hwndParent*.

## Returns

Type: **HRESULT**

Returns **S_OK** if the window specified by *hwnd* is equal to, a child of, or a descendent of the window specified by *hwndParent*.
Returns **S_FALSE** if the window specified by hwnd is not equal to, not a child of, and not a descendent of the window specified by *hwndParent*.
The return value is undefined if either window handle is invalid.

## Remarks

## See also

[IsChild](/windows/desktop/api/winuser/nf-winuser-ischild)
