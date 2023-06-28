---
description: When the DVD Navigator filter goes into karaoke mode, it informs the audio decoder through the AM\_PROPERTY\_DVDKARAOKE\_ENABLE property.
ms.assetid: 78b2998b-d8b3-424d-85bc-872e64eb4a4f
title: DVD Karaoke Property Set (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Karaoke Property Set

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When the [DVD Navigator](dvd-navigator-filter.md) filter goes into karaoke mode, it informs the audio decoder through the **AM\_PROPERTY\_DVDKARAOKE\_ENABLE** property. The decoder should then mute audio channels 2 through 5 until it receives from the DVD Navigator an **AM\_PROPERTY\_DVDKARAOKE\_DATA** property with a pointer to an [**AM\_DvdKaraokeData**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-am_dvdkaraokedata) data structure indicating how the auxiliary channels are to be mixed.



| Label | Value |
|-------------------|-----------------------------|
| Property Set GUID | AM\_KSPROPSETID\_DvdKaraoke |



 



| Property ID                      | Description                                                                                                                                                                                                                                                                                                 |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AM\_PROPERTY\_DVDKARAOKE\_ENABLE | BOOLEAN value. The DVD Navigator sends the decoder an AM\_PROPERTY\_DVDKARAOKE\_ENABLE with a value of **TRUE** to enable karaoke downmixing or **FALSE** to disable it.                                                                                                                                    |
| AM\_PROPERTY\_DVDKARAOKE\_DATA   | The DVD Navigator sends the decoder an AM\_PROPERTY\_DVDKARAOKE\_DATA property with a pointer to an [**AM\_DvdKaraokeData**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-am_dvdkaraokedata) structure to change the downmix configuration; that is, to turn certain karaoke channels on or off and direct them to the right or left output channel. |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 




