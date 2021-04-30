---
description: An application sends the WM\_MDITILE message to a multiple-document interface (MDI) client window to arrange all of its MDI child windows in a tile format.
ms.assetid: a480ba61-807e-4d0e-bda2-f1876e0bb13c
title: WM_MDITILE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDITILE message

An application sends the **WM\_MDITILE** message to a multiple-document interface (MDI) client window to arrange all of its MDI child windows in a tile format.


```C++
#define WM_MDITILE                      0x0226
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The tiling option. This parameter can be one of the following values, optionally combined with **MDITILE\_SKIPDISABLED** to prevent disabled MDI child windows from being tiled.



| Value                                                                                                                                                                                                                                    | Meaning                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="MDITILE_HORIZONTAL"></span><span id="mditile_horizontal"></span><dl> <dt>**MDITILE\_HORIZONTAL**</dt> <dt>0x0001</dt> </dl> | Tiles windows horizontally.<br/> |
| <span id="MDITILE_VERTICAL"></span><span id="mditile_vertical"></span><dl> <dt>**MDITILE\_VERTICAL**</dt> <dt>0x0000</dt> </dl>       | Tiles windows vertically.<br/>   |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **BOOL**

If the message succeeds, the return value is **TRUE**.

If the message fails, the return value is **FALSE**.

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

[**WM\_MDIICONARRANGE**](wm-mdiiconarrange.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 




