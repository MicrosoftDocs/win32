---
title: AmbientAttributes.enabled
description: The enabled attribute specifies or retrieves a value indicating whether the control is enabled or disabled.
ms.assetid: cf96ab7c-8acd-42b6-b7ca-d084a89c97e2
keywords:
- AmbientAttributes.enabled Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.enabled
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AmbientAttributes.enabled

The **enabled** attribute specifies or retrieves a value indicating whether the control is enabled or disabled.

``` syntax
        elementID.enabled
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description               |
|-------|---------------------------|
| true  | Default. Control enabled. |
| false | Control disabled.         |



 

## Remarks

If the control is enabled, it can have a tab stop, and will receive all ambient events. When disabled, the control does not have a tab stop, and does not receive any ambient mouse or keyboard events fired to it. (However, it will continue to receive all other ambient events fired to it.)

This attribute is not supported for the **SUBVIEW** element.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





