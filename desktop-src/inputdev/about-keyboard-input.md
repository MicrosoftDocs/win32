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

:::image type="content" source="images/keyboard-key-locations.png" alt-text="Diagram of a Type 4 keyboard with the key locations for each key.":::

The scan code is the value that the system generates when the user presses a key. It is a value that identifies the key pressed regardless of the active [keyboard layout](/globalization/windows-keyboard-layouts), as opposed to the character represented by the key. An application typically ignores scan codes. Instead, it uses the virtual-key codes to interpret keystroke messages.

Modern keyboards are using [Human Interface Devices (HID)](https://www.usb.org/hid) specification to communicate with a computer. [Keyboard driver](/windows-hardware/drivers/hid/keyboard-and-mouse-class-drivers) converts reported HID Usage values sent from the keyboard to scan сodes and passes them on to applications.

> [!NOTE]
> While virtual key codes are typically more useful to desktop applications, scan codes might be required in specific cases when you need to know which key is pressed regardless of the current [keyboard layout](/globalization/windows-keyboard-layouts). For example, the WASD (W is up, A is left, S is down, and D is right) key bindings for games, which ensure a consistent key formation across [US QWERTY](/globalization/keyboards/kbdus_7) or [French AZERTY](/globalization/keyboards/kbdfr) keyboard layouts.

The following table lists the set of Scan Codes as presently recognized by Windows. **HID Usage Page**/**HID Usage ID**/**HID Usage Name** values reference the [HID Usage Tables](https://www.usb.org/hid) document. The **Key Location** values reference the preceding keyboard image.

The **Scan 1 Make** code is delivered in [**WM\_KEYDOWN**](wm-keydown.md)/[**WM\_KEYUP**](wm-keyup.md)/[**WM\_SYSKEYDOWN**](wm-syskeydown.md)/[**WM\_SYSKEYUP**](wm-syskeyup.md) and [**WM\_INPUT**](wm-input.md) messages.

| HID Usage Page | HID Usage ID | HID Usage Name                    | Key Location | Scan 1 Make |
|----------------|--------------|-----------------------------------|--------------|-------------|
| 07             | 01           | ErrorRollOver                     |              | FF          |
| 07             | 04           | Keyboard A                        | 31           | 1E          |
| 07             | 05           | Keyboard B                        | 50           | 30          |
| 07             | 06           | Keyboard C                        | 48           | 2E          |
| 07             | 07           | Keyboard D                        | 33           | 20          |
| 07             | 08           | Keyboard E                        | 19           | 12          |
| 07             | 09           | Keyboard F                        | 34           | 21          |
| 07             | 0A           | Keyboard G                        | 35           | 22          |
| 07             | 0B           | Keyboard H                        | 36           | 23          |
| 07             | 0C           | Keyboard I                        | 24           | 17          |
| 07             | 0D           | Keyboard J                        | 37           | 24          |
| 07             | 0E           | Keyboard K                        | 38           | 25          |
| 07             | 0F           | Keyboard L                        | 39           | 26          |
| 07             | 10           | Keyboard M                        | 52           | 32          |
| 07             | 11           | Keyboard N                        | 51           | 31          |
| 07             | 12           | Keyboard O                        | 25           | 18          |
| 07             | 13           | Keyboard P                        | 26           | 19          |
| 07             | 14           | Keyboard Q                        | 17           | 10          |
| 07             | 15           | Keyboard R                        | 20           | 13          |
| 07             | 16           | Keyboard S                        | 32           | 1F          |
| 07             | 17           | Keyboard T                        | 21           | 14          |
| 07             | 18           | Keyboard U                        | 23           | 16          |
| 07             | 19           | Keyboard V                        | 49           | 2F          |
| 07             | 1A           | Keyboard W                        | 18           | 11          |
| 07             | 1B           | Keyboard X                        | 47           | 2D          |
| 07             | 1C           | Keyboard Y                        | 22           | 15          |
| 07             | 1D           | Keyboard Z                        | 46           | 2C          |
| 07             | 1E           | Keyboard 1 and Bang               | 2            | 02          |
| 07             | 1F           | Keyboard 2 and At                 | 3            | 03          |
| 07             | 20           | Keyboard 3 And Hash               | 4            | 04          |
| 07             | 21           | Keyboard 4 and Dollar             | 5            | 05          |
| 07             | 22           | Keyboard 5 and Percent            | 6            | 06          |
| 07             | 23           | Keyboard 6 and Caret              | 7            | 07          |
| 07             | 24           | Keyboard 7 and Ampersand          | 8            | 08          |
| 07             | 25           | Keyboard 8 and Star               | 9            | 09          |
| 07             | 26           | Keyboard 9 and Left Bracket       | 10           | 0A          |
| 07             | 27           | Keyboard 0 and Right Bracket      | 11           | 0B          |
| 07             | 28           | Keyboard Return Enter             | 43           | 1C          |
| 07             | 29           | Keyboard Escape                   | 110          | 01          |
| 07             | 2A           | Keyboard Delete                   | 15           | 0E          |
| 07             | 2B           | Keyboard Tab                      | 16           | 0F          |
| 07             | 2C           | Keyboard Spacebar                 | 61           | 39          |
| 07             | 2D           | Keyboard Dash and Underscore      | 12           | 0C          |
| 07             | 2E           | Keyboard Equals and Plus          | 13           | 0D          |
| 07             | 2F           | Keyboard Left Brace               | 27           | 1A          |
| 07             | 30           | Keyboard Right Brace              | 28           | 1B          |
| 07             | 31           | Keyboard Pipe and Slash           | 29           | 2B          |
| 07             | 32           | Keyboard Non-US                   | 42           | 2B          |
| 07             | 33           | Keyboard SemiColon and Colon      | 40           | 27          |
| 07             | 34           | Keyboard Left Apos and Double     | 41           | 28          |
| 07             | 35           | Keyboard Grave Accent and Tilde   | 1            | 29          |
| 07             | 36           | Keyboard Comma                    | 53           | 33          |
| 07             | 37           | Keyboard Period                   | 54           | 34          |
| 07             | 38           | Keyboard QuestionMark             | 55           | 35          |
| 07             | 39           | Keyboard Caps Lock                | 30           | 3A          |
| 07             | 3A           | Keyboard F1                       | 112          | 3B          |
| 07             | 3B           | Keyboard F2                       | 113          | 3C          |
| 07             | 3C           | Keyboard F3                       | 114          | 3D          |
| 07             | 3D           | Keyboard F4                       | 115          | 3E          |
| 07             | 3E           | Keyboard F5                       | 116          | 3F          |
| 07             | 3F           | Keyboard F6                       | 117          | 40          |
| 07             | 40           | Keyboard F7                       | 118          | 41          |
| 07             | 41           | Keyboard F8                       | 119          | 42          |
| 07             | 42           | Keyboard F9                       | 120          | 43          |
| 07             | 43           | Keyboard F10                      | 121          | 44          |
| 07             | 44           | Keyboard F11                      | 122          | 57          |
| 07             | 45           | Keyboard F12                      | 123          | 58          |
| 07             | 46           | Keyboard PrintScreen              | 124          | E0 37<br>54 \*Note 1 |
| 07             | 47           | Keyboard Scroll Lock              | 125          | 46          |
| 07             | 48           | Keyboard Pause                    | 126          | E1 1D 45<br>E0 46 \*Note 2<br>45 \*Note 3 |
| 07             | 49           | Keyboard Insert                   | 75           | E0 52       |
| 07             | 4A           | Keyboard Home                     | 80           | E0 47       |
| 07             | 4B           | Keyboard PageUp                   | 85           | E0 49       |
| 07             | 4C           | Keyboard Delete Forward           | 76           | E0 53       |
| 07             | 4D           | Keyboard End                      | 81           | E0 4F       |
| 07             | 4E           | Keyboard PageDown                 | 86           | E0 51       |
| 07             | 4F           | Keyboard RightArrow               | 89           | E0 4D       |
| 07             | 50           | Keyboard LeftArrow                | 79           | E0 4B       |
| 07             | 51           | Keyboard DownArrow                | 84           | E0 50       |
| 07             | 52           | Keyboard UpArrow                  | 83           | E0 48       |
| 07             | 53           | Keypad Num Lock and Clear         | 90           | 45<br>E0 45 \*Note 3 |
| 07             | 54           | Keypad Forward Slash              | 95           | E0 35       |
| 07             | 55           | Keypad Star                       | 100          | 37          |
| 07             | 56           | Keypad Dash                       | 105          | 4A          |
| 07             | 57           | Keypad Plus                       | 106          | 4E          |
| 07             | 58           | Keypad ENTER                      | 108          | E0 1C       |
| 07             | 59           | Keypad 1 and End                  | 93           | 4F          |
| 07             | 5A           | Keypad 2 and Down Arrow           | 98           | 50          |
| 07             | 5B           | Keypad 3 and PageDn               | 103          | 51          |
| 07             | 5C           | Keypad 4 and Left Arrow           | 92           | 4B          |
| 07             | 5D           | Keypad 5                          | 97           | 4C          |
| 07             | 5E           | Keypad 6 and Right Arrow          | 102          | 4D          |
| 07             | 5F           | Keypad 7 and Home                 | 91           | 47          |
| 07             | 60           | Keypad 8 and Up Arrow             | 96           | 48          |
| 07             | 61           | Keypad 9 and PageUp               | 101          | 49          |
| 07             | 62           | Keypad 0 and Insert               | 99           | 52          |
| 07             | 63           | Keypad Period                     | 104          | 53          |
| 07             | 64           | Keyboard Non-US Slash Bar         | 45           | 56          |
| 07             | 65           | Keyboard Application              | 129          | E0 5D       |
| 07             | 66           | Keyboard Power                    |              | E0 5E       |
| 07             | 67           | Keypad Equals                     |              | 59          |
| 07             | 68           | Keyboard F13                      |              | 64          |
| 07             | 69           | Keyboard F14                      |              | 65          |
| 07             | 6A           | Keyboard F15                      |              | 66          |
| 07             | 6B           | Keyboard F16                      |              | 67          |
| 07             | 6C           | Keyboard F17                      |              | 68          |
| 07             | 6D           | Keyboard F18                      |              | 69          |
| 07             | 6E           | Keyboard F19                      |              | 6A          |
| 07             | 6F           | Keyboard F20                      |              | 6B          |
| 07             | 70           | Keyboard F21                      |              | 6C          |
| 07             | 71           | Keyboard F22                      |              | 6D          |
| 07             | 72           | Keyboard F23                      |              | 6E          |
| 07             | 73           | Keyboard F24                      |              | 76          |
| 07             | 85           | Keypad Comma                      | 107\*Note 4  | 7E          |
| 07             | 87           | Keyboard International1           | 56\*Note 4, 5 | 73          |
| 07             | 88           | Keyboard International2           | 133\*Note 5  | 70          |
| 07             | 89           | Keyboard International3           | 14\*Note 5   | 7D          |
| 07             | 8A           | Keyboard International4           | 132\*Note 5  | 79          |
| 07             | 8B           | Keyboard International5           | 131\*Note 5  | 7B          |
| 07             | 8C           | Keyboard International6           |              | 5C          |
| 07             | 90           | Keyboard LANG1                    |              | F2          |
| 07             | 91           | Keyboard LANG2                    |              | F1          |
| 07             | 92           | Keyboard LANG3                    |              | 78          |
| 07             | 93           | Keyboard LANG4                    |              | 77          |
| 07             | 94           | Keyboard LANG5                    |              | 76          |
| 07             | E0           | Keyboard LeftControl              | 58           | 1D          |
| 07             | E1           | Keyboard LeftShift                | 44           | 2A          |
| 07             | E2           | Keyboard LeftAlt                  | 60           | 38          |
| 07             | E3           | Keyboard Left GUI                 | 127          | E0 5B       |
| 07             | E4           | Keyboard RightControl             | 64           | E0 1D       |
| 07             | E5           | Keyboard RightShift               | 57           | 36          |
| 07             | E6           | Keyboard RightAlt                 | 62           | E0 38       |
| 07             | E7           | Keyboard Right GUI                | 128          | E0 5C       |
| 01             | 81           | System Power Down                 |              | E0 5E       |
| 01             | 82           | System Sleep                      |              | E0 5F       |
| 01             | 83           | System Wake Up                    |              | E0 63       |
| 0C             | 00B5         | Scan Next Track                   |              | E0 19       |
| 0C             | 00B6         | Scan Previous Track               |              | E0 10       |
| 0C             | 00B7         | Stop                              |              | E0 24       |
| 0C             | 00CD         | Play/Pause                        |              | E0 22       |
| 0C             | 00E2         | Mute                              |              | E0 20       |
| 0C             | 00E9         | Volume Increment                  |              | E0 30       |
| 0C             | 00EA         | Volume Decrement                  |              | E0 2E       |
| 0C             | 0183         | AL Consumer Control Configuration |              | E0 6D       |
| 0C             | 018A         | AL Email Reader                   |              | E0 6C       |
| 0C             | 0192         | AL Calculator                     |              | E0 21       |
| 0C             | 0194         | AL Local Machine Browser          |              | E0 6B       |
| 0C             | 0221         | AC Search                         |              | E0 65       |
| 0C             | 0223         | AC Home                           |              | E0 32       |
| 0C             | 0224         | AC Back                           |              | E0 6A       |
| 0C             | 0225         | AC Forward                        |              | E0 69       |
| 0C             | 0226         | AC Stop                           |              | E0 68       |
| 0C             | 0227         | AC Refresh                        |              | E0 67       |
| 0C             | 022A         | AC Previous Link                  |              | E0 66       |

Notes:

1. *SysRq* key scan code is emmited on *Alt+Print screen* keystroke
2. *Break* key scan code is emmited on *Control+Pause* keystroke
3. As seen in [legacy keyboard messages](keyboard-input-notifications.md)
4. The key is present on Brazilian keyboards
5. The key is present on Japanese keyboards

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
