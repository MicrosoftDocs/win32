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
ms.date: 05/31/2018
---

# VIEW.resizeBackgroundImage

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

 

 





