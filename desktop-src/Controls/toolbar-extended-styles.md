---
title: Toolbar Extended Styles (CommCtrl.h)
description: This section lists the extended styles supported by toolbar controls.
ms.assetid: da31dbbf-8d0a-4711-a1af-382c62e653cd
topic_type:
- apiref
api_name:
- TBSTYLE_EX_DRAWDDARROWS
- TBSTYLE_EX_HIDECLIPPEDBUTTONS
- TBSTYLE_EX_DOUBLEBUFFER
- TBSTYLE_EX_MIXEDBUTTONS
- TBSTYLE_EX_MULTICOLUMN
- TBSTYLE_EX_VERTICAL
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Toolbar Extended Styles

This section lists the extended styles supported by toolbar controls.




| Constant | Description | 
|----------|-------------|
| <span id="TBSTYLE_EX_DRAWDDARROWS"></span><span id="tbstyle_ex_drawddarrows"></span><dl><dt><strong>TBSTYLE_EX_DRAWDDARROWS</strong></dt></dl> | <a href="common-control-versions.md">Version 4.71</a>. This style allows buttons to have a separate dropdown arrow. Buttons that have the <a href="toolbar-control-and-button-styles.md"><strong>BTNS_DROPDOWN</strong></a> style will be drawn with a dropdown arrow in a separate section, to the right of the button. If the arrow is clicked, only the arrow portion of the button will depress, and the toolbar control will send a <a href="tbn-dropdown.md">TBN_DROPDOWN</a> notification code to prompt the application to display the dropdown menu. If the main part of the button is clicked, the toolbar control sends a WM_COMMAND message with the button's ID. The application normally responds by launching the first command on the menu.<br /> There are many situations where you may want to have only some of the dropdown buttons on a toolbar with separated arrows. To do so, set the TBSTYLE_EX_DRAWDDARROWS extended style. Give those buttons that will not have separated arrows the <a href="toolbar-control-and-button-styles.md"><strong>BTNS_WHOLEDROPDOWN</strong></a> style. Buttons with this style will have an arrow displayed next to the image. However, the arrow will not be separate and when any part of the button is clicked, the toolbar control will send a <a href="tbn-dropdown.md">TBN_DROPDOWN</a> notification code. To prevent repainting problems, this style should be set before the toolbar control becomes visible.<br /> | 
| <span id="TBSTYLE_EX_HIDECLIPPEDBUTTONS"></span><span id="tbstyle_ex_hideclippedbuttons"></span><dl><dt><strong>TBSTYLE_EX_HIDECLIPPEDBUTTONS</strong></dt></dl> | <a href="common-control-versions.md">Version 5.81</a>. This style hides partially clipped buttons. The most common use of this style is for toolbars that are part of a rebar control. If an adjacent band covers part of a button, the button will not be displayed. However, if the rebar band has the <a href="/windows/win32/api/commctrl/ns-commctrl-rebarbandinfoa"><strong>RBBS_USECHEVRON</strong></a> style, the button will be displayed on the chevron's dropdown menu. <br /> | 
| <span id="TBSTYLE_EX_DOUBLEBUFFER"></span><span id="tbstyle_ex_doublebuffer"></span><dl><dt><strong>TBSTYLE_EX_DOUBLEBUFFER</strong></dt></dl> | <a href="common-control-versions.md">Version 6</a>. This style requires the toolbar to be double buffered. Double buffering is a mechanism that detects when the toolbar has changed. <br /><blockquote>[!Note]<br />Comctl32.dll version 6 is not redistributable but it is included in Windows or later. To use Comctl32.dll version 6, specify it in a manifest. For more information on manifests, see <a href="cookbook-overview.md">Enabling Visual Styles</a>.</blockquote><br /> | 
| <span id="TBSTYLE_EX_MIXEDBUTTONS"></span><span id="tbstyle_ex_mixedbuttons"></span><dl><dt><strong>TBSTYLE_EX_MIXEDBUTTONS</strong></dt></dl> | <a href="common-control-versions.md">Version 5.81</a>. This style allows you to set text for all buttons, but only display it for those buttons with the <a href="toolbar-control-and-button-styles.md"><strong>BTNS_SHOWTEXT</strong></a> button style. The <a href="toolbar-control-and-button-styles.md"><strong>TBSTYLE_LIST</strong></a> style must also be set. Normally, when a button does not display text, your application must handle <a href="tbn-getinfotip.md">TBN_GETINFOTIP</a> or <a href="ttn-getdispinfo.md">TTN_GETDISPINFO</a> to display a tooltip. With the TBSTYLE_EX_MIXEDBUTTONS extended style, text that is set but not displayed on a button will automatically be used as the button's tooltip text. Your application only needs to handle TBN_GETINFOTIP or or TTN_GETDISPINFO if it needs more flexibility in specifying the tooltip text. <br /> | 
| <span id="TBSTYLE_EX_MULTICOLUMN"></span><span id="tbstyle_ex_multicolumn"></span><dl><dt><strong>TBSTYLE_EX_MULTICOLUMN</strong></dt></dl> | <a href="common-control-versions.md">Version 5.82</a>. <strong>Intended for internal use; not recommended for use in applications.</strong> This style gives the toolbar a vertical orientation and organizes the toolbar buttons into columns. The buttons flow down vertically until a button has exceeded the bounding height of the toolbar (see <a href="tb-setboundingsize.md"><strong>TB_SETBOUNDINGSIZE</strong></a>), and then a new column is created. The toolbar flows the buttons in this manner until all buttons are positioned. To use this style, the TBSTYLE_EX_VERTICAL style must also be set. <br /><blockquote>[!Note]<br />This style may not be supported in future versions of Comctl32.dll. Also, this style is not defined in commctrl.h. Add the following definition to the source files of your application to use this style: <code>#define TBSTYLE_EX_MULTICOLUMN 0x00000002</code></blockquote><br /> | 
| <span id="TBSTYLE_EX_VERTICAL"></span><span id="tbstyle_ex_vertical"></span><dl><dt><strong>TBSTYLE_EX_VERTICAL</strong></dt></dl> | <a href="common-control-versions.md">Version 5.82</a>. <strong>Intended for internal use; not recommended for use in applications.</strong> This style gives the toolbar a vertical orientation. Toolbar buttons flow from top to bottom instead of horizontally. <br /><blockquote>[!Note]<br />This style may not be supported in future versions of Comctl32.dll. Also, this style is not defined in commctrl.h. Add the following definition to the source files of your application to use this style: <code>#define TBSTYLE_EX_VERTICAL 0x00000004</code></blockquote><br /> | 




## Remarks

To set an extended style, send the toolbar control a [**TB\_SETEXTENDEDSTYLE**](tb-setextendedstyle.md) message. To determine what extended styles are currently set, send a [**TB\_GETEXTENDEDSTYLE**](tb-getextendedstyle.md) message.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





