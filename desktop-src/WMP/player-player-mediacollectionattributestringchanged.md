---
title: Player.MediaCollectionAttributeStringChanged event
description: The MediaCollectionAttributeStringChanged event occurs when an attribute value in the library is changed. | Player.MediaCollectionAttributeStringChanged event
ms.assetid: 9bc81cf2-50a9-41cf-8eff-25c9395dfdac
keywords:
- MediaCollectionAttributeStringChanged event Windows Media Player
- MediaCollectionAttributeStringChanged event Windows Media Player , Player class
- Player class Windows Media Player , MediaCollectionAttributeStringChanged event
topic_type:
- apiref
api_name:
- Player.MediaCollectionAttributeStringChanged
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MediaCollectionAttributeStringChanged event

The **MediaCollectionAttributeStringChanged** event occurs when an attribute value in the library is changed.

## Syntax


```JScript
Player.MediaCollectionAttributeStringChanged(
  bstrAttribName,
  bstrOldAttribVal,
  bstrNewAttribVal
)
```



## Parameters

<dl> <dt>

*bstrAttribName* 
</dt> <dd>

**String** specifying the name of the attribute. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

</dd> <dt>

*bstrOldAttribVal* 
</dt> <dd>

**String** specifying the old value of the attribute.

</dd> <dt>

*bstrNewAttribVal* 
</dt> <dd>

**String** specifying the new value of the attribute.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

When a user modifies library metadata, the **MediaCollection** object is updated and this event fires for each attribute changed.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.mediaCollection**](player-mediacollection.md)
</dt> </dl>

 

 





