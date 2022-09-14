---
description: Sent to a window that the user is resizing. By processing this message, an application can monitor the size and position of the drag rectangle and, if needed, change its size or position.
ms.assetid: 8cf56194-8a10-48e1-b0eb-aa3d66896599
title: WM_SIZING message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SIZING message

Sent to a window that the user is resizing. By processing this message, an application can monitor the size and position of the drag rectangle and, if needed, change its size or position.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_SIZING                       0x0214
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The edge of the window that is being sized. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                         | Meaning                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| <span id="WMSZ_BOTTOM"></span><span id="wmsz_bottom"></span><dl> <dt>**WMSZ\_BOTTOM**</dt> <dt>6</dt> </dl>                | Bottom edge<br/>         |
| <span id="WMSZ_BOTTOMLEFT"></span><span id="wmsz_bottomleft"></span><dl> <dt>**WMSZ\_BOTTOMLEFT**</dt> <dt>7</dt> </dl>    | Bottom-left corner<br/>  |
| <span id="WMSZ_BOTTOMRIGHT"></span><span id="wmsz_bottomright"></span><dl> <dt>**WMSZ\_BOTTOMRIGHT**</dt> <dt>8</dt> </dl> | Bottom-right corner<br/> |
| <span id="WMSZ_LEFT"></span><span id="wmsz_left"></span><dl> <dt>**WMSZ\_LEFT**</dt> <dt>1</dt> </dl>                      | Left edge<br/>           |
| <span id="WMSZ_RIGHT"></span><span id="wmsz_right"></span><dl> <dt>**WMSZ\_RIGHT**</dt> <dt>2</dt> </dl>                   | Right edge<br/>          |
| <span id="WMSZ_TOP"></span><span id="wmsz_top"></span><dl> <dt>**WMSZ\_TOP**</dt> <dt>3</dt> </dl>                         | Top edge<br/>            |
| <span id="WMSZ_TOPLEFT"></span><span id="wmsz_topleft"></span><dl> <dt>**WMSZ\_TOPLEFT**</dt> <dt>4</dt> </dl>             | Top-left corner<br/>     |
| <span id="WMSZ_TOPRIGHT"></span><span id="wmsz_topright"></span><dl> <dt>**WMSZ\_TOPRIGHT**</dt> <dt>5</dt> </dl>          | Top-right corner<br/>    |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure with the screen coordinates of the drag rectangle. To change the size or position of the drag rectangle, an application must change the members of this structure.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return **TRUE** if it processes this message.

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

[**WM\_MOVING**](wm-moving.md)
</dt> <dt>

[**WM\_SIZE**](wm-size.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**RECT**](/previous-versions//dd162897(v=vs.85))
</dt> </dl>

 

 
