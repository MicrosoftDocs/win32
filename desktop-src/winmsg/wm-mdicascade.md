---
description: An application sends the WM\_MDICASCADE message to a multiple-document interface (MDI) client window to arrange all its child windows in a cascade format.
ms.assetid: 33d04859-4220-40a6-be46-74a812a44ca8
title: WM_MDICASCADE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDICASCADE message

An application sends the **WM\_MDICASCADE** message to a multiple-document interface (MDI) client window to arrange all its child windows in a cascade format.


```C++
#define WM_MDICASCADE                   0x0227
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The cascade behavior. This parameter can be one or more of the following values.



| Value                                                                                                                                                                                                                                          | Meaning                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <span id="MDITILE_SKIPDISABLED"></span><span id="mditile_skipdisabled"></span><dl> <dt>**MDITILE\_SKIPDISABLED**</dt> <dt>0x0002</dt> </dl> | Prevents disabled MDI child windows from being cascaded. <br/> |
| <span id="MDITILE_ZORDER"></span><span id="mditile_zorder"></span><dl> <dt>**MDITILE\_ZORDER**</dt> <dt>0x0004</dt> </dl>                   | Arranges the windows in Z order.<br/>                          |



 

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

[**WM\_MDIICONARRANGE**](wm-mdiiconarrange.md)
</dt> <dt>

[**WM\_MDITILE**](wm-mditile.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 




