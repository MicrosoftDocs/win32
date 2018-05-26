---
Description: Notifies an application when the sentence mode of the input context is updated. The application receives this command through the WM\_IME\_NOTIFY message with parameter settings as shown below.
ms.assetid: 72455193-cd17-45f8-b19c-a1f735ff81bf
title: IMN\_SETSENTENCEMODE notification code
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMN\_SETSENTENCEMODE notification code

Notifies an application when the sentence mode of the input context is updated. The application receives this command through the [**WM\_IME\_NOTIFY**](wm-ime-notify.md) message with parameter settings as shown below.


```C++
IMN_SETSENTENCEMODE
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMN\_SETSENTENCEMODE.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Not used.

</dd> </dl>

## Return Value

This command has no return value.

## Remarks

The application can get information about the sentence mode by using the [**ImmGetConversionStatus**](/windows/win32/Imm/nf-imm-immgetconversionstatus?branch=master) function.

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

[**ImmGetConversionStatus**](/windows/win32/Imm/nf-imm-immgetconversionstatus?branch=master)
</dt> <dt>

[**WM\_IME\_NOTIFY**](wm-ime-notify.md)
</dt> </dl>

 

 




