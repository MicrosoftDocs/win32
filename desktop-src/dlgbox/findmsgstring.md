---
title: FINDMSGSTRING message (Commdlg.h)
description: A Find or Replace dialog box sends the FINDMSGSTRING registered message to the window procedure of its owner window when the user clicks the Find Next, Replace, or Replace All button, or closes the dialog box.
ms.assetid: ed0b256a-96df-4588-b8f3-f7d1f89ffe74
keywords:
- FINDMSGSTRING message Dialog Boxes
topic_type:
- apiref
api_name:
- FINDMSGSTRING
- FINDMSGSTRINGA
- FINDMSGSTRINGW
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# FINDMSGSTRING message

A **Find** or **Replace** dialog box sends the **FINDMSGSTRING** registered message to the window procedure of its owner window when the user clicks the **Find Next**, **Replace**, or **Replace All** button, or closes the dialog box.


```C++
#define FINDMSGSTRING TEXT("commdlg_FindReplace")
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**FINDREPLACE**](/windows/win32/api/commdlg/ns-commdlg-findreplacea) structure. The members of this structure contain the latest user input, including the string to search for, the replacement string (if any) and the search-and-replacement options.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

You must specify the **FINDMSGSTRING** constant in a call to the [**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea) function to get the identifier for the message sent by the dialog box.

When you create the dialog box, use the **hwndOwner** member of the [**FINDREPLACE**](/windows/win32/api/commdlg/ns-commdlg-findreplacea) structure to identify the window to receive **FINDMSGSTRING** messages.

The **Flags** member of the [**FINDREPLACE**](/windows/win32/api/commdlg/ns-commdlg-findreplacea) structure includes one of the following flags to indicate the event that caused the message.



| Flag                            | Meaning                                                                                                                                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FR\_DIALOGTERM** (0x00000040) | The dialog box is closing. After the owner window processes this message, a handle to the dialog box is no longer valid.                                                                                    |
| **FR\_FINDNEXT** (0x00000008)   | The user clicked the **Find Next** button in a **Find** or **Replace** dialog box. The **lpstrFindWhat** member specifies the string to search for.                                                         |
| **FR\_REPLACE** (0x00000010)    | The user clicked the **Replace** button in a **Replace** dialog box. The **lpstrFindWhat** member specifies the string to replace and the **lpstrReplaceWith** member specifies the replacement string.     |
| **FR\_REPLACEALL** (0x00000020) | The user clicked the **Replace All** button in a **Replace** dialog box. The **lpstrFindWhat** member specifies the string to replace and the **lpstrReplaceWith** member specifies the replacement string. |



 

For a **Find Next** or **Replace All** message, the **Flags** member can include one or more of the following flags to indicate the search options.



| Flag                           | Meaning                                                                                                                                                                                                                                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FR\_DOWN** (0x00000001)      | If set, the **Down** button of the direction radio buttons is selected indicating that user wants to search from the current location to the end of the document. If **FR\_DOWN** is not set, the **Up** button is selected so the user wants to search to the beginning of the document.       |
| **FR\_MATCHCASE** (0x00000004) | If set, the **Match Case** check box is selected indicating that the user wants the search to be case-sensitive. If **FR\_MATCHCASE** is not set, the check box is unselected so the search should be case-insensitive.                                                                         |
| **FR\_WHOLEWORD** (0x00000002) | If set, the **Match Whole Word Only** check box is selected indicating that the user wants to search only for whole words that match the search string. If **FR\_WHOLEWORD** is not set, the check box is unselected so you should also search for word fragments that match the search string. |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **FINDMSGSTRINGW** (Unicode) and **FINDMSGSTRINGA** (ANSI)<br/>                                    |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**FINDREPLACE**](/windows/win32/api/commdlg/ns-commdlg-findreplacea)
</dt> <dt>

[**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

