---
title: EM_STREAMOUT message (Richedit.h)
description: Causes a rich edit control to pass its contents to an application \ 8211;defined EditStreamCallback callback function. The callback function can then write the stream of data to a file or any other location that it chooses.
ms.assetid: 3f14aaac-4b17-47af-8f2b-503390631a88
keywords:
- EM_STREAMOUT message Windows Controls
topic_type:
- apiref
api_name:
- EM_STREAMOUT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_STREAMOUT message

Causes a rich edit control to pass its contents to an application defined [*EditStreamCallback*](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback) callback function. The callback function can then write the stream of data to a file or any other location that it chooses.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the data format and replacement options.

This value must be one of the following values.



| Value                                                                                                                                                      | Meaning                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="SF_RTF"></span><span id="sf_rtf"></span><dl> <dt>**SF\_RTF**</dt> </dl>                   | RTF.<br/>                                            |
| <span id="SF_RTFNOOBJS"></span><span id="sf_rtfnoobjs"></span><dl> <dt>**SF\_RTFNOOBJS**</dt> </dl> | RTF with spaces in place of COM objects.<br/>        |
| <span id="SF_TEXT"></span><span id="sf_text"></span><dl> <dt>**SF\_TEXT**</dt> </dl>                | Text with spaces in place of COM objects.<br/>       |
| <span id="SF_TEXTIZED"></span><span id="sf_textized"></span><dl> <dt>**SF\_TEXTIZED**</dt> </dl>    | Text with a text representation of COM objects.<br/> |



 

The **SF\_RTFNOOBJS** option is useful if an application stores COM objects itself, as RTF representation of COM objects is not very compact. The control word, \\objattph, followed by a space denotes the object position.

In addition, you can specify the following flags.



| Value                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SFF_PLAINRTF"></span><span id="sff_plainrtf"></span><dl> <dt>**SFF\_PLAINRTF**</dt> </dl>       | If specified, the rich edit control streams out only the keywords common to all languages, ignoring language-specific keywords. If not specified, the rich edit control streams out all keywords. You can combine this flag with the **SF\_RTF** or **SF\_RTFNOOBJS** flag.<br/> |
| <span id="SFF_SELECTION"></span><span id="sff_selection"></span><dl> <dt>**SFF\_SELECTION**</dt> </dl>    | If specified, the rich edit control streams out only the contents of the current selection. If not specified, the control streams out the entire contents. You can combine this flag with any of data format values.<br/>                                                        |
| <span id="SF_UNICODE"></span><span id="sf_unicode"></span><dl> <dt>**SF\_UNICODE**</dt> </dl>             | **Microsoft Rich Edit 2.0 and later:** Indicates Unicode text. You can combine this flag with the **SF\_TEXT** flag.<br/>                                                                                                                                                        |
| <span id="SF_USECODEPAGE"></span><span id="sf_usecodepage"></span><dl> <dt>**SF\_USECODEPAGE**</dt> </dl> | **Rich Edit 3.0 and later:** Generates UTF-8 RTF as well as text using other code pages. The code page is set in the high word of *wParam*. For example, for UTF-8 RTF, set *wParam* to (CP\_UTF8 << 16) \| SF\_USECODEPAGE \| SF\_RTF.<br/>                               |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**EDITSTREAM**](/windows/desktop/api/Richedit/ns-richedit-editstream) structure. On input, the **pfnCallback** member of this structure must point to an application defined [*EditStreamCallback*](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback) function. On output, the **dwError** member can contain a nonzero error code if an error occurred.

</dd> </dl>

## Return value

This message returns the number of characters written to the data stream.

## Remarks

When you send an **EM\_STREAMOUT** message, the rich edit control makes repeated calls to the [*EditStreamCallback*](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback) function specified by the **pfnCallback** member of the [**EDITSTREAM**](/windows/desktop/api/Richedit/ns-richedit-editstream) structure. Each time it calls the callback function, the control passes a buffer containing a portion of the contents of the control. This process continues until the control has passed all its contents to the callback function, or until an error occurs.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EDITSTREAM**](/windows/desktop/api/Richedit/ns-richedit-editstream)
</dt> <dt>

[*EditStreamCallback*](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback)
</dt> <dt>

[**EM\_STREAMIN**](em-streamin.md)
</dt> </dl>

 

 





