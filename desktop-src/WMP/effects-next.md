---
title: EFFECTS.next
description: The next method displays the next visualization preset, moving to the next visualization if necessary.
ms.assetid: c03c8697-7729-41fe-b8eb-83c33ca32043
keywords:
- EFFECTS.next Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.next
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EFFECTS.next

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **next** method displays the next visualization preset, moving to the next visualization if necessary.

``` syntax
        elementID.next()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Remarks

If the current preset is the last one in the series of all available visualizations, the first preset of the first visualization is made current.

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

 

 





