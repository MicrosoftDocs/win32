---
title: EM_SETOPTIONS message (Richedit.h)
description: Sets the options for a rich edit control.
ms.assetid: 98ef2de9-4c34-45ba-8e8a-eaf505f97f56
keywords:
- EM_SETOPTIONS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETOPTIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETOPTIONS message

Sets the options for a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the operation, which can be one of these values.



| Value                                                                                                                                             | Meaning                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <span id="ECOOP_SET"></span><span id="ecoop_set"></span><dl> <dt>**ECOOP\_SET**</dt> </dl> | Sets the options to those specified by *lParam*.<br/>                             |
| <span id="ECOOP_OR"></span><span id="ecoop_or"></span><dl> <dt>**ECOOP\_OR**</dt> </dl>    | Combines the specified options with the current options.<br/>                     |
| <span id="ECOOP_AND"></span><span id="ecoop_and"></span><dl> <dt>**ECOOP\_AND**</dt> </dl> | Retains only those current options that are also specified by *lParam*.<br/>      |
| <span id="ECOOP_XOR"></span><span id="ecoop_xor"></span><dl> <dt>**ECOOP\_XOR**</dt> </dl> | Logically exclusive OR the current options with those specified by *lParam*.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies one or more of the following values.



| Value                                                                                                                                                                                 | Meaning                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <span id="ECO_AUTOWORDSELECTION"></span><span id="eco_autowordselection"></span><dl> <dt>**ECO\_AUTOWORDSELECTION**</dt> </dl> | Automatic selection of word on double-click.<br/>                                                                           |
| <span id="ECO_AUTOVSCROLL"></span><span id="eco_autovscroll"></span><dl> <dt>**ECO\_AUTOVSCROLL**</dt> </dl>                   | Same as [**ES\_AUTOVSCROLL**](rich-edit-control-styles.md) style.<br/>                                      |
| <span id="ECO_AUTOHSCROLL"></span><span id="eco_autohscroll"></span><dl> <dt>**ECO\_AUTOHSCROLL**</dt> </dl>                   | Same as [**ES\_AUTOHSCROLL**](rich-edit-control-styles.md) style.<br/>                                      |
| <span id="ECO_NOHIDESEL"></span><span id="eco_nohidesel"></span><dl> <dt>**ECO\_NOHIDESEL**</dt> </dl>                         | Same as [**ES\_NOHIDESEL**](rich-edit-control-styles.md) style.<br/>                                          |
| <span id="ECO_READONLY"></span><span id="eco_readonly"></span><dl> <dt>**ECO\_READONLY**</dt> </dl>                            | Same as [**ES\_READONLY**](rich-edit-control-styles.md) style.<br/>                                            |
| <span id="ECO_WANTRETURN"></span><span id="eco_wantreturn"></span><dl> <dt>**ECO\_WANTRETURN**</dt> </dl>                      | Same as [**ES\_WANTRETURN**](rich-edit-control-styles.md) style.<br/>                                        |
| <span id="ECO_SELECTIONBAR"></span><span id="eco_selectionbar"></span><dl> <dt>**ECO\_SELECTIONBAR**</dt> </dl>                | Same as [**ES\_SELECTIONBAR**](rich-edit-control-styles.md) style.<br/>                                    |
| <span id="ECO_VERTICAL"></span><span id="eco_vertical"></span><dl> <dt>**ECO\_VERTICAL**</dt> </dl>                            | Same as [**ES\_VERTICAL**](rich-edit-control-styles.md) style. Available in Asian-language versions only.<br/> |



 

</dd> </dl>

## Return value

This message returns the current options of the edit control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**Rich Edit Control Styles**](rich-edit-control-styles.md)
</dt> </dl>

 

 





