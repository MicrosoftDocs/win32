---
title: EM_GETEDITSTYLEEX message (Richedit.h)
description: Retrieves the current extended edit style flags.
ms.assetid: 3E81F7BB-404D-4465-982A-3CF6FD9359DA
keywords:
- EM_GETEDITSTYLEEX message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETEDITSTYLEEX
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETEDITSTYLEEX message

Retrieves the current extended edit style flags.


```C++
#define EM_GETEDITSTYLEEX       (WM_USER + 276)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

Returns the extended edit style flags, which can include one or more of the following values.



| Return code                                                                                                | Description                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SES\_EX\_HANDLEFRIENDLYURL**</dt> </dl>  | Display friendly name links with the same text color and underlining as automatic links, provided that temporary formatting isn t used or uses text autocolor (default: 0).<br/>                                                                       |
| <dl> <dt>**SES\_EX\_MULTITOUCH**</dt> </dl>         | Enable touch support in Rich Edit. This includes selection, caret placement, and context-menu invocation. When this flag is not set, touch is emulated by mouse commands, which do not take touch-mode specifics into account (default: 0). <br/>      |
| <dl> <dt>**SES\_EX\_NOACETATESELECTION**</dt> </dl> | Display selected text using classic Windows selection text and background colors instead of background acetate color (default: 0). <br/>                                                                                                               |
| <dl> <dt>**SES\_EX\_NOMATH**</dt> </dl>             | Disable insertion of math zones (default: 1). To enable math editing and display, send the [**EM\_SETEDITSTYLEEX**](em-seteditstyleex.md) message with *wParam* set to 0, and *lParam* set to **SES\_EX\_NOMATH**. <br/>                              |
| <dl> <dt>**SES\_EX\_NOTABLE**</dt> </dl>            | Disable insertion of tables. The [**EM\_INSERTTABLE**](em-inserttable.md) message returns **E\_FAIL** and RTF tables are skipped (default: 0). <br/>                                                                                                  |
| <dl> <dt>**SES\_EX\_USESINGLELINE**</dt> </dl>      | Enable a multiline control to act like a single-line control with the ability to scroll vertically when the single-line height is greater than the window height (default: 0). <br/>                                                                   |
| <dl> <dt>**SES\_HIDETEMPFORMAT**</dt> </dl>         | Hide temporary formatting that is created when [**ITextFont.Reset**](/windows/desktop/api/Tom/nf-tom-itextfont-reset) is called with **tomApplyTmp**. For example, such formatting is used by spell checkers to display a squiggly underline under possibly misspelled words.<br/> |
| <dl> <dt>**SES\_EX\_USEMOUSEWPARAM**</dt> </dl>     | Use *wParam* when handling the [**WM\_MOUSEMOVE**](/windows/desktop/inputdev/wm-mousemove) message and do not call [**GetAsyncKeyState**](/windows/desktop/api/winuser/nf-winuser-getasynckeystate).<br/>                                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETEDITSTYLEEX**](em-seteditstyleex.md)
</dt> </dl>

 

