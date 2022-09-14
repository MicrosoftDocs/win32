---
description: Notifies an application when an IME is about to close the candidates window. The application receives this command through the WM\_IME\_NOTIFY message with parameter settings as shown below.
ms.assetid: d96cea0a-1fc4-4ba7-bb96-7e9c0b67ce5b
title: IMN_CLOSECANDIDATE notification code (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMN\_CLOSECANDIDATE notification code

Notifies an application when an IME is about to close the candidates window. The application receives this command through the [**WM\_IME\_NOTIFY**](wm-ime-notify.md) message with parameter settings as shown below.


```C++
IMN_CLOSECANDIDATE
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMN\_CLOSECANDIDATE.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Candidate list flag. Each bit corresponds to a candidate list: bit 0 to the first list, bit 1 to the second, and so on. If a specified bit is 1, the corresponding candidates window is about to be closed.

</dd> </dl>

## Return Value

This command has no return value.

## Remarks

An application should process this command if it displays candidates itself.

By default, the IME window destroys a candidate window when it processes this command.

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

[**WM\_IME\_NOTIFY**](wm-ime-notify.md)
</dt> </dl>

 

 




