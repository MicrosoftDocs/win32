---
title: AmbientAttributes.moveTo
description: The moveTo method moves the control to a new location at a linear speed.
ms.assetid: 8670aa7b-a5c1-4d93-9f48-452bc53e65e6
keywords:
- AmbientAttributes.moveTo Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.moveTo
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AmbientAttributes.moveTo

The **moveTo** method moves the control to a new location at a linear speed.

``` syntax
        elementID.moveTo(newLeft, newTop, time)
```

## Parameters

<dl> <dt>

<span id="newLeft"></span><span id="newleft"></span><span id="NEWLEFT"></span>*newLeft*
</dt> <dd>

**Number** (**long**) specifying the new value for the **left** attribute of the control.

</dd> <dt>

<span id="newTop"></span><span id="newtop"></span><span id="NEWTOP"></span>*newTop*
</dt> <dd>

**Number** (**long**) specifying the new value for the **top** attribute of the control.

</dd> <dt>

<span id="time"></span><span id="TIME"></span>*time*
</dt> <dd>

**Number** (**long**) specifying the time, in milliseconds, that it takes for the control to move to its new location.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

This method is useful for animated **SUBVIEW** elements (for example, if the user clicks a tray and the controls slide down).

This method creates a linear motion when moving the control. This differs from **slideTo**, which creates a non-linear motion.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.left**](ambientattributes-left.md)
</dt> <dt>

[**AmbientAttributes.slideTo**](ambientattributes-slideto.md)
</dt> <dt>

[**AmbientAttributes.top**](ambientattributes-top.md)
</dt> </dl>

 

 





