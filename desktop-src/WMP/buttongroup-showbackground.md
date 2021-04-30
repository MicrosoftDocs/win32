---
title: BUTTONGROUP.showBackground
description: The showBackground attribute specifies or retrieves a value indicating whether the BUTTONGROUP displays only the buttons, or displays the full bitmap specified in the image attribute.
ms.assetid: 5c3fc873-937c-4dad-ac18-e7a37004ee1e
keywords:
- BUTTONGROUP.showBackground Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.showBackground
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONGROUP.showBackground

The **showBackground** attribute specifies or retrieves a value indicating whether the **BUTTONGROUP** displays only the buttons, or displays the full bitmap specified in the **image** attribute.

``` syntax
        elementID.showBackground
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                                                                |
|-------|--------------------------------------------------------------------------------------------|
| true  | Buttons are displayed and the area not occupied by buttons is drawn from the Image bitmap. |
| false | Default. Only the buttons are displayed.                                                   |



 

## Remarks

When **showBackground** is true, the entire main **image** will be visible.

When **showBackground** is false, only the areas corresponding to assigned **mappingImage** colors will be rendered. In other words, only **BUTTONELEMENTs** with their **mappingColor** assigned will be visible.

If an invalid value is specified, the previous state is maintained.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> <dt>

[**BUTTONELEMENT.mappingColor**](buttonelement-mappingcolor.md)
</dt> <dt>

[**BUTTONGROUP.image**](buttongroup-image.md)
</dt> <dt>

[**BUTTONGROUP.mappingImage**](buttongroup-mappingimage.md)
</dt> </dl>

 

 





