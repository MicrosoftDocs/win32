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
ms.date: 05/31/2018
---

# VIEW.titleBar

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

 

 





