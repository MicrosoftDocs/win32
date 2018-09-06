---
Description: Instructs an IME window to get the position of the status window. To send this command, the application uses the WM\_IME\_CONTROL message with the parameter settings shown below.
ms.assetid: 59c7baae-1b8a-4761-9814-31afd8d39691
title: IMC_GETSTATUSWINDOWPOS command
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMC\_GETSTATUSWINDOWPOS command

Instructs an IME window to get the position of the status window. To send this command, the application uses the [**WM\_IME\_CONTROL**](wm-ime-control.md) message with the parameter settings shown below.


```C++
LRESULT IMC_GETSTATUSWINDOWPOS
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMC\_GETSTATUSWINDOWPOS.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Not used.

</dd> </dl>

## Return Value

Returns a [**POINTS**](https://msdn.microsoft.com/en-us/library/Dd162808(v=VS.85).aspx) structure that contains the x coordinate and y coordinate of the status window position in screen coordinates, relative to the upper left corner of the screen.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>Imm.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Input Method Manager](input-method-manager.md)
</dt> <dt>

[Input Method Manager Commands](input-method-manager-commands.md)
</dt> <dt>

[**WM\_IME\_CONTROL**](wm-ime-control.md)
</dt> </dl>

 

 




