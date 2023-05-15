---
description: With the increase in media storage devices that require compressed audio formats, applications must identify, describe, and use a variety of new encoded audio content for transmitting content from PCs to devices such as HDMI or DisplayPort receiver.
ms.assetid: 86f3396c-b32a-4d70-9f21-e38a745f78bf
title: Representing Formats for IEC 61937 Transmissions
ms.topic: article
ms.date: 05/31/2018
---

# Representing Formats for IEC 61937 Transmissions

With the increase in media storage devices that require compressed audio formats, applications must identify, describe, and use a variety of new encoded audio content for transmitting content from PCs to devices such as HDMI or DisplayPort receiver.

To represent an encoded audio stream to be transmitted over an IEC 61937-compatible interface, an application must provide:

-   The characteristics of an encoded audio stream to be transmitted.

-   The characteristics of a decoded audio stream on the target device.

In Windows Vista and earlier Windows operating systems, an application can infer the quality level of an audio format from the number of channels, the sample size, and the data rate of an audio stream that uses the format. For a PCM format, this information is available from the **nChannels**, **nSamplesPerSec**, and **nAvgBytesPerSec** members of the **WAVEFORMATEX** structure that specifies the format. For a non-PCM format, these three members have been commandeered to store information about the compressed data in the audio stream. Thus, the **WAVEFORMATEX** structure lacks information about the effective number of channels, sample size, and data rate of the non-PCM audio stream after the stream is decompressed and played. Based on the information in this structure, a user or an application might have difficulty inferring the quality level of the non-PCM stream.

The **WAVEFORMATEX** was extended to the **WAVEFORMATEXTENSIBLE** structure to provide the extra stream characteristics. However, this structure is also not adequate in describing the stream for IEC 61937 transmissions because it was intended to represent a single set of characteristics and used for uncompressed, multi-channel PCM data.

In Windows 7, the operating system addresses this problem by providing support for a new structure, **WAVEFORMATEXTENSIBLE\_IEC61937** which extends **WAVEFORMATEXTENSIBLE** structure to store two sets of audio stream characteristics: the encoded audio format before transmission and characteristics of the audio stream after it has been decoded. The new structure explicitly specifies the effective number of channels, sample size, and data rate of a non-PCM format. With this information, an application can infer the quality level of the non-PCM stream after it is decompressed and played.

The **WAVEFORMATEXTENSIBLE\_IEC61937** structure is declared in the KsMedia.h header included with the Windows 7 SDK. The **FormatExt** member is the **WAVEFORMATEXTENSIBLE** structure that stores the characteristics of the stream to be transmitted. The **Format** member of the **WAVEFORMATEXTENSIBLE** structure is the **WAVEFORMATEX** structure. The contents of this **WAVEFORMATEX** and **WAVEFORMATEXTENSIBLE** indicate to an application whether the structure can be interpreted as a **WAVEFORMATEXTENSIBLE\_IEC61937** structure. For a **WAVEFORMATEXTENSIBLE\_IEC61937** structure:

-   The **wFormatTag** member of **WAVEFORMATEX** must contain WAVE\_FORMAT\_EXTENSIBLE (`FormatExt.Format.wFormatTag = WAVE_FORMAT_EXTENSIBLE`).

-   The **SubFormat** member of the **WAVEFORMATEXTENSIBLE** structure specifies the GUID of the encoded format to be transmitted. For example, `FormatExt.SubFormat = KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL` indicates the Dolby Digital Plus format. For the supported GUIDs, see SubFormat GUIDs.

-   The size indicated by **cbSize** member of the WAVEFORMATEX is 34 bytes. (`FormatExt.Format.cbSize = 34`). The total size of **WAVEFORMATEXTENSIBLE\_IEC61937** is 52 bytes.

The **dwEncodedSamplesPerSec**, **dwEncodedChannelCount**, and **dwAverageBytesPerSec** members of **WAVEFORMATEXTENSIBLE\_IEC61937** describe the sampling rate, number of channels, and bit rate in bytes of the stream of the audio stream after it has been decoded.

## SubFormat GUIDs

In Windows 7, the KsMedia.h header contains definitions for the SubFormat GUIDs for the compressed audio formats defined by CEA-861-D. The GUIDs are specified in the SubFormat member of the **WAVEFORMATEXTENSIBLE**, specified in the **FormatExt** member of the **WAVEFORMATEXTENSIBLE\_IEC61937** structure (`WAVEFORMATEXTENSIBLE_IEC61937.FormatExt.Subformat`).

The GUIDs for the compressed audio formats that are available as standard IEC 61937 encoded audio formats are listed in the following table. These formats are similar to the existing Active Coding 3 (AC-3) and Digital Theater Sound (DTS) formats representations in Windows.



| CEA 861 Type | SubFormat GUID                                                                                                          | Description                                  |
|--------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| 0x00         |                                                                                                                         | Refer to the stream.                         |
| 0x01         | 00000000-0000-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_WAVEFORMATEX<br/>                          | IEC 60958 PCM                                |
| 0x02         | 00000092-0000-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_DIGITAL<br/>              | AC-3                                         |
| 0x03         | 00000003-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_MPEG1<br/>                       | MPEG-1 (Layer 1 & 2)                         |
| 0x04         | 00000004-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_MPEG3<br/>                       | MPEG-3 (Layer 3)                             |
| 0x05         | 00000005-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_MPEG2 <br/>                      | MPEG-2(multichannel)                         |
| 0x06         | 00000006-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_AAC<br/>                         | Advanced Audio Coding (MPEG-2/4 AAC in ADTS) |
| 0x07         | 00000008-0000-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DTS<br/>                         | DTS                                          |
| 0x0a         | 0000000a-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_DIGITAL\_PLUS<br/>        | Dolby Digital Plus                           |
| 0x0a         | 0000010a-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_DIGITAL\_PLUS\_ATMOS<br/> | Dolby Atmos encoded with Dolby Digital Plus  |
| 0x0f         |                                                                                                                         | Unused Reserved                              |



 

The GUIDs for the compressed audio formats that are transmitted in high bit-rate audio sample packets are listed in the following table.



| CEA 861 Type | SubFormat GUID                                                                                           | Description                                                                                                                     |
|--------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 0x0b         | 0000000b-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DTS\_HD<br/>      | DTS-HD (24-bit, 96Khz)                                                                                                          |
| 0x0c         | 0000000c-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_MLP<br/>   | Dolby MAT 1.0:<br/> Dolby TrueHD (MLP – Meridian Lossless Packing) – 24-bit 192KHz/up to 18 Mbps, 8 channels) <br/> |
| 0x0c         | 0000010c-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_MAT20<br/> | Dolby MAT 2.0: <br/> Dolby TrueHD – 24-bit 192KHz/up to 18 Mbps, 8 channels, or LPCM up to 24 Mbps. <br/>           |
| 0x0c         | 0000030c-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_MAT21<br/> | Dolby MAT 2.1: <br/> Dolby TrueHD – 24-bit 192KHz/up to 18 Mbps, 8 channels, or LPCM up to 24 Mbps. <br/>           |
| 0x0e         | 00000164-0000-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_WMA\_PRO<br/>     | Windows Media Audio (WMA) Pro                                                                                                   |
| 0x0b         | 0000000b-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DTS\_HD<br/> | DTS HD  |
| 0x0b         | 0000010b-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DTSX\_E1<br/> | DTS:X E1  |
| 0x0b         | 0000030b-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DTSX\_E2<br/> | DTS:X E2  |



 

Microsoft-provided HD Audio class driver supports PCM, AC3, DTS, AAC, Dolby Digital Plus, WMA Pro, MAT(MLP) formats. The GUIDs for the compressed audio formats that are not supported by the HD audio class driver and can be implemented by third-party solutions are listed in the following table.



| CEA 861 Type | SubFormat GUID                                                                                              | Description                                                                    |
|--------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| 0x08         | 00000008-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_ATRAC<br/>           | Adaptive Transform Acoustic Coding (ATRAC)                                     |
| 0x09         | 00000009-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_ONE\_BIT\_AUDIO<br/> | One-Bit Audio                                                                  |
| 0x0d         | 0000000d-0cea-0010-8000-00aa00389b71<br/> KSDATAFORMAT\_SUBTYPE\_IEC61937\_DST<br/>             | Direct Stream Transport (DST)—lossless compressed DSD (Direct Stream Digital). |



 

## Dolby Digital Plus Format

When Dolby Digital Plus content is transmitted over IEC 60958, the link-sampling rate must be four times the sampling rate of the content. Dolby Digital Plus supports content sample rates of 32 KHz, 44.1 KHz, and 48 KHz. Interfaces such as HDMI do not support 128 KHz (32 KHz x 4), so only 44.1 and 48 KHz content sample rates can be supported.

The values set by an application in the WAVEFORMATEXTENSIBLE\_IEC61937 structure to represent Dolby Digital Plus format at a content sample rate of 48 KHz are shown in the following example.


```C++
WAVEFORMATEXTENSIBLE_IEC61937 wfext;
Wfext.FormatExt.Format.wFormatTag = WAVE_FORMAT_EXTENSIBLE;
wfext.FormatExt.Format.nChannels = 2;              // One IEC 60958 Line.
wfext.FormatExt.Format.nSamplesPerSec = 192000;    // Link runs at 192 KHz.
wfext.FormatExt.Format.nAvgBytesPerSec = 768000;   // 192 KHz * 4.
wfext.FormatExt.Format.nBlockAlign = 4;            // 16 bits * 2 channels.
wfext.FormatExt.Format.wBitsPerSample = 16;        // Always at 16 bits over IEC 60958.
wfext.FormatExt.Format.cbSize = 34;                // Indicates that Format is part of a 
                                                   // WAVEFORMATEXTENSIBLE_IEC61937 structure.
wfext.FormatExt.Samples.wValidBitsPerSample = 16;
wfext.FormatExt.dwChannelMask = KSAUDIO_SPEAKER_5POINT1;    // Dolby 5.1 Surround.
wfext.FormatExt.SubFormat = KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS;
wfext.dwEncodedSamplesPerSec = 48000;                       // Sample rate of encoded content.
wfext.dwEncodedChannelCount = 6;                            // Encoded data contains 6 channels.
wfext.dwAverageBytesPerSec = 0;                             // Ignored for this format.
```



## Dolby TrueHD (MAT)

Dolby TrueHD content is transmitted over IEC 60958 at 176.4 kHz / 8 channels (requiring an IEC 60958 frame rate of 705.6 kHz) for content sample rates of 44.1, 88.2 and 176.4 kHz, and 192 kHz / 8 channels (requiring an IEC 60958 frame rate of 768 kHz) for content sample rates of 48, 96 and 192 kHz.

The values set by an application in the WAVEFORMATEXTENSIBLE\_IEC61937 structure to represent Dolby TrueHD at a content sample rate of 96 KHz are shown in the following examples.

Dolby MAT 1.0


```C++
WAVEFORMATEXTENSIBLE_IEC61937 wfext;
Wfext.FormatExt.Format.wFormatTag = WAVE_FORMAT_EXTENSIBLE;
wfext.FormatExt.Format.nChannels = 8;                // Four IEC 60958 Lines.
wfext.FormatExt.Format.nSamplesPerSec = 192000;      // Link runs at 192 KHz.
wfext.FormatExt.Format.nAvgBytesPerSec = 3072000;    // 192 KHz * 16.
wfext.FormatExt.Format.nBlockAlign = 16;             // 16-bits * 8 channels.
wfext.FormatExt.Format.wBitsPerSample = 16;          // Always at 16 bits over IEC 60958.
wfext.FormatExt.Format.cbSize = 34;                  // Indicates that Format is part of a 
                                                     // WAVEFORMATEXTENSIBLE_IEC61937 structure.
wfext.FormatExt.Samples.wValidBitsPerSample = 16;
wfext.FormatExt.dwChannelMask = KSAUDIO_SPEAKER_7POINT1;    // Dolby 7.1 Surround.
wfext.FormatExt.SubFormat = KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MLP; // This structure indicates MLP (MAT 1.0) support.
wfext.dwEncodedSamplesPerSec = 96000;                       // Sample rate of encoded content.
wfext.dwEncodedChannelCount = 8;                            // Encoded data contains 8 channels.
wfext.dwAverageBytesPerSec = 0;                             // Ignored for this format.
```



Dolby MAT 2.0


```C++
WAVEFORMATEXTENSIBLE_IEC61937 wfext;
Wfext.FormatExt.Format.wFormatTag = WAVE_FORMAT_EXTENSIBLE;
wfext.FormatExt.Format.nChannels = 8;                // Four IEC 60958 Lines.
wfext.FormatExt.Format.nSamplesPerSec = 192000;      // Link runs at 192 KHz.
wfext.FormatExt.Format.nAvgBytesPerSec = 3072000;    // 192 KHz * 16.
wfext.FormatExt.Format.nBlockAlign = 16;             // 16-bits * 8 channels.
wfext.FormatExt.Format.wBitsPerSample = 16;          // Always at 16 bits over IEC 60958.
wfext.FormatExt.Format.cbSize = 34;                  // Indicates that Format is part of a 
                                                     // WAVEFORMATEXTENSIBLE_IEC61937 structure.
wfext.FormatExt.Samples.wValidBitsPerSample = 16;
wfext.FormatExt.dwChannelMask = KSAUDIO_SPEAKER_7POINT1;    // Dolby 7.1 Surround.
wfext.FormatExt.SubFormat = KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT20; // This structure indicates MAT 2.0 support.
wfext.dwEncodedSamplesPerSec = 96000;                       // Sample rate of encoded content.
wfext.dwEncodedChannelCount = 8;                            // Encoded data contains 8 channels.
wfext.dwAverageBytesPerSec = 0;                             // Ignored for this format.
```



Dolby MAT 2.1


```C++
WAVEFORMATEXTENSIBLE_IEC61937 wfext;
Wfext.FormatExt.Format.wFormatTag = WAVE_FORMAT_EXTENSIBLE;
wfext.FormatExt.Format.nChannels = 8;                // Four IEC 60958 Lines.
wfext.FormatExt.Format.nSamplesPerSec = 192000;      // Link runs at 192 KHz.
wfext.FormatExt.Format.nAvgBytesPerSec = 3072000;    // 192 KHz * 16.
wfext.FormatExt.Format.nBlockAlign = 16;             // 16-bits * 8 channels.
wfext.FormatExt.Format.wBitsPerSample = 16;          // Always at 16 bits over IEC 60958.
wfext.FormatExt.Format.cbSize = 34;                  // Indicates that Format is part of a 
                                                     // WAVEFORMATEXTENSIBLE_IEC61937 structure.
wfext.FormatExt.Samples.wValidBitsPerSample = 16;
wfext.FormatExt.dwChannelMask = KSAUDIO_SPEAKER_7POINT1;    // Dolby 7.1 Surround.
wfext.FormatExt.SubFormat = KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT21; // This structure indicates MAT 2.1 support.
wfext.dwEncodedSamplesPerSec = 96000;                       // Sample rate of encoded content.
wfext.dwEncodedChannelCount = 8;                            // Encoded data contains 8 channels.
wfext.dwAverageBytesPerSec = 0;                             // Ignored for this format.
```



> [!Note]  
> Support for one version of Dolby MAT does not imply support for Dolby MAT with a lower version number. Since Dolby MAT 2.1 is backwards compatible with previous versions of Dolby MAT, a class driver that indicates support for Dolby MAT 2.1 will typically also indicate support for Dolby MAT 2.0 and Dolby MAT 1.0, using a separate WAVEFORMATEXTENSIBLE\_IEC61937 structure for each version.

 

## WMA Pro

WMA Pro audio content can be encoded in one of the four profiles listed in the following table.



| Profile | Property - Value                                                                                                                                                                                                                                                      | Description                                                                                                                         |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| M0      | Maximum bit rate – 192000 bps <br/> Maximum sampling rate – 48 KHz <br/> Maximum channel count – 2 <br/> Maximum buffer size – 600\*1024 bits <br/> Maximum samples per frame – 2048 <br/> Maximum bits per frame - 655536<br/>   | Recommended for over-the-air music and streaming.<br/> Maximum bit rate in an audio frame is 1536000 bps.<br/>          |
| M1      | Maximum bit rate – 385000 bps <br/> Maximum sampling rate – 48 KHz <br/> Maximum channel count – 6 <br/> Maximum buffer size – 600\*1024 bits <br/> Maximum samples per frame – 4096 <br/> Maximum bits per frame - 131072<br/>   | Recommended for surround-sound standard definition movies.<br/> Maximum bit rate in an audio frame is 1536000 bps.<br/> |
| M2      | Maximum bit rate – 769000 bps <br/> Maximum sampling rate – 96 KHz <br/> Maximum channel count – 6 <br/> Maximum buffer size – 1200\*1024 bits <br/> Maximum samples per frame – 4096 <br/> Maximum bits per frame - 131072<br/>  | Recommended for surround-sound high definition movies.<br/> Maximum rate in an audio frame is 3072000 bps.<br/>         |
| M3      | Maximum bit rate – 3000000 bps <br/> Maximum sampling rate – 96 KHz <br/> Maximum channel count – 8 <br/> Maximum buffer size – 2400\*1024 bits <br/> Maximum samples per frame – 4096 <br/> Maximum bits per frame - 131072<br/> | Recommended for digital theater.<br/> Maximum rate in an audio frame is 3072000 bps.<br/>                               |



 

The M0 and M1 profiles fit into a 48 KHz/16 bit/Stereo (1536000 bps) IEC 60958 stream. The M2 and M3 profiles fit into a 96 KHz/16 bit/Stereo (3072000 bps) IEC 60958 stream.

The values set by an application in the WAVEFORMATEXTENSIBLE\_IEC61937 structure to represent WMA Pro as an M2 profile are shown in the following example.


```C++
WAVEFORMATEXTENSIBLE_IEC61937 wfext;
Wfext.FormatExt.Format.wFormatTag = WAVE_FORMAT_EXTENSIBLE;
wfext.FormatExt.Format.nChannels = 2;             // One IEC 60958 Line.
wfext.FormatExt.Format.nSamplesPerSec = 96000;    // Link runs at 96 KHz.
wfext.FormatExt.Format.nAvgBytesPerSec = 384000;  // 96 KHz * 4.
wfext.FormatExt.Format.nBlockAlign = 4;           // 16 bits * 8 channels.
wfext.FormatExt.Format.wBitsPerSample = 16;       // Always at 16 bits over link.
wfext.FormatExt.Format.cbSize = 34;               // Indicates that Format is part of a 
                                                  // WAVEFORMATEXTENSIBLE_IEC61937 structure.
wfext.FormatExt.Samples.wValidBitsPerSample = 16;
wfext.FormatExt.dwChannelMask = KSAUDIO_SPEAKER_5POINT1;    // 5.1 Surround.
wfext.FormatExt.SubFormat = KSDATAFORMAT_SUBTYPE_IEC61937_WMA_PRO;
wfext.dwEncodedSamplesPerSec = 96000;                       // Sample rate of encoded content.
wfext.dwEncodedChannelCount = 6;                            // Encoded data contains 6 channels.
wfext.dwAverageBytesPerSec = 0;                             // Ignored for this format.
```



## Related topics

<dl> <dt>

[Device Formats](device-formats.md)
</dt> </dl>

 

 




