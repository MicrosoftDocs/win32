---
title: TEXT.justification
description: The justification attribute specifies or retrieves the alignment of the text within the Text control.
ms.assetid: 72086142-198b-41cf-ad84-733fa23f9efe
keywords:
- TEXT.justification Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.justification
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.justification

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **justification** attribute specifies or retrieves the alignment of the text within the Text control.

``` syntax
        elementID.justification
```

## Possible Values

This attribute is a read/write **String**.



| Value  | Description                                                   |
|--------|---------------------------------------------------------------|
| Left   | Default. Aligns the text to the left of the Text control.     |
| Right  | Aligns the text to the right of the Text control.             |
| Center | Aligns the text to the horizontal center of the Text control. |



 

## Remarks

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> </dl>

 

 





