---
title: EM_AUTOURLDETECT message (Richedit.h)
description: Enables or disables automatic detection of hyperlinks by a rich edit control.
ms.assetid: 6970ff36-ff3f-4413-a471-9389a76c8f38
keywords:
- EM_AUTOURLDETECT message Windows Controls
topic_type:
- apiref
api_name:
- EM_AUTOURLDETECT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_AUTOURLDETECT message

Enables or disables automatic detection of hyperlinks by a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specify 0 to disable automatic link detection, or one of the following values to enable various kinds of detection.



| Value                                                                                                                                                                                       | Meaning                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="AURL_DISABLEMIXEDLGC"></span><span id="aurl_disablemixedlgc"></span><dl> <dt>**AURL\_DISABLEMIXEDLGC**</dt> </dl>          | **Windows 8**: Disable recognition of domain names that contain labels with characters belonging to more than one of the following scripts: Latin, Greek, and Cyrillic. <br/> |
| <span id="AURL_ENABLEDRIVELETTERS"></span><span id="aurl_enabledriveletters"></span><dl> <dt>**AURL\_ENABLEDRIVELETTERS**</dt> </dl> | **Windows 8**: Recognize file names that have a leading drive specification, such as c:\\temp.<br/>                                                                           |
| <span id="AURL_ENABLEEA"></span><span id="aurl_enableea"></span><dl> <dt>**AURL\_ENABLEEA**</dt> </dl>                               | This value is deprecated; use **AURL\_ENABLEEAURLS** instead.<br/>                                                                                                            |
| <span id="AURL_ENABLEEAURLS"></span><span id="aurl_enableeaurls"></span><dl> <dt>**AURL\_ENABLEEAURLS**</dt> </dl>                   | Recognize URLs that contain East Asian characters. <br/>                                                                                                                      |
| <span id="AURL_ENABLEEMAILADDR"></span><span id="aurl_enableemailaddr"></span><dl> <dt>**AURL\_ENABLEEMAILADDR**</dt> </dl>          | **Windows 8**: Recognize email addresses.<br/>                                                                                                                                |
| <span id="AURL_ENABLETELNO"></span><span id="aurl_enabletelno"></span><dl> <dt>**AURL\_ENABLETELNO**</dt> </dl>                      | **Windows 8**: Recognize telephone numbers.<br/>                                                                                                                              |
| <span id="AURL_ENABLEURL"></span><span id="aurl_enableurl"></span><dl> <dt>**AURL\_ENABLEURL**</dt> </dl>                            | **Windows 8**: Recognize URLs that include the path.<br/>                                                                                                                     |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter determines the URL schemes recognized if **AURL\_ENABLEURL** is active. If *lParam* is NULL, the default scheme name list is used (see Remarks). Alternatively, *lParam* can point to a null-terminated string consisting of up to 50 colon-terminated scheme names that supersede the default scheme name list. For example, the string could be "news:http:ftp:telnet:". The scheme name syntax is defined in the [Uniform Resource Identifiers (URI): Generic Syntax]( https://www.ietf.org/rfc/rfc2396.txt) document on The Internet Engineering Task Force (IETF) website. Specifically, a scheme name can contain up to 13 characters (including the colon), must start with an ASCII alphabetic, and can be followed by a mixture of ASCII alphabetics, digits, and the three punctuation characters: ".", "+", and "-". The string type can be either **char\*** or **WCHAR\***; the rich edit control automatically detects the type.

</dd> </dl>

## Return value

If the message succeeds, the return value is zero.

If the message fails, the return value is a nonzero value. For example, the message might fail due to insufficient memory, an invalid detection option, or an invalid scheme-name string.

If *lParam* contains more than 50 scheme names, the message fails with a return value of **E\_INVALIDARG**.

## Remarks

If automatic URL detection is enabled (that is, *wParam* includes **AURL\_ENABLEURL**), the rich edit control scans any modified text to determine whether the text matches the format of a URL (or more generally in Windows 8 or later an IRI International Resource Identifier). If *lParam* is NULL, the control detects URLs that begin with the following scheme names:

-   callto
-   file
-   ftp
-   gopher
-   http
-   https
-   mailto
-   news
-   notes
-   nntp
-   onenote
-   outlook
-   prospero
-   tel
-   telnet
-   wais
-   webcal

When automatic link detection is enabled, the rich edit control removes the **CFE\_LINK** effect from modified text that does not have a format recognized by the control. If your application uses the **CFE\_LINK** effect to mark other types of text, do not enable automatic link detection. The rich edit control does not check whether a detected link exists; that responsibility belongs to the client.

A rich edit control sends the [EN\_LINK](en-link.md) notification when it receives various messages while the mouse pointer is over text that has the **CFE\_LINK** effect. For more information, see [Automatic RichEdit Hyperlinks](/archive/blogs/murrays/automatic-richedit-hyperlinks) and [RichEdit Friendly Name Hyperlinks](/archive/blogs/murrays/richedit-friendly-name-hyperlinks).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a)
</dt> <dt>

[EN\_LINK](en-link.md)
</dt> </dl>

 

