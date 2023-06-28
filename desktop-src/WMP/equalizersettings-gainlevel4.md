---
title: EQUALIZERSETTINGS.gainLevel4
description: The gainLevel4 attribute specifies or retrieves the gain level of band 4.
ms.assetid: 01383171-f991-4d09-858a-ce21ce93e14e
keywords:
- EQUALIZERSETTINGS.gainLevel4 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel4
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.gainLevel4

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **gainLevel4** attribute specifies or retrieves the gain level of band 4.

``` syntax
        elementID.gainLevel4
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 250Hz.

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

 

 





