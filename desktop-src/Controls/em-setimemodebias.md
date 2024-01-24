---
title: EM_SETIMEMODEBIAS message (Richedit.h)
description: Set the Input Method Editor (IME) mode bias for a rich edit control.
ms.assetid: 4a3f97eb-fe80-4e84-a73e-3ed6d73644de
keywords:
- EM_SETIMEMODEBIAS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETIMEMODEBIAS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETIMEMODEBIAS message

Set the Input Method Editor (IME) mode bias for a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

IME mode bias value. It can be one of the following.



| Value                                                                                                                                                                                        | Meaning                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <span id="IMF_SMODE_PLAURALCLAUSE"></span><span id="imf_smode_plauralclause"></span><dl> <dt>**IMF\_SMODE\_PLAURALCLAUSE**</dt> </dl> | Sets the IME mode bias to Name.<br/> |
| <span id="IMF_SMODE_NONE"></span><span id="imf_smode_none"></span><dl> <dt>**IMF\_SMODE\_NONE**</dt> </dl>                            | No bias.<br/>                        |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This must be the same value as *wParam*.

</dd> </dl>

## Return value

This message returns the new IME mode bias setting.

## Remarks

When the IME generates a list of alternative choices for a set of characters, this message sets the criteria by which some of the choices will appear at the top of the list.

To set the Text Services Framework (TSF) mode bias, use [**EM\_SETCTFMODEBIAS**](em-setctfmodebias.md).

The application should call [**EM\_ISIME**](em-isime.md) before calling this function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_ISIME**](em-isime.md)
</dt> <dt>

[**EM\_SETCTFMODEBIAS**](em-setctfmodebias.md)
</dt> </dl>

 

 





