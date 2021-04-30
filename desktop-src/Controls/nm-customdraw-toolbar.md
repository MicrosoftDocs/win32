---
title: NM_CUSTOMDRAW (toolbar) notification code (Commctrl.h)
description: Sent by a toolbar to notify its parent window about drawing operations. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: e83a85f4-7955-411d-9a08-29f5b30158c5
keywords:
- NM_CUSTOMDRAW (toolbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_CUSTOMDRAW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_CUSTOMDRAW (toolbar) notification code

Sent by a toolbar to notify its parent window about drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CUSTOMDRAW
        
    lpNMCustomDraw = (LPNMCUSTOMDRAW) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

[Version 4.70](common-control-versions.md). Pointer to an [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure that contains information about the drawing operation. The **dwItemSpec** member of this structure contains the command identifier of the item being drawn. The **lItemlParam** member of this structure contains the **dwData** value for the item being drawn.

[Version 4.71](common-control-versions.md). Pointer to an [**NMTBCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-nmtbcustomdraw) structure that contains information about the drawing operation. The **dwItemSpec** member of the **nmcd** member of this structure contains the command identifier of the item being drawn. The **lItemlParam** member of the **nmcd** member of this structure contains the **dwData** value for the item being drawn.

</dd> </dl>

## Return value

The value your application can return depends on the current drawing stage. The **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure holds a value that specifies the drawing stage. You must return one of the following values.



| Return code                                                                                            | Description                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CDRF\_DODEFAULT**</dt> </dl>         | The control will draw itself. It will not send any additional [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes for this paint cycle. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                             |
| <dl> <dt>**CDRF\_NOTIFYITEMDRAW**</dt> </dl>    | The control will notify the parent of any item-related drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                         |
| <dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> </dl>   | The control will notify the parent after erasing an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                              |
| <dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> </dl>   | The control will notify the parent after painting an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                             |
| <dl> <dt>**CDRF\_NOTIFYSUBITEMDRAW**</dt> </dl> | [Version 4.71](common-control-versions.md). The control will notify the parent when a list-view subitem is being drawn. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                               |
| <dl> <dt>**CDRF\_NEWFONT**</dt> </dl>           | Your application specified a new font for the item; the control will use the new font. For more information on changing fonts, see [Changing fonts and colors](custom-draw.md). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/> |
| <dl> <dt>**CDRF\_SKIPDEFAULT**</dt> </dl>       | Your application drew the item manually. The control will not draw the item. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                       |
| <dl> <dt>**TBCDRF\_BLENDICON**</dt> </dl>       | [Version 5.00](common-control-versions.md). Blend the button 50 percent with the background. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                      |
| <dl> <dt>**TBCDRF\_NOBACKGROUND**</dt> </dl>    | [Version 5.00](common-control-versions.md). Do not draw button background. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                        |
| <dl> <dt>**TBCDRF\_NOEDGES**</dt> </dl>         | [Version 4.71](common-control-versions.md). Do not draw button edges. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                             |
| <dl> <dt>**TBCDRF\_HILITEHOTTRACK**</dt> </dl>  | [Version 4.71](common-control-versions.md). Use the **clrHighlightHotTrack** member of the [**NMTBCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-nmtbcustomdraw) structure to draw the background of hot-tracked items. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                        |
| <dl> <dt>**TBCDRF\_NOOFFSET**</dt> </dl>        | [Version 4.71](common-control-versions.md). Do not offset the button when pressed. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                |
| <dl> <dt>**TBCDRF\_NOMARK**</dt> </dl>          | Do not draw default highlight of items that have the [**TBSTATE\_MARKED**](toolbar-button-states.md). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                              |
| <dl> <dt>**TBCDRF\_NOETCHEDEFFECT**</dt> </dl>  | [Version 4.71](common-control-versions.md). Do not draw etched effect for disabled items. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                         |
| <dl> <dt>**TBCDRF\_USECDCOLORS**</dt> </dl>     | [Version 6.00](common-control-versions.md), **Windows Vista** only. Use custom draw colors to render text regardless of visual style.<br/>                                                                                                                                         |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[Using Custom Draw](custom-draw.md)
</dt> </dl>

 

 





