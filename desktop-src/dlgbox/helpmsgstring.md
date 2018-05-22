---
title: HELPMSGSTRING message
description: A common dialog box sends the HELPMSGSTRING registered message to the window procedure of its owner window when the user clicks the Help button.
ms.assetid: '21c0fcf5-785b-4005-8133-e48347f991a8'
keywords: ["HELPMSGSTRING message Dialog Boxes"]
topic_type:
- apiref
api_name:
- HELPMSGSTRING
- HELPMSGSTRINGA
- HELPMSGSTRINGW
api_location:
- Commdlg.h
api_type:
- HeaderDef
---

# HELPMSGSTRING message

A common dialog box sends the **HELPMSGSTRING** registered message to the window procedure of its owner window when the user clicks the **Help** button.


```C++
#define HELPMSGSTRING TEXT("commdlg_help")
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the common dialog box.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the initialization structure for the common dialog box. This structure can be a [**CHOOSECOLOR**](choosecolor-str.md), [**CHOOSEFONT**](choosefont-str.md), [**FINDREPLACE**](findreplace-str.md), [**OPENFILENAME**](openfilename-str.md), [**PRINTDLG**](printdlg-str.md) or [**PAGESETUPDLG**](pagesetupdlg-str.md) structure.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

You must specify the **HELPMSGSTRING** constant in a call to the [**RegisterWindowMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644947) function to get the identifier for the message sent by the dialog box.

When you create the dialog box, use the **hwndOwner** member of the initialization structure to identify the window to receive **HELPMSGSTRING** messages.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **HELPMSGSTRINGW** (Unicode) and **HELPMSGSTRINGA** (ANSI)<br/>                                    |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CDN\_HELP**](cdn-help.md)
</dt> <dt>

[**CHOOSECOLOR**](choosecolor-str.md)
</dt> <dt>

[**CHOOSEFONT**](choosefont-str.md)
</dt> <dt>

[**FINDREPLACE**](findreplace-str.md)
</dt> <dt>

[**OPENFILENAME**](openfilename-str.md)
</dt> <dt>

[**PRINTDLG**](printdlg-str.md)
</dt> <dt>

[**PAGESETUPDLG**](pagesetupdlg-str.md)
</dt> <dt>

[**RegisterWindowMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644947)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





