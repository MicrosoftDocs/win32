---
description: Windows Portable Devices supports the following audio properties.
ms.assetid: 5d6c6a95-abb7-4191-a961-bcb30ca96bb6
title: Audio Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Audio
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Audio Properties

Windows Portable Devices supports the following audio properties.



| Property                         | VarType     | Description                                                                                                                                                                                                        |
|----------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_AUDIO\_BIT\_DEPTH**       | **VT\_UI4** | The bit-depth of the audio.                                                                                                                                                                                        |
| **WPD\_AUDIO\_BITRATE**          | **VT\_UI4** | The bit rate of the audio, in bits per second.                                                                                                                                                                     |
| **WPD\_AUDIO\_BLOCK\_ALIGNMENT** | **VT\_UI4** | The block alignment of the audio file, in bytes.                                                                                                                                                                   |
| **WPD\_AUDIO\_CHANNEL\_COUNT**   | **VT\_R4**  | The number of channels in this audio file, for example, 1, 2, or 5.1.                                                                                                                                              |
| **WPD_AUDIO_FORMAT_CODE**     | **VT\_UI4** | The registered WAVE format code number. For a listing of registered WAVE formats, see the article [Extensible wave-format descriptors](/windows-hardware/drivers/audio/extensible-wave-format-descriptors). |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




