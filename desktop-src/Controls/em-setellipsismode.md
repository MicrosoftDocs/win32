---
title: EM_SETELLIPSISMODE message (Richedit.h)
description: This message sets the current ellipsis mode.
ms.assetid: C77263E8-424B-4EDE-ACBF-BA85248FC31F
keywords:
- EM_SETELLIPSISMODE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETELLIPSISMODE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETELLIPSISMODE message

This message sets the current ellipsis mode. When enabled, an ellipsis ( ) is displayed for text that doesn t fit in the display window. The ellipsis is only used when the control isn t active. When active, scroll bars are used to reveal text that doesn t fit into the display window.


```C++
#define EM_SETELLIPSISMODE       (WM_USER + 306)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A DWORD which receives one of the following values.



| Value                                                                                                                                                         | Meaning                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <span id="ELLIPSIS_NONE"></span><span id="ellipsis_none"></span><dl> <dt>**ELLIPSIS\_NONE**</dt> </dl> | No ellipsis is used.<br/>                |
| <span id="ELLIPSIS_END"></span><span id="ellipsis_end"></span><dl> <dt>**ELLIPSIS\_END**</dt> </dl>    | Ellipsis at the end (forced break).<br/> |
| <span id="ELLIPSIS_WORD"></span><span id="ellipsis_word"></span><dl> <dt>**ELLIPSIS\_WORD**</dt> </dl> | Ellipsis at the end (word break).<br/>   |



 

The bits for these values all fit in the **ELLIPSIS\_MASK**.

</dd> </dl>

## Return value

If wparam is 0 and lparam is one of the values in the table above, the return value equals TRUE; otherwise, the return value equals FALSE.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETELLIPSISMODE**](em-getellipsismode.md)
</dt> <dt>

[**EM\_GETELLIPSISSTATE**](em-getellipsisstate.md)
</dt> </dl>

 

 





