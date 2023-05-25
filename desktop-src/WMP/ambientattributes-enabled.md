---
title: AmbientAttributes.enabled
description: The enabled attribute specifies or retrieves a value indicating whether the control is enabled or disabled.
ms.assetid: cf96ab7c-8acd-42b6-b7ca-d084a89c97e2
keywords:
- AmbientAttributes.enabled Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.enabled
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.enabled

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **enabled** attribute specifies or retrieves a value indicating whether the control is enabled or disabled.

``` syntax
        elementID.enabled
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description               |
|-------|---------------------------|
| true  | Default. Control enabled. |
| false | Control disabled.         |



 

## Remarks

If the control is enabled, it can have a tab stop, and will receive all ambient events. When disabled, the control does not have a tab stop, and does not receive any ambient mouse or keyboard events fired to it. (However, it will continue to receive all other ambient events fired to it.)

This attribute is not supported for the **SUBVIEW** element.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





