---
title: SLIDER.useForegroundProgress
description: The useForegroundProgress attribute specifies or retrieves a value indicating whether the foreground progress bar will be used.
ms.assetid: 10f3b4d9-ba82-4e30-affa-50c15a809ed6
keywords:
- SLIDER.useForegroundProgress Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.useForegroundProgress
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.useForegroundProgress

The **useForegroundProgress** attribute specifies or retrieves a value indicating whether the foreground progress bar will be used.

``` syntax
        elementID.useForegroundProgress
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                              |
|-------|------------------------------------------|
| true  | Use foreground progress.                 |
| false | Default. Do not use foreground progress. |



 

## Remarks

This attribute allows the use of the **foregroundProgress** attribute, which is used primarily to track the download progress of a media file while simultaneously tracking the current play position of the file using the **value** attribute.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.foregroundProgress**](slider-foregroundprogress.md)
</dt> <dt>

[**SLIDER.value**](slider-value.md)
</dt> </dl>

 

 





