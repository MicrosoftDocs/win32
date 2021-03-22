---
description: The LINEMEDIAMODE\_ constants describe media types (or modes)of a communications session or call.
ms.assetid: cbb758be-3ecd-4ac4-b1b5-57136a1aad8e
title: LINEMEDIAMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEMEDIAMODE\_ Constants

The **LINEMEDIAMODE\_** constants describe media types (or modes)of a communications session or call.

<dl> <dt>

<span id="LINEMEDIAMODE_AUTOMATEDVOICE"></span><span id="linemediamode_automatedvoice"></span>**LINEMEDIAMODE\_AUTOMATEDVOICE**
</dt> <dd> <dl> <dt>



Voice energy was detected on the call, and the voice is locally handled by an automated application such as with an answering machine application. When a service provider cannot distinguish between interactive and automated voice on an incoming call, it will report the call as interactive voice.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_DATAMODEM"></span><span id="linemediamode_datamodem"></span>**LINEMEDIAMODE\_DATAMODEM**
</dt> <dd> <dl> <dt>



A data modem session on the call. Current modem protocols require the called station to initiate the handshake. For an incoming data modem call, the application can typically make no positive detection. How the service provider makes this determination is its choice. For example, a period of silence just after answering an incoming call can be used as a heuristic to decide that this might be a data modem call.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_ADSI"></span><span id="linemediamode_adsi"></span>**LINEMEDIAMODE\_ADSI**
</dt> <dd> <dl> <dt>



An ADSI (Analog Display Services Interface) session on the call. ADSI enhances voice calls with alphanumeric information downloaded to the phone and the use of soft buttons on the phone.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_DIGITALDATA"></span><span id="linemediamode_digitaldata"></span>**LINEMEDIAMODE\_DIGITALDATA**
</dt> <dd> <dl> <dt>



A digital data stream of unspecified format.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_G3FAX"></span><span id="linemediamode_g3fax"></span>**LINEMEDIAMODE\_G3FAX**
</dt> <dd> <dl> <dt>



A group 3 fax is being sent or received over the call.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_G4FAX"></span><span id="linemediamode_g4fax"></span>**LINEMEDIAMODE\_G4FAX**
</dt> <dd> <dl> <dt>



A group 4 fax is being sent or received over the call.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_INTERACTIVEVOICE"></span><span id="linemediamode_interactivevoice"></span>**LINEMEDIAMODE\_INTERACTIVEVOICE**
</dt> <dd> <dl> <dt>



Voice energy was detected on the call, and the call is handled as an interactive voice call with humans on both ends.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_MIXED"></span><span id="linemediamode_mixed"></span>**LINEMEDIAMODE\_MIXED**
</dt> <dd> <dl> <dt>



A mixed session on the call. Mixed is one of the ISDN telematic services.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_TDD"></span><span id="linemediamode_tdd"></span>**LINEMEDIAMODE\_TDD**
</dt> <dd> <dl> <dt>



A TDD (Telephony Devices for the Deaf) session on the call.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_TELETEX"></span><span id="linemediamode_teletex"></span>**LINEMEDIAMODE\_TELETEX**
</dt> <dd> <dl> <dt>



A teletex session on the call. Teletex is one of the telematic services.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_TELEX"></span><span id="linemediamode_telex"></span>**LINEMEDIAMODE\_TELEX**
</dt> <dd> <dl> <dt>



A telex session on the call. Telex is one of the telematic services.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_VIDEO"></span><span id="linemediamode_video"></span>**LINEMEDIAMODE\_VIDEO**
</dt> <dd> <dl> <dt>



The media type of the call is video. (TAPI versions 2.1 and later)


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_VIDEOTEX"></span><span id="linemediamode_videotex"></span>**LINEMEDIAMODE\_VIDEOTEX**
</dt> <dd> <dl> <dt>



A videotex session on the call. Videotex is one the telematic services.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_VOICEVIEW"></span><span id="linemediamode_voiceview"></span>**LINEMEDIAMODE\_VOICEVIEW**
</dt> <dd> <dl> <dt>



The media type of the call is VoiceView. (TAPI versions 1.4 and later)


</dt> </dl> </dd> <dt>

<span id="LINEMEDIAMODE_UNKNOWN"></span><span id="linemediamode_unknown"></span>**LINEMEDIAMODE\_UNKNOWN**
</dt> <dd> <dl> <dt>



A media stream exists but its mode is not currently known and may become known later. This would correspond to a call with an unclassified media type. In typical analog telephony environments, an incoming call's media type may be unknown until after the call has been answered and the media stream has been filtered to make a determination.

If the unknown media-mode flag is set, other media flags can also be set. This is used to signify that the media is unknown but that it is likely to be one of the other selected media types.


</dt> </dl> </dd> </dl>

## Remarks

All 32 bits are reserved.

Note that bearer mode and media type are different notions. The bearer mode of a call is an indication of the quality of the telephone connection as provided primarily by the network. The media type of a call is an indication of the type of information stream that is exchanged over that call. Group 3 fax or data modem are media types that use a call with a 3.1 kHz voice bearer mode.

For backward compatibility, it is the responsibility of the service provider to examine the negotiated API version on the line, and to not use this LINEMEDIAMODE\_ value if not supported on the negotiated version.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




