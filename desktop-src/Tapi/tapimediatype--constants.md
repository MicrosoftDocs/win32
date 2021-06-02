---
description: The media type constants are defined below.
ms.assetid: 3e418c9a-a008-4b94-b5d2-7c2eccb3bf87
title: TAPIMEDIATYPE_ Constants (Tapi3.h)
ms.topic: reference
ms.date: 05/31/2018
---

# TAPIMEDIATYPE\_ Constants

The following media types are defined:



| Constant/value                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TAPIMEDIATYPE_AUDIO"></span><span id="tapimediatype_audio"></span><dl> <dt>**TAPIMEDIATYPE\_AUDIO**</dt> <dt>0x8</dt> </dl>                    | An audio media stream that is entering or leaving the computer. An entering media stream would typically be played on speakers, or sent to a handset device and a leaving stream would typically be captured through a microphone or handset device.<br/>                                                                                                                                                                                                                                      |
| <span id="TAPIMEDIATYPE_VIDEO"></span><span id="tapimediatype_video"></span><dl> <dt>**TAPIMEDIATYPE\_VIDEO**</dt> <dt>0x8000</dt> </dl>                 | A video media stream that is entering or leaving the computer. An entering media stream would typically be rendered in a video window and a leaving media stream would typically be captured with a video camera.<br/>                                                                                                                                                                                                                                                                         |
| <span id="TAPIMEDIATYPE_DATAMODEM"></span><span id="tapimediatype_datamodem"></span><dl> <dt>**TAPIMEDIATYPE\_DATAMODEM**</dt> <dt>0x10</dt> </dl>       | A data media stream that is associated with a data modem.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="TAPIMEDIATYPE_G3FAX"></span><span id="tapimediatype_g3fax"></span><dl> <dt>**TAPIMEDIATYPE\_G3FAX**</dt> <dt>0x20</dt> </dl>                   | A data media stream that is associated with a G3 protocol fax.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="TAPIMEDIATYPE_MULTITRACK"></span><span id="tapimediatype_multitrack"></span><dl> <dt>**TAPIMEDIATYPE\_MULTITRACK**</dt> <dt>0x10000</dt> </dl> | A stream is on a multitrack terminal.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="MEDIATYPE_RTP_Single_Stream"></span><span id="mediatype_rtp_single_stream"></span><span id="MEDIATYPE_RTP_SINGLE_STREAM"></span><dl> <dt>**MEDIATYPE\_RTP\_Single\_Stream**</dt> </dl>     | This GUID is used between an application supplied terminal and the MSP's stream. If the pin of the terminal supports this media type, the stream will exchange raw RTP data with the terminal. This mode is supported only by the video streams on the H323 MSP and IPConf MSP for Windows 2000 SP1 or above.<br/> **Header:** Declared in ipmsp.h. The header ipmsp.h is not available in in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. <br/> |



## Requirements



| Requirement | Value |
|-------------------------|------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                              |
| Header<br/>       | <dl> <dt>Tapi3.h</dt> </dl> |



## See also

<dl> <dt>

[**ITQOSEvent::get\_MediaType**](/windows/desktop/api/tapi3if/nf-tapi3if-itqosevent-get_mediatype)
</dt> <dt>

[**ITAMMediaFormat::get\_MediaFormat**](/windows/win32/api/tapi3/nf-tapi3-itammediaformat-get_mediaformat)
</dt> <dt>

[**ITAMMediaFormat::put\_MediaFormat**](/windows/win32/api/tapi3/nf-tapi3-itammediaformat-put_mediaformat)
</dt> <dt>

[**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong)
</dt> <dt>

[**ITMediaSupport::get\_MediaTypes**](/windows/desktop/api/tapi3if/nf-tapi3if-itmediasupport-get_mediatypes)
</dt> <dt>

[**ITTerminalSupport::CreateTerminal**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-createterminal)
</dt> </dl>

 

