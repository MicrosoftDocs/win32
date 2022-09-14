---
title: Player.MediaCollectionAttributeStringAdded event
description: The MediaCollectionAttributeStringAdded event occurs when an attribute value is added to the library. | Player.MediaCollectionAttributeStringAdded event
ms.assetid: 0a7fd61f-0429-4c1c-8790-d2f0e7f41d44
keywords:
- MediaCollectionAttributeStringAdded event Windows Media Player
- MediaCollectionAttributeStringAdded event Windows Media Player , Player class
- Player class Windows Media Player , MediaCollectionAttributeStringAdded event
topic_type:
- apiref
api_name:
- Player.MediaCollectionAttributeStringAdded
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MediaCollectionAttributeStringAdded event

The **MediaCollectionAttributeStringAdded** event occurs when an attribute value is added to the library.

## Syntax


```JScript
Player.MediaCollectionAttributeStringAdded(
  bstrAttribName,
  bstrAttribVal
)
```



## Parameters

<dl> <dt>

*bstrAttribName* 
</dt> <dd>

**String** specifying the name of the attribute. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

</dd> <dt>

*bstrAttribVal* 
</dt> <dd>

**String** specifying the value of the attribute.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

When a media item is added to the library its metadata is added to the **MediaCollection** object and this event is fired for each attribute added.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.mediaCollection**](player-mediacollection.md)
</dt> </dl>

 

 





