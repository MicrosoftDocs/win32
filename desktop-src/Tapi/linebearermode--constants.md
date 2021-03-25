---
description: The LINEBEARERMODE\_ bit-flag constants describe different bearer modes of a call.
ms.assetid: 87e46ec9-ed5f-4ff5-a382-34eb164f4e66
title: LINEBEARERMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEBEARERMODE\_ Constants

The **LINEBEARERMODE\_** bit-flag constants describe different bearer modes of a call. When an application makes a call, it can request a specific bearer mode. These modes are used to select a certain quality of service for the requested connection from the underlying telephone network. Bearer modes available on a given line are a device capability of the line.

<dl> <dt>

<span id="LINEBEARERMODE_ALTSPEECHDATA"></span><span id="linebearermode_altspeechdata"></span>**LINEBEARERMODE\_ALTSPEECHDATA**
</dt> <dd> <dl> <dt>



The alternate transfer of speech or unrestricted data on the same call (ISDN).


</dt> </dl> </dd> <dt>

<span id="LINEBEARERMODE_DATA"></span><span id="linebearermode_data"></span>**LINEBEARERMODE\_DATA**
</dt> <dd> <dl> <dt>



The unrestricted data transfer on the call. The data rate is specified separately.


</dt> </dl> </dd> <dt>

<span id="LINEBEARERMODE_MULTIUSE"></span><span id="linebearermode_multiuse"></span>**LINEBEARERMODE\_MULTIUSE**
</dt> <dd> <dl> <dt>



The multiuse mode defined by ISDN.


</dt> </dl> </dd> <dt>

<span id="LINEBEARERMODE_NONCALLSIGNALING"></span><span id="linebearermode_noncallsignaling"></span>**LINEBEARERMODE\_NONCALLSIGNALING**
</dt> <dd> <dl> <dt>



This corresponds to a non-call-associated signaling connection from the application to the service provider or switch (treated as a media stream by TAPI).


</dt> </dl> </dd> <dt>

<span id="LINEBEARERMODE_PASSTHROUGH"></span><span id="linebearermode_passthrough"></span>**LINEBEARERMODE\_PASSTHROUGH**
</dt> <dd> <dl> <dt>



When a call is active in LINEBEARERMODE\_PASSTHROUGH, the service provider gives direct access to the attached hardware for control by the application. This mode is used primarily by applications desiring temporary direct control over asynchronous modems, accessed through the [communications functions](/windows/desktop/DevIO/communications-functions), for the purpose of configuring or using special features not otherwise supported by the service provider.


</dt> </dl> </dd> <dt>

<span id="LINEBEARERMODE_RESTRICTEDDATA"></span><span id="linebearermode_restricteddata"></span>**LINEBEARERMODE\_RESTRICTEDDATA**
</dt> <dd> <dl> <dt>



Bearer service for digital data in which only the low-order seven bits of each octet may contain user data (for example, for Switched 56kbit/s service).


</dt> </dl> </dd> <dt>

<span id="LINEBEARERMODE_SPEECH"></span><span id="linebearermode_speech"></span>**LINEBEARERMODE\_SPEECH**
</dt> <dd> <dl> <dt>



This corresponds to G.711 speech transmission on the call. The network can use processing techniques such as analog transmission, echo cancellation, and compression/decompression. Bit integrity is not assured. Speech is not intended to support fax and modem media types.


</dt> </dl> </dd> <dt>

<span id="LINEBEARERMODE_VOICE"></span><span id="linebearermode_voice"></span>**LINEBEARERMODE\_VOICE**
</dt> <dd> <dl> <dt>



This is a regular 3.1 kHz analog voice-grade bearer service. Bit integrity is not assured. Voice can support fax and modem media types.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

Note that bearer mode and media type are different notions. The bearer mode of a call is an indication of the quality of the telephone connection as provided primarily by the network. The media type of a call is an indication of the type of information stream that is exchanged over that call. Group 3 fax or data modem are media types that use a call with a 3.1 kHz voice bearer mode.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

