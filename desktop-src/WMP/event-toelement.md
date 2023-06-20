---
title: event.toElement
description: The toElement attribute retrieves the element that the keyboard focus moved to. This attribute only applies to the onblur event; for all other events, its value is NULL.
ms.assetid: 05d15001-2f07-421b-b66f-ea9f46a130a2
keywords:
- event.toElement Windows Media Player
topic_type:
- apiref
api_name:
- event.toElement
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# event.toElement

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **toElement** attribute retrieves the element that the keyboard focus moved to. This attribute only applies to the **onblur** event; for all other events, its value is **NULL**.

``` syntax
event.toElement
```

## Possible Values

This attribute is a read-only object.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Event Attributes**](ambient-event-attributes.md)
</dt> </dl>

 

 





