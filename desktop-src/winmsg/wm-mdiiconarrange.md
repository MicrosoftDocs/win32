---
description: An application sends the WM\_MDIICONARRANGE message to a multiple-document interface (MDI) client window to arrange all minimized MDI child windows. It does not affect child windows that are not minimized.
ms.assetid: 935b9e29-224d-449e-b89f-b6062bed7702
title: WM_MDIICONARRANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDIICONARRANGE message

An application sends the **WM\_MDIICONARRANGE** message to a multiple-document interface (MDI) client window to arrange all minimized MDI child windows. It does not affect child windows that are not minimized.


```C++
#define WM_MDIICONARRANGE               0x0228
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**WM\_MDICASCADE**](wm-mdicascade.md)
</dt> <dt>

[**WM\_MDITILE**](wm-mditile.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 




