---
title: EQUALIZERSETTINGS.gainLevel8
description: The gainLevel8 attribute specifies or retrieves the gain level of band 8.
ms.assetid: 1cd4fa26-ed9b-4312-8272-9fe8011658e8
keywords:
- EQUALIZERSETTINGS.gainLevel8 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel8
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.gainLevel8

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **gainLevel8** attribute specifies or retrieves the gain level of band 8.

``` syntax
        elementID.gainLevel8
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 4kHz.

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

 

 





