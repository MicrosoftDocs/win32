---
description: The following table contains error codes that are specific to Microsoft DirectX Media Objects (DMOs). These error codes are defined in the header file Mediaerr.h.
ms.assetid: 1ded5656-084d-4315-a414-aebf4a1820dc
title: DMO Error Codes (Mediaerr.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMO Error Codes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table contains error codes that are specific to Microsoft DirectX Media Objects (DMOs). These error codes are defined in the header file Mediaerr.h.



| Constant/value                                                                                                                                                                                                                                                  | Description                                                                                                                                                         |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DMO_E_INVALIDSTREAMINDEX"></span><span id="dmo_e_invalidstreamindex"></span><dl> <dt>**DMO\_E\_INVALIDSTREAMINDEX**</dt> <dt>0x80040201</dt> </dl> | Invalid stream index.<br/>                                                                                                                                    |
| <span id="DMO_E_INVALIDTYPE"></span><span id="dmo_e_invalidtype"></span><dl> <dt>**DMO\_E\_INVALIDTYPE**</dt> <dt>0x80040202</dt> </dl>                      | Invalid media type.<br/>                                                                                                                                      |
| <span id="DMO_E_TYPE_NOT_SET"></span><span id="dmo_e_type_not_set"></span><dl> <dt>**DMO\_E\_TYPE\_NOT\_SET**</dt> <dt>0x80040203</dt> </dl>                 | Media type was not set. One or more streams require a media type before this operation can be performed.<br/>                                                 |
| <span id="DMO_E_NOTACCEPTING"></span><span id="dmo_e_notaccepting"></span><dl> <dt>**DMO\_E\_NOTACCEPTING**</dt> <dt>0x80040204</dt> </dl>                   | Data cannot be accepted on this stream. You might need to process more output data; see [**IMediaObject::ProcessInput**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-processinput).<br/> |
| <span id="DMO_E_TYPE_NOT_ACCEPTED"></span><span id="dmo_e_type_not_accepted"></span><dl> <dt>**DMO\_E\_TYPE\_NOT\_ACCEPTED**</dt> <dt>0x80040205</dt> </dl>  | Media type was not accepted.<br/>                                                                                                                             |
| <span id="DMO_E_NO_MORE_ITEMS"></span><span id="dmo_e_no_more_items"></span><dl> <dt>**DMO\_E\_NO\_MORE\_ITEMS**</dt> <dt>0x80040206</dt> </dl>              | Media-type index is out of range.<br/>                                                                                                                        |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mediaerr.h</dt> </dl> |



## See also

<dl> <dt>

[DMO Constants](dmo-constants.md)
</dt> </dl>

 

 




