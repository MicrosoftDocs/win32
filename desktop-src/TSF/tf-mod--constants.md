---
title: TF_MOD_ Constants (Msctf.h)
description: The TF\_MOD\_\ constants specify key modifiers in the TF\_PRESERVEDKEY structure.
ms.assetid: 4642ef17-34bd-4482-a9e9-0fbed7b574b1
topic_type:
- apiref
api_name:
- TF_MOD_ALT
- TF_MOD_CONTROL
- TF_MOD_SHIFT
- TF_MOD_RALT
- TF_MOD_RCONTROL
- TF_MOD_RSHIFT
- TF_MOD_LALT
- TF_MOD_LCONTROL
- TF_MOD_LSHIFT
- TF_MOD_ON_KEYUP
- TF_MOD_IGNORE_ALL_MODIFIER
api_location:
- Msctf.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_MOD\_\* Constants

The TF\_MOD\_\* constants specify key modifiers in the [TF\_PRESERVEDKEY](/windows/desktop/api/Msctf/ns-msctf-tf_preservedkey) structure.



| Constant/value                                                                                                                                                                                                                                                      | Description                                                                                                                                                                          |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_MOD_ALT"></span><span id="tf_mod_alt"></span><dl> <dt>**TF\_MOD\_ALT**</dt> <dt>0x0001</dt> </dl>                                                   | Either of the ALT keys is pressed<br/>                                                                                                                                         |
| <span id="TF_MOD_CONTROL"></span><span id="tf_mod_control"></span><dl> <dt>**TF\_MOD\_CONTROL**</dt> <dt>0x0002</dt> </dl>                                       | Either of the CTRL keys is pressed<br/>                                                                                                                                        |
| <span id="TF_MOD_SHIFT"></span><span id="tf_mod_shift"></span><dl> <dt>**TF\_MOD\_SHIFT**</dt> <dt>0x0004</dt> </dl>                                             | Either of the SHIFT keys is pressed<br/>                                                                                                                                       |
| <span id="TF_MOD_RALT"></span><span id="tf_mod_ralt"></span><dl> <dt>**TF\_MOD\_RALT**</dt> <dt>0x0008</dt> </dl>                                                | The right ALT key is pressed<br/>                                                                                                                                              |
| <span id="TF_MOD_RCONTROL"></span><span id="tf_mod_rcontrol"></span><dl> <dt>**TF\_MOD\_RCONTROL**</dt> <dt>0x0010</dt> </dl>                                    | The right CTRL key is pressed<br/>                                                                                                                                             |
| <span id="TF_MOD_RSHIFT"></span><span id="tf_mod_rshift"></span><dl> <dt>**TF\_MOD\_RSHIFT**</dt> <dt>0x0020</dt> </dl>                                          | The right SHIFT key is pressed<br/>                                                                                                                                            |
| <span id="TF_MOD_LALT"></span><span id="tf_mod_lalt"></span><dl> <dt>**TF\_MOD\_LALT**</dt> <dt>0x0040</dt> </dl>                                                | The left ALT key is pressed<br/>                                                                                                                                               |
| <span id="TF_MOD_LCONTROL"></span><span id="tf_mod_lcontrol"></span><dl> <dt>**TF\_MOD\_LCONTROL**</dt> <dt>0x0080</dt> </dl>                                    | The left CTRL key is pressed<br/>                                                                                                                                              |
| <span id="TF_MOD_LSHIFT"></span><span id="tf_mod_lshift"></span><dl> <dt>**TF\_MOD\_LSHIFT**</dt> <dt>0x0100</dt> </dl>                                          | The left SHIFT key is pressed<br/>                                                                                                                                             |
| <span id="TF_MOD_ON_KEYUP"></span><span id="tf_mod_on_keyup"></span><dl> <dt>**TF\_MOD\_ON\_KEYUP**</dt> <dt>0x0200</dt> </dl>                                   | The event will be fired when the key is released. Without this flag, the event is fired when the key is pressed.<br/>                                                          |
| <span id="TF_MOD_IGNORE_ALL_MODIFIER"></span><span id="tf_mod_ignore_all_modifier"></span><dl> <dt>**TF\_MOD\_IGNORE\_ALL\_MODIFIER**</dt> <dt>0x0400</dt> </dl> | The state of the ALT, CTRL, and SHIFT keys is ignored. This means the event will be fired when the virtual key is pressed, regardless of which modifier keys are pressed.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[TF\_PRESERVEDKEY](/windows/desktop/api/Msctf/ns-msctf-tf_preservedkey)
</dt> </dl>

 

 





