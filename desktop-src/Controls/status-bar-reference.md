---
title: Status Bar
description: This section contains information about the programming elements used with status bar controls.
ms.assetid: 77923055-9d00-4528-bda7-b602a26b577f
ms.topic: article
ms.date: 05/31/2018
---

# Status Bar

This section contains information about the programming elements used with status bar controls.

### Overviews



| Topic                          | Contents                                                                                                                                                   |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Status Bars](status-bars.md) | A *status bar* is a horizontal window at the bottom of a parent window in which an application can display various kinds of status information.<br/> |



 

### Functions




| Topic | Contents | 
|-------|----------|
| <a href="/windows/desktop/api/Commctrl/nf-commctrl-createstatuswindowa"><strong>CreateStatusWindow</strong></a> | Creates a status window, which is typically used to display the status of an application. The window generally appears at the bottom of the parent window, and it contains the specified text.<blockquote>[!Note]<br />This function is obsolete. Use <a href="/windows/desktop/api/winuser/nf-winuser-createwindowa"><strong>CreateWindow</strong></a> instead.</blockquote><br /><br /> | 
| <a href="/windows/desktop/api/Commctrl/nf-commctrl-drawstatustexta"><strong>DrawStatusText</strong></a> | The <a href="/windows/desktop/api/Commctrl/nf-commctrl-drawstatustexta"><strong>DrawStatusText</strong></a> function draws the specified text in the style of a status window with borders.<br /> | 
| <a href="/windows/desktop/api/Commctrl/nf-commctrl-menuhelp"><strong>MenuHelp</strong></a> | Processes <a href="/windows/desktop/menurc/wm-menuselect"><strong>WM_MENUSELECT</strong></a> and <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> messages and displays Help text about the current menu in the specified status window.<br /> | 




 

### Messages



| Topic                                               | Contents                                                                                                                                                                                             |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SB\_GETBORDERS**](sb-getborders.md)             | Retrieves the current widths of the horizontal and vertical borders of a status window. <br/>                                                                                                  |
| [**SB\_GETICON**](sb-geticon.md)                   | Retrieves the icon for a part in a status bar. <br/>                                                                                                                                           |
| [**SB\_GETPARTS**](sb-getparts.md)                 | Retrieves a count of the parts in a status window. The message also retrieves the coordinate of the right edge of the specified number of parts. <br/>                                         |
| [**SB\_GETRECT**](sb-getrect.md)                   | Retrieves the bounding rectangle of a part in a status window. <br/>                                                                                                                           |
| [**SB\_GETTEXT**](sb-gettext.md)                   | The [**SB\_GETTEXT**](sb-gettext.md) message retrieves the text from the specified part of a status window. <br/>                                                                             |
| [**SB\_GETTEXTLENGTH**](sb-gettextlength.md)       | The [**SB\_GETTEXTLENGTH**](sb-gettextlength.md) message retrieves the length, in characters, of the text from the specified part of a status window. <br/>                                   |
| [**SB\_GETTIPTEXT**](sb-gettiptext.md)             | Retrieves the tooltip text for a part in a status bar. The status bar must be created with the [**SBT\_TOOLTIPS**](status-bar-styles.md) style to enable tooltips. <br/>         |
| [**SB\_GETUNICODEFORMAT**](sb-getunicodeformat.md) | Retrieves the Unicode character format flag for the control. <br/>                                                                                                                             |
| [**SB\_ISSIMPLE**](sb-issimple.md)                 | Checks a status bar control to determine if it is in simple mode. <br/>                                                                                                                        |
| [**SB\_SETBKCOLOR**](sb-setbkcolor.md)             | Sets the background color in a status bar. <br/>                                                                                                                                               |
| [**SB\_SETICON**](sb-seticon.md)                   | Sets the icon for a part in a status bar. <br/>                                                                                                                                                |
| [**SB\_SETMINHEIGHT**](sb-setminheight.md)         | Sets the minimum height of a status window's drawing area. <br/>                                                                                                                               |
| [**SB\_SETPARTS**](sb-setparts.md)                 | Sets the number of parts in a status window and the coordinate of the right edge of each part. <br/>                                                                                           |
| [**SB\_SETTEXT**](sb-settext.md)                   | The SB\_SETTEXT message sets the text in the specified part of a status window.<br/>                                                                                                           |
| [**SB\_SETTIPTEXT**](sb-settiptext.md)             | Sets the tooltip text for a part in a status bar. The status bar must have been created with the [**SBT\_TOOLTIPS**](status-bar-styles.md) style to enable tooltips.<br/>        |
| [**SB\_SETUNICODEFORMAT**](sb-setunicodeformat.md) | Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control. <br/> |
| [**SB\_SIMPLE**](sb-simple.md)                     | Specifies whether a status window displays simple text or displays all window parts set by a previous [**SB\_SETPARTS**](sb-setparts.md) message. <br/>                                       |



 

### Notifications



| Topic                                                 | Contents                                                                                                                                                                                                                                                           |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NM\_CLICK (status bar)](nm-click-status-bar.md)     | Notifies the parent window of a status bar control that the user has clicked the left mouse button within the control. [NM\_CLICK (status bar)](nm-click-status-bar.md) is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>              |
| [NM\_DBLCLK (status bar)](nm-dblclk-status-bar.md)   | Notifies the parent window of a status bar control that the user has double-clicked the left mouse button within the control. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                       |
| [NM\_RCLICK (status bar)](nm-rclick-status-bar.md)   | Notifies the parent window of a status bar control that the user has clicked the right mouse button within the control. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                             |
| [NM\_RDBLCLK (status bar)](nm-rdblclk-status-bar.md) | Notifies the parent windows of a status bar control that the user has double-clicked the right mouse button within the control. [NM\_RDBLCLK (status bar)](nm-rdblclk-status-bar.md) is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/> |
| [SBN\_SIMPLEMODECHANGE](sbn-simplemodechange.md)     | Sent by a status bar control when the simple mode changes due to a [**SB\_SIMPLE**](sb-simple.md) message. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                        |



 

### Constants



| Topic                                      | Contents                                                                                                              |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [Status Bar Styles](status-bar-styles.md) | This section lists the styles, in addition to standard window styles, supported by *status bar* controls. <br/> |



 

 

