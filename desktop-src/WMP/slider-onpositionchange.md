---
title: SLIDER.onPositionChange
description: The onPositionChange event handler handles an event that occurs when the position of the slider changes as a result of the user clicking or dragging. | SLIDER.onPositionChange
ms.assetid: 'c18e9a49-9576-42ae-9f30-249c44d40f41'
keywords:
- SLIDER.onPositionChange Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.onPositionChange
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.onPositionChange

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **onPositionChange** event handler handles an event that occurs when the position of the slider changes as a result of the user clicking or dragging.

``` syntax
onPositionChange
```

## Remarks

If the position of the slider changes as a result of the **value** attribute being modified in script, this event is not fired. To accommodate this possibility, implement the **value\_onchange** event handler instead.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> </dl>

 

 





