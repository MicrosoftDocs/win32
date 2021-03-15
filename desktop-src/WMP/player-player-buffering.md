---
title: Player.Buffering event
description: The Buffering event occurs when the Windows Media Player control begins or ends buffering or downloading. | Player.Buffering event
ms.assetid: a0a09bf7-19bc-4838-a403-924e8d83b48d
keywords:
- Buffering event Windows Media Player
- Buffering event Windows Media Player , Player class
- Player class Windows Media Player , Buffering event
topic_type:
- apiref
api_name:
- Player.Buffering
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.Buffering event

The **Buffering** event occurs when the Windows Media Player control begins or ends buffering or downloading.

## Syntax


```JScript
Player.Buffering(
  Start
)
```



## Parameters

<dl> <dt>

*Start* 
</dt> <dd>

**Boolean** containing one of the following values.



| Value | Description            |
|-------|------------------------|
| true  | Buffering has started. |
| false | Buffering has ended.   |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Use this event to determine when buffering or downloading starts or stops. You can use the same event block for both cases and test *Network*.**bufferingProgress** and *Network*.**downloadProgress** to determine whether Windows Media Player is currently buffering or downloading content.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file by using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network.bufferingProgress**](network-bufferingprogress.md)
</dt> <dt>

[**Network.downloadProgress**](network-downloadprogress.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





