---
title: TF_FLOATINGLANGBAR_ Constants (Ctfutb.h)
description: The define a TF\_FLOATINGLANGBAR\_\ constants string for the title of the language bar window.
ms.assetid: 05394b71-2cc3-440e-943b-d69ee0432fb0
topic_type:
- apiref
api_name:
- TF_FLOATINGLANGBAR_WNDTITLEW
- TF_FLOATINGLANGBAR_WNDTITLEA
- TF_FLOATINGLANGBAR_WNDTITLE
api_location:
- Ctfutb.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_FLOATINGLANGBAR\_\* Constants

The define a TF\_FLOATINGLANGBAR\_\* constants string for the title of the language bar window.



| Constant/value                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_FLOATINGLANGBAR_WNDTITLEW"></span><span id="tf_floatinglangbar_wndtitlew"></span><dl> <dt>**TF\_FLOATINGLANGBAR\_WNDTITLEW**</dt> <dt>LTF\_FloatingLangBar\_WndTitle</dt> </dl> | The string of Unicode characters L"TF\_FloatingLangBar\_WndTitle" for the title.<br/>                                                                                  |
| <span id="TF_FLOATINGLANGBAR_WNDTITLEA"></span><span id="tf_floatinglangbar_wndtitlea"></span><dl> <dt>**TF\_FLOATINGLANGBAR\_WNDTITLEA**</dt> <dt>TF\_FloatingLangBar\_WndTitle</dt> </dl>  | The string of ANSI characters "TF\_FloatingLangBar\_WndTitle" for the title.<br/>                                                                                      |
| <span id="TF_FLOATINGLANGBAR_WNDTITLE"></span><span id="tf_floatinglangbar_wndtitle"></span><dl> <dt>**TF\_FLOATINGLANGBAR\_WNDTITLE**</dt> <dt>TF\_FLOATINGLANGBAR\_WNDTITLEA</dt> </dl>    | If Unicode is defined, takes the value of the TF\_FLOATINGLANGBAR\_WNDTITLEW constant. Otherwise, takes the value of the TF\_FLOATINGLANGBAR\_WNDTITLEA constant.<br/> |



## Remarks

Although there are three constants in this group, the primary one is TF\_FLOATINGLANGBAR\_WNDTITLE, which takes either the ANSI or Unicode value, as appropriate.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                       |
| Header<br/>                   | <dl> <dt>Ctfutb.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Ctfutb.idl</dt> </dl> |



 

 





