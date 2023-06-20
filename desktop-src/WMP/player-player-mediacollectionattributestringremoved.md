---
title: Player.MediaCollectionAttributeStringRemoved event
description: The MediaCollectionAttributeStringRemoved event occurs when an attribute value is removed from the library. | Player.MediaCollectionAttributeStringRemoved event
ms.assetid: f1253996-10d1-42fa-89f9-1e52ca830aea
keywords:
- MediaCollectionAttributeStringRemoved event Windows Media Player
- MediaCollectionAttributeStringRemoved event Windows Media Player , Player class
- Player class Windows Media Player , MediaCollectionAttributeStringRemoved event
topic_type:
- apiref
api_name:
- Player.MediaCollectionAttributeStringRemoved
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.MediaCollectionAttributeStringRemoved event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **MediaCollectionAttributeStringRemoved** event occurs when an attribute value is removed from the library.

## Syntax


```JScript
Player.MediaCollectionAttributeStringRemoved(
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

When a media item is removed from the library, its metadata is removed from the **MediaCollection** object and this event is fired for each attribute removed.

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

 

 





