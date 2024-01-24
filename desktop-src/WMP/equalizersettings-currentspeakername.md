---
title: EQUALIZERSETTINGS.currentSpeakerName
description: The currentSpeakerName attribute retrieves the name of the current speaker setting.
ms.assetid: 22a7fb76-1345-42b1-9b6b-ef36dfb027bd
keywords:
- EQUALIZERSETTINGS.currentSpeakerName Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.currentSpeakerName
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.currentSpeakerName

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **currentSpeakerName** attribute retrieves the name of the current speaker setting.

``` syntax
        elementID.currentSpeakerName
```

## Possible Values

This attribute is a read-only **String** containing one of the following values.



| Value           | Description                              |
|-----------------|------------------------------------------|
| Headphones      | The current speakers are headphones.     |
| Normal Speakers | The current speakers are of normal size. |
| Large Speakers  | The current speakers are large.          |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.speakerSize**](equalizersettings-speakersize.md)
</dt> </dl>

 

 





