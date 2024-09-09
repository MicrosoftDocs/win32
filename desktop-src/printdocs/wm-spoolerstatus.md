---
description: The WM\_SPOOLERSTATUS message is sent from Print Manager whenever a job is added to or removed from the Print Manager queue.
ms.assetid: 6140c9d8-0e5b-49f2-a4a6-cc1f2a0bed0a
title: WM_SPOOLERSTATUS message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SPOOLERSTATUS message

The **WM\_SPOOLERSTATUS** message is sent from Print Manager whenever a job is added to or removed from the Print Manager queue.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND hwnd, 
  UINT  uMsg, 
  WPARAM wParam, 
  LPARAM lParam     
);
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The PR\_JOBSTATUS flag.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the number of jobs remaining in the Print Manager queue.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

This message is for informational purposes only. This message is advisory and does not have guaranteed delivery semantics. Applications should not assume that they will receive a WM\_SPOOLERSTATUS message for every change in spooler status.

The WM\_SPOOLERSTATUS message is not supported after Windows XP. To be notified of changes to the print queue status, you can use [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) and [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Messages](printing-and-print-spooler-messages.md)
</dt> <dt>

[**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md)
</dt> <dt>

[**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md)
</dt> </dl>

 

