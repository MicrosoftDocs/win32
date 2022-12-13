---
title: Keyboard Input Overview
description: This topic discusses keyboard input.
ms.assetid: de34727e-e8c7-481d-982d-0e42a02704db
keywords:
- user input,keyboard input
- capturing user input,keyboard input
- keyboard input
- keyboard focus
- keystroke messages
- character messages
- system keystrokes
- nonsystem keystrokes
- nonsystem character messages
- dead keys
- dead-character messages
ms.topic: article
ms.date: 08/01/2022
---

# Keyboard Input Overview

Applications should accept user input from the keyboard as well as from the mouse. An application receives keyboard input in the form of messages posted to its windows.

## Keyboard Input Model

The system provides device-independent keyboard support for applications by installing a keyboard device driver appropriate for the current keyboard. The system provides language-independent keyboard support by using the language-specific keyboard layout currently selected by the user or the application. The keyboard device driver receives scan codes from the keyboard, which are sent to the keyboard layout where they are translated into messages and posted to the appropriate windows in your application.

Assigned to each key on a keyboard is a unique value called a *scan code*, a device-dependent identifier for the key on the keyboard. A keyboard generates two scan codes when the user types a key—one when the user presses the key and another when the user releases the key.

The keyboard device driver interprets a scan code and translates (maps) it to a *virtual-key code*, a device-independent value defined by the system that identifies the purpose of a key. After translating a scan code, the keyboard layout creates a message that includes the scan code, the virtual-key code, and other information about the keystroke, and then places the message in the system message queue. The system removes the message from the system message queue and posts it to the message queue of the appropriate thread. Eventually, the thread's message loop removes the message and passes it to the appropriate window procedure for processing. The following figure illustrates the keyboard input model.

![keyboard input processing model](images/csinp-01.png)

## Keyboard Focus and Activation

The system posts keyboard messages to the message queue of the foreground thread that created the window with the keyboard focus. The *keyboard focus* is a temporary property of a window. The system shares the keyboard among all windows on the display by shifting the keyboard focus, at the user's direction, from one window to another. The window that has the keyboard focus receives (from the message queue of the thread that created it) all keyboard messages until the focus changes to a different window.

A thread can call the [**GetFocus**](/windows/win32/api/winuser/nf-winuser-getfocus) function to determine which of its windows (if any) currently has the keyboard focus. A thread can give the keyboard focus to one of its windows by calling the [**SetFocus**](/windows/win32/api/winuser/nf-winuser-setfocus) function. When the keyboard focus changes from one window to another, the system sends a [**WM\_KILLFOCUS**](wm-killfocus.md) message to the window that has lost the focus, and then sends a [**WM\_SETFOCUS**](wm-setfocus.md) message to the window that has gained the focus.

The concept of keyboard focus is related to that of the active window. The *active window* is the top-level window the user is currently working with. The window with the keyboard focus is either the active window, or a child window of the active window. To help the user identify the active window, the system places it at the top of the Z order and highlights its title bar (if it has one) and border.

The user can activate a top-level window by clicking it, selecting it using the ALT+TAB or ALT+ESC key combination, or selecting it from the Task List. A thread can activate a top-level window by using the [**SetActiveWindow**](/windows/win32/api/winuser/nf-winuser-setactivewindow) function. It can determine whether a top-level window it created is active by using the [**GetActiveWindow**](/windows/win32/api/winuser/nf-winuser-getactivewindow) function.

When one window is deactivated and another activated, the system sends the [**WM\_ACTIVATE**](wm-activate.md) message. The low-order word of the *wParam* parameter is zero if the window is being deactivated and nonzero if it is being activated. When the default window procedure receives the **WM\_ACTIVATE** message, it sets the keyboard focus to the active window.

To block keyboard and mouse input events from reaching applications, use [**BlockInput**](/windows/win32/api/winuser/nf-winuser-blockinput). Note, the **BlockInput** function will not interfere with the asynchronous keyboard input-state table. This means that calling the [**SendInput**](/windows/win32/api/winuser/nf-winuser-sendinput) function while input is blocked will change the asynchronous keyboard input-state table.

## Keystroke Messages

Pressing a key causes a [**WM\_KEYDOWN**](wm-keydown.md) or [**WM\_SYSKEYDOWN**](wm-syskeydown.md) message to be placed in the thread message queue attached to the window that has the keyboard focus. Releasing a key causes a [**WM\_KEYUP**](wm-keyup.md) or [**WM\_SYSKEYUP**](wm-syskeyup.md) message to be placed in the queue.

Key-up and key-down messages typically occur in pairs, but if the user holds down a key long enough to start the keyboard's automatic repeat feature, the system generates a number of [**WM\_KEYDOWN**](wm-keydown.md) or [**WM\_SYSKEYDOWN**](wm-syskeydown.md) messages in a row. It then generates a single [**WM\_KEYUP**](wm-keyup.md) or [**WM\_SYSKEYUP**](wm-syskeyup.md) message when the user releases the key.

This section covers the following topics:

-   [System and Nonsystem Keystrokes](#system-and-nonsystem-keystrokes)
-   [Virtual-Key Codes Described](#virtual-key-codes-described)
-   [Keystroke Message Flags](#keystroke-message-flags)

### System and Nonsystem Keystrokes

The system makes a distinction between system keystrokes and nonsystem keystrokes. System keystrokes produce system keystroke messages, [**WM\_SYSKEYDOWN**](wm-syskeydown.md) and [**WM\_SYSKEYUP**](wm-syskeyup.md). Nonsystem keystrokes produce nonsystem keystroke messages, [**WM\_KEYDOWN**](wm-keydown.md) and [**WM\_KEYUP**](wm-keyup.md).

If your window procedure must process a system keystroke message, make sure that after processing the message the procedure passes it to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. Otherwise, all system operations involving the ALT key will be disabled whenever the window has the keyboard focus. That is, the user won't be able to access the window's menus or System menu, or use the ALT+ESC or ALT+TAB key combination to activate a different window.

System keystroke messages are primarily for use by the system rather than by an application. The system uses them to provide its built-in keyboard interface to menus and to allow the user to control which window is active. System keystroke messages are generated when the user types a key in combination with the ALT key, or when the user types and no window has the keyboard focus (for example, when the active application is minimized). In this case, the messages are posted to the message queue attached to the active window.

Nonsystem keystroke messages are for use by application windows; the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function does nothing with them. A window procedure can discard any nonsystem keystroke messages that it does not need.

### Virtual-Key Codes Described

The **wParam** parameter of a keystroke message contains the [virtual-key code](virtual-key-codes.md) of the key that was pressed or released. A window procedure processes or ignores a keystroke message, depending on the value of the virtual-key code.

A typical window procedure processes only a small subset of the keystroke messages that it receives and ignores the rest. For example, a window procedure might process only [**WM\_KEYDOWN**](wm-keydown.md) keystroke messages, and only those that contain virtual-key codes for the cursor movement keys, shift keys (also called control keys), and function keys. A typical window procedure does not process keystroke messages from character keys. Instead, it uses the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function to convert the message into character messages. For more information about **TranslateMessage** and character messages, see [Character Messages](#character-messages).

### Keystroke Message Flags

The **lParam** parameter of a keystroke message contains additional information about the keystroke that generated the message. This information includes the [repeat count](#repeat-count), the [scan code](#scan-codes), the [extended-key flag](#extended-key-flag), the [context code](#context-code), the [previous key-state flag](#previous-key-state-flag), and the [transition-state flag](#transition-state-flag). The following illustration shows the locations of these flags and values in the **lParam** parameter.

![the locations of the flags and values in the lparam parameter of a keystroke message](images/csinp-02.png)

An application can use the following values to get the keystroke flags from high-order word of the **lParam**.

| Value                       | Description                                                                       |
|-----------------------------|-----------------------------------------------------------------------------------|
| **KF\_EXTENDED**<br/>0x0100 | Manipulates the [extended key flag](#extended-key-flag).                          |
| **KF\_DLGMODE**<br/>0x0800  | Manipulates the dialog mode flag, which indicates whether a dialog box is active. |
| **KF\_MENUMODE**<br/>0x1000 | Manipulates the menu mode flag, which indicates whether a menu is active.         |
| **KF\_ALTDOWN**<br/>0x2000  | Manipulates the [context code flag](#context-code).                               |
| **KF\_REPEAT**<br/>0x4000   | Manipulates the [previous key state flag](#previous-key-state-flag).              |
| **KF\_UP**<br/>0x8000       | Manipulates the [transition state flag](#previous-key-state-flag).                |


Example code:

```cpp
case WM_KEYDOWN:
case WM_KEYUP:
case WM_SYSKEYDOWN:
case WM_SYSKEYUP:
{
    WORD vkCode = LOWORD(wParam);                                 // virtual-key code
    
    WORD keyFlags = HIWORD(lParam);

    WORD scanCode = LOBYTE(keyFlags);                             // scan code
    BOOL isExtendedKey = (keyFlags & KF_EXTENDED) == KF_EXTENDED; // extended-key flag, 1 if scancode has 0xE0 prefix
    
    if (isExtendedKey)
        scanCode = MAKEWORD(scanCode, 0xE0);

    BOOL wasKeyDown = (keyFlags & KF_REPEAT) == KF_REPEAT;        // previous key-state flag, 1 on autorepeat
    WORD repeatCount = LOWORD(lParam);                            // repeat count, > 0 if several keydown messages was combined into one message

    BOOL isKeyReleased = (keyFlags & KF_UP) == KF_UP;             // transition-state flag, 1 on keyup

    // if we want to distinguish these keys:
    switch (vkCode)
    {
    case VK_SHIFT:   // converts to VK_LSHIFT or VK_RSHIFT
    case VK_CONTROL: // converts to VK_LCONTROL or VK_RCONTROL
    case VK_MENU:    // converts to VK_LMENU or VK_RMENU
        vkCode = LOWORD(MapVirtualKeyW(scanCode, MAPVK_VSC_TO_VK_EX));
        break;
    }

    // ...
}
break;
```

### Repeat Count

You can check the repeat count to determine whether a keystroke message represents more than one keystroke. The system increments the count when the keyboard generates [**WM\_KEYDOWN**](wm-keydown.md) or [**WM\_SYSKEYDOWN**](wm-syskeydown.md) messages faster than an application can process them. This often occurs when the user holds down a key long enough to start the keyboard's automatic repeat feature. Instead of filling the system message queue with the resulting key-down messages, the system combines the messages into a single key down message and increments the repeat count. Releasing a key cannot start the automatic repeat feature, so the repeat count for [**WM\_KEYUP**](wm-keyup.md) and [**WM\_SYSKEYUP**](wm-syskeyup.md) messages is always set to 1.

### Scan Codes

:::image type="content" source="images/keyboard-key-locations.png" alt-text="Diagram of a keyboard with the Scan Code specification for each key.":::

The scan code is the value that the keyboard class driver generates when the user presses a key. It is a value that identifies the key pressed, as opposed to the character represented by the key. An application typically ignores scan codes. Instead, it uses the virtual-key codes to interpret keystroke messages.

> [!NOTE]
> While virtual key codes are typically more useful, scan codes might be required in specific cases when you need to know which key is pressed regardless of the current keyboard layout. For example, the WASD (W is up, A is left, S is down, and D is right) key bindings for games, which ensure a consistent key formation across keyboard layouts.

The following table lists the full set of Scan Codes as presently recognized by Windows. The US Key assignments are for reference to a type 101/102 Enhanced keyboard as supported by the Type 4 Keyboard layout. The **Key location** values reference the preceding keyboard image.

The "Scan 1 make" code is delivered in WM_KEYDOWN/WM_KEYUP and WM_SYSKEYDOWN/WM_SYSKEYUP messages.

| Key location | 101/102 Enhanced keyboard | Scan 1 make |
|-----|------------------------------------------------------------------------------------------------|-------|
| 1   | \~ \`                                                                                          | 29    |
| 2   | ! 1                                                                                            | 02    |
| 3   | @ 2                                                                                            | 03    |
| 4   | \# 3                                                                                           | 04    |
| 5   | $ 4                                                                                            | 05    |
| 6   | % 5                                                                                            | 06    |
| 7   | ^ 6                                                                                            | 07    |
| 8   | & 7                                                                                            | 08    |
| 9   | \* 8                                                                                           | 09    |
| 10  | ( 9                                                                                            | 0A    |
| 11  | ) 0                                                                                            | 0B    |
| 12  | \_ -                                                                                           | 0C    |
| 13  | \+ =                                                                                           | 0D    |
| 15  | Backspace                                                                                      | 0E    |
| 16  | Tab                                                                                            | 0F    |
| 17  | Q                                                                                              | 10    |
| 18  | W                                                                                              | 11    |
| 19  | E                                                                                              | 12    |
| 20  | R                                                                                              | 13    |
| 21  | T                                                                                              | 14    |
| 22  | Y                                                                                              | 15    |
| 23  | U                                                                                              | 16    |
| 24  | I                                                                                              | 17    |
| 25  | O                                                                                              | 18    |
| 26  | P                                                                                              | 19    |
| 27  | { \[                                                                                           | 1A    |
| 28  | } \]                                                                                           | 1B    |
| 29  | \\ \|<br>*(Available on the US and not on the International Keyboard.)*                        | 2B    |
| 30  | Caps Lock                                                                                      | 3A    |
| 31  | A                                                                                              | 1E    |
| 32  | S                                                                                              | 1F    |
| 33  | D                                                                                              | 20    |
| 34  | F                                                                                              | 21    |
| 35  | G                                                                                              | 22    |
| 36  | H                                                                                              | 23    |
| 37  | J                                                                                              | 24    |
| 38  | K                                                                                              | 25    |
| 39  | L                                                                                              | 26    |
| 40  | : ;                                                                                            | 27    |
| 41  | “ ‘                                                                                            | 28    |
| 42  | Europe 1<br>*(Available on the International Keyboard and not on the US Keyboard.*             | 2B    |
| 43  | Enter                                                                                          | 1C    |
| 44  | Left Shift                                                                                     | 2A    |
| 45  | Europe 2<br>*(Available on the International Keyboard and not on the US Keyboard.*             | 56    |
| 46  | Z                                                                                              | 2C    |
| 47  | X                                                                                              | 2D    |
| 48  | C                                                                                              | 2E    |
| 49  | V                                                                                              | 2F    |
| 50  | B                                                                                              | 30    |
| 51  | N                                                                                              | 31    |
| 52  | M                                                                                              | 32    |
| 53  | \< ,                                                                                           | 33    |
| 54  | \> .                                                                                           | 34    |
| 55  | ? /                                                                                            | 35    |
| 56  | RO<br>*(Used on Brazilian and some Far East keyboards. Not available on US Keyboards.)*        | 73    |
| 57  | Right Shift                                                                                    | 36    |
| 58  | Left Control                                                                                   | 1D    |
| 60  | Left Alt                                                                                       | 38    |
| 61  | Space Bar                                                                                      | 39    |
| 62  | Right Alt                                                                                      | E0_38 |
| 64  | Right Control                                                                                  | E0_1D |
| 75  | Insert                                                                                         | E0_52 |
| 76  | Delete                                                                                         | E0_53 |
| 79  | Left Arrow                                                                                     | E0_4B |
| 80  | Home                                                                                           | E0_47 |
| 81  | End                                                                                            | E0_4F |
| 83  | Up Arrow                                                                                       | E0_48 |
| 84  | Down Arrow                                                                                     | E0_50 |
| 85  | Page Up                                                                                        | E0_49 |
| 86  | Page Down                                                                                      | E0_51 |
| 89  | Right Arrow                                                                                    | E0_4D |
| 90  | Num Lock                                                                                       | 45    |
| 91  | Numeric 7                                                                                      | 47    |
| 92  | Numeric 4                                                                                      | 4B    |
| 93  | Numeric 1                                                                                      | 4F    |
| 95  | Numeric /                                                                                      | E0_35 |
| 96  | Numeric 8                                                                                      | 48    |
| 97  | Numeric 5                                                                                      | 4C    |
| 98  | Numeric 2                                                                                      | 50    |
| 99  | Numeric 0                                                                                      | 52    |
| 100 | Numeric \*                                                                                     | 37    |
| 101 | Numeric 9                                                                                      | 49    |
| 102 | Numeric 6                                                                                      | 4D    |
| 103 | Numeric 3                                                                                      | 51    |
| 104 | Numeric .                                                                                      | 53    |
| 105 | Numeric -                                                                                      | 4A    |
| 106 | Numeric +                                                                                      | 4E    |
| 107 | Numeric ,<br>*(Used on Brazilian and some Far East keyboards. Not available on US Keyboards.)* | 7E    |
| 108 | Numeric Enter                                                                                  | E0_1C |
| 110 | Esc                                                                                            | 01    |
| 112 | F1                                                                                             | 3B    |
| 113 | F2                                                                                             | 3C    |
| 114 | F3                                                                                             | 3D    |
| 115 | F4                                                                                             | 3E    |
| 116 | F5                                                                                             | 3F    |
| 117 | F6                                                                                             | 40    |
| 118 | F7                                                                                             | 41    |
| 119 | F8                                                                                             | 42    |
| 120 | F9                                                                                             | 43    |
| 121 | F10                                                                                            | 44    |
| 122 | F11                                                                                            | 57    |
| 123 | F12                                                                                            | 58    |
| 124 | Print Screen                                                                                   | E0_37 |
| 125 | Scroll Lock                                                                                    | 46    |
| 126 | Pause                                                                                          | E1_1D |
|     | Katakana/Hiragana<br>*(Used for Far East keyboards.)*                                          | 70    |
|     | Hiragana<br>*(Used for Far East keyboards.)*                                                   | 77    |
|     | Henkan<br>*(Used for Far East keyboards.)*                                                     | 79    |
|     | Muhenkan<br>*(Used for Far East keyboards.)*                                                   | 7B    |
|     | Previous Track                                                                                 | E0_10 |
|     | Next Track                                                                                     | E0_19 |
|     | Volume Mute                                                                                    | E0_20 |
|     | Launch App 2                                                                                   | E0_21 |
|     | Media Play/Pause                                                                               | E0_22 |
|     | Media Stop                                                                                     | E0_24 |
|     | Volume Down                                                                                    | E0_2E |
|     | Volume Up                                                                                      | E0_30 |
|     | Browser Home                                                                                   | E0_32 |
|     | Break*(Ctrl + Pause)*                                                                          | E0_46 |
|     | Left Win                                                                                       | E0_5B |
|     | Right Win                                                                                      | E0_5C |
|     | Application                                                                                    | E0_5D |
|     | System Power                                                                                   | E0_5E |
|     | System Sleep                                                                                   | E0_5F |
|     | System Wake                                                                                    | E0_63 |
|     | Browser Search                                                                                 | E0_65 |
|     | Browser Favorites                                                                              | E0_66 |
|     | Browser Refresh                                                                                | E0_67 |
|     | Browser Stop                                                                                   | E0_68 |
|     | Browser Forward                                                                                | E0_69 |
|     | Browser Back                                                                                   | E0_6A |
|     | Launch App 1                                                                                   | E0_6B |
|     | Launch Mail                                                                                    | E0_6C |
|     | Launch Media Select                                                                            | E0_6D |
|     | Pause*(Ctrl + NumLock)*                                                                        | E1_1D |

### Extended-Key Flag

The extended-key flag indicates whether the keystroke message originated from one of the additional keys on the Enhanced 101/102-key keyboard. The extended keys consist of the ALT and CTRL keys on the right-hand side of the keyboard; the INS, DEL, HOME, END, PAGE UP, PAGE DOWN, and arrow keys in the clusters to the left of the numeric keypad; the NUM LOCK key; the BREAK (CTRL+PAUSE) key; the PRINT SCRN key; and the divide (/) and ENTER keys in the numeric keypad. The right-hand SHIFT key is not considered an extended-key, it has a separate scan code instead.

If specified, the scan code consists of a sequence of two bytes, where the first byte has a value of 0xE0.

### Context Code

The context code indicates whether the ALT key was down when the keystroke message was generated. The code is 1 if the ALT key was down and 0 if it was up.

### Previous Key-State Flag

The previous key-state flag indicates whether the key that generated the keystroke message was previously up or down. It is 1 if the key was previously down and 0 if the key was previously up. You can use this flag to identify keystroke messages generated by the keyboard's automatic repeat feature. This flag is set to 1 for [**WM\_KEYDOWN**](wm-keydown.md) and [**WM\_SYSKEYDOWN**](wm-syskeydown.md) keystroke messages generated by the automatic repeat feature. It is always set to 1 for [**WM\_KEYUP**](wm-keyup.md) and [**WM\_SYSKEYUP**](wm-syskeyup.md) messages.

### Transition-State Flag

The transition-state flag indicates whether pressing a key or releasing a key generated the keystroke message. This flag is always set to 0 for [**WM\_KEYDOWN**](wm-keydown.md) and [**WM\_SYSKEYDOWN**](wm-syskeydown.md) messages; it is always set to 1 for [**WM\_KEYUP**](wm-keyup.md) and [**WM\_SYSKEYUP**](wm-syskeyup.md) messages.

## Character Messages

Keystroke messages provide a lot of information about keystrokes, but they do not provide character codes for character keystrokes. To retrieve character codes, an application must include the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function in its thread message loop. **TranslateMessage** passes a [**WM\_KEYDOWN**](wm-keydown.md) or [**WM\_SYSKEYDOWN**](wm-syskeydown.md) message to the keyboard layout. The layout examines the message's virtual-key code and, if it corresponds to a character key, provides the character code equivalent (taking into account the state of the SHIFT and CAPS LOCK keys). It then generates a character message that includes the character code and places the message at the top of the message queue. The next iteration of the message loop removes the character message from the queue and dispatches the message to the appropriate window procedure.

This section covers the following topics:

-   [Nonsystem Character Messages](#nonsystem-character-messages)
-   [Dead-Character Messages](#dead-character-messages)

### Nonsystem Character Messages

A window procedure can receive the following character messages: [**WM\_CHAR**](wm-char.md), [**WM\_DEADCHAR**](wm-deadchar.md), [**WM\_SYSCHAR**](/windows/desktop/menurc/wm-syschar), [**WM\_SYSDEADCHAR**](wm-sysdeadchar.md), and [**WM\_UNICHAR**](wm-unichar.md). The [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function generates a **WM\_CHAR** or **WM\_DEADCHAR** message when it processes a [**WM\_KEYDOWN**](wm-keydown.md) message. Similarly, it generates a **WM\_SYSCHAR** or **WM\_SYSDEADCHAR** message when it processes a [**WM\_SYSKEYDOWN**](wm-syskeydown.md) message.

An application that processes keyboard input typically ignores all but the [**WM\_CHAR**](wm-char.md) and [**WM\_UNICHAR**](wm-unichar.md) messages, passing any other messages to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowprocw) function. Note that **WM\_CHAR** uses UTF-16 (16-bit Unicode Transformation Format) or ANSI character set while **WM\_UNICHAR** always uses UTF-32 (32-bit Unicode Transformation Format). The system uses the [**WM\_SYSCHAR**](/windows/desktop/menurc/wm-syschar) and [**WM\_SYSDEADCHAR**](wm-sysdeadchar.md) messages to implement menu mnemonics.

The **wParam** parameter of all character messages contains the character code of the character key that was pressed. The value of the character code depends on the window class of the window receiving the message. If the Unicode version of the [**RegisterClass**](/windows/win32/api/winuser/nf-winuser-registerclassw) function was used to register the window class, the system provides Unicode characters to all windows of that class. Otherwise, the system provides ANSI character codes. For more information, see [Registering Window Classes](/windows/win32/intl/registering-window-classes) and [Use UTF-8 code pages in Windows apps](/windows/apps/design/globalizing/use-utf8-code-page).

The contents of the **lParam** parameter of a character message are identical to the contents of the **lParam** parameter of the key-down message that was translated to produce the character message. For information, see [Keystroke Message Flags](#keystroke-message-flags).

### Dead-Character Messages

Some non-English keyboards contain character keys that are not expected to produce characters by themselves. Instead, they are used to add a diacritic to the character produced by the subsequent keystroke. These keys are called *dead keys*. The circumflex key on a German keyboard is an example of a dead key. To enter the character consisting of an "o" with a circumflex, a German user would type the circumflex key followed by the "o" key. The window with the keyboard focus would receive the following sequence of messages:

1.  [**WM\_KEYDOWN**](wm-keydown.md)
2.  [**WM\_DEADCHAR**](wm-deadchar.md)
3.  [**WM\_KEYUP**](wm-keyup.md)
4.  [**WM\_KEYDOWN**](wm-keydown.md)
5.  [**WM\_CHAR**](wm-char.md)
6.  [**WM\_KEYUP**](wm-keyup.md)

[**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) generates the [**WM\_DEADCHAR**](wm-deadchar.md) message when it processes the [**WM\_KEYDOWN**](wm-keydown.md) message from a dead key. Although the *wParam* parameter of the **WM\_DEADCHAR** message contains the character code of the diacritic for the dead key, an application typically ignores the message. Instead, it processes the [**WM\_CHAR**](wm-char.md) message generated by the subsequent keystroke. The *wParam* parameter of the **WM\_CHAR** message contains the character code of the letter with the diacritic. If the subsequent keystroke generates a character that cannot be combined with a diacritic, the system generates two **WM\_CHAR** messages. The *wParam* parameter of the first contains the character code of the diacritic; the *wParam* parameter of the second contains the character code of the subsequent character key.

The [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function generates the [**WM\_SYSDEADCHAR**](wm-sysdeadchar.md) message when it processes the [**WM\_SYSKEYDOWN**](wm-syskeydown.md) message from a system dead key (a dead key that is pressed in combination with the ALT key). An application typically ignores the **WM\_SYSDEADCHAR** message.

## Key Status

While processing a keyboard message, an application may need to determine the status of another key besides the one that generated the current message. For example, a word-processing application that allows the user to press SHIFT+END to select a block of text must check the status of the SHIFT key whenever it receives a keystroke message from the END key. The application can use the [**GetKeyState**](/windows/win32/api/winuser/nf-winuser-getkeystate) function to determine the status of a virtual key at the time the current message was generated; it can use the [**GetAsyncKeyState**](/windows/win32/api/winuser/nf-winuser-getasynckeystate) function to retrieve the current status of a virtual key.

The keyboard layout maintains a list of names. The name of a key that produces a single character is the same as the character produced by the key. The name of a noncharacter key such as TAB and ENTER is stored as a character string. An application can retrieve the name of any key from the device driver by calling the [**GetKeyNameText**](/windows/win32/api/winuser/nf-winuser-getkeynametexta) function.

## Keystroke and Character Translations

The system includes several special purpose functions that translate scan codes, character codes, and virtual-key codes provided by various keystroke messages. These functions include [**MapVirtualKey**](/windows/win32/api/winuser/nf-winuser-mapvirtualkeya), [**ToAscii**](/windows/win32/api/winuser/nf-winuser-toascii), [**ToUnicode**](/windows/win32/api/winuser/nf-winuser-tounicode), and [**VkKeyScan**](/windows/win32/api/winuser/nf-winuser-vkkeyscana).

In addition, Microsoft Rich Edit 3.0 supports the [HexToUnicode IME](/windows/desktop/Intl/hextounicode-ime), which allows a user to convert between hexadecimal and Unicode characters by using hot keys. This means that when Microsoft Rich Edit 3.0 is incorporated into an application, the application will inherit the features of the HexToUnicode IME.

## Hot-Key Support

A *hot key* is a key combination that generates a [**WM\_HOTKEY**](wm-hotkey.md) message, a message the system places at the top of a thread's message queue, bypassing any existing messages in the queue. Applications use hot keys to obtain high-priority keyboard input from the user. For example, by defining a hot key consisting of the CTRL+C key combination, an application can allow the user to cancel a lengthy operation.

To define a hot key, an application calls the [**RegisterHotKey**](/windows/win32/api/winuser/nf-winuser-registerhotkey) function, specifying the combination of keys that generates the [**WM\_HOTKEY**](wm-hotkey.md) message, the handle to the window to receive the message, and the identifier of the hot key. When the user presses the hot key, a **WM\_HOTKEY** message is placed in the message queue of the thread that created the window. The *wParam* parameter of the message contains the identifier of the hot key. The application can define multiple hot keys for a thread, but each hot key in the thread must have a unique identifier. Before the application terminates, it should use the [**UnregisterHotKey**](/windows/win32/api/winuser/nf-winuser-unregisterhotkey) function to destroy the hot key.

Applications can use a hot key control to make it easy for the user to choose a hot key. Hot key controls are typically used to define a hot key that activates a window; they do not use the [**RegisterHotKey**](/windows/win32/api/winuser/nf-winuser-registerhotkey) and [**UnregisterHotKey**](/windows/win32/api/winuser/nf-winuser-unregisterhotkey) functions. Instead, an application that uses a hot key control typically sends the [**WM\_SETHOTKEY**](wm-sethotkey.md) message to set the hot key. Whenever the user presses the hot key, the system sends a [**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand) message specifying SC\_HOTKEY. For more information about hot key controls, see "Using Hot Key Controls" in [Hot Key Controls](../controls/hot-key-controls.md).

## Keyboard Keys for Browsing and Other Functions

Windows provides support for keyboards with special keys for browser functions, media functions, application launching, and power management. The [**WM\_APPCOMMAND**](wm-appcommand.md) supports the extra keyboard keys. In addition, the [**ShellProc**](/previous-versions/windows/desktop/legacy/ms644991(v=vs.85)) function is modified to support the extra keyboard keys.

It is unlikely that a child window in a component application will be able to directly implement commands for these extra keyboard keys. So when one of these keys is pressed, [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) will send a [**WM\_APPCOMMAND**](wm-appcommand.md) message to a window. **DefWindowProc** will also bubble the **WM\_APPCOMMAND** message to its parent window. This is similar to the way context menus are invoked with the right mouse button, which is that **DefWindowProc** sends a [**WM\_CONTEXTMENU**](/windows/desktop/menurc/wm-contextmenu) message on a right button click, and bubbles it to its parent. Additionally, if **DefWindowProc** receives a **WM\_APPCOMMAND** message for a top-level window, it will call a shell hook with code **HSHELL\_APPCOMMAND**.

Windows also supports the Microsoft IntelliMouse Explorer, which is a mouse with five buttons. The two extra buttons support forward and backward browser navigation. For more information, see [XBUTTONs](about-mouse-input.md).

## Simulating Input

To simulate an uninterrupted series of user input events, use the [**SendInput**](/windows/win32/api/winuser/nf-winuser-sendinput) function. The function accepts three parameters. The first parameter, *cInputs*, indicates the number of input events that will be simulated. The second parameter, *rgInputs*, is an array of [**INPUT**](/windows/win32/api/winuser/ns-winuser-input) structures, each describing a type of input event and additional information about that event. The last parameter, *cbSize*, accepts the size of the **INPUT** structure, in bytes.

The [**SendInput**](/windows/win32/api/winuser/nf-winuser-sendinput) function works by injecting a series of simulated input events into a device's input stream. The effect is similar to calling the [**keybd\_event**](/windows/win32/api/winuser/nf-winuser-keybd_event) or [**mouse\_event**](/windows/win32/api/winuser/nf-winuser-mouse_event) function repeatedly, except that the system ensures that no other input events intermingle with the simulated events. When the call completes, the return value indicates the number of input events successfully played. If this value is zero, then input was blocked.

The [**SendInput**](/windows/win32/api/winuser/nf-winuser-sendinput) function does not reset the keyboard's current state. Therefore, if the user has any keys pressed when you call this function, they might interfere with the events that this function generates. If you are concerned about possible interference, check the keyboard's state with the [**GetAsyncKeyState**](/windows/win32/api/winuser/nf-winuser-getasynckeystate) function and correct as necessary.

## Languages, Locales, and Keyboard Layouts

A *language* is a natural language, such as English, French, and Japanese. A *sublanguage* is a variant of a natural language that is spoken in a specific geographical region, such as the English sublanguages spoken in the United Kingdom and the United States. Applications use values, called [language identifiers](/windows/desktop/Intl/language-identifiers), to uniquely identify languages and sublanguages.

Applications typically use *locales* to set the language in which input and output is processed. Setting the locale for the keyboard, for example, affects the character values generated by the keyboard. Setting the locale for the display or printer affects the glyphs displayed or printed. Applications set the locale for a keyboard by loading and using keyboard layouts. They set the locale for a display or printer by selecting a font that supports the specified locale.

A keyboard layout not only specifies the physical position of the keys on the keyboard but also determines the character values generated by pressing those keys. Each layout identifies the current input language and determines which character values are generated by which keys and key combinations.

Every keyboard layout has a corresponding handle that identifies the layout and language. The low word of the handle is a language identifier. The high word is a device handle, specifying the physical layout, or is zero, indicating a default physical layout. The user can associate any input language with a physical layout. For example, an English-speaking user who very occasionally works in French can set the input language of the keyboard to French without changing the physical layout of the keyboard. This means the user can enter text in French using the familiar English layout.

Applications are generally not expected to manipulate input languages directly. Instead, the user sets up language and layout combinations, then switches among them. When the user clicks into text marked with a different language, the application calls the [**ActivateKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-activatekeyboardlayout) function to activate the user's default layout for that language. If the user edits text in a language which is not in the active list, the application can call the [**LoadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-loadkeyboardlayouta) function with the language to get a layout based on that language.

The [**ActivateKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-activatekeyboardlayout) function sets the input language for the current task. The *hkl* parameter can be either the handle to the keyboard layout or a zero-extended language identifier. Keyboard layout handles can be obtained from the [**LoadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-loadkeyboardlayouta) or [**GetKeyboardLayoutList**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayoutlist) function. The **HKL\_NEXT** and **HKL\_PREV** values can also be used to select the next or previous keyboard.

The [**GetKeyboardLayoutName**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayoutnamea) function retrieves the name of the active keyboard layout for the calling thread. If an application creates the active layout using the [**LoadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-loadkeyboardlayouta) function, **GetKeyboardLayoutName** retrieves the same string used to create the layout. Otherwise, the string is the primary language identifier corresponding to the locale of the active layout. This means the function may not necessarily differentiate among different layouts with the same primary language, so cannot return specific information about the input language. The [**GetKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayout) function, however, can be used to determine the input language.

The [**LoadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-loadkeyboardlayouta) function loads a keyboard layout and makes the layout available to the user. Applications can make the layout immediately active for the current thread by using the **KLF\_ACTIVATE** value. An application can use the **KLF\_REORDER** value to reorder the layouts without also specifying the **KLF\_ACTIVATE** value. Applications should always use the **KLF\_SUBSTITUTE\_OK** value when loading keyboard layouts to ensure that the user's preference, if any, is selected.

For multilingual support, the [**LoadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-loadkeyboardlayouta) function provides the **KLF\_REPLACELANG** and **KLF\_NOTELLSHELL** flags. The **KLF\_REPLACELANG** flag directs the function to replace an existing keyboard layout without changing the language. Attempting to replace an existing layout using the same language identifier but without specifying **KLF\_REPLACELANG** is an error. The **KLF\_NOTELLSHELL** flag prevents the function from notifying the shell when a keyboard layout is added or replaced. This is useful for applications that add multiple layouts in a consecutive series of calls. This flag should be used in all but the last call.

The [**UnloadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-unloadkeyboardlayout) function is restricted in that it cannot unload the system default input language. This ensures that the user always has one layout available for enter text using the same character set as used by the shell and file system.
