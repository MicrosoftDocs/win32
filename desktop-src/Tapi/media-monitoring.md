---
description: When a call is in the connected state, data can be transported over the call. The call media type provides an indication of the type of data (for example, its datatype, or higher-level protocol) of this media stream.
ms.assetid: 3281387e-3f72-4fda-8199-b3ce6e45e910
title: Media Monitoring
ms.topic: article
ms.date: 05/31/2018
---

# Media Monitoring

When a call is in the *connected* state, data can be transported over the call. The call media type provides an indication of the type of data (for example, its datatype, or higher-level protocol) of this media stream.

TAPI allows applications to be provided with a notification about changes in a call's media type. The notification provides an indication of the call's new media type. The service provider decides how it wants to make this determination. For example, the service provider could use signal processing of the media stream to determine the media type, or it could rely on distinctive ringing patterns assigned to different media streams, or on information elements passed in an out-of-band signaling protocol. Independent of how the media type determination is achieved, the application is simply informed about media type changes on an existing call.

For more information and a list of currently defined TAPI media types or modes, see [LINEMEDIAMODE\_ Constants](linemediamode--constants.md). Service providers may implement provider-specific media types for highly specialized devices. Information on these will be found in device documentation.

The media types defined by TAPI include:

-   Unknown. The media type of the call is not currently known—the call is unclassified.
-   Interactive voice. Voice energy was detected on the call, and the call is handled as an interactive voice call with a person at the application's end.
-   Automated voice. Voice energy was detected on the call, and the call is handled as a voice call but with no person at the application's end, such as with an answering machine application.
-   Data modem. A modem session on the call. Current modem protocols require the called station to initiate the handshake. For an incoming data modem call, the application can typically make no positive detection. How the service provider makes this determination is its choice. For example, a period of silence just after answering an incoming call can be used as a heuristic to decide that this might be a data modem call.
-   G3 fax. A group 3 fax session on the call.
-   G4 fax. A group 4 fax session on the call.
-   TDD. The call's media stream uses the Telephony Devices for the Deaf protocol.
-   Digital data. A digital data stream of unspecified format.
-   Teletex, Videotex, Telex, Mixed. These correspond to the telematic services of the same names.
-   ADSI. An Analog Display Services Interface session on the call. ADSI enhances voice calls with alphanumeric information downloaded to the phone and the use of soft buttons on the phone.

An application can enable or disable media monitoring on a specified call with [**lineMonitorMedia**](/windows/desktop/api/Tapi/nf-tapi-linemonitormedia). The application specifies which media types it is interested in monitoring, and when media monitoring is enabled, the detection of a media type change causes the application to be notified with the [**LINE\_MONITORMEDIA**](line-monitormedia.md) message. This message provides the call handle on which the media type change was detected as well as the new media type.

There is a distinction between the media type of a call as reported by [**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo) and the media type event reports by LINE\_MONITORMEDIA messages. A call's media type is determined exclusively by owner applications of the call and is not automatically changed by media monitoring events. The one exception is the initial media type determination that can be performed by the TAPI dynamic-link library to select the first owner of a call. One could argue that in this case, the library is the owner of the call.

Default media type monitoring is performed for the media types for which the line device has been opened. This allows an incoming call's media type to be determined before the call is handed to an application based on what the application demands. The scope of the media monitoring of a call is bound by the lifetime of the call. Media monitoring on a call ends as soon as the call *disconnects* or goes *idle*.

An application can obtain device identifiers for various device classes associated with an opened line by calling [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid). This function takes a line handle, address, or call handle and a device class description. It returns the device identifier for the device of the given device class that is associated with the open line device, address, or call. If the device class is "tapi/line," then the device identifier of the line device is returned. If the device class is "mci/wave," then the device identifier of an mci waveaudio device is returned (if supported), which allows activities such as the recording or playback of audio over the call on the line.

The application can use the returned device identifier with the corresponding media API to query the device's capabilities and subsequently open the media device. For example, if your application needs to use the line as a waveform device, it must first call [**waveInGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-waveingetdevcaps) and/or [**waveOutGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutgetdevcaps) to determine the waveform capabilities of the device. The typical waveform data format supported by telephony in North America is 8-bit m-law at 8000 samples per second, although the wave device driver can convert this sample rate and companding to other more common multimedia audio formats.

To subsequently open a line device for audio playback using the waveform API, an application calls [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen). The implementation of **waveOutOpen** is device specific, and there are a variety of options for implementing this function.

 

 
