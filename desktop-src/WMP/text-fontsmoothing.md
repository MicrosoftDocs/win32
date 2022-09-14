---
title: TEXT.fontSmoothing
description: The fontSmoothing attribute specifies or retrieves a value indicating whether font smoothing is enabled.
ms.assetid: bd6f0468-285e-44b3-a5e8-361744c5ce4a
keywords:
- TEXT.fontSmoothing Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.fontSmoothing
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# TEXT.fontSmoothing

The **fontSmoothing** attribute specifies or retrieves a value indicating whether font smoothing is enabled.

``` syntax
        elementID.fontSmoothing
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                          |
|-------|--------------------------------------|
| true  | Font smoothing is enabled.           |
| false | Default. Font smoothing is disabled. |



 

## Remarks

Font smoothing uses the anti-aliasing feature of the operating system. If font smoothing is enabled and the operating system supports anti-aliasing, Windows Media Player attempts to smooth the text. Not all fonts support anti-aliasing. Windows Media Player 10 uses the Windows XP ClearType anti-aliasing method.

-   **Warning** Font smoothing over a transparent color may cause the transparent color to blend into the characters. It is not recommended that you use **fontSmoothing** if the text will display over a transparency.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> </dl>

 

 





