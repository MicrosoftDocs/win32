---
title: EFFECTS.nextEffect
description: The nextEffect method displays the first preset of the next visualization, skipping intervening presets.
ms.assetid: dedd8e8b-2337-46f5-91a8-43ef54c86012
keywords:
- EFFECTS.nextEffect Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.nextEffect
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# EFFECTS.nextEffect

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **nextEffect** method displays the first preset of the next visualization, skipping intervening presets.

``` syntax
        elementID.nextEffect()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Remarks

This method displays the first preset of the next visualization in the authoring order. If the current visualization is the last in the authoring order, and if **allowAll** is false, the first visualization is made current.

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

[**EFFECTS.previousEffect**](effects-previouseffect.md)
</dt> </dl>

 

 





