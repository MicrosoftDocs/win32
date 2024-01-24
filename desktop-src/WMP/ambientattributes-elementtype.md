---
title: AmbientAttributes.elementType
description: The elementType attribute retrieves the type of the element (for instance, BUTTON).
ms.assetid: afff5a23-d981-4a60-b709-a5b926ea1fc3
keywords:
- AmbientAttributes.elementType Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.elementType
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.elementType

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **elementType** attribute retrieves the type of the element (for instance, BUTTON).

``` syntax
        elementID.elementType
```

## Possible Values

This attribute is a read-only **String** indicating the name of the element.

## Remarks

This attribute is useful in determining the type of element that fired an event and writing a generic event handler for this class of elements.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





