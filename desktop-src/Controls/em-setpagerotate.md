---
title: EM_SETPAGEROTATE message (Richedit.h)
description: Sets the text layout for a rich edit control.
ms.assetid: 3c2a37fe-ee9f-4b34-87bf-7ac27d010afc
keywords:
- EM_SETPAGEROTATE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETPAGEROTATE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETPAGEROTATE message

\[**EM\_SETPAGEROTATE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets the text layout for a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Text layout value. This can be one of the following values.



| Value                                                                                                                                       | Meaning                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <span id="EPR_0"></span><span id="epr_0"></span><dl> <dt>**EPR\_0**</dt> </dl>       | Text flows from left to right and from top to bottom.<br/>                              |
| <span id="EPR_90"></span><span id="epr_90"></span><dl> <dt>**EPR\_90**</dt> </dl>    | Text flows from bottom to top and from left to right.<br/>                              |
| <span id="EPR_180"></span><span id="epr_180"></span><dl> <dt>**EPR\_180**</dt> </dl> | Text flows from right to left and from bottom to top.<br/>                              |
| <span id="EPR_270"></span><span id="epr_270"></span><dl> <dt>**EPR\_270**</dt> </dl> | Text flows from top to bottom and from right to left.<br/>                              |
| <span id="EPR_SE"></span><span id="epr_se"></span><dl> <dt>**EPR\_SE**</dt> </dl>    | **Windows 8:** Text flows top to bottom and left to right (Mongolian text layout).<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

Return value is the new text layout value.

## Remarks

This message sets the text layout for the entire document. However, embedded contents are not rotated and must be rotated separately by the application.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETPAGEROTATE**](em-getpagerotate.md)
</dt> </dl>

 

 





