---
title: VIEW.resizeBackgroundImage
description: The resizeBackgroundImage attribute specifies or retrieves a value indicating whether the background image can be resized.
ms.assetid: d18f3def-777f-4a71-961e-73bae98a4c64
keywords:
- VIEW.resizeBackgroundImage Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.resizeBackgroundImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.resizeBackgroundImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **resizeBackgroundImage** attribute specifies or retrieves a value indicating whether the background image can be resized.

``` syntax
        elementID.resizeBackgroundImage
```

## Possible Values

This attribute is a read/write **Boolean**.



| Values | Description                                      |
|--------|--------------------------------------------------|
| true   | The background image can be resized.             |
| false  | Default. The background image cannot be resized. |



 

## Remarks

If you set this attribute to true, the background image will resize to fit the current values of the **width** and **height** attributes.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**VIEW.backgroundImage**](view-backgroundimage.md)
</dt> </dl>

 

 





