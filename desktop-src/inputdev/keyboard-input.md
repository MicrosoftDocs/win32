---
title: Keyboard Input
description: This section discusses how the system generates keyboard input and how an application receives and processes that input.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\userinput\keyboardinput.htm'
keywords:
- user input,keyboard input
- capturing user input,keyboard input
- keyboard input
ms.topic: article
ms.date: 08/01/2022
---

# Keyboard Input

This section describes how the system generates keyboard input and how an application receives and processes that input.

## In This Section



| Name                                                     | Description                                                       |
|----------------------------------------------------------|-------------------------------------------------------------------|
| [About Keyboard Input](about-keyboard-input.md)         | Discusses keyboard input.<br/>                              |
| [Using Keyboard Input](using-keyboard-input.md)         | Covers tasks that are associated with keyboard input. <br/> |
| [Keyboard Input Reference](keyboard-input-reference.md) | Contains the API reference.<br/>                            |



 

### Functions



| Name                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivateKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-activatekeyboardlayout) | Sets the input locale identifier (formerly called the keyboard layout handle) for the calling thread or the current process. The input locale identifier specifies a locale as well as the physical layout of the keyboard.<br/>                                                                                                                                                                |
| [**BlockInput**](/windows/win32/api/winuser/nf-winuser-blockinput)                         | Blocks keyboard and mouse input events from reaching applications. <br/>                                                                                                                                                                                                                                                                                                                        |
| [**EnableWindow**](/windows/win32/api/winuser/nf-winuser-enablewindow)                     | Enables or disables mouse and keyboard input to the specified window or control. When input is disabled, the window does not receive input such as mouse clicks and key presses. When input is enabled, the window receives all input.<br/>                                                                                                                                                     |
| [**GetActiveWindow**](/windows/win32/api/winuser/nf-winuser-getactivewindow)               | Retrieves the window handle to the active window attached to the calling thread's message queue. <br/>                                                                                                                                                                                                                                                                                          |
| [**GetAsyncKeyState**](/windows/win32/api/winuser/nf-winuser-getasynckeystate)             | Determines whether a key is up or down at the time the function is called, and whether the key was pressed after a previous call to [**GetAsyncKeyState**](/windows/win32/api/winuser/nf-winuser-getasynckeystate). <br/>                                                                                                                                                                                                         |
| [**GetFocus**](/windows/win32/api/winuser/nf-winuser-getfocus)                             | Retrieves the handle to the window that has the keyboard focus, if the window is attached to the calling thread's message queue. <br/>                                                                                                                                                                                                                                                          |
| [**GetKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayout)           | Retrieves the active input locale identifier (formerly called the keyboard layout) for the specified thread. If the *idThread* parameter is zero, the input locale identifier for the active thread is returned.<br/>                                                                                                                                                                           |
| [**GetKeyboardLayoutList**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayoutlist)   | Retrieves the input locale identifiers (formerly called keyboard layout handles) corresponding to the current set of input locales in the system. The function copies the identifiers to the specified buffer.<br/>                                                                                                                                                                             |
| [**GetKeyboardLayoutName**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayoutnamea)   | Retrieves the name of the active input locale identifier (formerly called the keyboard layout). <br/>                                                                                                                                                                                                                                                                                           |
| [**GetKeyboardState**](/windows/win32/api/winuser/nf-winuser-getkeyboardstate)             | Copies the status of the 256 virtual keys to the specified buffer. <br/>                                                                                                                                                                                                                                                                                                                        |
| [**GetKeyNameText**](/windows/win32/api/winuser/nf-winuser-getkeynametexta)                 | Retrieves a string that represents the name of a key. <br/>                                                                                                                                                                                                                                                                                                                                     |
| [**GetKeyState**](/windows/win32/api/winuser/nf-winuser-getkeystate)                       | Retrieves the status of the specified virtual key. The status specifies whether the key is up, down, or toggled (on, off alternating each time the key is pressed). <br/>                                                                                                                                                                                                                       |
| [**GetLastInputInfo**](/windows/win32/api/winuser/nf-winuser-getlastinputinfo)             | Retrieves the time of the last input event.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**IsWindowEnabled**](/windows/win32/api/winuser/nf-winuser-iswindowenabled)               | Determines whether the specified window is enabled for mouse and keyboard input. <br/>                                                                                                                                                                                                                                                                                                          |
| [**LoadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-loadkeyboardlayouta)         | Loads a new input locale identifier (formerly called the keyboard layout) into the system. Several input locale identifiers can be loaded at a time, but only one per process is active at a time. Loading multiple input locale identifiers makes it possible to rapidly switch between them.<br/>                                                                                             |
| [**MapVirtualKey**](/windows/win32/api/winuser/nf-winuser-mapvirtualkeya)                   | Translates (maps) a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code. <br/> To specify a handle to the keyboard layout to use for translating the specified code, use the [**MapVirtualKeyEx**](/windows/win32/api/winuser/nf-winuser-mapvirtualkeyexa) function.<br/>                                                                                                |
| [**MapVirtualKeyEx**](/windows/win32/api/winuser/nf-winuser-mapvirtualkeyexa)               | Maps a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code. The function translates the codes using the input language and an input locale identifier.<br/>                                                                                                                                                                                 |
| [**OemKeyScan**](/windows/win32/api/winuser/nf-winuser-oemkeyscan)                         | Maps OEMASCII codes 0 through 0x0FF into the OEM scan codes and shift states. The function provides information that allows a program to send OEM text to another program by simulating keyboard input. <br/>                                                                                                                                                                                   |
| [**RegisterHotKey**](/windows/win32/api/winuser/nf-winuser-registerhotkey)                 | Defines a system-wide hot key.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**SendInput**](/windows/win32/api/winuser/nf-winuser-sendinput)                           | Synthesizes keystrokes, mouse motions, and button clicks.<br/>                                                                                                                                                                                                                                                                                                                                  |
| [**SetActiveWindow**](/windows/win32/api/winuser/nf-winuser-setactivewindow)               | Activates a window. The window must be attached to the calling thread's message queue. <br/>                                                                                                                                                                                                                                                                                                    |
| [**SetFocus**](/windows/win32/api/winuser/nf-winuser-setfocus)                             | Sets the keyboard focus to the specified window. The window must be attached to the calling thread's message queue. <br/>                                                                                                                                                                                                                                                                       |
| [**SetKeyboardState**](/windows/win32/api/winuser/nf-winuser-setkeyboardstate)             | Copies a 256-byte array of keyboard key states into the calling thread's keyboard input-state table. This is the same table accessed by the [**GetKeyboardState**](/windows/win32/api/winuser/nf-winuser-getkeyboardstate) and [**GetKeyState**](/windows/win32/api/winuser/nf-winuser-getkeystate) functions. Changes made to this table do not affect keyboard input to any other thread. <br/>                                                                   |
| [**ToAscii**](/windows/win32/api/winuser/nf-winuser-toascii)                               | Translates the specified virtual-key code and keyboard state to the corresponding character or characters. The function translates the code using the input language and physical keyboard layout identified by the keyboard layout handle.<br/> To specify a handle to the keyboard layout to use to translate the specified code, use the [**ToAsciiEx**](/windows/win32/api/winuser/nf-winuser-toasciiex) function.<br/> |
| [**ToAsciiEx**](/windows/win32/api/winuser/nf-winuser-toasciiex)                           | Translates the specified virtual-key code and keyboard state to the corresponding character or characters. The function translates the code using the input language and physical keyboard layout identified by the input locale identifier.<br/>                                                                                                                                               |
| [**ToUnicode**](/windows/win32/api/winuser/nf-winuser-tounicode)                           | Translates the specified virtual-key code and keyboard state to the corresponding Unicode character or characters. <br/> To specify a handle to the keyboard layout to use to translate the specified code, use the [**ToUnicodeEx**](/windows/win32/api/winuser/nf-winuser-tounicodeex) function.<br/>                                                                                                                     |
| [**ToUnicodeEx**](/windows/win32/api/winuser/nf-winuser-tounicodeex)                       | Translates the specified virtual-key code and keyboard state to the corresponding Unicode character or characters.<br/>                                                                                                                                                                                                                                                                         |
| [**UnloadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-unloadkeyboardlayout)     | Unloads an input locale identifier (formerly called a keyboard layout). <br/>                                                                                                                                                                                                                                                                                                                   |
| [**UnregisterHotKey**](/windows/win32/api/winuser/nf-winuser-unregisterhotkey)             | Frees a hot key previously registered by the calling thread. <br/>                                                                                                                                                                                                                                                                                                                              |
| [**VkKeyScanEx**](/windows/win32/api/winuser/nf-winuser-vkkeyscanexa)                       | Translates a character to the corresponding virtual-key code and shift state. The function translates the character using the input language and physical keyboard layout identified by the input locale identifier. <br/>                                                                                                                                                                      |



 

The following functions are obsolete.



| Function                               | Description                                                                                                                                                                                                                                                                   |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetKBCodePage**](/windows/win32/api/winuser/nf-winuser-getkbcodepage) | Retrieves the current code page.<br/>                                                                                                                                                                                                                                   |
| [**keybd_event**](/windows/win32/api/winuser/nf-winuser-keybd_event)    | Synthesizes a keystroke. The system can use such a synthesized keystroke to generate a [**WM\_KEYUP**](wm-keyup.md) or [**WM\_KEYDOWN**](wm-keydown.md) message. The keyboard driver's interrupt handler calls the [**keybd_event**](/windows/win32/api/winuser/nf-winuser-keybd_event) function.<br/> |
| [**VkKeyScan**](/windows/win32/api/winuser/nf-winuser-vkkeyscana)         | Translates a character to the corresponding virtual-key code and shift state for the current keyboard.<br/>                                                                                                                                                             |



 

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
| [**WM\_CHAR**](wm-char.md)               | Posted to the window with the keyboard focus when a [**WM\_KEYDOWN**](wm-keydown.md) message is translated by the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function. The [**WM\_CHAR**](wm-char.md) message contains the character code of the key that was pressed. <br/>                                                                                                                                                                                                                                                                             |
| [**WM\_DEADCHAR**](wm-deadchar.md)       | Posted to the window with the keyboard focus when a [**WM\_KEYUP**](wm-keyup.md) message is translated by the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function. [**WM\_DEADCHAR**](wm-deadchar.md) specifies a character code generated by a dead key. A dead key is a key that generates a character, such as the umlaut (double-dot), that is combined with another character to form a composite character. For example, the umlaut-O character ( ) is generated by typing the dead key for the umlaut character, and then typing the O key. <br/> |
| [**WM\_HOTKEY**](wm-hotkey.md)           | Posted when the user presses a hot key registered by the [**RegisterHotKey**](/windows/win32/api/winuser/nf-winuser-registerhotkey) function. The message is placed at the top of the message queue associated with the thread that registered the hot key. <br/>                                                                                                                                                                                                                                                                                                                                 |
| [**WM\_KEYDOWN**](wm-keydown.md)         | Posted to the window with the keyboard focus when a nonsystem key is pressed. A nonsystem key is a key that is pressed when the ALT key is not pressed. <br/>                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**WM\_KEYUP**](wm-keyup.md)             | Posted to the window with the keyboard focus when a nonsystem key is released. A nonsystem key is a key that is pressed when the ALT key is not pressed, or a keyboard key that is pressed when a window has the keyboard focus. <br/>                                                                                                                                                                                                                                                                                                                          |
| [**WM\_KILLFOCUS**](wm-killfocus.md)     | Sent to a window immediately before it loses the keyboard focus. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**WM\_SETFOCUS**](wm-setfocus.md)       | Sent to a window after it has gained the keyboard focus. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**WM\_SYSDEADCHAR**](wm-sysdeadchar.md) | Sent to the window with the keyboard focus when a [**WM\_SYSKEYDOWN**](wm-syskeydown.md) message is translated by the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function. [**WM\_SYSDEADCHAR**](wm-sysdeadchar.md) specifies the character code of a system dead key   that is, a dead key that is pressed while holding down the ALT key. <br/>                                                                                                                                                                                                        |
| [**WM\_SYSKEYDOWN**](wm-syskeydown.md)   | Posted to the window with the keyboard focus when the user presses the F10 key (which activates the menu bar) or holds down the ALT key and then presses another key. It also occurs when no window currently has the keyboard focus; in this case, the [**WM\_SYSKEYDOWN**](wm-syskeydown.md) message is sent to the active window. The window that receives the message can distinguish between these two contexts by checking the context code in the *lParam* parameter. <br/>                                                                             |
| [**WM\_SYSKEYUP**](wm-syskeyup.md)       | Posted to the window with the keyboard focus when the user releases a key that was pressed while the ALT key was held down. It also occurs when no window currently has the keyboard focus; in this case, the [**WM\_SYSKEYUP**](wm-syskeyup.md) message is sent to the active window. The window that receives the message can distinguish between these two contexts by checking the context code in the *lParam* parameter. <br/>                                                                                                                           |
| [**WM\_UNICHAR**](wm-unichar.md)         | Posted to the window with the keyboard focus when a [**WM\_KEYDOWN**](wm-keydown.md) message is translated by the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function. The [**WM\_UNICHAR**](wm-unichar.md) message contains the character code of the key that was pressed.<br/>                                                                                                                                                                                                                                                                        |



 

### Structures



| Name                                   | Description                                                                                                              |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**HARDWAREINPUT**](/windows/win32/api/winuser/ns-winuser-hardwareinput) | Contains information about a simulated message generated by an input device other than a keyboard or mouse. <br/>  |
| [**INPUT**](/windows/win32/api/winuser/ns-winuser-input)                 | Contains information used for synthesizing input events such as keystrokes, mouse movement, and mouse clicks.<br/> |
| [**KEYBDINPUT**](/windows/win32/api/winuser/ns-winuser-keybdinput)       | Contains information about a simulated keyboard event. <br/>                                                       |
| [**LASTINPUTINFO**](/windows/win32/api/winuser/ns-winuser-lastinputinfo) | Contains the time of the last input.<br/>                                                                          |
| [**MOUSEINPUT**](/windows/win32/api/winuser/ns-winuser-mouseinput)       | Contains information about a simulated mouse event.<br/>                                                           |



 

### Constants



| Name                                           | Description                                                                                                                                                                         |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Virtual-Key Codes**](virtual-key-codes.md) | The symbolic constant names, hexadecimal values, and mouse or keyboard equivalents for the virtual-key codes used by the system. The codes are listed in numeric order. <br/> |



## See also
- [Keyboard Input](keyboard-input.md)
- [About Keyboard Input](about-keyboard-input.md)

 

 

 

