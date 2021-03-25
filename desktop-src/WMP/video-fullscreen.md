---
title: VIDEO.fullScreen
description: The fullScreen attribute specifies or retrieves a value indicating whether the video is displayed in full-screen mode.
ms.assetid: de74d95a-31a2-4f65-811c-4e8018ee484a
keywords:
- VIDEO.fullScreen Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.fullScreen
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VIDEO.fullScreen

The **fullScreen** attribute specifies or retrieves a value indicating whether the video is displayed in full-screen mode.

``` syntax
        elementID.fullScreen
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                          |
|-------|------------------------------------------------------|
| true  | Video displays in full-screen mode.                  |
| false | Default. Video does not display in full-screen mode. |



 

## Remarks

This property can be specified only at run time, after a file has been loaded. It must therefore be set within a script event handler. The escape button is used to return to normal viewing.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIDEO Element**](video-element.md)
</dt> <dt>

[**VIDEO.maintainAspectRatio**](video-maintainaspectratio.md)
</dt> <dt>

[**VIDEO.shrinkToFit**](video-shrinktofit.md)
</dt> <dt>

[**VIDEO.stretchToFit**](video-stretchtofit.md)
</dt> </dl>

 

 





