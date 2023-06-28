---
title: EFFECTS.effectTitle
description: The effectTitle method retrieves the display title of the visualization with the specified registry index.
ms.assetid: f3ea33f6-a8fc-4a18-993e-69b549fbea16
keywords:
- EFFECTS.effectTitle Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.effectTitle
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# EFFECTS.effectTitle

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **effectTitle** method retrieves the display title of the visualization with the specified registry index.

``` syntax
        elementID.effectTitle(index)
```

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number** (**long**) containing the registry index of a visualization.

</dd> </dl>

## Return Value

This method returns a **String**.

## Remarks

This method is used for displaying visualization titles in a user interface.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> <dt>

[**EFFECTS.currentEffectTitle**](effects-currenteffecttitle.md)
</dt> </dl>

 

 





