---
title: EQUALIZERSETTINGS.speakerSize
description: The speakerSize attribute specifies or retrieves the index number of the current speaker size.
ms.assetid: 454d07bf-49cd-48a5-9724-6415a925367a
keywords:
- EQUALIZERSETTINGS.speakerSize Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.speakerSize
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.speakerSize

The **speakerSize** attribute specifies or retrieves the index number of the current speaker size.

``` syntax
        elementID.speakerSize
```

## Possible Values

This attribute is a read/write **Number** (long) containing one of the following values.



| Value | Description                              |
|-------|------------------------------------------|
| 0     | The current speakers are headphones.     |
| 1     | The current speakers are of normal size. |
| 2     | The current speakers are large.          |



 

## Remarks

The friendly name of the speaker size can be retrieved using the **currentSpeakerName** attribute.

This attribute is ignored if **enhancedAudio** is set to false.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.currentSpeakerName**](equalizersettings-currentspeakername.md)
</dt> <dt>

[**EQUALIZERSETTINGS.enhancedAudio**](equalizersettings-enhancedaudio.md)
</dt> </dl>

 

 





