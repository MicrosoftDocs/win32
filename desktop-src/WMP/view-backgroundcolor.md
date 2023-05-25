---
title: VIEW.backgroundColor
description: The backgroundColor attribute specifies or retrieves the background color of the VIEW or SUBVIEW.
ms.assetid: 02804e03-3518-4825-8ad0-bf91f74b5f74
keywords:
- VIEW.backgroundColor Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.backgroundColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.backgroundColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **backgroundColor** attribute specifies or retrieves the background color of the **VIEW** or **SUBVIEW**.

``` syntax
        elementID.backgroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value or the value "none". It has a default value of "white" for **VIEW** elements or "none" for **SUBVIEW** elements.

In a Windows Media Download package, if you specify the backgroundImage attribute for a **VIEW** element, then you must also specify the **backgroundColor** attribute for that element.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





