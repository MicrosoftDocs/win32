---
title: EM_STREAMIN message (Richedit.h)
description: Replaces the contents of a rich edit control with a stream of data provided by an application defined \ 8211;EditStreamCallback callback function.
ms.assetid: b8d3a108-b415-4f5e-99e7-0e0e7a82a778
keywords:
- EM_STREAMIN message Windows Controls
topic_type:
- apiref
api_name:
- EM_STREAMIN
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_STREAMIN message

Replaces the contents of a rich edit control with a stream of data provided by an application defined [*EditStreamCallback*](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback) callback function.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the data format and replacement options. This value must be one of the following values.



| Value                                                                                                                                       | Meaning         |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| <span id="SF_RTF"></span><span id="sf_rtf"></span><dl> <dt>**SF\_RTF**</dt> </dl>    | RTF<br/>  |
| <span id="SF_TEXT"></span><span id="sf_text"></span><dl> <dt>**SF\_TEXT**</dt> </dl> | Text<br/> |



 

In addition, you can specify the following flags.



| Value                                                                                                                                                         | Meaning                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SFF_PLAINRTF"></span><span id="sff_plainrtf"></span><dl> <dt>**SFF\_PLAINRTF**</dt> </dl>    | If specified, only keywords common to all languages are streamed in. Language-specific RTF keywords in the stream are ignored. If not specified, all keywords are streamed in. You can combine this flag with the **SF\_RTF** flag.<br/> |
| <span id="SFF_SELECTION"></span><span id="sff_selection"></span><dl> <dt>**SFF\_SELECTION**</dt> </dl> | If specified, the data stream replaces the contents of the current selection. If not specified, the data stream replaces the entire contents of the control. You can combine this flag with the **SF\_TEXT** or **SF\_RTF** flags.<br/>  |
| <span id="SF_UNICODE"></span><span id="sf_unicode"></span><dl> <dt>**SF\_UNICODE**</dt> </dl>          | **Microsoft Rich Edit 2.0 and later:** Indicates Unicode text. You can combine this flag with the **SF\_TEXT** flag. <br/>                                                                                                               |
| <span id="SF_USECODEPAGE"></span><span id="sf_usecodepage"></span><dl> <dt>**SF\_USECODEPAGE**</dt> </dl> | **Rich Edit 3.0 and later:** Reads UTF-8 RTF and text using other code pages. The code page is set in the high word of *wParam*. For example, for UTF-8 RTF, set *wParam* to (CP\_UTF8 << 16) \| SF\_USECODEPAGE \| SF\_RTF.<br/>                               |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**EDITSTREAM**](/windows/desktop/api/Richedit/ns-richedit-editstream) structure. On input, the **pfnCallback** member of this structure must point to an application defined [*EditStreamCallback*](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback) function. On output, the **dwError** member can contain a nonzero error code if an error occurred.

</dd> </dl>

## Return value

This message returns the number of characters read.

## Remarks

When you send an **EM\_STREAMIN** message, the rich edit control makes repeated calls to the [*EditStreamCallback*](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback) function specified by the **pfnCallback** member of the [**EDITSTREAM**](/windows/desktop/api/Richedit/ns-richedit-editstream) structure. Each time the callback function is called, it fills a buffer with data to read into the control. This continues until the callback function indicates that the stream-in operation has been completed or an error occurs.

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

[**EM\_STREAMOUT**](em-streamout.md)
</dt> </dl>

 

 





