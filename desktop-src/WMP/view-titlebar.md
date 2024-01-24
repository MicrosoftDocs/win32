---
title: VIEW.titleBar
description: The titleBar attribute retrieves a value indicating whether the window title bar is shown.
ms.assetid: 996aa2e0-0313-4a48-adcb-b82f76f38b6a
keywords:
- VIEW.titleBar Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.titleBar
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.titleBar

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **titleBar** attribute retrieves a value indicating whether the window title bar is shown.

``` syntax
        elementID.titleBar
```

## Possible Values

This attribute is a read-only **Boolean**.



| Value | Description                             |
|-------|-----------------------------------------|
| true  | Default. The window title bar is shown. |
| false | The window title bar is not shown.      |



 

## Remarks

If the title bar is shown, the control box, minimize, and close buttons will be shown. The title of the window will be the title of the **VIEW** element.

If **titleBar** is set to true and the user attempts to change the value of **Video.zoom**, the change will not take place unless the skin monitors **zoom** and takes appropriate action to resize itself.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**VIEW.title**](view-title.md)
</dt> <dt>

[**VIDEO.zoom**](video-zoom.md)
</dt> </dl>

 

 





