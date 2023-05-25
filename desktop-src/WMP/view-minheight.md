---
title: VIEW.minHeight
description: The minHeight attribute specifies or retrieves the minimum height in pixels of the VIEW when resizing.
ms.assetid: e9a29642-e09d-40f8-9c2b-86be9f509089
keywords:
- VIEW.minHeight Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.minHeight
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.minHeight

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **minHeight** attribute specifies or retrieves the minimum height in pixels of the **VIEW** when resizing.

``` syntax
        elementID.minHeight
```

## Possible Values

This attribute is a read/write **Number** (**long**) with a value of zero or greater. It has a default value of zero, which means there is no restriction on the minimum height of the **VIEW**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**VIEW.maxHeight**](view-maxheight.md)
</dt> </dl>

 

 





