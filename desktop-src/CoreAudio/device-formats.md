---
description: Device Formats
ms.assetid: 591437e4-21ef-42f1-a752-7f50440cbd63
title: Device Formats
ms.topic: article
ms.date: 05/31/2018
---

# Device Formats

For an audio application, a benefit of using a higher-level audio API, such as DirectSound or the Windows multimedia **waveOutXxx** functions, is that the API automatically converts between the stream formats used by the application and the formats used by the audio device. In contrast, the core audio APIs are more restrictive because they require application streams to use formats that are the same as, or are closely related to, the formats used by the device. Thus, applications that use the core audio APIs to play or record audio streams might be required to do some or all of the conversions between stream formats.

An application that uses WASAPI to manage shared-mode streams can rely on the audio engine to perform only limited format conversions. The audio engine can convert between a standard PCM sample size used by the application and the floating-point samples that the engine uses for its internal processing. However, the format for an application stream typically must have the same number of channels and the same sample rate as the stream format used by the device.

If an application is using a device in exclusive mode, the application must use a stream format that the audio hardware explicitly supports. In exclusive mode, the application and device exchange audio data directly, without intervention by the audio engine.

Many audio devices support both PCM and non-PCM stream formats. However, the audio engine can mix only PCM streams. Thus, only exclusive-mode streams can have non-PCM formats. In addition, only non-PCM formats with fixed data rates are supported in exclusive mode. An example of a fixed-rate non-PCM format is a 48-kHz Windows Media Audio Professional (WMA Pro) audio stream that passes through a Sony/Philips digital interface (S/PDIF) link in digital form without being decoded. For more information about using WMA Pro streams over S/PDIF, see the following documentation:

-   The description of the WAVE\_FORMAT\_WMA\_SPDIF wave-format tag in the Windows DDK documentation.
-   The white paper titled "Audio Driver Support for the WMA Pro-over-S/PDIF Format" at the [Audio Device Technologies for Windows](https://www.microsoft.com/whdc/device/audio/default.mspx) website.

WASAPI uses a **WAVEFORMATEX** or **WAVEFORMATEXTENSIBLE** structure to specify a stream format. A **WAVEFORMATEXTENSIBLE** structure is effectively a **WAVEFORMATEX** structure that has been extended to describe a greater range of formats. Any format that can be described by a stand-alone **WAVEFORMATEX** structure can also be described by a **WAVEFORMATEXTENSIBLE** structure.

The first member of the **WAVEFORMATEXTENSIBLE** structure is a **WAVEFORMATEX** structure. The contents of a **WAVEFORMATEX** structure indicate whether it is a stand-alone **WAVEFORMATEX** structure or part of a **WAVEFORMATEXTENSIBLE** structure.

A stand-alone **WAVEFORMATEX** structure can adequately describe a format with one or two channels and a sample size that is a multiple of 8 bits. By itself, a **WAVEFORMATEX** structure cannot specify the mapping of channels to speaker positions. In addition, although **WAVEFORMATEX** specifies the size of the container for each audio sample, it cannot specify the number of bits of precision in a sample (for example, 20 bits of precision in a 24-bit container). In contrast, the **WAVEFORMATEXTENSIBLE** structure can specify both the mapping of channels to speakers and the number of bits of precision in each sample.

For more information about **WAVEFORMATEX** and **WAVEFORMATEXTENSIBLE**, see the Windows DDK documentation.

Starting with Windows 7, the **WAVEFORMATEXTENSIBLE** has been extended to represent device formats for transmitting encoded audio over an IEC 61937-compatible interface. For information about the new structure, see [Representing Formats for IEC 61937 Transmissions](representing-formats-for-iec-61937-transmissions.md).

### Specifying the Device Format

The following WASAPI methods use the **WAVEFORMATEX** and **WAVEFORMATEXTENSIBLE** structures to describe stream formats:

-   [**IAudioClient::GetMixFormat**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getmixformat)
-   [**IAudioClient::IsFormatSupported**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-isformatsupported)
-   [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize)

The **GetMixFormat** method retrieves the stream format that the audio engine uses for its internal processing of shared-mode streams. The method always uses a **WAVEFORMATEXTENSIBLE** structure, instead of a stand-alone **WAVEFORMATEX** structure, to specify the format.

The **IsFormatSupported** method indicates whether an audio endpoint device supports a particular stream format. The caller must specify whether the stream format is intended for use in shared mode or in exclusive mode. For shared-mode formats, the method queries the audio engine to determine whether it supports the specified format. For exclusive-mode formats, the method queries the device driver. Some device drivers will report that they support a 1-channel or 2-channel PCM format if the format is specified by a stand-alone **WAVEFORMATEX** structure, but will reject the same format if it is specified by a **WAVEFORMATEXTENSIBLE** structure. To obtain reliable results from these drivers, exclusive-mode applications should call **IsFormatSupported** twice for each 1-channel or 2-channel PCM format—one call should use a stand-alone **WAVEFORMATEX** structure to specify the format, and the other call should use a **WAVEFORMATEXTENSIBLE** structure to specify the same format.

After an application has used **GetMixFormat** or **IsFormatSupported** to find an appropriate format for a shared-mode or exclusive-mode stream, the application can call the **Initialize** method to initialize a stream with that format. An application that attempts to initialize a shared-mode stream with a format that is not identical to the mix format obtained from the **GetMixFormat** method, but that has the same number of channels and the same sample rate as the mix format, is likely to succeed. Before calling **Initialize**, the application can call **IsFormatSupported** to verify that **Initialize** will accept the format.

The mix format that the audio engine uses for its internal processing of shared-mode streams is closely related to, but is not necessarily identical to, the stream format that the audio endpoint device uses in shared mode. Through the Windows multimedia control panel, Mmsys.cpl, the user can select the stream format that an audio endpoint device will use when it operates in shared mode. The steps are as follows:

1.  To run Mmsys.cpl, open a Command Prompt window and enter the following command:

    **control mmsys.cpl**

    Alternatively, you can run Mmsys.cpl by right-clicking the speaker icon in the notification area, which is located on the right side of the taskbar, and selecting either **Playback Devices** or **Recording Devices**.

2.  After the Mmsys.cpl window opens, select a device from either the list of playback devices or the list of recording devices, and click **Properties**.
3.  When the properties window opens, click **Advanced**, and select a format from the list of available formats in the box labeled **Default Format**.

For example, assume that the user selects the following default format from the list of available formats for a playback device:

**2 channel, 16 bit, 44100 Hz (CD Quality)**

This is the format that the device will subsequently use when it operates in shared mode. In Windows Vista, the audio engine will use a slightly modified version of this format for its internal processing of shared-mode streams. The audio engine will use a format with the same number of channels (two) and the same sample rate (44100 Hz), but it will convert samples to floating-point numbers before processing them. The audio engine will convert the floating-point samples in the output mix to 16-bit integers before playing them through the device.

An application can query an audio endpoint device's [**PKEY\_AudioEngine\_DeviceFormat**](pkey-audioengine-deviceformat.md) property to obtain the shared-mode format that the user has selected for the device. For information about querying the properties of a device, see [Device Properties](device-properties.md).

Some applications might find the format specified by a device's **PKEY\_AudioEngine\_DeviceFormat** property to be a suitable format for opening an exclusive-mode stream on the device. Other applications that manage exclusive-mode streams might have additional requirements that mandate a complex format negotiation with the device. Typically, one of these applications constructs a list of suitable formats, with the preferred formats at the beginning of the list. The application then iteratively calls **IsFormatSupported** with each successive format in the list, beginning at the start of the list, until it finds a format that the device supports.

## Related topics

<dl> <dt>

[Audio Endpoint Devices](audio-endpoint-devices.md)
</dt> </dl>

 

 



