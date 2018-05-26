---
title: Keyboard Input
description: This section discusses how the system generates keyboard input and how an application receives and processes that input.
ms.assetid: de34727e-e8c7-481d-982d-0e42a02704db
keywords:
- user input,keyboard input
- capturing user input,keyboard input
- keyboard input
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Keyboard Input

This section describes how the system generates keyboard input and how an application receives and processes that input.

### In This Section



| Name                                                     | Description                                                       |
|----------------------------------------------------------|-------------------------------------------------------------------|
| [About Keyboard Input](about-keyboard-input.md)         | Discusses keyboard input.<br/>                              |
| [Using Keyboard Input](using-keyboard-input.md)         | Covers tasks that are associated with keyboard input. <br/> |
| [Keyboard Input Reference](keyboard-input-reference.md) | Contains the API reference.<br/>                            |



 

### Functions



| Name                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivateKeyboardLayout**](activatekeyboardlayout.md) | Sets the input locale identifier (formerly called the keyboard layout handle) for the calling thread or the current process. The input locale identifier specifies a locale as well as the physical layout of the keyboard.<br/>                                                                                                                                                                |
| [**BlockInput**](blockinput.md)                         | Blocks keyboard and mouse input events from reaching applications. <br/>                                                                                                                                                                                                                                                                                                                        |
| [**EnableWindow**](enablewindow.md)                     | Enables or disables mouse and keyboard input to the specified window or control. When input is disabled, the window does not receive input such as mouse clicks and key presses. When input is enabled, the window receives all input.<br/>                                                                                                                                                     |
| [**GetActiveWindow**](getactivewindow.md)               | Retrieves the window handle to the active window attached to the calling thread's message queue. <br/>                                                                                                                                                                                                                                                                                          |
| [**GetAsyncKeyState**](getasynckeystate.md)             | Determines whether a key is up or down at the time the function is called, and whether the key was pressed after a previous call to [**GetAsyncKeyState**](getasynckeystate.md). <br/>                                                                                                                                                                                                         |
| [**GetFocus**](getfocus.md)                             | Retrieves the handle to the window that has the keyboard focus, if the window is attached to the calling thread's message queue. <br/>                                                                                                                                                                                                                                                          |
| [**GetKeyboardLayout**](getkeyboardlayout.md)           | Retrieves the active input locale identifier (formerly called the keyboard layout) for the specified thread. If the *idThread* parameter is zero, the input locale identifier for the active thread is returned.<br/>                                                                                                                                                                           |
| [**GetKeyboardLayoutList**](getkeyboardlayoutlist.md)   | Retrieves the input locale identifiers (formerly called keyboard layout handles) corresponding to the current set of input locales in the system. The function copies the identifiers to the specified buffer.<br/>                                                                                                                                                                             |
| [**GetKeyboardLayoutName**](getkeyboardlayoutname.md)   | Retrieves the name of the active input locale identifier (formerly called the keyboard layout). <br/>                                                                                                                                                                                                                                                                                           |
| [**GetKeyboardState**](getkeyboardstate.md)             | Copies the status of the 256 virtual keys to the specified buffer. <br/>                                                                                                                                                                                                                                                                                                                        |
| [**GetKeyNameText**](getkeynametext.md)                 | Retrieves a string that represents the name of a key. <br/>                                                                                                                                                                                                                                                                                                                                     |
| [**GetKeyState**](getkeystate.md)                       | Retrieves the status of the specified virtual key. The status specifies whether the key is up, down, or toggled (on, off alternating each time the key is pressed). <br/>                                                                                                                                                                                                                       |
| [**GetLastInputInfo**](getlastinputinfo.md)             | Retrieves the time of the last input event.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**IsWindowEnabled**](iswindowenabled.md)               | Determines whether the specified window is enabled for mouse and keyboard input. <br/>                                                                                                                                                                                                                                                                                                          |
| [**LoadKeyboardLayout**](loadkeyboardlayout.md)         | Loads a new input locale identifier (formerly called the keyboard layout) into the system. Several input locale identifiers can be loaded at a time, but only one per process is active at a time. Loading multiple input locale identifiers makes it possible to rapidly switch between them.<br/>                                                                                             |
| [**MapVirtualKey**](mapvirtualkey.md)                   | Translates (maps) a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code. <br/> To specify a handle to the keyboard layout to use for translating the specified code, use the [**MapVirtualKeyEx**](mapvirtualkeyex.md) function.<br/>                                                                                                |
| [**MapVirtualKeyEx**](mapvirtualkeyex.md)               | Maps a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code. The function translates the codes using the input language and an input locale identifier.<br/>                                                                                                                                                                                 |
| [**OemKeyScan**](oemkeyscan.md)                         | Maps OEMASCII codes 0 through 0x0FF into the OEM scan codes and shift states. The function provides information that allows a program to send OEM text to another program by simulating keyboard input. <br/>                                                                                                                                                                                   |
| [**RegisterHotKey**](registerhotkey.md)                 | Defines a system-wide hot key.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**SendInput**](sendinput.md)                           | Synthesizes keystrokes, mouse motions, and button clicks.<br/>                                                                                                                                                                                                                                                                                                                                  |
| [**SetActiveWindow**](setactivewindow.md)               | Activates a window. The window must be attached to the calling thread's message queue. <br/>                                                                                                                                                                                                                                                                                                    |
| [**SetFocus**](setfocus.md)                             | Sets the keyboard focus to the specified window. The window must be attached to the calling thread's message queue. <br/>                                                                                                                                                                                                                                                                       |
| [**SetKeyboardState**](setkeyboardstate.md)             | Copies a 256-byte array of keyboard key states into the calling thread's keyboard input-state table. This is the same table accessed by the [**GetKeyboardState**](getkeyboardstate.md) and [**GetKeyState**](getkeystate.md) functions. Changes made to this table do not affect keyboard input to any other thread. <br/>                                                                   |
| [**ToAscii**](/windows/win32/Winuser/nf-ntifs-rtlidntoascii?branch=master)                               | Translates the specified virtual-key code and keyboard state to the corresponding character or characters. The function translates the code using the input language and physical keyboard layout identified by the keyboard layout handle.<br/> To specify a handle to the keyboard layout to use to translate the specified code, use the [**ToAsciiEx**](toasciiex.md) function.<br/> |
| [**ToAsciiEx**](toasciiex.md)                           | Translates the specified virtual-key code and keyboard state to the corresponding character or characters. The function translates the code using the input language and physical keyboard layout identified by the input locale identifier.<br/>                                                                                                                                               |
| [**ToUnicode**](/windows/win32/Winuser/nf-ntifs-rtlidntounicode?branch=master)                           | Translates the specified virtual-key code and keyboard state to the corresponding Unicode character or characters. <br/> To specify a handle to the keyboard layout to use to translate the specified code, use the [**ToUnicodeEx**](tounicodeex.md) function.<br/>                                                                                                                     |
| [**ToUnicodeEx**](tounicodeex.md)                       | Translates the specified virtual-key code and keyboard state to the corresponding Unicode character or characters.<br/>                                                                                                                                                                                                                                                                         |
| [**UnloadKeyboardLayout**](unloadkeyboardlayout.md)     | Unloads an input locale identifier (formerly called a keyboard layout). <br/>                                                                                                                                                                                                                                                                                                                   |
| [**UnregisterHotKey**](unregisterhotkey.md)             | Frees a hot key previously registered by the calling thread. <br/>                                                                                                                                                                                                                                                                                                                              |
| [**VkKeyScanEx**](vkkeyscanex.md)                       | Translates a character to the corresponding virtual-key code and shift state. The function translates the character using the input language and physical keyboard layout identified by the input locale identifier. <br/>                                                                                                                                                                      |



 

The following functions are obsolete.



| Function                               | Description                                                                                                                                                                                                                                                                   |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetKBCodePage**](getkbcodepage.md) | Retrieves the current code page.<br/>                                                                                                                                                                                                                                   |
| [**keybd\_event**](keybd-event.md)    | Synthesizes a keystroke. The system can use such a synthesized keystroke to generate a [**WM\_KEYUP**](wm-keyup.md) or [**WM\_KEYDOWN**](wm-keydown.md) message. The keyboard driver's interrupt handler calls the [**keybd\_event**](keybd-event.md) function.<br/> |
| [**VkKeyScan**](vkkeyscan.md)         | Translates a character to the corresponding virtual-key code and shift state for the current keyboard.<br/>                                                                                                                                                             |



 

### Messages



| Name                                  | Description                                                                                                           |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**WM\_GETHOTKEY**](wm-gethotkey.md) | Determines the hot key associated with a window. <br/>                                                          |
| [**WM\_SETHOTKEY**](wm-sethotkey.md) | Associates a hot key with the window. When the user presses the hot key, the system activates the window. <br/> |



 

### Notifications



| Name                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_ACTIVATE**](wm-activate.md)       | Sent to both the window being activated and the window being deactivated. If the windows use the same input queue, the message is sent synchronously, first to the window procedure of the top-level window being deactivated, then to the window procedure of the top-level window being activated. If the windows use different input queues, the message is sent asynchronously, so the window is activated immediately. <br/>                                                                                                                               |
| [**WM\_APPCOMMAND**](wm-appcommand.md)   | Notifies a window that the user generated an application command event, for example, by clicking an application command button using the mouse or typing an application command key on the keyboard.<br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**WM\_CHAR**](wm-char.md)               | Posted to the window with the keyboard focus when a [**WM\_KEYDOWN**](wm-keydown.md) message is translated by the [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) function. The [**WM\_CHAR**](wm-char.md) message contains the character code of the key that was pressed. <br/>                                                                                                                                                                                                                                                                             |
| [**WM\_DEADCHAR**](wm-deadchar.md)       | Posted to the window with the keyboard focus when a [**WM\_KEYUP**](wm-keyup.md) message is translated by the [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) function. [**WM\_DEADCHAR**](wm-deadchar.md) specifies a character code generated by a dead key. A dead key is a key that generates a character, such as the umlaut (double-dot), that is combined with another character to form a composite character. For example, the umlaut-O character ( ) is generated by typing the dead key for the umlaut character, and then typing the O key. <br/> |
| [**WM\_HOTKEY**](wm-hotkey.md)           | Posted when the user presses a hot key registered by the [**RegisterHotKey**](registerhotkey.md) function. The message is placed at the top of the message queue associated with the thread that registered the hot key. <br/>                                                                                                                                                                                                                                                                                                                                 |
| [**WM\_KEYDOWN**](wm-keydown.md)         | Posted to the window with the keyboard focus when a nonsystem key is pressed. A nonsystem key is a key that is pressed when the ALT key is not pressed. <br/>                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**WM\_KEYUP**](wm-keyup.md)             | Posted to the window with the keyboard focus when a nonsystem key is released. A nonsystem key is a key that is pressed when the ALT key is not pressed, or a keyboard key that is pressed when a window has the keyboard focus. <br/>                                                                                                                                                                                                                                                                                                                          |
| [**WM\_KILLFOCUS**](wm-killfocus.md)     | Sent to a window immediately before it loses the keyboard focus. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**WM\_SETFOCUS**](wm-setfocus.md)       | Sent to a window after it has gained the keyboard focus. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**WM\_SYSDEADCHAR**](wm-sysdeadchar.md) | Sent to the window with the keyboard focus when a [**WM\_SYSKEYDOWN**](wm-syskeydown.md) message is translated by the [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) function. [**WM\_SYSDEADCHAR**](wm-sysdeadchar.md) specifies the character code of a system dead key   that is, a dead key that is pressed while holding down the ALT key. <br/>                                                                                                                                                                                                        |
| [**WM\_SYSKEYDOWN**](wm-syskeydown.md)   | Posted to the window with the keyboard focus when the user presses the F10 key (which activates the menu bar) or holds down the ALT key and then presses another key. It also occurs when no window currently has the keyboard focus; in this case, the [**WM\_SYSKEYDOWN**](wm-syskeydown.md) message is sent to the active window. The window that receives the message can distinguish between these two contexts by checking the context code in the *lParam* parameter. <br/>                                                                             |
| [**WM\_SYSKEYUP**](wm-syskeyup.md)       | Posted to the window with the keyboard focus when the user releases a key that was pressed while the ALT key was held down. It also occurs when no window currently has the keyboard focus; in this case, the [**WM\_SYSKEYUP**](wm-syskeyup.md) message is sent to the active window. The window that receives the message can distinguish between these two contexts by checking the context code in the *lParam* parameter. <br/>                                                                                                                           |
| [**WM\_UNICHAR**](wm-unichar.md)         | Posted to the window with the keyboard focus when a [**WM\_KEYDOWN**](wm-keydown.md) message is translated by the [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) function. The [**WM\_UNICHAR**](wm-unichar.md) message contains the character code of the key that was pressed.<br/>                                                                                                                                                                                                                                                                        |



 

### Structures



| Name                                   | Description                                                                                                              |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**HARDWAREINPUT**](hardwareinput.md) | Contains information about a simulated message generated by an input device other than a keyboard or mouse. <br/>  |
| [**INPUT**](/windows/win32/Winuser/nf-d3d10tokenizedprogramformat-decode_d3d10_sb_gs_input_primitive?branch=master)                 | Contains information used for synthesizing input events such as keystrokes, mouse movement, and mouse clicks.<br/> |
| [**KEYBDINPUT**](keybdinput.md)       | Contains information about a simulated keyboard event. <br/>                                                       |
| [**LASTINPUTINFO**](lastinputinfo.md) | Contains the time of the last input.<br/>                                                                          |
| [**MOUSEINPUT**](mouseinput.md)       | Contains information about a simulated mouse event.<br/>                                                           |



 

### Constants



| Name                                           | Description                                                                                                                                                                         |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Virtual-Key Codes**](virtual-key-codes.md) | The symbolic constant names, hexadecimal values, and mouse or keyboard equivalents for the virtual-key codes used by the system. The codes are listed in numeric order. <br/> |



 

 

 





