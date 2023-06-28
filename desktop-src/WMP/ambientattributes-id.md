---
title: AmbientAttributes.id
description: The id attribute specifies or retrieves the identifier of a control. This attribute will support any name permitted by Microsoft Visual Basic for Applications. Can only be set at design time.
ms.assetid: a1e8d493-ac11-46a0-9b79-18270d188427
keywords:
- AmbientAttributes.id Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.id
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.id

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **id** attribute specifies or retrieves the identifier of a control. This attribute will support any name permitted by Microsoft Visual Basic for Applications. Can only be set at design time.

``` syntax
        elementID.id
```

## Possible Values

This attribute is a **String** specified at design time and read-only thereafter. It has a default value of

Unnamed\_*elementtype*\_*num*

where *elementtype* is the name of the control type, and *num* is a number corresponding to the position of the control in the sequence of all unnamed controls in the Theme. This number is reset to zero for each new Theme.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





