---
description: Notifies an application when the status window position in the input context is updated. The application receives this command through the WM\_IME\_NOTIFY message with parameter settings as follows.
ms.assetid: 15e65aff-67d9-4d1a-a6a7-b921cecb3aec
title: IMN_SETSTATUSWINDOWPOS notification code (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMN\_SETSTATUSWINDOWPOS notification code

Notifies an application when the status window position in the input context is updated. The application receives this command through the [**WM\_IME\_NOTIFY**](wm-ime-notify.md) message with parameter settings as follows.


```C++
IMN_SETSTATUSWINDOWPOS
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMN\_SETSTATUSWINDOWPOS.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Not used.

</dd> </dl>

## Return Value

This command has no return value.

## Remarks

The application can get information about the status window position by using the [**IMC\_GETSTATUSWINDOWPOS**](imc-getstatuswindowpos.md) command.

## Requirements



| Requirement | Value |
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

[**IMC\_GETSTATUSWINDOWPOS**](imc-getstatuswindowpos.md)
</dt> <dt>

[**WM\_IME\_NOTIFY**](wm-ime-notify.md)
</dt> </dl>

 

 




