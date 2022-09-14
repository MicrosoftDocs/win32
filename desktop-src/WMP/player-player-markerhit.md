---
title: Player.MarkerHit event
description: The MarkerHit event occurs when a marker is reached. | Player.MarkerHit event
ms.assetid: c97aff61-6f06-4589-a75b-ac2af340cb1d
keywords:
- MarkerHit event Windows Media Player
- MarkerHit event Windows Media Player , Player class
- Player class Windows Media Player , MarkerHit event
topic_type:
- apiref
api_name:
- Player.MarkerHit
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MarkerHit event

The **MarkerHit** event occurs when a marker is reached.

## Syntax


```JScript
Player.MarkerHit(
  MarkerNum
)
```



## Parameters

<dl> <dt>

*MarkerNum* 
</dt> <dd>

**Number** (**long**) indicating the number of the marker that was hit.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





