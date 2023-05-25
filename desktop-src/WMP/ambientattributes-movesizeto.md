---
title: AmbientAttributes.moveSizeTo
description: The moveSizeTo method moves the control and specifies a new size for the control in the new location. The control moves and resizes in an animated fashion over the specified time period.
ms.assetid: 89e3bf16-a123-4fb1-8c24-bc22a978e7f6
keywords:
- AmbientAttributes.moveSizeTo Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.moveSizeTo
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.moveSizeTo

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **moveSizeTo** method moves the control and specifies a new size for the control in the new location. The control moves and resizes in an animated fashion over the specified time period.

``` syntax
        elementID.moveSizeTo(newX, newY, newWidth, newHeight, moveTime, fSlide)
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

<span id="newWidth"></span><span id="newwidth"></span><span id="NEWWIDTH"></span>*newWidth*
</dt> <dd>

**Number** (**long**) specifying the new value for the **width** attribute of the control.

</dd> <dt>

<span id="newHeight"></span><span id="newheight"></span><span id="NEWHEIGHT"></span>*newHeight*
</dt> <dd>

**Number** (**long**) specifying the new value for the **height** attribute of the control.

</dd> <dt>

<span id="moveTime"></span><span id="movetime"></span><span id="MOVETIME"></span>*moveTime*
</dt> <dd>

**Number** (**long**) specifying the time, in milliseconds, that it takes for the control to move to its new location.

</dd> <dt>

<span id="fSlide"></span><span id="fslide"></span><span id="FSLIDE"></span>*fSlide*
</dt> <dd>

**Boolean** specifying the type of motion created when moving the control.



| Value | Description                                                             |
|-------|-------------------------------------------------------------------------|
| true  | Motion is non-linear (sliding motion that accelerates and decelerates). |
| false | Motion is linear.                                                       |



 

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

The motion of the control can be linear or non-linear. Linear motion means the control moves at a constant speed to its new location, starting and stopping abruptly. When non-linear motion is specified, a sliding motion is created that accelerates from zero at the beginning of the motion and decelerates back to zero at the end, coming to a smooth stop.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.height**](ambientattributes-height.md)
</dt> <dt>

[**AmbientAttributes.left**](ambientattributes-left.md)
</dt> <dt>

[**AmbientAttributes.top**](ambientattributes-top.md)
</dt> <dt>

[**AmbientAttributes.width**](ambientattributes-width.md)
</dt> </dl>

 

 





