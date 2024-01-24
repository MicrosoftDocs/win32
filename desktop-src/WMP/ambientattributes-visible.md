---
title: AmbientAttributes.visible
description: The visible attribute specifies or retrieves the visibility for the control.
ms.assetid: 8347d42a-4af1-4ea1-b968-a2ae58278430
keywords:
- AmbientAttributes.visible Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.visible
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.visible

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **visible** attribute specifies or retrieves the visibility for the control.

``` syntax
        elementID.visible
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                      |
|-------|----------------------------------|
| true  | Default. The control is visible. |
| false | The control is not visible.      |



 

## Remarks

This attribute is useful for hiding controls, for example when swapping a pause button for a play button.

If the value is false, the control is not visible and click events are passed to the control behind it. If the value is true, the control is visible and receives the click event itself.

The default value for the **AUTOMENU** element is false.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





