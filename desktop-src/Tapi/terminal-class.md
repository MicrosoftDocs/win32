---
description: The terminal class GUIDs identify a particular terminal by capabilities.
ms.assetid: 2a16d33c-2d87-4172-a5ff-33ff62e96615
title: Terminal Class (Tapi3if.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Terminal Class

The terminal class GUIDs identify a particular terminal by capabilities.

<dl> <dt>

<span id="CLSID_FilePlaybackTerminal"></span><span id="clsid_fileplaybackterminal"></span><span id="CLSID_FILEPLAYBACKTERMINAL"></span>**CLSID\_FilePlaybackTerminal**
</dt> <dd> <dl> <dt>



File playback terminal.


</dt> </dl> </dd> <dt>

<span id="CLSID_FileRecordingTerminal"></span><span id="clsid_filerecordingterminal"></span><span id="CLSID_FILERECORDINGTERMINAL"></span>**CLSID\_FileRecordingTerminal**
</dt> <dd> <dl> <dt>



File recording terminal.


</dt> </dl> </dd> <dt>

<span id="CLSID_FileRecordingTrack"></span><span id="clsid_filerecordingtrack"></span><span id="CLSID_FILERECORDINGTRACK"></span>**CLSID\_FileRecordingTrack**
</dt> <dd> <dl> <dt>



File recording track.


</dt> </dl> </dd> <dt>

<span id="CLSID_HandsetTerminal"></span><span id="clsid_handsetterminal"></span><span id="CLSID_HANDSETTERMINAL"></span>**CLSID\_HandsetTerminal**
</dt> <dd> <dl> <dt>



Telephone handset.


</dt> </dl> </dd> <dt>

<span id="CLSID_HeadsetTerminal"></span><span id="clsid_headsetterminal"></span><span id="CLSID_HEADSETTERMINAL"></span>**CLSID\_HeadsetTerminal**
</dt> <dd> <dl> <dt>



Head set.


</dt> </dl> </dd> <dt>

<span id="CLSID_MediaStreamTerminal"></span><span id="clsid_mediastreamterminal"></span><span id="CLSID_MEDIASTREAMTERMINAL"></span>**CLSID\_MediaStreamTerminal**
</dt> <dd> <dl> <dt>



Media stream terminal, dynamically created.


</dt> </dl> </dd> <dt>

<span id="CLSID_MicrophoneTerminal"></span><span id="clsid_microphoneterminal"></span><span id="CLSID_MICROPHONETERMINAL"></span>**CLSID\_MicrophoneTerminal**
</dt> <dd> <dl> <dt>



Microphone.


</dt> </dl> </dd> <dt>

<span id="CLSID_SpeakerphoneTerminal"></span><span id="clsid_speakerphoneterminal"></span><span id="CLSID_SPEAKERPHONETERMINAL"></span>**CLSID\_SpeakerphoneTerminal**
</dt> <dd> <dl> <dt>



Speaker phone.


</dt> </dl> </dd> <dt>

<span id="CLSID_SpeakersTerminal"></span><span id="clsid_speakersterminal"></span><span id="CLSID_SPEAKERSTERMINAL"></span>**CLSID\_SpeakersTerminal**
</dt> <dd> <dl> <dt>



Speakers.


</dt> </dl> </dd> <dt>

<span id="CLSID_VideoInputTerminal"></span><span id="clsid_videoinputterminal"></span><span id="CLSID_VIDEOINPUTTERMINAL"></span>**CLSID\_VideoInputTerminal**
</dt> <dd> <dl> <dt>



Video input terminal.


</dt> </dl> </dd> <dt>

<span id="CLSID_VideoWindowTerm"></span><span id="clsid_videowindowterm"></span><span id="CLSID_VIDEOWINDOWTERM"></span>**CLSID\_VideoWindowTerm**
</dt> <dd> <dl> <dt>



Video display window, dynamically created.


</dt> </dl> </dd> </dl>

## Remarks

The **BSTR** version of the terminal classes is mainly designated for the use of Visual Basic applications. (For example, they are returned as the elements of the collection obtained with [**get\_DynamicTerminalClasses**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-get_dynamicterminalclasses).)

-   BSTR CLSID\_String\_HandsetTerminal
-   BSTR CLSID\_String\_HeadsetTerminal
-   BSTR CLSID\_String\_MediaStreamTerminal
-   BSTR CLSID\_String\_MicrophoneTerminal
-   BSTR CLSID\_String\_SpeakerphoneTerminal
-   BSTR CLSID\_String\_SpeakersTerminal
-   BSTR CLSID\_String\_VideoInputTerminal
-   BSTR CLSID\_String\_VideoWindowTerm

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                |
| Header<br/>       | <dl> <dt>Tapi3if.h</dt> </dl> |



## See also

<dl> <dt>

[**ITTerminalSupport::CreateTerminal**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-createterminal)
</dt> <dt>

[**ITTerminal::get\_TerminalClass**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_terminalclass)
</dt> <dt>

[**ITTerminalManager::CreateDynamicTerminal**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalmanager-createdynamicterminal)
</dt> <dt>

[**ITTerminalManager::GetDynamicTerminalClasses**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalmanager-getdynamicterminalclasses)
</dt> <dt>

[**ITTerminalSupport::EnumerateDynamicTerminalClasses**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-enumeratedynamicterminalclasses)
</dt> </dl>

 

