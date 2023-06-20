---
title: AmbientAttributes.accName
description: The accName attribute specifies or retrieves a name for any element.
ms.assetid: 4cb453c9-1b5b-4bd9-8ae4-6d4bccc45562
keywords:
- AmbientAttributes.accName Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.accName
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.accName

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **accName** attribute specifies or retrieves a name for any element.

``` syntax
        elementID.accName
```

## Possible Values

This attribute is a read/write **String** with a default value equal to the **id** attribute.

## Remarks

This attribute is used for accessibility purposes. It allows the name of any element to be read aloud by a reader program.

This attribute also applies to button elements inside a button group control.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





