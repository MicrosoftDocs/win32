---
title: Tooltip
description: This section contains information about the programming elements used with tooltip controls.
ms.assetid: 'vs|controls|~\controls\tooltip\reflist.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Tooltip

This section contains information about the programming elements used with tooltip controls.

### Overviews



| Topic                                              | Contents                                                                                                                          |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [About Tooltip Controls](tooltip-controls.md)     | Tooltips appear automatically, or pop up, when the user pauses the mouse pointer over a tool or some other UI element.<br/> |
| [Using Tooltip Controls](using-tooltip-contro.md) | This section contains examples that demonstrate how to create different types of tooltips.<br/>                             |



 

### Messages



| Topic                                               | Contents                                                                                                                                                                                                          |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TTM\_ACTIVATE**](ttm-activate.md)               | Activates or deactivates a tooltip control. <br/>                                                                                                                                                           |
| [**TTM\_ADDTOOL**](ttm-addtool.md)                 | Registers a tool with a tooltip control. <br/>                                                                                                                                                              |
| [**TTM\_ADJUSTRECT**](ttm-adjustrect.md)           | Calculates a tooltip control's text display rectangle from its window rectangle, or the tooltip window rectangle needed to display a specified text display rectangle. <br/>                                |
| [**TTM\_DELTOOL**](ttm-deltool.md)                 | Removes a tool from a tooltip control. <br/>                                                                                                                                                                |
| [**TTM\_ENUMTOOLS**](ttm-enumtools.md)             | Retrieves the information that a tooltip control maintains about the current tool that is, the tool for which the tooltip is currently displaying text. <br/>                                               |
| [**TTM\_GETBUBBLESIZE**](ttm-getbubblesize.md)     | Returns the width and height of a tooltip control.<br/>                                                                                                                                                     |
| [**TTM\_GETCURRENTTOOL**](ttm-getcurrenttool.md)   | Retrieves the information for the current tool in a tooltip control. <br/>                                                                                                                                  |
| [**TTM\_GETDELAYTIME**](ttm-getdelaytime.md)       | Retrieves the initial, pop-up, and reshow durations currently set for a tooltip control.<br/>                                                                                                               |
| [**TTM\_GETMARGIN**](ttm-getmargin.md)             | Retrieves the top, left, bottom, and right margins set for a tooltip window. A margin is the distance, in pixels, between the tooltip window border and the text contained within the tooltip window. <br/> |
| [**TTM\_GETMAXTIPWIDTH**](ttm-getmaxtipwidth.md)   | Retrieves the maximum width for a tooltip window. <br/>                                                                                                                                                     |
| [**TTM\_GETTEXT**](ttm-gettext.md)                 | Retrieves the information a tooltip control maintains about a tool. <br/>                                                                                                                                   |
| [**TTM\_GETTIPBKCOLOR**](ttm-gettipbkcolor.md)     | Retrieves the background color in a tooltip window. <br/>                                                                                                                                                   |
| [**TTM\_GETTIPTEXTCOLOR**](ttm-gettiptextcolor.md) | Retrieves the text color in a tooltip window. <br/>                                                                                                                                                         |
| [**TTM\_GETTITLE**](ttm-gettitle.md)               | Retrieve information concerning the title of a tooltip control.<br/>                                                                                                                                        |
| [**TTM\_GETTOOLCOUNT**](ttm-gettoolcount.md)       | Retrieves a count of the tools maintained by a tooltip control. <br/>                                                                                                                                       |
| [**TTM\_GETTOOLINFO**](ttm-gettoolinfo.md)         | Retrieves the information that a tooltip control maintains about a tool. <br/>                                                                                                                              |
| [**TTM\_HITTEST**](ttm-hittest.md)                 | Tests a point to determine whether it is within the bounding rectangle of the specified tool and, if it is, retrieves information about the tool. <br/>                                                     |
| [**TTM\_NEWTOOLRECT**](ttm-newtoolrect.md)         | Sets a new bounding rectangle for a tool. <br/>                                                                                                                                                             |
| [**TTM\_POP**](ttm-pop.md)                         | Removes a displayed tooltip window from view. <br/>                                                                                                                                                         |
| [**TTM\_POPUP**](ttm-popup.md)                     | Causes the tooltip to display at the coordinates of the last mouse message.<br/>                                                                                                                            |
| [**TTM\_RELAYEVENT**](ttm-relayevent.md)           | Passes a mouse message to a tooltip control for processing. <br/>                                                                                                                                           |
| [**TTM\_SETDELAYTIME**](ttm-setdelaytime.md)       | Sets the initial, pop-up, and reshow durations for a tooltip control.<br/>                                                                                                                                  |
| [**TTM\_SETMARGIN**](ttm-setmargin.md)             | Sets the top, left, bottom, and right margins for a tooltip window. A margin is the distance, in pixels, between the tooltip window border and the text contained within the tooltip window. <br/>          |
| [**TTM\_SETMAXTIPWIDTH**](ttm-setmaxtipwidth.md)   | Sets the maximum width for a tooltip window. <br/>                                                                                                                                                          |
| [**TTM\_SETTIPBKCOLOR**](ttm-settipbkcolor.md)     | Sets the background color in a tooltip window. <br/>                                                                                                                                                        |
| [**TTM\_SETTIPTEXTCOLOR**](ttm-settiptextcolor.md) | Sets the text color in a tooltip window. <br/>                                                                                                                                                              |
| [**TTM\_SETTITLE**](ttm-settitle.md)               | Adds a standard icon and title string to a tooltip.<br/>                                                                                                                                                    |
| [**TTM\_SETTOOLINFO**](ttm-settoolinfo.md)         | Sets the information that a tooltip control maintains for a tool. <br/>                                                                                                                                     |
| [**TTM\_SETWINDOWTHEME**](ttm-setwindowtheme.md)   | Sets the visual style of a tooltip control.<br/>                                                                                                                                                            |
| [**TTM\_TRACKACTIVATE**](ttm-trackactivate.md)     | Activates or deactivates a tracking tooltip.<br/>                                                                                                                                                           |
| [**TTM\_TRACKPOSITION**](ttm-trackposition.md)     | Sets the position of a tracking tooltip.<br/>                                                                                                                                                               |
| [**TTM\_UPDATE**](ttm-update.md)                   | Forces the current tooltip to be redrawn. <br/>                                                                                                                                                             |
| [**TTM\_UPDATETIPTEXT**](ttm-updatetiptext.md)     | Sets the tooltip text for a tool. <br/>                                                                                                                                                                     |
| [**TTM\_WINDOWFROMPOINT**](ttm-windowfrompoint.md) | Allows a subclass procedure to cause a tooltip to display text for a window other than the one beneath the mouse cursor. <br/>                                                                              |



 

### Notifications



| Topic                                                 | Contents                                                                                                                                                                                                                                                              |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NM\_CUSTOMDRAW (Tooltip)](nm-customdraw-tooltip.md) | Sent by a tooltip control to notify its parent windows about drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                 |
| [TTN\_GETDISPINFO](ttn-getdispinfo.md)               | Sent by a tooltip control to retrieve information needed to display a tooltip window. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                            |
| [TTN\_LINKCLICK](ttn-linkclick.md)                   | Sent when a text link inside a balloon tooltip is clicked. <br/>                                                                                                                                                                                                |
| [TTN\_NEEDTEXT](ttn-needtext.md)                     | Sent by a tooltip control to retrieve information needed to display a tooltip window. This notification is identical to [TTN\_GETDISPINFO](ttn-getdispinfo.md). This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |
| [TTN\_POP](ttn-pop.md)                               | Notifies the owner window that a tooltip is about to be hidden. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                  |
| [TTN\_SHOW](ttn-show.md)                             | Notifies the owner window that a tooltip control is about to be displayed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                       |



 

### Structures



| Topic                                    | Contents                                                                                                                                                                                                                           |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NMTTCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmttcustomdraw) | Contains information specific to an [NM\_CUSTOMDRAW](nm-customdraw-tooltip.md) notification code sent by a tooltip control. <br/>                                                                                           |
| [**NMTTDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmttdispinfoa)     | Contains information used in handling the [TTN\_GETDISPINFO](ttn-getdispinfo.md) notification code. This structure supersedes the **TOOLTIPTEXT** structure. <br/>                                                          |
| [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa)             | The [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure contains information about a tool in a tooltip control.<br/>                                                                                                                      |
| [**TTGETTITLE**](/windows/desktop/api/Commctrl/ns-commctrl-ttgettitle)         | Provides information about the title of a tooltip control. <br/>                                                                                                                                                             |
| [**TTHITTESTINFO**](/windows/win32/api/commctrl/ns-commctrl-tthittestinfoa)   | Contains information that a tooltip control uses to determine whether a point is in the bounding rectangle of the specified tool. If the point is in the rectangle, the structure receives information about the tool. <br/> |



 

### Constants



| Topic                                | Contents                                                                     |
|--------------------------------------|------------------------------------------------------------------------------|
| [Tooltip Styles](tooltip-styles.md) | This section lists the control styles used with tooltip controls.<br/> |



 

 

 





