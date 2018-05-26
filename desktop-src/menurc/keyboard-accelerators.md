---
title: Keyboard Accelerators
description: This section discusses keyboard accelerators. A keyboard accelerator is a keystroke or combination of keystrokes that generates a command message for an application.
ms.assetid: cbf7619d-289d-40c9-9a06-6ce47026d43f
keywords:
- user input,keyboard accelerators
- capturing user input,keyboard accelerators
- keyboard accelerators
- accelerators
- WM_COMMAND message
- WM_SYS COMMAND message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Keyboard Accelerators

A *keyboard accelerator* (or, simply, accelerator) is a keystroke or combination of keystrokes that generates a [**WM\_COMMAND**](wm-command.md) or [**WM\_SYSCOMMAND**](wm-syscommand.md) message for an application.

### In This Section



| Name                                                                 | Description                                                                |
|----------------------------------------------------------------------|----------------------------------------------------------------------------|
| [About Keyboard Accelerators](about-keyboard-accelerators.md)       | Discusses keyboard accelerators.<br/>                                |
| [Using Keyboard Accelerators](using-keyboard-accelerators.md)       | Discusses tasks that are associated with keyboard accelerators.<br/> |
| [Keyboard Accelerator Reference](keyboard-accelerator-reference.md) | Contains the API reference.<br/>                                     |



 

### Keyboard Accelerator Functions



| Name                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CopyAcceleratorTable**](/windows/win32/Winuser/nf-winuser-copyacceleratortablea?branch=master)       | Copies the specified accelerator table. This function is used to obtain the accelerator-table data that corresponds to an accelerator-table handle, or to determine the size of the accelerator-table data. <br/>                                                                                                                                                                                                                                                                                                                                                                    |
| [**CreateAcceleratorTable**](/windows/win32/Winuser/nf-winuser-createacceleratortablea?branch=master)   | Creates an accelerator table. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**DestroyAcceleratorTable**](/windows/win32/Winuser/nf-winuser-destroyacceleratortable?branch=master) | Destroys an accelerator table.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**LoadAccelerators**](/windows/win32/Winuser/nf-winuser-loadacceleratorsa?branch=master)               | Loads the specified accelerator table. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [**TranslateAccelerator**](/windows/win32/Winuser/nf-winuser-translateacceleratora?branch=master)       | Processes accelerator keys for menu commands. The function translates a [**WM\_KEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646280) or [**WM\_SYSKEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646286) message to a [**WM\_COMMAND**](wm-command.md) or [**WM\_SYSCOMMAND**](wm-syscommand.md) message (if there is an entry for the key in the specified accelerator table) and then sends the **WM\_COMMAND** or **WM\_SYSCOMMAND** message directly to the specified window procedure. [**TranslateAccelerator**](/windows/win32/Winuser/nf-winuser-translateacceleratora?branch=master) does not return until the window procedure has processed the message. <br/> |



 

### Keyboard Accelerator Messages



| Name                                          | Description                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CHANGEUISTATE**](wm-changeuistate.md) | Sent to indicate that the UI state should be changed.<br/>                                                                                                                                                                                                                                                  |
| [**WM\_INITMENU**](wm-initmenu.md)           | Sent when a menu is about to become active. It occurs when the user clicks an item on the menu bar or presses a menu key. This allows the application to modify the menu before it is displayed. <br/> A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. <br/> |
| [**WM\_QUERYUISTATE**](wm-queryuistate.md)   | Sent to retrieve the UI state for a window.<br/>                                                                                                                                                                                                                                                            |
| [**WM\_UPDATEUISTATE**](wm-updateuistate.md) | Sent to change the UI state for the specified window and all its child windows.<br/>                                                                                                                                                                                                                        |



 

### Keyboard Accelerator Notifications



| Name                                          | Description                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_INITMENUPOPUP**](wm-initmenupopup.md) | Sent when a drop-down menu or submenu is about to become active. This allows an application to modify the menu before it is displayed, without changing the entire menu. <br/>                                                                                                                                              |
| [**WM\_MENUCHAR**](wm-menuchar.md)           | Sent when a menu is active and the user presses a key that does not correspond to any mnemonic or accelerator key. This message is sent to the window that owns the menu. <br/>                                                                                                                                             |
| [**WM\_MENUSELECT**](wm-menuselect.md)       | Sent to a menu's owner window when the user selects a menu item. <br/>                                                                                                                                                                                                                                                      |
| [**WM\_SYSCHAR**](wm-syschar.md)             | Posted to the window with the keyboard focus when a [**WM\_SYSKEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646286) message is translated by the [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) function. It specifies the character code of a system character key that is, a character key that is pressed while the ALT key is down. <br/> |
| [**WM\_SYSCOMMAND**](wm-syscommand.md)       | A window receives this message when the user chooses a command from the **Window** menu or when the user chooses the maximize button, minimize button, restore button, or close button.<br/>                                                                                                                                |



 

### Keyboard Accelerator Structures



| Name                   | Description                                                          |
|------------------------|----------------------------------------------------------------------|
| [**ACCEL**](/windows/win32/Winuser/ns-winuser-tagaccel?branch=master) | Defines an accelerator key used in an accelerator table. <br/> |



 

 

 





