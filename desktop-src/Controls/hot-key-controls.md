---
title: About Hot Key Controls
description: A hot key control is a window that enables the user to enter a combination of keystrokes to be used as a hot key.
ms.assetid: 5f011459-4c30-45d4-9668-19f575b041ce
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Hot Key Controls

A hot key control is a window that enables the user to enter a combination of keystrokes to be used as a hot key. A hot key is a key combination that the user can press to perform an action quickly. For example, a user can create a hot key that activates a given window and brings it to the top of the z-order. The hot key control displays the user's choices and ensures that the user selects a valid key combination. The following screen shot shows how a hot key control appears in a dialog box after the user presses the Alt key.

![screen shot of a dialog box that contains a hot key control](images/hotkey.png)

## Using Hot Key Controls

When the user enters a key combination to be used as a hot key, the names of the keys appear in the hot key control. A key combination can consist of a modifier key (such as CTRL, ALT, or SHIFT) and an accompanying key (such as a character key, an arrow key, a function key, and so on).

After the user has chosen a key combination, the application retrieves the key combination from the hot key control and uses it to set up a hot key in the system. The information retrieved from the hot key control includes a flag indicating the modifier key and the virtual key code of the accompanying key.

The application can use the information provided by a hot key control to set up a global hot key or a thread-specific hot key. A global hot key is associated with a particular window; it allows the user to activate the window from any part of the system. An application sets a global hot key by using the [**WM\_SETHOTKEY**](https://msdn.microsoft.com/library/windows/desktop/ms646284) message. Whenever the user presses a global hot key, the window specified in **WM\_SETHOTKEY** receives a [**WM\_SYSCOMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms646360) message that specifies the [**SC\_HOTKEY**](https://msdn.microsoft.com/library/windows/desktop/ms646284#sc-hotkey) value. This message activates the window that receives it. The hot key remains valid until the application that called **WM\_SETHOTKEY** exits.

A thread-specific hot key generates a [**WM\_HOTKEY**](https://msdn.microsoft.com/library/windows/desktop/ms646279) message that is posted to the beginning of a particular thread so that it is removed by the next iteration of the message loop. An application sets a thread-specific hot key by using the [**RegisterHotKey**](https://msdn.microsoft.com/library/windows/desktop/ms646309) function.

### Hot Key Control Messages

After creating a hot key control, an application interacts with it by using three messages: [**HKM\_SETRULES**](hkm-setrules.md), [**HKM\_SETHOTKEY**](hkm-sethotkey.md), and [**HKM\_GETHOTKEY**](hkm-gethotkey.md).

An application can send the [**HKM\_SETRULES**](hkm-setrules.md) message to specify a set of CTRL, ALT, and SHIFT key combinations that are considered invalid hot keys. If the application specifies an invalid key combination, it should also specify a default modifier combination to use when the user selects the invalid combination. When the user enters the invalid combination, the system performs a logical OR operation on the invalid combination and the default combination. The result is considered a valid combination; it is converted to a string and displayed in the control.

The [**HKM\_SETHOTKEY**](hkm-sethotkey.md) message allows an application to set the hot key combination for a hot key control. This message is also typically used when the hot key control is created.

Applications use the [**HKM\_GETHOTKEY**](hkm-gethotkey.md) message to retrieve the virtual key code and modifier flags of the hot key chosen by the user.

### Hot Key Control Notifications

The hot key control does not send any notification codes via the [**WM\_NOTIFY**](wm-notify.md) message. It will, however, send the [EN\_CHANGE](en-change.md) notification via the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message when the user changes the contents of the control.

### Default Hot Key Message Processing

This section describes the window messages handled by the window procedure for the pre defined [**HOTKEY\_CLASS**](common-control-window-classes.md#hotkey-class) window class used with hot key controls.



|                                                |                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Message**                                    | **Processing performed**                                                                                                                                                                                                                                                                                                                      |
| [**WM\_CHAR**](https://msdn.microsoft.com/library/windows/desktop/ms646276)               | Retrieves the virtual key code.                                                                                                                                                                                                                                                                                                               |
| [**WM\_CREATE**](https://msdn.microsoft.com/library/windows/desktop/ms632619)             | Initializes the hot key control, clears any hot key rules, and uses the system font.                                                                                                                                                                                                                                                          |
| [**WM\_ERASEBKGND**](https://msdn.microsoft.com/library/windows/desktop/ms648055)     | Hides the caret, calls the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function, and shows the caret again.                                                                                                                                                                                                                                     |
| [**WM\_GETDLGCODE**](https://msdn.microsoft.com/library/windows/desktop/ms645425)     | Returns a combination of the [**DLGC\_WANTCHARS**](https://msdn.microsoft.com/library/windows/desktop/ms645425#dlgc-wantchars) and [**DLGC\_WANTARROWS**](https://msdn.microsoft.com/library/windows/desktop/ms645425#dlgc-wantarrows) values.                                                                                                                                               |
| [**WM\_GETFONT**](https://msdn.microsoft.com/library/windows/desktop/ms632624)           | Retrieves the font.                                                                                                                                                                                                                                                                                                                           |
| [**WM\_KEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646280)         | Calls the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function if the key is ENTER, TAB, SPACE BAR, DEL, ESC, or BACKSPACE. If the key is SHIFT, CTRL, or ALT, it checks whether the combination is valid and, if it is, sets the hot key using the combination. All other keys are set as hot keys without their validity being checked first. |
| [**WM\_KEYUP**](https://msdn.microsoft.com/library/windows/desktop/ms646281)             | Retrieves the virtual key code.                                                                                                                                                                                                                                                                                                               |
| [**WM\_KILLFOCUS**](https://msdn.microsoft.com/library/windows/desktop/ms646282)     | Destroys the caret.                                                                                                                                                                                                                                                                                                                           |
| [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607) | Sets the focus to the window.                                                                                                                                                                                                                                                                                                                 |
| [**WM\_NCCREATE**](https://msdn.microsoft.com/library/windows/desktop/ms632635)         | Sets the [**WS\_EX\_CLIENTEDGE**](https://msdn.microsoft.com/library/windows/desktop/ff700543#ws-ex-clientedge) window style.                                                                                                                                                                                                                              |
| [**WM\_PAINT**](https://msdn.microsoft.com/library/windows/desktop/dd145213)                  | Paints the hot key control.                                                                                                                                                                                                                                                                                                                   |
| [**WM\_SETFOCUS**](https://msdn.microsoft.com/library/windows/desktop/ms646283)       | Creates and shows the caret.                                                                                                                                                                                                                                                                                                                  |
| [**WM\_SETFONT**](https://msdn.microsoft.com/library/windows/desktop/ms632642)           | Sets the font.                                                                                                                                                                                                                                                                                                                                |
| [**WM\_SYSCHAR**](https://msdn.microsoft.com/library/windows/desktop/ms646357)           | Retrieves the virtual key code.                                                                                                                                                                                                                                                                                                               |
| [**WM\_SYSKEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646286)   | Calls the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function if the key is ENTER, TAB, SPACE BAR, DEL, ESC, or BACKSPACE. If the key is SHIFT, CTRL, or ALT, it checks whether the combination is valid and, if it is, sets the hot key using the combination. All other keys are set as hot keys without their validity being checked first. |
| [**WM\_SYSKEYUP**](https://msdn.microsoft.com/library/windows/desktop/ms646287)       | Retrieves the virtual key code.                                                                                                                                                                                                                                                                                                               |



 

 

 




