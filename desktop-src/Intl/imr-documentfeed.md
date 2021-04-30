---
description: Notifies an application when the selected IME needs the converted string from the application. The application receives this command through the WM\_IME\_REQUEST message with parameters set as shown below.
ms.assetid: 1a007bed-15e5-4400-9d2f-32e37e1765d2
title: IMR_DOCUMENTFEED notification code (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMR\_DOCUMENTFEED notification code

Notifies an application when the selected IME needs the converted string from the application. The application receives this command through the [**WM\_IME\_REQUEST**](wm-ime-request.md) message with parameters set as shown below.


```C++
LRESULT IMR_DOCUMENTFEED
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMR\_DOCUMENTFEED.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Pointer to a buffer to contain the [**RECONVERTSTRING**](/windows/win32/api/imm/ns-imm-reconvertstring) structure.

</dd> </dl>

## Return Value

Returns the current reconversion string structure. If *lParam* is set to **NULL**, the application returns the required size for the buffer to hold the structure. The command returns 0 if it does not succeed.

## Remarks

The IME caches converted strings for higher conversion accuracy. One caching limitation of the IME is that it loses the converted string under the following circumstances:

-   The caret position for the application is moved by a key, for example, a cursor key.
-   The caret position for the application is moved by the mouse.
-   A new document is opened.

With the **IMR\_DOCUMENTFEED** command, the IME can refresh its cached strings any time. Use of this command improves conversion accuracy.

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

[**RECONVERTSTRING**](/windows/win32/api/imm/ns-imm-reconvertstring)
</dt> <dt>

[**WM\_IME\_REQUEST**](wm-ime-request.md)
</dt> </dl>

 

 




