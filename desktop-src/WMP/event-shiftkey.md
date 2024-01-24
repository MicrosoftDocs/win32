---
title: event.shiftKey
description: The shiftKey attribute retrieves a value indicating whether the SHIFT key was down when the event occurred.
ms.assetid: 02b70533-936f-4543-8a36-88e7c2d1b2a8
keywords:
- event.shiftKey Windows Media Player
topic_type:
- apiref
api_name:
- event.shiftKey
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# event.shiftKey

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **shiftKey** attribute retrieves a value indicating whether the SHIFT key was down when the event occurred.

``` syntax
event.shiftKey
```

## Possible Values

This attribute is a read-only **Boolean**.



| Value | Description                                       |
|-------|---------------------------------------------------|
| true  | Indicates the SHIFT key was in the down position. |
| false | Indicates the SHIFT key was in the up position.   |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Event Attributes**](ambient-event-attributes.md)
</dt> </dl>

 

 





