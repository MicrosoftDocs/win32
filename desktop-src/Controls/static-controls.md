---
title: Static Control
description: This section contains information about the programming elements used with static controls. A static control is a control that enables an application to provide the user with informational text and graphics that typically require no response.
ms.assetid: 'vs|controls|~\controls\staticcontrols\staticcontrols.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Static Control

This section contains information about the programming elements used with static controls. A *static control* is a control that enables an application to provide the user with informational text and graphics that typically require no response.

### Overviews



| Topic                                              | Contents                                                              |
|----------------------------------------------------|-----------------------------------------------------------------------|
| [About Static Controls](about-static-controls.md) | This topic discusses how static controls are used.<br/>         |
| [Static Control Styles](static-control-styles.md) |                                                                       |
| [Using Static Controls](using-static-controls.md) | This topic provides an example that uses a static control.<br/> |



 

### Messages



| Topic                                 | Contents                                                                                                                                                                        |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**STM\_GETICON**](stm-geticon.md)   | An application sends the [**STM\_GETICON**](stm-geticon.md) message to retrieve a handle to the icon associated with a static control that has the SS\_ICON style. <br/> |
| [**STM\_GETIMAGE**](stm-getimage.md) | An application sends an [**STM\_GETIMAGE**](stm-getimage.md) message to retrieve a handle to the image (icon or bitmap) associated with a static control. <br/>          |
| [**STM\_SETICON**](stm-seticon.md)   | An application sends the [**STM\_SETICON**](stm-seticon.md) message to associate an icon with an icon control. <br/>                                                     |
| [**STM\_SETIMAGE**](stm-setimage.md) | An application sends an [**STM\_SETIMAGE**](stm-setimage.md) message to associate a new image with a static control.<br/>                                                |



 

### Notifications



| Topic                                           | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [STN\_CLICKED](stn-clicked.md)                 | The [STN\_CLICKED](stn-clicked.md) notification code is sent when the user clicks a static control that has the [**SS\_NOTIFY**](static-control-styles.md) style. The parent window of the control receives this notification code through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.<br/>                                                                                                                                                                  |
| [STN\_DBLCLK](stn-dblclk.md)                   | The [STN\_DBLCLK](stn-dblclk.md) notification code is sent when the user double-clicks a static control that has the **SS\_NOTIFY** style. The parent window of the control receives this notification code through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.<br/>                                                                                                                                                                                          |
| [STN\_DISABLE](stn-disable.md)                 | The [STN\_DISABLE](stn-disable.md) notification code is sent when a static control is disabled. The static control must have the **SS\_NOTIFY** style to receive this notification code. The parent window of the control receives this notification code through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.<br/>                                                                                                                                            |
| [STN\_ENABLE](stn-enable.md)                   | The [STN\_ENABLE](stn-enable.md) notification code is sent when a static control is enabled. The static control must have the **SS\_NOTIFY** style to receive this notification code. The parent window of the control receives this notification code through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.<br/>                                                                                                                                               |
| [**WM\_CTLCOLORSTATIC**](wm-ctlcolorstatic.md) | A static control, or an edit control that is read-only or disabled, sends the [**WM\_CTLCOLORSTATIC**](wm-ctlcolorstatic.md) message to its parent window when the control is about to be drawn. By responding to this message, the parent window can use the specified device context handle to set the text and background colors of the static control. <br/> A window receives this message through its [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc) function. <br/> |



 

 

