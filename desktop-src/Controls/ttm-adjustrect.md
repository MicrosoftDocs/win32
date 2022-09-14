---
title: TTM_ADJUSTRECT message (Commctrl.h)
description: Calculates a tooltip control's text display rectangle from its window rectangle, or the tooltip window rectangle needed to display a specified text display rectangle.
ms.assetid: b848c16f-9f41-4ed2-918a-9c03aebe535c
keywords:
- TTM_ADJUSTRECT message Windows Controls
topic_type:
- apiref
api_name:
- TTM_ADJUSTRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_ADJUSTRECT message

Calculates a tooltip control's text display rectangle from its window rectangle, or the tooltip window rectangle needed to display a specified text display rectangle.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value that specifies which operation to perform. If **TRUE**, *lParam* is used to specify a text-display rectangle and it receives the corresponding window rectangle. If **FALSE**, *lParam* is used to specify a window rectangle and it receives the corresponding text display rectangle.

</dd> <dt>

*lParam* 
</dt> <dd>

**RECT** structure to hold either a tooltip window rectangle or a text display rectangle.

</dd> </dl>

## Return value

Returns a nonzero value if the rectangle is successfully adjusted, and returns zero if an error occurs.

## Remarks

This message is particularly useful when you want to use a tooltip control to display the full text of a string that is usually truncated. It is commonly used with listview and treeview controls. You typically send this message in response to a [TTN\_SHOW](ttn-show.md) notification code so that you can position the tooltip control properly.

The tooltip window rectangle is somewhat larger than the text display rectangle that bounds the tooltip string. The window origin is also offset up and to the left from the origin of the text display rectangle. To position the text display rectangle, you must calculate the corresponding window rectangle and use that rectangle to position the tooltip. **TTM\_ADJUSTRECT** handles this calculation for you.

If you set *wParam* to **TRUE**, **TTM\_ADJUSTRECT** takes the size and position of the desired tooltip text display rectangle, and passes back the size and position of the tooltip window needed to display the text in the specified position. If you set *wParam* to **FALSE**, you can specify a tooltip window rectangle and **TTM\_ADJUSTRECT** will return the size and position of its text rectangle.

The following code fragment illustrates the use of the **TTM\_ADJUSTRECT** message to position a tooltip control to display the full text of a control's string in place of a truncated string. The application-defined **GetMyItemRect** function returns the text rectangle that will be needed to display the tooltip text directly over the truncated string. The details of how this function is implemented will depend on the particular control. **TTM\_ADJUSTRECT** is used to send this text rectangle to the tooltip control. It returns an appropriately sized and positioned window rectangle that is then used to position the tooltip window.


```
case TTN_SHOW:

if (MyStringIsTruncated) {
    RECT rc;
    
    GetMyItemRect(&rc);
    SendMessage(hwndToolTip, TTM_ADJUSTRECT, TRUE, (LPARAM)&rc);
    SetWindowPos(hwndToolTip,
                 NULL,
                 rc.left, rc.top,
                 0, 0,
                 SWP_NOSIZE|SWP_NOZORDER|SWP_NOACTIVATE);
} 
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





