---
Description: Notifies an application when the open status of the input context is updated. The application receives this command through the WM\_IME\_NOTIFY message with parameter settings as shown below.
ms.assetid: cc6fa7f4-b85a-486a-985d-53c071321bd1
title: IMN\_SETOPENSTATUS notification code
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMN\_SETOPENSTATUS notification code

Notifies an application when the open status of the input context is updated. The application receives this command through the [**WM\_IME\_NOTIFY**](wm-ime-notify.md) message with parameter settings as shown below.


```C++
IMN_SETOPENSTATUS
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMN\_SETOPENSTATUS.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Not used.

</dd> </dl>

## Return Value

This command has no return value.

## Remarks

The application can get information about the open status by using the [**ImmGetOpenStatus**](/windows/win32/Imm/nf-imm-immgetopenstatus?branch=master) function.

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

[**ImmGetOpenStatus**](/windows/win32/Imm/nf-imm-immgetopenstatus?branch=master)
</dt> <dt>

[**WM\_IME\_NOTIFY**](wm-ime-notify.md)
</dt> </dl>

 

 




