---
title: AmbientAttributes.slideTo
description: The slideTo method moves the control to a new location. The control moves in a non-linear fashion over the specified time period.
ms.assetid: 06dd610b-cb58-4b60-9f4b-8929c54c3c33
keywords:
- AmbientAttributes.slideTo Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.slideTo
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AmbientAttributes.slideTo

The **slideTo** method moves the control to a new location. The control moves in a non-linear fashion over the specified time period.

``` syntax
        elementID.slideTo(newX, newY, moveTime)
```

## Parameters

<dl> <dt>

<span id="newX"></span><span id="newx"></span><span id="NEWX"></span>*newX*
</dt> <dd>

**Number** (**long**) specifying the new value for the **left** attribute of the control.

</dd> <dt>

<span id="newY"></span><span id="newy"></span><span id="NEWY"></span>*newY*
</dt> <dd>

**Number** (**long**) specifying the new value for the **top** attribute of the control.

</dd> <dt>

<span id="moveTime"></span><span id="movetime"></span><span id="MOVETIME"></span>*moveTime*
</dt> <dd>

**Number** (**long**) specifying the time, in milliseconds, that it takes for the control to move to its new location.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

This method is different from **moveTo**, which creates a linear motion when moving the control. The non-linear motion created by this method is a sliding motion that accelerates from a speed of zero at the beginning of the motion and decelerates back to zero at the end, coming to a smooth stop.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.left**](ambientattributes-left.md)
</dt> <dt>

[**AmbientAttributes.moveTo**](ambientattributes-moveto.md)
</dt> <dt>

[**AmbientAttributes.top**](ambientattributes-top.md)
</dt> </dl>

 

 





