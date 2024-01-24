---
description: The AUDCLNT\_SESSIONFLAGS\_XXX constants indicate characteristics of an audio session associated with the stream.
ms.assetid: 5745d5bc-71e8-4b33-8227-c1c84226b6ee
title: AUDCLNT_SESSIONFLAGS_XXX Constants (Audiosessiontypes.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AUDCLNT\_SESSIONFLAGS\_XXX Constants

The AUDCLNT\_SESSIONFLAGS\_XXX constants indicate characteristics of an audio session associated with the stream. A client can specify these options during the initialization of the stream by through the *StreamFlags* parameter of the [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) method.



| Constant/value                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                      |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="AUDCLNT_SESSIONFLAGS_EXPIREWHENUNOWNED"></span><span id="audclnt_sessionflags_expirewhenunowned"></span><dl> <dt>**AUDCLNT\_SESSIONFLAGS\_EXPIREWHENUNOWNED**</dt> <dt>0x10000000 </dt> </dl>                       | The session expires when there are no associated streams and owning session control objects holding references.<br/>                                                                                                                                                                                       |
| <span id="AUDCLNT_SESSIONFLAGS_DISPLAY_HIDE"></span><span id="audclnt_sessionflags_display_hide"></span><dl> <dt>**AUDCLNT\_SESSIONFLAGS\_DISPLAY\_HIDE**</dt> <dt>0x20000000 </dt> </dl>                                     | The volume control is hidden in the volume mixer user interface when the audio session is created. If the session associated with the stream already exists before [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) opens the stream, the volume control is displayed in the volume mixer.<br/> |
| <span id="_AUDCLNT_SESSIONFLAGS_DISPLAY_HIDEWHENEXPIRED"></span><span id="_audclnt_sessionflags_display_hidewhenexpired"></span><dl> <dt> **AUDCLNT\_SESSIONFLAGS\_DISPLAY\_HIDEWHENEXPIRED**</dt> <dt>0x40000000 </dt> </dl> | The volume control is hidden in the volume mixer user interface after the session expires. <br/>                                                                                                                                                                                                           |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Audiosessiontypes.h</dt> </dl> |



## See also

<dl> <dt>

[Core Audio Constants](core-audio-constants.md)
</dt> <dt>

[**IAudioSessionControl**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol)
</dt> </dl>

 

 




