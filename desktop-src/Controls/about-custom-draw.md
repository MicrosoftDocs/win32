---
title: About Custom Draw
description: This section contains general information about custom draw functionality and provides a conceptual overview of how an application can support custom draw.
ms.assetid: dd104661-1e0c-4569-9753-817bcded1894
ms.topic: article
ms.date: 05/31/2018
---

# About Custom Draw

This section contains general information about custom draw functionality and provides a conceptual overview of how an application can support custom draw. Currently, the following controls support custom draw functionality:

-   Header controls
-   List-view controls
-   Rebar controls
-   Toolbar controls
-   Tooltip controls
-   Trackbar controls
-   Tree-view controls

<!-- -->

-   [About Custom Draw Notification Messages](#about-custom-draw-notification-messages)
-   [Paint Cycles, Drawing Stages, and Notification Messages](#paint-cycles-drawing-stages-and-notification-messages)
-   [Taking Advantage of Custom Draw Services](#taking-advantage-of-custom-draw-services)
    -   [Responding to the prepaint notification](#responding-to-the-prepaint-notification)
    -   [Requesting item-specific notifications](#requesting-item-specific-notifications)
    -   [Drawing the item yourself](#drawing-the-item-yourself)
    -   [Changing fonts and colors](#changing-fonts-and-colors)
-   [Custom Draw With List-View and Tree-View Controls](#custom-draw-with-list-view-and-tree-view-controls)
    -   [Custom Draw With List-View Controls](#custom-draw-with-list-view-controls)
-   [Related topics](#related-topics)

## About Custom Draw Notification Messages

All common controls that support custom draw send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes at specific points during drawing operations. These notification codes describe drawing operations that apply to the entire control as well as drawing operations specific to items within the control. Like many notification codes, NM\_CUSTOMDRAW notifications are sent as [**WM\_NOTIFY**](wm-notify.md) messages.

The *lParam* parameter of a custom draw notification will be the address of an [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure or a control-specific structure that contains an **NMCUSTOMDRAW** structure as its first member. The following table illustrates the relationship between the controls and the structures they use.



| Structure                                | Used by                              |
|------------------------------------------|--------------------------------------|
| [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw)     | Rebar, trackbar, and header controls |
| [**NMLVCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmlvcustomdraw) | List-view controls                   |
| [**NMTBCUSTOMDRAW**](/windows/desktop/api/Commctrl/ns-commctrl-nmtbcustomdraw) | Toolbar controls                     |
| [**NMTTCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmttcustomdraw) | Tooltip controls                     |
| [**NMTVCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmtvcustomdraw) | Tree-view controls                   |



 

## Paint Cycles, Drawing Stages, and Notification Messages

Like all Windows applications, common controls periodically paint and erase themselves based on messages received from the system or other applications. The process of a control painting or erasing itself is called a *paint cycle*. Controls that support custom draw send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes periodically through each paint cycle. This notification code is accompanied by an [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure or another structure that contains an **NMCUSTOMDRAW** structure as its first member.

One piece of information that the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure contains is the current stage of the paint cycle. This is referred to as the *draw stage* and is represented by the value in the structure's **dwDrawStage** member. A control informs its parent about four basic draw stages. These basic, or global, draw stages are represented in the structure by the following flag values (defined in Commctrl.h).



| Global draw stage values | Description                        |
|--------------------------|------------------------------------|
| CDDS\_PREPAINT           | Before the paint cycle begins.     |
| CDDS\_POSTPAINT          | After the paint cycle is complete. |
| CDDS\_PREERASE           | Before the erase cycle begins.     |
| CDDS\_POSTERASE          | After the erase cycle is complete. |



 

Each of the preceding values can be combined with the CDDS\_ITEM flag to specify draw stages specific to items. For convenience, Commctrl.h contains the following item-specific values.



| Item-specific draw stage values | Description                                                                                                                                                                                                                                                                         |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CDDS\_ITEMPREPAINT              | Before an item is drawn.                                                                                                                                                                                                                                                            |
| CDDS\_ITEMPOSTPAINT             | After an item has been drawn.                                                                                                                                                                                                                                                       |
| CDDS\_ITEMPREERASE              | Before an item is erased.                                                                                                                                                                                                                                                           |
| CDDS\_ITEMPOSTERASE             | After an item has been erased.                                                                                                                                                                                                                                                      |
| CDDS\_SUBITEM                   | [Common Control Versions](common-control-versions.md) 4.71. Flag combined with CDDS\_ITEMPREPAINT or CDDS\_ITEMPOSTPAINT if a subitem is being drawn. This will only be set if [**CDRF\_NOTIFYITEMDRAW**](cdrf-constants.md) is returned from CDDS\_PREPAINT. |



 

Your application must process the [NM\_CUSTOMDRAW](nm-customdraw.md) notification code and then return a specific value that informs the control what it must do. See the following sections for more information about these return values.

## Taking Advantage of Custom Draw Services

The key to harnessing custom draw functionality is in responding to the [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes that a control sends. The return values your application sends in response to these notifications determine the control's behavior for that paint cycle.

This section contains information about how your application can use [NM\_CUSTOMDRAW](nm-customdraw.md) notification return values to determine the control's behavior.

Details are broken into the following topics:

-   [Responding to the prepaint notification](#responding-to-the-prepaint-notification)
-   [Requesting item-specific notifications](#requesting-item-specific-notifications)
-   [Drawing the item yourself](#drawing-the-item-yourself)
-   [Changing fonts and colors](#changing-fonts-and-colors)

### Responding to the prepaint notification

At the beginning of each paint cycle, the control sends the [NM\_CUSTOMDRAW](nm-customdraw.md) notification code, specifying the CDDS\_PREPAINT value in the **dwDrawStage** member of the accompanying NM\_CUSTOMDRAW structure. The value that your application returns to this first notification dictates how and when the control sends subsequent custom draw notifications for the rest of that paint cycle. Your application can return a combination of the following flags in response to the first notification.



| Return value            | Effect                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CDRF\_DODEFAULT         | The control will draw itself. It will not send additional [NM\_CUSTOMDRAW](nm-customdraw.md) notifications for this paint cycle. This flag cannot be used with any other flag.                                                                                                                                                                                                                                                                               |
| CDRF\_DOERASE           | The control will only draw the background.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| CDRF\_NEWFONT           | Your application specified a new font for the item; the control will use the new font. For more information on changing fonts, see [Changing fonts and colors](#changing-fonts-and-colors). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.                                                                                                                                                                                                       |
| CDRF\_NOTIFYITEMDRAW    | The control will notify the parent of any item-specific drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after it draws items.This occurs when **dwDrawStage** equals CDDS\_PREPAINT.                                                                                                                                                                                                                       |
| CDRF\_NOTIFYPOSTERASE   | The control will notify the parent after erasing an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.                                                                                                                                                                                                                                                                                                                                             |
| CDRF\_NOTIFYPOSTPAINT   | The control will send an [NM\_CUSTOMDRAW](nm-customdraw.md) notification when the painting cycle for the entire control is complete. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.                                                                                                                                                                                                                                                                 |
| CDRF\_NOTIFYSUBITEMDRAW | [Version 4.71](common-control-versions.md). Your application will receive an [NM\_CUSTOMDRAW](nm-customdraw.md) notification with **dwDrawStage** set to CDDS\_ITEMPREPAINT \| CDDS\_SUBITEM before each list-view subitem is drawn. You can then specify font and color for each subitem separately or return [**CDRF\_DODEFAULT**](cdrf-constants.md) for default processing. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT. |
| CDRF\_SKIPDEFAULT       | Your application drew the item manually. The control will not draw the item. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.                                                                                                                                                                                                                                                                                                                      |
| CDRF\_SKIPPOSTPAINT     | The control will not draw the focus rectangle around an item.                                                                                                                                                                                                                                                                                                                                                                                                 |



 

### Requesting item-specific notifications

If your application returns [**CDRF\_NOTIFYITEMDRAW**](cdrf-constants.md) to the initial prepaint custom draw notification, the control will send notifications for each item it draws during that paint cycle. These item-specific notifications will have the CDDS\_ITEMPREPAINT value in the **dwDrawStage** member of the accompanying [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure. You can request that the control send another notification when it is finished drawing the item by returning [**CDRF\_NOTIFYPOSTPAINT**](cdrf-constants.md) to these item-specific notifications. Otherwise, return [**CDRF\_DODEFAULT**](cdrf-constants.md) and the control will not notify the parent window until it starts to draw the next item.

### Drawing the item yourself

If your application draws the entire item, return [**CDRF\_SKIPDEFAULT**](cdrf-constants.md). This allows the control to skip items that it does not need to draw, thereby decreasing system overhead. Keep in mind that returning this value means the control will not draw any portion of the item.

### Changing fonts and colors

Your application can use custom draw to change an item's font. Simply select the HFONT you want into the device context specified by the **hdc** member of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure associated with the custom draw notification. Since the font you select might have different metrics than the default font, make sure you include the [**CDRF\_NEWFONT**](cdrf-constants.md) bit in the return value for the notification message. For more information on using this functionality, see the sample code in [Using Custom Draw](using-custom-draw.md). The font that your application specifies is used to display that item when it is not selected. Custom draw does not allow you to change the font attributes for selected items.

To change text colors for all controls that support custom draw except for the list view and tree view, simply set the desired text and background colors in the device context supplied in the custom draw notification structure with the [**SetTextColor**](/windows/desktop/api/wingdi/nf-wingdi-settextcolor) and [**SetBkColor**](/windows/desktop/api/wingdi/nf-wingdi-setbkcolor) functions. To modify the text colors in the list view or tree view, you need to place the desired color values in the **clrText** and **clrTextBk** members of the [**NMLVCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmlvcustomdraw) or [**NMTVCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmtvcustomdraw) structure.

> [!Note]  
> Prior to [Version 6.0](common-control-versions.md) of the common controls, toolbars ignore the [**CDRF\_NEWFONT**](cdrf-constants.md) flag. Version 6.0 supports the **CDRF\_NEWFONT** flag, and you can use it to select a different font for the toolbar. However, you cannot change a toolbar's color when a visual style is active. To change a toolbar's color in Version 6.0, you must first disable visual styles by calling [**SetWindowTheme**](/windows/desktop/api/Uxtheme/nf-uxtheme-setwindowtheme) and specifying no visual style:

 


```
SetWindowTheme (hwnd, "", "");
```



## Custom Draw With List-View and Tree-View Controls

Most common controls can be handled in essentially the same way. However, the list-view and tree-view controls have some features that require a somewhat different approach to custom draw.

For [Version 5.0](common-control-versions.md), these two controls may display clipped text if you change the font by returning [**CDRF\_NEWFONT**](cdrf-constants.md). This behavior is necessary for backward compatibility with earlier versions of the common controls. If you want to change the font of a list-view or tree-view control, you will get better results if you send a [**CCM\_SETVERSION**](ccm-setversion.md) message with the *wParam* value set to 5 before adding any items to the control. For an example of a tree-view control that uses custom draw see Knowledge Base article [SAMPLE: CustDTv Illustrates Custom Draw in a TreeView (Q248496)]( https://support.microsoft.com/default.aspx?scid=kb;EN-US;q248496).

### Custom Draw With List-View Controls

Because list-view controls have subitems and multiple display modes, you will need to handle the [NM\_CUSTOMDRAW](nm-customdraw.md) notification somewhat differently than for the other common controls.

For report mode, use the following procedure.

1.  The first [NM\_CUSTOMDRAW](nm-customdraw.md) notification will have the **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure set to CDDS\_PREPAINT. Return [**CDRF\_NOTIFYITEMDRAW**](cdrf-constants.md).
2.  You will then receive an [NM\_CUSTOMDRAW](nm-customdraw.md) notification with **dwDrawStage** set to CDDS\_ITEMPREPAINT. If you specify new fonts or colors and return [**CDRF\_NEWFONT**](cdrf-constants.md), all subitems of the item will be changed. If you want instead to handle each subitem separately, return [**CDRF\_NOTIFYSUBITEMDRAW**](cdrf-constants.md).
3.  If you returned [**CDRF\_NOTIFYSUBITEMDRAW**](cdrf-constants.md) in the previous step, you will then receive an [NM\_CUSTOMDRAW](nm-customdraw.md) notification for each subitem with **dwDrawStage** set to CDDS\_SUBITEM \| CDDS\_ITEMPREPAINT. To change the font or color for that subitem, specify a new font or color and return [**CDRF\_NEWFONT**](cdrf-constants.md).

For the large icon, small icon, and list modes, use the following procedure.

1.  The first [NM\_CUSTOMDRAW](nm-customdraw.md) notification will have the **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure set to CDDS\_PREPAINT. Return [**CDRF\_NOTIFYITEMDRAW**](cdrf-constants.md).
2.  You will then receive an [NM\_CUSTOMDRAW](nm-customdraw.md) notification with **dwDrawStage** set to CDDS\_ITEMPREPAINT. You can change the fonts or colors of an item by specifying new fonts and colors and returning [**CDRF\_NEWFONT**](cdrf-constants.md). Because these modes do not have subitems, you will not receive any additional NM\_CUSTOMDRAW notifications.

For an example of a list-view [NM\_CUSTOMDRAW](nm-customdraw.md) notification handler, see [Using Custom Draw](using-custom-draw.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Using Custom Draw](using-custom-draw.md)
</dt> <dt>

[Custom Draw Reference](custom-draw-reference.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[SAMPLE: CustDTv Illustrates Custom Draw in a TreeView (Q248496)]( https://support.microsoft.com/default.aspx?scid=kb;EN-US;q248496)
</dt> </dl>

 

 