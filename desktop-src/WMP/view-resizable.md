---
title: VIEW.resizable
description: The resizable attribute retrieves a value indicating whether the VIEW can be resized.
ms.assetid: 4f0e4f31-cf16-498f-823f-da43566043b1
keywords:
- VIEW.resizable Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.resizable
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.resizable

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **resizable** attribute retrieves a value indicating whether the **VIEW** can be resized.

``` syntax
        elementID.resizable
```

## Possible Values

This attribute is a read-only **Boolean** with a default value equal to the **titlebar** attribute.



| Values | Description             |
|--------|-------------------------|
| true   | View can be resized.    |
| false  | View cannot be resized. |



 

## Remarks

If there is no **titlebar**, and therefore no window or border, you must use the **size** method to resize the **VIEW** element.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





