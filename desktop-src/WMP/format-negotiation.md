---
title: Format Negotiation
description: Format Negotiation
ms.assetid: 7847d4e3-1250-4c35-88e1-52d61bf1553f
keywords:
- Windows Media Player plug-ins,format negotiation
- plug-ins,format negotiation
- digital signal processing plug-ins,format negotiation
- DSP plug-ins,format negotiation
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Format Negotiation

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

For Windows Media Player and a DSP plug-in to share data, both programs must agree on the format of the data they are processing. The DSP plug-in implements methods that the Player calls to determine which formats the plug-in supports. The plug-in also implements methods that the Player calls to set the current format.

If the plug-in is acting as a DirextX Media Object (DMO), Windows Media Player discovers and sets media formats by calling methods of the **IMediaObject** interface. For example, the Player calls the plug-in's **IMediaObject::GetInputType** repeatedly to get a list of all input formats supported by the plug-in. DMO plug-ins use the **DMO\_MEDIA\_TYPE** structure to organize the information that specifies a media format. For more information about how DMO plug-ins and the Player negotiate format, see [About IMediaObject](about-imediaobject.md).

If the plug-in is acting as a Media Foundation Transform (MFT), Windows Media Player discovers and sets media formats by calling methods of the **IMFTransform** interface. For example, the Player calls the plug-in's **IMFTransform::GetInputAvailableType** repeatedly to get a list of all input formats supported by the plug-in. MFT plug-ins and the Player use the **IMFMediaType** interface to organize and exchange format information.

Windows Media Player will use an audio DSP plug-in only if the plug-in supports the same bit depth as the digital audio being played. For instance, if the digital audio is 20-bit, the plug-in must be written to process 20-bit audio. For CD audio, DSP plug-ins must support 20-bit processing.

During format negotiation of multi-channel content on a computer configured for use with stereo speakers, Windows Media Player first attempts to connect to an audio DSP plug-in using the existing input and output format by calling **IMediaObject::SetInputType** and **IMediaObject::SetOutputType**. Once this initial negotiation occurs, the Player then enumerates the formats the plug-in supports and attempts to negotiate the best format combination for the Player and the plug-in. If the plug-in accepts stereo audio (defined by a **WAVEFORMATEX** structure) as the input format during the initial negotiation, and then subsequently accepts only multi-channel audio (defined by a **WAVEFORMATEXTENSIBLE** structure), the Player will provide multi-channel audio as the input format to the plug-in. This behavior during format negotiation is available for use in the Microsoft Windows XP operating system. It may be altered or unavailable in subsequent versions.

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> </dl>

 

 




