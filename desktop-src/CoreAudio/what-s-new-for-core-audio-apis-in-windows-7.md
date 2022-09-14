---
description: The Core Audio APIs were introduced in Windows Vista, which provided a new set of user-mode audio components that a client application can use to render or capture audio streams with improved audio capabilities.
ms.assetid: eb99c266-16d2-4a14-bc1d-059a0a94db13
title: What's New for Core Audio APIs in Windows 7
ms.topic: article
ms.date: 05/31/2018
---

# What's New for Core Audio APIs in Windows 7

The Core Audio APIs were introduced in Windows Vista, which provided a new set of user-mode audio components that a client application can use to render or capture audio streams with improved audio capabilities. For a general overview of this API set, see [About the Windows Core Audio APIs](about-the-windows-core-audio-apis.md).

The Core Audio APIs have been improved in Windows 7. The following table summarizes the new features and the improvements to the Core Audio APIs:




| Feature | Description | 
|---------|-------------|
| Generic improvements | The following features have been improved in Windows 7:<ul><li>In Windows 7 share mode streams run in <em>low-latency mode</em>. The audio engine runs in pull mode with a significant reduction in latency. This is very useful for communication applications that require low audio stream latency for faster streaming.</li><li>Windows 7 provides better device role detection when a new device is added to the system. For more information, see <a href="device-roles-in-windows-vista.md">Working with Device Roles</a>.</li><li>In Windows 7 you can listen to music from your portable media player through your computer speakers. You can use this Capture Monitor feature by plugging a portable media player into your computer with an analog audio cable. In the past some OEMs have provided this functionality in the audio driver by using a hardware loopback. In Windows 7, this functionality has been added to the operating system. Because this is in the system and not the driver, you can use this for any other device connected to the system, such as a USB headset.</li><li>HDMI audio has been enhanced in Windows 7, which provides support for high-bit-rate format. With this improvement, you can support multichannel audio and compressed audio formats over an HDMI connector to an audio receiver.</li><li>In Windows Vista, Windows Media Player plays music only through the default audio device, which cannot be changed by the user. For Windows Media Player to render audio to a particular device, the default device must be changed in the <strong>Sounds</strong> control panel. In Windows 7, Windows Media Player provides APIs that enable an application to render to any device selected by the user and not just the default device.</li><li>In Windows Vista, if a computer that is playing audio switches to the power-save mode, the computer is locked, and if the user wants to interrupt the playback, the user must log on and press the stop key to stop the playback. In Windows 7, if the computer is locked, you can still control the playback by using the HID control on the keyboard.</li><li>Windows 7 reduces power consumption for any application that uses DirectSound and DirectShow to render media. In addition, the Multimedia Class Scheduler Service enables glitch-resilient audio and uses less power while the audio samples are being generated.</li></ul> | 
| Communication device (New) | In this release a new device type has been added to the <strong>Sounds</strong> control panel: <strong>Communications</strong> device. This device is used primarily for communications, that is, to place or receive phone calls on the computer. A communication application can use Core Audio components to get a reference to the endpoint of the default communication device and render audio streams for communication purposes. The operating system considers the stream opened on a communication device to be a communication stream. The WASAPI operations on a communication stream are similar to any other audio stream. For more information, see <a href="device-roles-in-windows-vista.md">Working with Device Roles</a>. | 
| Stream attenuation or audio ducking (New) | Automatic ducking or <a href="stream-attenuation.md">Stream Attenuation</a> is a new feature in Windows 7 that is intended for VoIP and Unified Communication applications. By default, the operating system reduces the intensity of an audio stream when a communication stream, such as a phone call, is received on the communication device through the computer. The volume options are set by the user in the <strong>Sound</strong> control panel. New APIs have been added in the Windows SDK that enable applications to replace the default ducking behavior. For more information about implementing a custom ducking feature, see <a href="providing-a-custom-ducking-experience.md">Providing a Custom Ducking Behavior</a>. <br /> | 
| Stream routing (New) | In Windows 7, the Core Audio APIs have been improved to transfer an audio stream seamlessly from an existing device to a new default audio endpoint. High-level audio API sets that use Core Audio APIs, such as Media Foundation, DirectSound, and WAVE APIs, implement the stream routing feature. Media applications that use these API sets to play or capture a stream use the default implementation and do not have to modify the application. However, if your media application uses Core Audio APIs directly, the application needs to provide the stream routing implementation. To do so, the application must handle new events that have been added that notify a WASAPI client when the default device is connected or removed. For more information about this feature, see <a href="stream-routing.md">Stream Routing</a>. | 
| Protected User Mode Audio (PUMA) (Improved) | PUMA has been updated for Windows 7 to provide the following features:<ul><li>Setting Serial Copying Management System (SCMS) bits on S/PDIF endpoints and High-bandwidth Digital Content Protection (HDCP) bits on High-Definition Multimedia Interface (HDMI) endpoints.</li><li>Enabling SCMS and HDMI protection controls outside of a Protected Environment (PE).</li></ul>For more information about the improvements, see <a href="protected-user-mode-audio--puma-.md">Protected User Mode Audio (PUMA)</a>.<br /> | 
| The <strong>WAVEFORMATEXTENSIBLE</strong> structure has been extended to the <strong>WAVEFORMATEXTENSIBLE_IEC61937</strong> structure (New) | In Windows 7, a new structure has been added to support IEC 61937 transmissions. <strong>WAVEFORMATEXTENSIBLE_IEC61937</strong> extends the <strong>WAVEFORMATEXTENSIBLE</strong> structure to store two sets of audio stream characteristics: the encoded audio format before transmission and characteristics of the audio stream after it has been decoded. The new structure explicitly specifies the effective number of channels, sample size, and data rate of a non-PCM format. With this information, an application can infer the quality level of the non-PCM stream after it is decompressed and played. For more information, see <a href="representing-formats-for-iec-61937-transmissions.md">Representing Formats for IEC 61937 Transmissions</a>.<br /> | 
| <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize"><strong>IAudioClient::Initialize</strong></a> (Improved) | The <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize"><strong>IAudioClient::Initialize</strong></a> method has been improved to indicate specific errors that might occur while opening an audio stream. The new error codes are:<ul><li>AUDCLNT_E_BUFFER_SIZE_NOT_ALIGNED</li><li>AUDCLNT_E_BUFFER_SIZE_ERROR</li><li>AUDCLNT_E_INVALID_DEVICE_PERIOD</li></ul>For more information about these errors, see the Return Value section in <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize"><strong>IAudioClient::Initialize</strong></a>.<br /> | 
| <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudiocaptureclient-getbuffer"><strong>IAudioCaptureClient::GetBuffer</strong></a> and <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-getbuffer"><strong>IAudioRenderClient::GetBuffer</strong></a> (Improved) | <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudiocaptureclient-getbuffer"><strong>IAudioCaptureClient::GetBuffer</strong></a> and <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-getbuffer"><strong>IAudioRenderClient::GetBuffer</strong></a> methods have been improved to return the AUDCLNT_E_BUFFER_ERROR error code that indicates that the endpoint buffer in the exclusive mode was not retrieved. For more information, see Remarks in <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudiocaptureclient-getbuffer"><strong>IAudioCaptureClient::GetBuffer</strong></a> and <a href="/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-getbuffer"><strong>IAudioRenderClient::GetBuffer</strong></a>. | 
| Jack detection capability (Improved) | A new interface in Windows 7, <a href="/windows/desktop/api/Devicetopology/nn-devicetopology-iksjackdescription2"><strong>IKsJackDescription2</strong></a>, extends <a href="/windows/desktop/api/Devicetopology/nn-devicetopology-iksjackdescription"><strong>IKsJackDescription</strong></a>. By using the new interface, the audio stack or an application can get additional jack information. This includes the jack's detection capability and whether the format of the device has changed dynamically. | 
| Windows Samples (New) | New samples have been added to the Windows SDK that demonstrate the use of the Core Audio APIs. For more information, see <a href="sdk-samples-that-use-the-core-audio-apis.md">SDK Samples That Use the Core Audio APIs</a>. | 




 

## Major New Interfaces

The following interfaces are new for Windows 7:

-   [**IAudioClock2**](/windows/desktop/api/audioclient/nn-audioclient-iaudioclock2)
-   [**IAudioClockAdjustment**](/windows/desktop/api/audioclient/nn-audioclient-iaudioclockadjustment)
-   [**IAudioEndpointVolumeEx**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolumeex)
-   [**IAudioSessionManager2**](/windows/desktop/api/audiopolicy/nn-audiopolicy-iaudiosessionmanager2)
-   [**IAudioSessionControl2**](/windows/desktop/api/audiopolicy/nn-audiopolicy-iaudiosessioncontrol2)
-   [**IAudioSessionEnumerator**](/windows/desktop/api/audiopolicy/nn-audiopolicy-iaudiosessionenumerator)
-   [**IAudioSessionNotification**](/windows/desktop/api/audiopolicy/nn-audiopolicy-iaudiosessionnotification)
-   [**IAudioVolumeDuckNotification**](/windows/desktop/api/AudioPolicy/nn-audiopolicy-iaudiovolumeducknotification)
-   [**IKsJackDescription2**](/windows/desktop/api/Devicetopology/nn-devicetopology-iksjackdescription2)
-   [**IKsJackSinkInformation**](/windows/desktop/api/Devicetopology/nn-devicetopology-iksjacksinkinformation)

## Related topics

<dl> <dt>

[About the Windows Core Audio APIs](about-the-windows-core-audio-apis.md)
</dt> </dl>

 

 




