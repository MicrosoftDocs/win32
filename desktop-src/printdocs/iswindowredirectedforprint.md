---
Description: The IsWindowRedirectedForPrint function determines whether the specified window is currently redirected for printing.
ms.assetid: 49FD0D63-0F7F-48C6-81B6-25715294E7B7
title: IsWindowRedirectedForPrint function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it by using the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>User32.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrintWindow**](/windows/desktop/api/Winuser/nf-winuser-printwindow)
</dt> <dt>

[**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212)
</dt> <dt>

[**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175)
</dt> <dt>

[**WM\_PRINT**](https://msdn.microsoft.com/library/windows/desktop/dd145216)
</dt> <dt>

[**WM\_PRINTCLIENT**](https://msdn.microsoft.com/library/windows/desktop/dd145217)
</dt> </dl>

 

 




