---
title: attribute_onchange
description: When a skin attribute changes value, an event occurs that can be handled by an event handler. The name of the event handler is the name of the attribute followed by an underscore and \ 0034;onchange \ 0034;, such as \ 0034;value\_onchange \ 0034;.
ms.assetid: 783b686c-d56c-4036-9af4-97b9b246ef7e
keywords:
- attribute_onchange Windows Media Player
topic_type:
- apiref
api_name:
- attribute_onchange
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# attribute\_onchange

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When a skin attribute changes value, an event occurs that can be handled by an event handler. The name of the event handler is the name of the attribute followed by an underscore and "onchange", such as "value\_onchange".

``` syntax
        attribute_onchange
```

## Examples


```JScript
<SLIDER 
  thumbImage = "thumb.gif"
  value_onchange = "JScript: if (value == 100) backgroundColor = 'green';"
/>

```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------|
| Version<br/> | Windows Media Player version 70 or later<br/> |



## See also

<dl> <dt>

[**Ambient Event Handlers**](ambient-event-handlers.md)
</dt> </dl>

 

 





