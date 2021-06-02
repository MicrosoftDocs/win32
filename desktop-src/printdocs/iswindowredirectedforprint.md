---
description: The IsWindowRedirectedForPrint function determines whether the specified window is currently redirected for printing.
ms.assetid: 49FD0D63-0F7F-48C6-81B6-25715294E7B7
title: IsWindowRedirectedForPrint function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IsWindowRedirectedForPrint
api_type: 
- DllExport
api_location: 
- user32.dll
---

# IsWindowRedirectedForPrint function

The **IsWindowRedirectedForPrint** function determines whether the specified window is currently redirected for printing.

## Syntax


```C++
BOOL WINAPI IsWindowRedirectedForPrint(
  _In_   HWND hWnd
);
```



## Parameters

<dl> <dt>

*hWnd* \[in\]
</dt> <dd>

The handle of the window.

</dd> </dl>

## Return value

If the window is currently redirected for printing, the function returns a nonzero value; otherwise, it returns zero.

## Remarks

A window is redirected for printing when it processes a call to [**PrintWindow**](/windows/desktop/api/Winuser/nf-winuser-printwindow). In a call to **PrintWindow**, a window renders its content to an off-screen device context.

This function has no associated import library or header file; you must call it by using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>User32.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrintWindow**](/windows/desktop/api/Winuser/nf-winuser-printwindow)
</dt> <dt>

[**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress)
</dt> <dt>

[**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya)
</dt> <dt>

[**WM\_PRINT**](/windows/desktop/gdi/wm-print)
</dt> <dt>

[**WM\_PRINTCLIENT**](/windows/desktop/gdi/wm-printclient)
</dt> </dl>

 

