---
description: XAudio2 specific error codes returned by XAudio2 methods.
ms.assetid: 42a1c21c-4b14-114a-d79e-15a61eb2139b
title: XAudio2 Error Codes (Xaudio2.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XAudio2 Error Codes

XAudio2 specific error codes returned by XAudio2 methods.



| Constant/value                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                       |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="XAUDIO2_E_INVALID_CALL"></span><span id="xaudio2_e_invalid_call"></span><dl> <dt>**XAUDIO2\_E\_INVALID\_CALL**</dt> <dt>0x88960001</dt> </dl>                          | Returned by XAudio2 for certain API usage errors (invalid calls and so on) that are hard to avoid completely and should be handled by a title at runtime. (API usage errors that are completely avoidable, such as invalid parameters, cause an ASSERT in debug builds and undefined behavior in retail builds, so no error code is defined for them.)<br/> |
| <span id="XAUDIO2_E_XMA_DECODER_ERROR"></span><span id="xaudio2_e_xma_decoder_error"></span><dl> <dt>**XAUDIO2\_E\_XMA\_DECODER\_ERROR**</dt> <dt>0x88960002</dt> </dl>          | The Xbox 360 XMA hardware suffered an unrecoverable error.<br/>                                                                                                                                                                                                                                                                                             |
| <span id="XAUDIO2_E_XAPO_CREATION_FAILED"></span><span id="xaudio2_e_xapo_creation_failed"></span><dl> <dt>**XAUDIO2\_E\_XAPO\_CREATION\_FAILED**</dt> <dt>0x88960003</dt> </dl> | An effect failed to instantiate.<br/>                                                                                                                                                                                                                                                                                                                       |
| <span id="XAUDIO2_E_DEVICE_INVALIDATED"></span><span id="xaudio2_e_device_invalidated"></span><dl> <dt>**XAUDIO2\_E\_DEVICE\_INVALIDATED**</dt> <dt>0x88960004</dt> </dl>        | An audio device became unusable through being unplugged or some other event.<br/>                                                                                                                                                                                                                                                                           |



## Remarks

### Platform Requirements

Windows 10 (XAudio2.9); Windows 8, Windows Phone 8 (XAudio 2.8); DirectX SDK (XAudio 2.7)

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Xaudio2.h</dt> </dl> |



## See also

<dl> <dt>

[XAudio2::Constants](constants.md)
</dt> </dl>

 

 




