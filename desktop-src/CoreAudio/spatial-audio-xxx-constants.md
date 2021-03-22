---
description: The SPATIAL\_AUDIO\_XXX constants define values related to spatial sound features.
ms.assetid: F1A01BDB-0CC2-45ED-A423-8CC7F54D4E55
title: SPATIAL_AUDIO_XXX Constants (SpatialAudioMetadata.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SPATIAL\_AUDIO\_XXX Constants

The SPATIAL\_AUDIO\_XXX constants define values related to spatial sound features.



| Constant/value                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                     |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SPATIAL_AUDIO_POSITION"></span><span id="spatial_audio_position"></span><dl> <dt>**SPATIAL\_AUDIO\_POSITION**</dt> <dt>200</dt> </dl>                                                   | A standard Microsoft-defined spatial audio metadata command which represents the listener position in the standard model used by [**ISpatialAudioClient**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient) where the listener's head is position at coordinates (0,0,0), defined in meters.<br/> |
| <span id="SPATIAL_AUDIO_POSITION_BYTE_COUNT"></span><span id="spatial_audio_position_byte_count"></span><dl> <dt>**SPATIAL\_AUDIO\_POSITION\_BYTE\_COUNT**</dt> <dt>sizeof(float) \* 3</dt> </dl> | Specifies the size of the **SPATIAL\_AUDIO\_POSITION** value.<br/>                                                                                                                                                                                                        |
| <span id="SPATIAL_AUDIO_STANDARD_COMMANDS_START"></span><span id="spatial_audio_standard_commands_start"></span><dl> <dt>**SPATIAL\_AUDIO\_STANDARD\_COMMANDS\_START**</dt> <dt>200</dt> </dl>    | Specifies the start of the range of Microsoft-reserved spatial audio metadata commands. Custom metadata commands are restricted to command IDs 0 - 199. Commands 200 - 255 are reserved for Microsoft use.<br/>                                                           |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>SpatialAudioMetadata.h</dt> </dl> |



 

 




