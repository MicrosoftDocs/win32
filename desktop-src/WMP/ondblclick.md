---
title: ondblclick
description: The ondblclick event handler handles an event that occurs when the user double-clicks the element.
ms.assetid: 36183f66-79f6-4748-ad2d-af433a5986dd
keywords:
- ondblclick Windows Media Player
topic_type:
- apiref
api_name:
- ondblclick
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# ondblclick

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ondblclick** event handler handles an event that occurs when the user double-clicks the element.

``` syntax
ondblclick
```

## Remarks

This event handler is not applicable to the **PLAYLIST** element, the **POPUP** element, the **VIDEO** element when *VIDEO*.**windowless** is false, or the **EFFECTS** element when *EFFECTS*.**windowed** is true.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------|
| Version<br/> | Windows Media Player version 70 or later<br/> |



## See also

<dl> <dt>

[**Ambient Event Handlers**](ambient-event-handlers.md)
</dt> </dl>

 

 





