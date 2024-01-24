---
title: onclick
description: The onclick event handler handles an event that occurs when the user clicks the element.
ms.assetid: 59aa0038-b004-4dc3-849a-6015db764843
keywords:
- onclick Windows Media Player
topic_type:
- apiref
api_name:
- onclick
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# onclick

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **onclick** event handler handles an event that occurs when the user clicks the element.

``` syntax
onclick
```

## Remarks

This event handler is not applicable to the **PLAYLIST** element, the **POPUP** element, the **VIDEO** element, the **LISTBOX** element, when *VIDEO*.**windowless** is false, or the **EFFECTS** element when *EFFECTS*.**windowed** is true.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------|
| Version<br/> | Windows Media Player version 70 or later<br/> |



## See also

<dl> <dt>

[**Ambient Event Handlers**](ambient-event-handlers.md)
</dt> </dl>

 

 





