---
title: event.button
description: The button attribute retrieves a value indicating which mouse buttons were down when the event occurred.
ms.assetid: 58fb1522-9946-4942-b4bf-4cff37f7dbaf
keywords:
- event.button Windows Media Player
topic_type:
- apiref
api_name:
- event.button
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# event.button

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **button** attribute retrieves a value indicating which mouse buttons were down when the event occurred.

``` syntax
event.button
```

## Possible Values

This attribute is a read-only **Number** (**long**).



| Value | Description                      |
|-------|----------------------------------|
| 0     | No mouse buttons were down.      |
| 1     | The left mouse button was down.  |
| 2     | The right mouse button was down. |
| 3     | Both mouse buttons were down.    |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Event Attributes**](ambient-event-attributes.md)
</dt> </dl>

 

 





