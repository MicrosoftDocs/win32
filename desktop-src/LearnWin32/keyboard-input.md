---
title: Keyboard Input (Get Started with Win32 and C++)
description: Keyboard Input
ms.assetid: FC682E8B-8360-4D58-AC42-4CEFD9CB750F
ms.topic: article
ms.date: 05/31/2018
---

# Keyboard Input (Get Started with Win32 and C++)

The keyboard is used for several distinct types of input, including:

-   Character input. Text that the user types into a document or edit box.
-   Keyboard shortcuts. Key strokes that invoke application functions; for example, CTRL + O to open a file.
-   System commands. Key strokes that invoke system functions; for example, ALT + TAB to switch windows.

When thinking about keyboard input, it is important to remember that a key stroke is not the same as a character. For example, pressing the A key could result in any of the following characters.

-   a
-   A
-   á (if the keyboard supports combining diacritics)

Further, if the ALT key is held down, pressing the A key produces ALT+A, which the system does not treat as a character at all, but rather as a system command.

## Key Codes

When you press a key, the hardware generates a *scan code*. Scan codes vary from one keyboard to the next, and there are separate scan codes for key-up and key-down events. You will almost never care about scan codes. The keyboard driver translates scan codes into *virtual-key codes*. Virtual-key codes are device-independent. Pressing the A key on any keyboard generates the same virtual-key code.

In general, virtual-key codes do not correspond to ASCII codes or any other character-encoding standard. This is obvious if you think about it, because the same key can generate different characters (a, A, á), and some keys, such as function keys, do not correspond to any character.

That said, the following virtual-key codes do map to ASCII equivalents:

-   0 through 9 keys = ASCII '0' – '9' (0x30 – 0x39)
-   A through Z keys = ASCII 'A' – 'Z' (0x41 – 0x5A)

In some respects this mapping is unfortunate, because you should never think of virtual-key codes as characters, for the reasons discussed.

The header file WinUser.h defines constants for most of the virtual-key codes. For example, the virtual-key code for the LEFT ARROW key is **VK\_LEFT** (0x25). For the complete list of virtual-key codes, see [**Virtual-Key Codes**](/windows/desktop/inputdev/virtual-key-codes). No constants are defined for the virtual-key codes that match ASCII values. For example, the virtual-key code for the A key is 0x41, but there is no constant named **VK\_A**. Instead, just use the numeric value.

## Key-Down and Key-Up Messages

When you press a key, the window that has keyboard focus receives one of the following messages.

-   [**WM\_SYSKEYDOWN**](/windows/desktop/inputdev/wm-syskeydown)
-   [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown)

The [**WM\_SYSKEYDOWN**](/windows/desktop/inputdev/wm-syskeydown) message indicates a *system key*, which is a key stroke that invokes a system command. There are two types of system key:

-   ALT + any key
-   F10

The F10 key activates the menu bar of a window. Various ALT-key combinations invoke system commands. For example, ALT + TAB switches to a new window. In addition, if a window has a menu, the ALT key can be used to activate menu items. Some ALT key combinations do not do anything.

All other key strokes are considered nonsystem keys and produce the [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) message. This includes the function keys other than F10.

When you release a key, the system sends a corresponding key-up message:

-   [**WM\_KEYUP**](/windows/desktop/inputdev/wm-keyup)
-   [**WM\_SYSKEYUP**](/windows/desktop/inputdev/wm-syskeyup)

If you hold down a key long enough to start the keyboard's repeat feature, the system sends multiple key-down messages, followed by a single key-up message.

In all four of the keyboard messages discussed so far, the *wParam* parameter contains the virtual-key code of the key. The *lParam* parameter contains some miscellaneous information packed into 32 bits. You typically do not need the information in *lParam*. One flag that might be useful is bit 30, the "previous key state" flag, which is set to 1 for repeated key-down messages.

As the name implies, system key strokes are primarily intended for use by the operating system. If you intercept the [**WM\_SYSKEYDOWN**](/windows/desktop/inputdev/wm-syskeydown) message, call [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) afterward. Otherwise, you will block the operating system from handling the command.

## Character Messages

Key strokes are converted into characters by the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function, which we first saw in [Module 1](your-first-windows-program.md). This function examines key-down messages and translates them into characters. For each character that is produced, the **TranslateMessage** function puts a [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) or [**WM\_SYSCHAR**](/windows/desktop/menurc/wm-syschar) message on the message queue of the window. The *wParam* parameter of the message contains the UTF-16 character.

As you might guess, [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) messages are generated from [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) messages, while [**WM\_SYSCHAR**](/windows/desktop/menurc/wm-syschar) messages are generated from [**WM\_SYSKEYDOWN**](/windows/desktop/inputdev/wm-syskeydown) messages. For example, suppose the user presses the SHIFT key followed by the A key. Assuming a standard keyboard layout, you would get the following sequence of messages:

**WM\_KEYDOWN**: SHIFT  
**WM\_KEYDOWN**: A  
**WM\_CHAR**: 'A'  


On the other hand, the combination ALT + P would generate:

 **WM\_SYSKEYDOWN**: VK\_MENU  
**WM\_SYSKEYDOWN**: 0x50  
**WM\_SYSCHAR**: 'p'  
**WM\_SYSKEYUP**: 0x50  
**WM\_KEYUP**: VK\_MENU  


(The virtual-key code for the ALT key is named VK\_MENU for historical reasons.)

The [**WM\_SYSCHAR**](/windows/desktop/menurc/wm-syschar) message indicates a system character. As with [**WM\_SYSKEYDOWN**](/windows/desktop/inputdev/wm-syskeydown), you should generally pass this message directly to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca). Otherwise, you may interfere with standard system commands. In particular, do not treat **WM\_SYSCHAR** as text that the user has typed.

The [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) message is what you normally think of as character input. The data type for the character is **wchar\_t**, representing a UTF-16 Unicode character. Character input can include characters outside the ASCII range, especially with keyboard layouts that are commonly used outside of the United States. You can try different keyboard layouts by installing a regional keyboard and then using the On-Screen Keyboard feature.

Users can also install an Input Method Editor (IME) to enter complex scripts, such as Japanese characters, with a standard keyboard. For example, using a Japanese IME to enter the katakana character カ (ka), you might get the following messages:

**WM\_KEYDOWN**: VK\_PROCESSKEY (the IME PROCESS key)  
**WM\_KEYUP**: 0x4B  
**WM\_KEYDOWN**: VK\_PROCESSKEY  
**WM\_KEYUP**: 0x41  
**WM\_KEYDOWN**: VK\_PROCESSKEY  
**WM\_CHAR**: カ  
**WM\_KEYUP**: VK\_RETURN  


Some CTRL key combinations are translated into ASCII control characters. For example, CTRL+A is translated to the ASCII ctrl-A (SOH) character (ASCII value 0x01). For text input, you should generally filter out the control characters. Also, avoid using [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) to implement keyboard shortcuts. Instead, use [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) messages; or even better, use an accelerator table. Accelerator tables are described in the next topic, [Accelerator Tables](accelerator-tables.md).

The following code displays the main keyboard messages in the debugger. Try playing with different keystroke combinations and see what messages are generated.

> [!Note]  
> Be sure to include wchar.h or else swprintf_s will be undefined.

```C++
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    wchar_t msg[32];
    switch (uMsg)
    {
    case WM_SYSKEYDOWN:
        swprintf_s(msg, L"WM_SYSKEYDOWN: 0x%x\n", wParam);
        OutputDebugString(msg);
        break;

    case WM_SYSCHAR:
        swprintf_s(msg, L"WM_SYSCHAR: %c\n", (wchar_t)wParam);
        OutputDebugString(msg);
        break;

    case WM_SYSKEYUP:
        swprintf_s(msg, L"WM_SYSKEYUP: 0x%x\n", wParam);
        OutputDebugString(msg);
        break;

    case WM_KEYDOWN:
        swprintf_s(msg, L"WM_KEYDOWN: 0x%x\n", wParam);
        OutputDebugString(msg);
        break;

    case WM_KEYUP:
        swprintf_s(msg, L"WM_KEYUP: 0x%x\n", wParam);
        OutputDebugString(msg);
        break;

    case WM_CHAR:
        swprintf_s(msg, L"WM_CHAR: %c\n", (wchar_t)wParam);
        OutputDebugString(msg);
        break;

    /* Handle other messages (not shown) */

    }
    return DefWindowProc(m_hwnd, uMsg, wParam, lParam);
}
```



## Miscellaneous Keyboard Messages

Some other keyboard messages can safely be ignored by most applications.

-   The [**WM\_DEADCHAR**](/windows/desktop/inputdev/wm-deadchar) message is sent for a combining key, such as a diacritic. For example, on a Spanish language keyboard, typing accent (') followed by E produces the character é. The **WM\_DEADCHAR** is sent for the accent character.
-   The [**WM\_UNICHAR**](/windows/desktop/inputdev/wm-unichar) message is obsolete. It enables ANSI programs to receive Unicode character input.
-   The [**WM\_IME\_CHAR**](/windows/desktop/Intl/wm-ime-char) character is sent when an IME translates a keystroke sequence into characters. It is sent in addition to the usual [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) message.

## Keyboard State

The keyboard messages are event-driven. That is, you get a message when something interesting happens, such as a key press, and the message tells you what just happened. But you can also test the state of a key at any time, by calling the [**GetKeyState**](/windows/desktop/api/winuser/nf-winuser-getkeystate) function.

For example, consider how would you detect the combination of left mouse click + ALT key. You could track the state of the ALT key by listening for key-stroke messages and storing a flag, but [**GetKeyState**](/windows/desktop/api/winuser/nf-winuser-getkeystate) saves you the trouble. When you receive the [**WM\_LBUTTONDOWN**](/windows/desktop/inputdev/wm-lbuttondown) message, just call **GetKeyState** as follows:


```C++
if (GetKeyState(VK_MENU) & 0x8000)
{
    // ALT key is down.
}
```



The [**GetKeyState**](/windows/desktop/api/winuser/nf-winuser-getkeystate) message takes a virtual-key code as input and returns a set of bit flags (actually just two flags). The value 0x8000 contains the bit flag that tests whether the key is currently pressed.

Most keyboards have two ALT keys, left and right. The previous example tests whether either of them of pressed. You can also use [**GetKeyState**](/windows/desktop/api/winuser/nf-winuser-getkeystate) to distinguish between the left and right instances of the ALT, SHIFT, or CTRL keys. For example, the following code tests if the right ALT key is pressed.


```C++
if (GetKeyState(VK_RMENU) & 0x8000))
{
    // Right ALT key is down.
}
```



The [**GetKeyState**](/windows/desktop/api/winuser/nf-winuser-getkeystate) function is interesting because it reports a *virtual* keyboard state. This virtual state is based on the contents of your message queue, and gets updated as you remove messages from the queue. As your program processes window messages, **GetKeyState** gives you a snapshot of the keyboard at the time that each message was queued. For example, if the last message on the queue was [**WM\_LBUTTONDOWN**](/windows/desktop/inputdev/wm-lbuttondown), **GetKeyState** reports the keyboard state at the moment when the user clicked the mouse button.

Because [**GetKeyState**](/windows/desktop/api/winuser/nf-winuser-getkeystate) is based on your message queue, it also ignores keyboard input that was sent to another program. If the user switches to another program, any key presses that are sent to that program are ignored by **GetKeyState**. If you really want to know the immediate physical state of the keyboard, there is a function for that: [**GetAsyncKeyState**](/windows/desktop/api/winuser/nf-winuser-getasynckeystate). For most UI code, however, the correct function is **GetKeyState**.

## Next

[Accelerator Tables](accelerator-tables.md)

 

 
