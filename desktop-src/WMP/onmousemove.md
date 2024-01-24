---
title: onmousemove
description: The onmousemove event handler handles an event that occurs when the user moves the mouse pointer while it is over an element.
ms.assetid: 8c834593-c842-48db-862d-994922aad776
keywords:
- onmousemove Windows Media Player
topic_type:
- apiref
api_name:
- onmousemove
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# onmousemove

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **onmousemove** event handler handles an event that occurs when the user moves the mouse pointer while it is over an element.

``` syntax
onmousemove
```

## Remarks

This event handler is not applicable to the **PLAYLIST** element, the **VIDEO** element when *VIDEO*.**windowless** is false, or the **EFFECTS** element when *EFFECTS*.**windowed** is true.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------|
| Version<br/> | Windows Media Player version 70 or later<br/> |



## See also

<dl> <dt>

[**Ambient Event Handlers**](ambient-event-handlers.md)
</dt> </dl>

 

 





