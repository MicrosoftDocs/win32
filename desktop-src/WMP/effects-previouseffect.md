---
title: EFFECTS.previousEffect
description: The previousEffect method displays the previous visualization, skipping presets.
ms.assetid: f1cfef29-0241-4028-b047-4f17bf0e9250
keywords:
- EFFECTS.previousEffect Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.previousEffect
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# EFFECTS.previousEffect

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **previousEffect** method displays the previous visualization, skipping presets.

``` syntax
        elementID.previousEffect()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Remarks

This method displays the previous visualization in the authoring order. If the current visualization is the first in the authoring order, and if **allowAll** is false, the last visualization is made current.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> <dt>

[**EFFECTS.nextEffect**](effects-nexteffect.md)
</dt> <dt>

[**EFFECTS.allowAll**](effects-allowall.md)
</dt> </dl>

 

 





