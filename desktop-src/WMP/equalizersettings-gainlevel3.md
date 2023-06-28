---
title: EQUALIZERSETTINGS.gainLevel3
description: The gainLevel3 attribute specifies or retrieves the gain level of band 3.
ms.assetid: 508d00c6-2429-4f35-b7ab-bf30f774e614
keywords:
- EQUALIZERSETTINGS.gainLevel3 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel3
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.gainLevel3

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **gainLevel3** attribute specifies or retrieves the gain level of band 3.

``` syntax
        elementID.gainLevel3
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 125Hz.

If this attribute is not specified, the previous value will be retained.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS. gainLevels**](equalizersettings-gainlevels.md)
</dt> </dl>

 

 





