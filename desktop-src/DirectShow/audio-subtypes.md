---
description: The following tables list media subtype GUIDs for audio. Where applicable, each table lists the equivalent format tag, declared in Mmreg.h.
ms.assetid: 55012be5-2d61-4d38-aab7-0c42f161f555
title: Audio Subtypes
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio Subtypes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following tables list media subtype GUIDs for audio. Where applicable, each table lists the equivalent format tag, declared in Mmreg.h.

## Uncompressed Audio Types



| GUID                          | Description                | Header  | Equivalent Format Tag                  |
|-------------------------------|----------------------------|---------|----------------------------------------|
| **MEDIASUBTYPE\_IEEE\_FLOAT** | IEEE floating-point audio. | uuids.h | **WAVE\_FORMAT\_IEEE\_FLOAT** (0x0003) |
| **MEDIASUBTYPE\_PCM**         | PCM audio.                 | uuids.h | **WAVE\_FORMAT\_PCM** (0x0001)         |



 

## MPEG-4 and AAC Audio Types



| GUID                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Header       | Equivalent Format Tag                      |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------------------------------------|
| **MEDIASUBTYPE\_MPEG\_ADTS\_AAC** | Advanced Audio Coding (AAC) audio in Audio Data Transport Stream (ADTS) format.<br/> The format block is a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure with **wFormatTag** equal to **WAVE\_FORMAT\_MPEG\_ADTS\_AAC**.<br/> The [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure specifies the core AAC-LC sample rate and number of channels, prior to applying spectral band replication (SBR) or parametric stereo (PS) tools, if present.<br/> No additional data is required after the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure.<br/>                                                                                                                                                                 | wmcodecdsp.h | **WAVE\_FORMAT\_MPEG\_ADTS\_AAC** (0x1600) |
| **MEDIASUBTYPE\_MPEG\_HEAAC**     | High-Efficiency Advanced Audio Coding (HE-AAC) stream.<br/> The format block is an [**HEAACWAVEFORMAT**](/windows/win32/api/mmreg/ns-mmreg-heaacwaveformat) structure.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | wmcodecdsp.h | **WAVE\_FORMAT\_MPEG\_HEAAC** (0x1610)     |
| **MEDIASUBTYPE\_MPEG\_LOAS**      | MPEG-4 audio transport stream with a synchronization layer (LOAS) and a multiplex layer (LATM).<br/> The format block is a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure with **wFormatTag** equal to **WAVE\_FORMAT\_MPEG\_LOAS**.<br/> The [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure specifies the core AAC-LC sample rate and number of channels, prior to applying spectral SBR or PS tools, if present.<br/> No additional data is required after the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure.<br/>                                                                                                                                                                                             | wmcodecdsp.h | **WAVE\_FORMAT\_MPEG\_LOAS** (0x1602)      |
| **MEDIASUBTYPE\_RAW\_AAC1**       | Raw AAC.<br/> The format block is a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure with **wFormatTag** equal to **WAVE\_FORMAT\_RAW\_AAC1**.<br/> The [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure specifies the sample rate and number of channels in the decoded audio after applying SBR and PS tools, if present.<br/> The [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure is followed by additional bytes that contain the AudioSpecificConfig() data, as defined by ISO/IEC 14496-3 (MPEG-4 Audio). <br/> The length of the AudioSpecificConfig() data is 2 bytes for AAC-LC or HE-AAC with implicit signaling of SBR/PS. It is more than 2 bytes for HE-AAC with explicit signaling of SBR/PS.<br/> | wmcodecdps.h | **WAVE\_FORMAT\_RAW\_AAC1** (0x00FF)       |



 

## Dolby Audio Types



| GUID                                | Description                                                                                                                                                                                                             | Header       | Equivalent Format Tag                        |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|----------------------------------------------|
| **MEDIASUBTYPE\_DOLBY\_DDPLUS**     | Dolby Digital Plus audio.                                                                                                                                                                                               | wmcodecdsp.h | n/a                                          |
| **MEDIASUBTYPE\_DOLBY\_AC3**        | Dolby Digital (AC-3) audio.                                                                                                                                                                                             | ksuuids.h    | n/a                                          |
| **MEDIASUBTYPE\_DOLBY\_AC3\_SPDIF** | Dolby AC-3 over S/PDIF.                                                                                                                                                                                                 | uuids.h      | **WAVE\_FORMAT\_DOLBY\_AC3\_SPDIF** (0x0092) |
| **MEDIASUBTYPE\_DVM**               | DVM AC-3 codec. Used when playing an AVI files with Dolby Digital audio.<br/> The format block is a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure with the format tag equal to **WAVE\_FORMAT\_DVM**.<br/> | wmcodecdsp.h | **WAVE\_FORMAT\_DVM** (0x2000)               |
| **MEDIASUBTYPE\_RAW\_SPORT**        | AC-3 over S/PDIF; see Remarks.                                                                                                                                                                                          | uuids.h      | **WAVE\_FORMAT\_RAW\_SPORT** (0x0240)        |
| **MEDIASUBTYPE\_SPDIF\_TAG\_241h**  | AC-3 over S/PDIF; see Remarks.                                                                                                                                                                                          | uuids.h      | **WAVE\_FORMAT\_ESST\_AC3** (0x0241)         |



 

To specify padded AC-3, use the subtype **MEDIASUBTYPE\_DOLBY\_AC3\_SPDIF**, which corresponds to a format tag of 0x0092 (WAVE\_FORMAT\_DOLBY\_AC3\_SPDIF). The values 0x240 and 0x241 have also been used to indicate padded AC-3, but Microsoft encourages the use of 0x0092.

## Miscellaneous Audio Types



| GUID                                | Description                                                                                                                                                                                                                                                                          | Header       | Equivalent Format Tag           |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------|
| **MEDIASUBTYPE\_DRM\_Audio**        | Audio with digital rights management (DRM) protection.                                                                                                                                                                                                                               | uuids.h      | **WAVE\_FORMAT\_DRM** (0x0009)  |
| **MEDIASUBTYPE\_DTS**               | Digital Theater Systems (DTS) audio.<br/> The format block is a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure with the format tag equal to **WAVE\_FORMAT\_UNKNOWN**.<br/>                                                                                              | ksuuids.h    | n/a                             |
| **MEDIASUBTYPE\_DTS2**              | Digital Theater Systems (DTS) audio.<br/> The format block is a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure with the format tag equal to **WAVE\_FORMAT\_DTS2**.<br/> This subtype is equivalent to **MEDIASUBTYPE\_DTS** but uses a different format tag.<br/> | wmcodecdsp.h | **WAVE\_FORMAT\_DTS2** (0x2001) |
| **MEDIASUBTYPE\_DVD\_LPCM\_AUDIO**  | DVD audio data.                                                                                                                                                                                                                                                                      | ksuuids.h    | n/a                             |
| **MEDIASUBTYPE\_MPEG1AudioPayload** | MPEG-1 audio payload.                                                                                                                                                                                                                                                                | uuids.h      | **WAVE\_FORMAT\_MPEG** (0x0050) |
| **MEDIASUBTYPE\_MPEG1Packet**       | MPEG1 audio packet.                                                                                                                                                                                                                                                                  | uuids.h      | n/a                             |
| **MEDIASUBTYPE\_MPEG1Payload**      | MPEG1 audio Payload.                                                                                                                                                                                                                                                                 | uuids.h      | n/a                             |
| **MEDIASUBTYPE\_MPEG2\_AUDIO**      | MPEG-2 audio data.                                                                                                                                                                                                                                                                   | ksuuids.h    | n/a                             |



 

## Audio Format Tags

The **wFormatTag** field in the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure specifies the audio format type. Media samples are generally whole number of samples as specified in the **wBitsPerSample** field in the **WAVEFORMATEX** structure. This is not necessarily true for MPEG audio samples that can come from packetized streams and are therefore not necessarily packaged on sample / frame boundaries. For MPEG audio the time stamp in a media sample is the time stamp for the first frame whose first byte is contained in the media sample.

Media subtypes are defined for each **wFormatTag** as follows:

-   The Data1 subfield of the subtype GUID is the same as the **wFormatTag** value.
-   The Data 2 field is 0.
-   The Data 3 field is 0x0010.
-   The Data 4 field is 0x80, 0x00, 0x00, 0xAA, 0x00, 0x38, 0x9B, 0x71.

Thus, for PCM audio the subtype GUID (defined in uuids.h as **MEDIASUBTYPE\_PCM**) is:

`{00000001-0000-0010-8000-00AA00389B71}`

The [**CreateAudioMediaType**](createaudiomediatype.md) function can be used to create an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure from a **WAVEFORMATEX** structure.

## Obsolete Audio Types

The following audio subtypes are obsolete and should not be used:

-   **MEDIASUBTYPE\_MPEG\_RAW\_AAC**
-   **MEDIASUBTYPE\_PCMAudioObsolete**

## See also

<dl> <dt>

[**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type)
</dt> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

