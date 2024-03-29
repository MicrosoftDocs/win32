---
title: EFFECTS.nextPreset
description: The nextPreset method displays the next preset of the current visualization.
ms.assetid: e17917c0-95b5-4799-8657-1f0d9bb7ec86
keywords:
- EFFECTS.nextPreset Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.nextPreset
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# EFFECTS.nextPreset

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **nextPreset** method displays the next preset of the current visualization.

``` syntax
        elementID.nextPreset()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Remarks

If the current preset is the last one in the list for the current visualization, the first preset is made current.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> <dt>

[**EFFECTS.allowAll**](effects-allowall.md)
</dt> <dt>

[**EFFECTS.previous**](effects-previous.md)
</dt> </dl>

 

 





