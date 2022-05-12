---
title: WM_CHAR message (Winuser.h)
description: Posted to the window with the keyboard focus when a WM\_KEYDOWN message is translated by the TranslateMessage function. The WM\_CHAR message contains the character code of the key that was pressed.
ms.assetid: 7e45dc6f-ff68-4534-9e52-46e5f4110532
keywords:
- WM_CHAR message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_CHAR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/28/2020
---

# WM\_CHAR message

Posted to the window with the keyboard focus when a [**WM\_KEYDOWN**](wm-keydown.md) message is translated by the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) function. The **WM\_CHAR** message contains the character code of the key that was pressed.


```C++
#define WM_CHAR                         0x0102
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The character code of the key.

</dd> <dt>

*lParam* 
</dt> <dd>

The repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag, as shown in the following table.



| Bits  | Meaning                                                                                                                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0-15  | The repeat count for the current message. The value is the number of times the keystroke is autorepeated as a result of the user holding down the key. If the keystroke is held long enough, multiple messages are sent. However, the repeat count is not cumulative. |
| 16-23 | The scan code. The value depends on the OEM.                                                                                                                                                                                                                          |
| 24    | Indicates whether the key is an extended key, such as the right-hand ALT and CTRL keys that appear on an enhanced 101- or 102-key keyboard. The value is 1 if it is an extended key; otherwise, it is 0.                                                              |
| 25-28 | Reserved; do not use.                                                                                                                                                                                                                                                 |
| 29    | The context code. The value is 1 if the ALT key is held down while the key is pressed; otherwise, the value is 0.                                                                                                                                                     |
| 30    | The previous key state. The value is 1 if the key is down before the message is sent, or it is 0 if the key is up.                                                                                                                                                    |
| 31    | The transition state. The value is 1 if the key is being released, or it is 0 if the key is being pressed.                                                                                                                                                            |

For more detail, see [Keystroke Message Flags](about-keyboard-input.md#keystroke-message-flags).
 

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Example

```cpp
LRESULT CALLBACK WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
   
    // ...

    case WM_CHAR:
        OnKeyPress(wParam);
        break;

    default:
        return DefWindowProc(hwnd, message, wParam, lParam);
    }
    return 0;
}
```
Example from [Windows Classic Samples](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/Win7Samples/multimedia/mediafoundation/protectedplayback/winmain.cpp) on GitHub.

## Remarks

The **WM\_CHAR** message uses UTF-16 (16-bit Unicode Transformation Format) code units in its **wParam** if the Unicode version of the [**RegisterClass**](/windows/win32/api/winuser/nf-winuser-registerclassw) function was used to register the window class. Otherwise, the system provides characters in the current process code page - that could be set to UTF-8 since Windows Version 1903 (May 2019 Update). For more information, see [Registering Window Classes](/windows/win32/intl/registering-window-classes) and [Use UTF-8 code pages in Windows apps](/windows/apps/design/globalizing/use-utf8-code-page).

Since Windows Vista **WM\_CHAR** message can send [UTF-16 surrogate pairs](/windows/win32/intl/surrogates-and-supplementary-characters) to Unicode windows. [IS_HIGH_SURROGATE](/windows/win32/api/Winnls/nf-winnls-is_high_surrogate), [IS_LOW_SURROGATE](/windows/win32/api/winnls/nf-winnls-is_low_surrogate), and [IS_SURROGATE_PAIR](/windows/win32/api/winnls/nf-winnls-is_surrogate_pair) macros can be used to detect such cases where appropriate.

There is not necessarily a one-to-one correspondence between keys pressed and character messages generated, and so the information in the high-order word of the *lParam* parameter is generally not useful to applications. The information in the high-order word applies only to the most recent [**WM\_KEYDOWN**](wm-keydown.md) message that precedes the posting of the **WM\_CHAR** message.

For enhanced 101- and 102-key keyboards, extended keys are the right ALT and the right CTRL keys on the main section of the keyboard; the INS, DEL, HOME, END, PAGE UP, PAGE DOWN and arrow keys in the clusters to the left of the numeric keypad; and the divide (/) and ENTER keys in the numeric keypad. Some other keyboards may support the extended-key bit in the *lParam* parameter.

The [**WM\_UNICHAR**](wm-unichar.md) message is the same as **WM\_CHAR**, except it uses UTF-32. It is designed to send or post Unicode characters to ANSI windows, and it can handle Unicode Supplementary Plane characters.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage)
</dt> <dt>

[**WM\_KEYDOWN**](wm-keydown.md)
</dt> <dt>

[**WM\_UNICHAR**](wm-unichar.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Input](keyboard-input.md)
</dt> </dl>

 

