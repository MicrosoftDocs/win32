---
title: AmbientAttributes.accDescription
description: The accDescription attribute specifies or retrieves a description for any element.
ms.assetid: 660d886d-5dd2-4f7d-b343-6d9c7c8f8389
keywords:
- AmbientAttributes.accDescription Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.accDescription
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.accDescription

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **accDescription** attribute specifies or retrieves a description for any element.

``` syntax
        elementID.accDescription
```

## Possible Values

This attribute is a read/write **String** with a default value of "" (empty string).

## Remarks

This attribute is used for accessibility purposes. It allows the description of any element to be read aloud by a reader program.

This attribute also applies to button elements inside the button group control.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





