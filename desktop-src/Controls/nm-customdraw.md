---
title: NM_CUSTOMDRAW notification code
description: Notifies a control's parent window about custom drawing operations. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 2ca51ee0-4431-45c0-880c-a8b74318d8a9
keywords:
- NM_CUSTOMDRAW notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_CUSTOMDRAW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NM\_CUSTOMDRAW notification code

Notifies a control's parent window about custom drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CUSTOMDRAW

#ifdef LIST_VIEW_CUSTOM_DRAW

    lpNMCustomDraw = (LPNMLVCUSTOMDRAW) lParam;

#elif TOOL_TIPS_CUSTOM_DRAW

    lpNMCustomDraw = (LPNMTTCUSTOMDRAW) lParam;

#elif TREE_VIEW_CUSTOM_DRAW

    lpNMCustomDraw = (LPNMTVCUSTOMDRAW) lParam;

#elif TOOL_BAR_CUSTOM_DRAW

    lpNMCustomDraw = (LPNMTBCUSTOMDRAW) lParam;

#else

    lpNMCustomDraw = (LPNMCUSTOMDRAW) lParam;

#endif
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a custom draw-related structure that contains information about the drawing operation. The following list specifies the controls and their associated structures.



| Control                     | Custom Draw Structure                    |
|-----------------------------|------------------------------------------|
| Rebar, trackbar, and header | [**NMCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmcustomdrawinfo)     |
| List view                   | [**NMLVCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmlvcustomdraw) |
| Tooltip                     | [**NMTTCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmttcustomdraw) |
| Tree view                   | [**NMTVCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmtvcustomdraw) |
| Toolbar                     | [**NMTBCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-_nmtbcustomdraw) |



 

</dd> </dl>

## Return value

The value your application can return depends on the current drawing stage. The **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmcustomdrawinfo) structure holds a value that specifies the drawing stage. You must return one of the following values.



| Return code                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CDRF\_DODEFAULT**</dt> </dl>         | The control will draw itself. It will not send additional [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes for this paint cycle. This flag cannot be used with any other flag. <br/>                                                                                                                                                                                                                                 |
| <dl> <dt>**CDRF\_DOERASE**</dt> </dl>           | The control will only draw the background.<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**CDRF\_NEWFONT**</dt> </dl>           | Your application specified a new font for the item; the control will use the new font. For more information on changing fonts, see [Changing fonts and colors](custom-draw.md). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                        |
| <dl> <dt>**CDRF\_NOTIFYITEMDRAW**</dt> </dl>    | The control will notify the parent of any item-related drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                |
| <dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> </dl>   | The control will notify the parent after erasing an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                                                                                                                                     |
| <dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> </dl>   | The control will send an [NM\_CUSTOMDRAW](nm-customdraw.md) notification code when the painting cycle for the entire control is complete. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                                                    |
| <dl> <dt>**CDRF\_NOTIFYSUBITEMDRAW**</dt> </dl> | Your application will receive an [NM\_CUSTOMDRAW](nm-customdraw.md) notification code with **dwDrawStage** set to CDDS\_ITEMPREPAINT \| CDDS\_SUBITEM before each list-view subitem is drawn. You can then specify font and color for each subitem separately or return [**CDRF\_DODEFAULT**](cdrf-constants.md) for default processing. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/> |
| <dl> <dt>**CDRF\_SKIPDEFAULT**</dt> </dl>       | Your application drew the item manually. The control will not draw the item. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                                                                                                                                                              |
| <dl> <dt>**CDRF\_SKIPPOSTPAINT**</dt> </dl>     | The control will not draw the focus rectangle around an item.<br/>                                                                                                                                                                                                                                                                                                                                                         |



 

## Remarks

Currently, the following controls support custom draw functionality: header, list view, rebar, toolbar, tooltip, trackbar, and tree view. Custom draw is also supported for button controls if you have an application manifest to ensure that Comctl32.dll version 6 is available.

If this message is handled in a dialog procedure, you must set the return value as part of the window data before returning **TRUE**. For more information, see [**DialogProc**](https://msdn.microsoft.com/library/windows/desktop/ms645469).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Conceptual**
</dt> <dt>

[Custom Draw](custom-draw.md)
</dt> </dl>

 

 





