---
title: EFFECTS.allowAll
description: The allowAll attribute specifies or retrieves a value indicating whether to include all the visualizations that are in the registry.
ms.assetid: 8552cc06-05b2-4049-ba7d-f6bd770449e0
keywords:
- EFFECTS.allowAll Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.allowAll
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EFFECTS.allowAll

The **allowAll** attribute specifies or retrieves a value indicating whether to include all the visualizations that are in the registry.

``` syntax
        elementID.allowAll
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                                         |
|-------|---------------------------------------------------------------------|
| true  | Default. Allows cycling of all visualizations on the user's system. |
| false | Limits cycling to visualizations appearing within **EFFECTS** tags. |



 

## Remarks

If this attribute is set to false, only the visualizations appearing within **EFFECTS** tags can be cycled through using previous/next. If it is set to true, then all visualizations that are registered on the user's system can be cycled through. If it is set to true and you specify any visualizations within **EFFECTS** tags, then the attributes specified in these tags are applied to all visualizations on the user's system.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> </dl>

 

 





