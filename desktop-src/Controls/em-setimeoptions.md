---
title: EM_SETIMEOPTIONS message (Richedit.h)
description: Sets the Input Method Editor (IME) options.
ms.assetid: 8a72ee1c-f6b8-44eb-b8df-57cd834db326
keywords:
- EM_SETIMEOPTIONS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETIMEOPTIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETIMEOPTIONS message

Sets the Input Method Editor (IME) options.

> [!Note]  
> This message is supported only in Asian-language versions of Microsoft Rich Edit 1.0. It is not supported in any later versions.

 

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies one of the following values.



| Value                                                                                                                                             | Meaning                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <span id="ECOOP_SET"></span><span id="ecoop_set"></span><dl> <dt>**ECOOP\_SET**</dt> </dl> | Sets the options to those specified by *lParam*.<br/>                             |
| <span id="ECOOP_OR"></span><span id="ecoop_or"></span><dl> <dt>**ECOOP\_OR**</dt> </dl>    | Combines the specified options with the current options.<br/>                     |
| <span id="ECOOP_AND"></span><span id="ecoop_and"></span><dl> <dt>**ECOOP\_AND**</dt> </dl> | Retains only those current options that are also specified by *lParam*.<br/>      |
| <span id="ECOOP_XOR"></span><span id="ecoop_xor"></span><dl> <dt>**ECOOP\_XOR**</dt> </dl> | Logically exclusive OR the current options with those specified by *lParam.*<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies one of more of the following values.



| Value                                                                                                                                                                                 | Meaning                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="IMF_CLOSESTATUSWINDOW"></span><span id="imf_closestatuswindow"></span><dl> <dt>**IMF\_CLOSESTATUSWINDOW**</dt> </dl> | Closes the IME status window when the control receives the input focus.<br/>                                                                                                               |
| <span id="IMF_FORCEACTIVE"></span><span id="imf_forceactive"></span><dl> <dt>**IMF\_FORCEACTIVE**</dt> </dl>                   | Activates the IME when the control receives the input focus.<br/>                                                                                                                          |
| <span id="IMF_FORCEDISABLE"></span><span id="imf_forcedisable"></span><dl> <dt>**IMF\_FORCEDISABLE**</dt> </dl>                | Disables the IME when the control receives the input focus.<br/>                                                                                                                           |
| <span id="IMF_FORCEENABLE"></span><span id="imf_forceenable"></span><dl> <dt>**IMF\_FORCEENABLE**</dt> </dl>                   | Enables the IME when the control receives the input focus.<br/>                                                                                                                            |
| <span id="IMF_FORCEINACTIVE"></span><span id="imf_forceinactive"></span><dl> <dt>**IMF\_FORCEINACTIVE**</dt> </dl>             | Inactivates the IME when the control receives the input focus.<br/>                                                                                                                        |
| <span id="IMF_FORCENONE"></span><span id="imf_forcenone"></span><dl> <dt>**IMF\_FORCENONE**</dt> </dl>                         | Disables IME handling.<br/>                                                                                                                                                                |
| <span id="IMF_FORCEREMEMBER"></span><span id="imf_forceremember"></span><dl> <dt>**IMF\_FORCEREMEMBER**</dt> </dl>             | Restores the previous IME status when the control receives the input focus.<br/>                                                                                                           |
| <span id="IMF_MULTIPLEEDIT"></span><span id="imf_multipleedit"></span><dl> <dt>**IMF\_MULTIPLEEDIT**</dt> </dl>                | Specifies that the composition string will not be canceled or determined by focus changes. This allows an application to have separate composition strings on each rich edit control.<br/> |
| <span id="IMF_VERTICAL"></span><span id="imf_vertical"></span><dl> <dt>**IMF\_VERTICAL**</dt> </dl>                            | Note used in Rich Edit 2.0 and later. <br/>                                                                                                                                                |



 

</dd> </dl>

## Return value

If the operation succeeds, the return value is a nonzero value.

If the operation fails, the return value is zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETIMEOPTIONS**](em-getimeoptions.md)
</dt> </dl>

 

 





