---
title: AmbientAttributes.passThrough
description: The passThrough attribute specifies or retrieves a value indicating whether the control will pass all mouse events through to the control under it.
ms.assetid: 907ae233-3421-4e80-84be-64db4a3ab654
keywords:
- AmbientAttributes.passThrough Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.passThrough
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.passThrough

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **passThrough** attribute specifies or retrieves a value indicating whether the control will pass all mouse events through to the control under it.

``` syntax
        elementID.passThrough
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                            |
|-------|--------------------------------------------------------|
| true  | Control passes events through to the control under it. |
| false | Default. Control does not pass events through.         |



 

## Remarks

This attribute is useful if, for example, a text control sits on top of a button control only to provide labeling. In this case, clicks on the text control must be passed through to the button control.

The **passThrough** attribute is not supported by the **VIEW**, **SUBVIEW**, and **PLAYLIST** elements. It will not work with the **VIDEO** element if *VIDEO*.**windowless** is set to false, nor with the **EFFECTS** element if *EFFECTS*.**windowed** is set to true.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





