---
title: Speech Recognition Constants (Ctffunc.h)
description: The following values are used with the speech recognition text service.
ms.assetid: ac433d15-738a-46ab-8f69-0fbfb6a8b654
topic_type:
- apiref
api_name:
- TF_DICTATION_ON
- TF_DICTATION_ENABLED
- TF_COMMANDING_ENABLED
- TF_COMMANDING_ON
- TF_SPEECHUI_SHOWN
- TF_SHOW_BALLOON
- TF_DISABLE_BALLOON
- TF_DISABLE_SPEECH
- TF_DISABLE_DICTATION
- TF_DISABLE_COMMANDING
api_location:
- Ctffunc.h
- Msctf.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Speech Recognition Constants

The following values are used with the speech recognition text service.



| Constant/value                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                 |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_DICTATION_ON"></span><span id="tf_dictation_on"></span><dl> <dt>**TF\_DICTATION\_ON**</dt> <dt>0x00000001</dt> </dl>                   | If this bit is 1, speech dictation is active. Otherwise, speech dictation is inactive. This value cannot be combined with TF\_COMMANDING\_ON. Used with the [GUID\_COMPARTMENT\_SPEECH\_DICTATIONSTAT](predefined-compartments.md) compartment.<br/> |
| <span id="TF_DICTATION_ENABLED"></span><span id="tf_dictation_enabled"></span><dl> <dt>**TF\_DICTATION\_ENABLED**</dt> <dt>0x00000002</dt> </dl>    | If this bit is 1, speech dictation is enabled. Otherwise, speech dictation is disabled. Used with the [GUID\_COMPARTMENT\_SPEECH\_DICTATIONSTAT](predefined-compartments.md) compartment.<br/>                                                       |
| <span id="TF_COMMANDING_ENABLED"></span><span id="tf_commanding_enabled"></span><dl> <dt>**TF\_COMMANDING\_ENABLED**</dt> <dt>0x00000004</dt> </dl> | If this bit is 1, speech command is enabled. Otherwise, speech command is disabled. Used with the [GUID\_COMPARTMENT\_SPEECH\_DICTATIONSTAT](predefined-compartments.md) compartment.<br/>                                                           |
| <span id="TF_COMMANDING_ON"></span><span id="tf_commanding_on"></span><dl> <dt>**TF\_COMMANDING\_ON**</dt> <dt>0x00000008</dt> </dl>                | If this bit is 1, speech command is active. Otherwise, speech command is inactive. This value cannot be combined with TF\_DICTATION\_ON. Used with the [GUID\_COMPARTMENT\_SPEECH\_DICTATIONSTAT](predefined-compartments.md) compartment.<br/>      |
| <span id="TF_SPEECHUI_SHOWN"></span><span id="tf_speechui_shown"></span><dl> <dt>**TF\_SPEECHUI\_SHOWN**</dt> <dt>0x00000010</dt> </dl>             | Not currently used.<br/>                                                                                                                                                                                                                              |
| <span id="TF_SHOW_BALLOON"></span><span id="tf_show_balloon"></span><dl> <dt>**TF\_SHOW\_BALLOON**</dt> <dt>0x00000001</dt> </dl>                   | Not currently used. Used with the [GUID\_COMPARTMENT\_SPEECH\_UI\_STATUS](predefined-compartments.md) compartment.<br/>                                                                                                                              |
| <span id="TF_DISABLE_BALLOON"></span><span id="tf_disable_balloon"></span><dl> <dt>**TF\_DISABLE\_BALLOON**</dt> <dt>0x00000002</dt> </dl>          | If this bit is 1, balloon display for the current speech mode is disabled. Otherwise, balloon display for the current speech mode is enabled. Used with the [GUID\_COMPARTMENT\_SPEECH\_UI\_STATUS](predefined-compartments.md) compartment.<br/>    |
| <span id="TF_DISABLE_SPEECH"></span><span id="tf_disable_speech"></span><dl> <dt>**TF\_DISABLE\_SPEECH**</dt> <dt>0x00000001</dt> </dl>             | If this bit is 1, speech input is disabled. Otherwise, speech input is enabled. Used with the [GUID\_COMPARTMENT\_SPEECH\_DISABLED](predefined-compartments.md) compartment.<br/>                                                                    |
| <span id="TF_DISABLE_DICTATION"></span><span id="tf_disable_dictation"></span><dl> <dt>**TF\_DISABLE\_DICTATION**</dt> <dt>0x00000002</dt> </dl>    | If this bit is 1, speech dictation is disabled. Otherwise, speech dictation is enabled. Used with the [GUID\_COMPARTMENT\_SPEECH\_DISABLED](predefined-compartments.md) compartment.<br/>                                                            |
| <span id="TF_DISABLE_COMMANDING"></span><span id="tf_disable_commanding"></span><dl> <dt>**TF\_DISABLE\_COMMANDING**</dt> <dt>0x00000004</dt> </dl> | If this bit is 1, speech command is disabled. Otherwise, speech command is enabled. Used with the [GUID\_COMPARTMENT\_SPEECH\_DISABLED](predefined-compartments.md) compartment.<br/>                                                                |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                    |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                                                                                         |
| Header<br/>                   | <dl> <dt>Ctffunc.h; </dt> <dt>Msctf.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>Ctffunc.idl; </dt> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[Predefined Compartments](predefined-compartments.md)
</dt> </dl>

 

 





