---
title: event.screenWidth
description: The screenWidth attribute retrieves the width of the available screen size in pixels.
ms.assetid: 613defdd-3644-4bf1-a0aa-93431d3bb35a
keywords:
- event.screenWidth Windows Media Player
topic_type:
- apiref
api_name:
- event.screenWidth
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# event.screenWidth

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **screenWidth** attribute retrieves the width of the available screen size in pixels.

``` syntax
event.screenWidth
```

## Possible Values

This attribute is a read-only **Number** (**long**).

## Remarks

This is useful for determining the amount of space there is in the monitor. If there are two monitors, it calculates the space for both monitors.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Ambient Event Attributes**](ambient-event-attributes.md)
</dt> <dt>

[**event.screenHeight**](event-screenheight.md)
</dt> </dl>

 

 





