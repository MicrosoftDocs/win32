---
description: Sent to the topmost affected window after an application's input language has been changed. You should make any application-specific settings and pass the message to the DefWindowProc function, which passes the message to all first-level child windows.
ms.assetid: 4d403b1d-f6f7-40d5-9bf5-6a9c4da0803c
title: WM_INPUTLANGCHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_INPUTLANGCHANGE message

Sent to the topmost affected window after an application's input language has been changed. You should make any application-specific settings and pass the message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function, which passes the message to all first-level child windows. These child windows can pass the message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) to have it pass the message to their child windows, and so on.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.

```C++
#define WM_INPUTLANGCHANGE              0x0051
```

## Parameters

<dl> <dt>

*wParam*

</dt> <dd>
  
Type: **WPARAM**

The [code page](../Intl/code-pages.md) of the new locale.

</dd> <dt>

*lParam*

</dt> <dd>
 
Type: **LPARAM**

The **HKL** input locale identifier.
  
The low word contains a [Language Identifier](/windows/win32/intl/language-identifiers) for the input language. The high word contains a device handle.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return nonzero if it processes this message.

## Remarks

You can retrieve the [BCP 47](https://www.rfc-editor.org/info/bcp47) [locale name](../Intl/locale-names.md) from the language identifier by calling the [LCIDToLocaleName](/windows/win32/api/winnls/nf-winnls-lcidtolocalename) function. Once you have the locale name, you can then use [modern locale functions](/windows/win32/intl/calling-the--locale-name--functions) to extract additional locale information.

```cpp
case WM_INPUTLANGCHANGE:
{
    HKL hkl = (HKL)lParam;
    LANGID langId = LOWORD(hkl);

    WCHAR localeName[LOCALE_NAME_MAX_LENGTH];
    LCIDToLocaleName(MAKELCID(langId, SORT_DEFAULT), localeName, LOCALE_NAME_MAX_LENGTH, 0);

    // Get the ISO abbreviated language name (for example, "eng").
    WCHAR lang[9];
    GetLocaleInfoEx(localeName, LOCALE_SISO639LANGNAME2, lang, 9);
}
```

To get the the name of the currently active input locale identifier, call the [GetKeyboardLayoutName](/windows/win32/api/winuser/nf-winuser-getkeyboardlayoutnamew). For more information, see [Languages, Locales, and Keyboard Layouts](/windows/win32/inputdev/about-keyboard-input#languages-locales-and-keyboard-layouts).

For a list of the input layouts that are supplied with Windows, see [Keyboard Identifiers and Input Method Editors for Windows](/windows-hardware/manufacture/desktop/windows-language-pack-default-values).

[Input Method Editor (IME)](/windows/apps/design/input/input-method-editors) profile changes may not be notified with *WM_INPUTLANGCHANGE*. You can use [ITfActiveLanguageProfileNotifySink](/windows/win32/api/msctf/nn-msctf-itfactivelanguageprofilenotifysink) from the [Text Services Framework](/windows/win32/tsf/text-services-framework) to handle active language or text service changes.

**Starting with Windows 8**

Some input layouts may not have assigned language identifiers and could be reported as transient language identifiers, such as `LOCALE_TRANSIENT_KEYBOARD1` (`0x2000`) or `LOCALE_TRANSIENT_KEYBOARD2` (`0x2400`), in the low word of *LPARAM*. 

As these transient language identifiers can be re-assigned by the system at any time (such as when the user changes their Language Profile), and can identify a different locale based on the user and/or system, they cannot be considered durable identifiers. See [The deprecation of LCIDs](/globalization/locale/locale-names#the-deprecation-of-lcids) for more info.

Retrieve the language associated with the current keyboard layout or input method by calling [Windows.Globalization.Language.CurrentInputMethodLanguageTag](/uwp/api/windows.globalization.language.currentinputmethodlanguagetag). If your app passes language tags from **CurrentInputMethodLanguageTag** to any [National Language Support](/windows/win32/intl/national-language-support-functions) functions, it must first convert the tags with [ResolveLocaleName](/windows/win32/api/winnls/nf-winnls-resolvelocalename). If you want to be notified about a language change in a UWP app, handle the [Windows.UI.Text.Core.CoreTextServicesManager.InputLanguageChanged](/uwp/api/windows.ui.text.core.coretextservicesmanager.inputlanguagechanged) event.

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |

## See also

**Reference**

- [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca)
- [WindowProc](/windows/win32/api/winuser/nc-winuser-wndproc)
- [WM\_INPUTLANGCHANGEREQUEST](wm-inputlangchangerequest.md)
- [GetKeyboardLayout](/windows/win32/api/winuser/nf-winuser-getkeyboardlayout)
- [GetKeyboardLayoutList](/windows/win32/api/winuser/nf-winuser-getkeyboardlayoutlist)
- [GetKeyboardLayoutName](/windows/win32/api/winuser/nf-winuser-getkeyboardlayoutnamew)
- [Windows.Globalization.Language.CurrentInputMethodLanguageTag](/uwp/api/windows.globalization.language.currentinputmethodlanguagetag)
- [Windows.UI.Text.Core.CoreTextServicesManager.InputLanguageChanged](/uwp/api/windows.ui.text.core.coretextservicesmanager.inputlanguagechanged)

**Conceptual**

- [Windows](windows.md)
- [Windows keyboard layouts](/globalization/windows-keyboard-layouts)
- [Keyboard Identifiers and Input Method Editors for Windows](/windows-hardware/manufacture/desktop/windows-language-pack-default-values)
- [Languages, Locales, and Keyboard Layouts](/windows/win32/inputdev/about-keyboard-input#languages-locales-and-keyboard-layouts)
