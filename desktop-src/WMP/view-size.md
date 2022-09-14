---
title: VIEW.size
description: The size method resizes the VIEW on a specified edge.
ms.assetid: c15a33b2-3618-41a7-bff1-9d48a566ed4f
keywords:
- VIEW.size Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.size
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# VIEW.size

The **size** method resizes the **VIEW** on a specified edge.

``` syntax
        elementID.size(handle)
```

## Parameters

<dl> <dt>

<span id="handle"></span><span id="HANDLE"></span>*handle*
</dt> <dd>

String specifying the edge or corner to move when sizing. This string must have one of the following eight values.



| Edge   | Corner      |
|--------|-------------|
| top    | topright    |
| right  | bottomright |
| bottom | bottomleft  |
| left   | topleft     |



 

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

This method is typically called from within an **onmousedown** handler. It takes care of resizing while the mouse is dragged and stops resizing when the mouse button is released. If the size of the **VIEW** is restricted, you cannot drag the mouse to resize the **View** beyond the restricted bounds.

## Examples


```JScript
<THEME>
  <VIEW id="View1" backgroundImage="greenstone.bmp">
    <BUTTON id="sizer" horizontalAlignment="right" 
        verticalAlignment="bottom" image="Open.png" 
        onmousedown="jscript:View1.size('bottomright')">
    </BUTTON>
  </VIEW>
</THEME>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





