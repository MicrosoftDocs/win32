---
title: EQUALIZERSETTINGS.previousPreset
description: The previousPreset method applies the previous equalizer preset.
ms.assetid: 0b344e5f-fe0d-4a23-b204-8fea340a8e21
keywords:
- EQUALIZERSETTINGS.previousPreset Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.previousPreset
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.previousPreset

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **previousPreset** method applies the previous equalizer preset.

``` syntax
        elementID.previousPreset()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Remarks

If the current preset is the first one available, the last preset is made current.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.nextPreset**](equalizersettings-nextpreset.md)
</dt> </dl>

 

 





