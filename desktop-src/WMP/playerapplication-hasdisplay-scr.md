---
title: PLAYERAPPLICATION.hasDisplay Attribute
description: The hasDisplay attribute retrieves a value indicating whether video can display through the remoted Windows Media Player control.
ms.assetid: c6a735a4-29ae-401c-9381-d8aad2c456eb
keywords:
- PLAYERAPPLICATION.hasDisplay Windows Media Player
topic_type:
- apiref
api_name:
- PLAYERAPPLICATION.hasDisplay
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PLAYERAPPLICATION.hasDisplay

The **hasDisplay** attribute retrieves a value indicating whether video can display through the remoted Windows Media Player control.

``` syntax
        elementID.hasDisplay
```

## Possible Values

This attribute is a read-only **Boolean**.



| Value | Description               |
|-------|---------------------------|
| True  | The video can display.    |
| False | The video cannot display. |



 

## Remarks

This attribute is used only when remoting the Windows Media Player control.

Several Windows Media Player controls can be running remotely at the same time, but video can only display in one location at a time, either in the full mode of the Player or in one of the remoted controls. Use this property to determine whether the current control is the one through which video can be displayed.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYERAPPLICATION Element**](playerapplication-element.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 





