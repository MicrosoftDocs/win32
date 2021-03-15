---
title: Player.CdromMediaChange event
description: The CdromMediaChange event occurs when a CD or DVD is inserted into or ejected from a CD or DVD drive. | Player.CdromMediaChange event
ms.assetid: d31a791a-55e5-49ee-bfe5-7488277e3fda
keywords:
- CdromMediaChange event Windows Media Player
- CdromMediaChange event Windows Media Player , Player class
- Player class Windows Media Player , CdromMediaChange event
topic_type:
- apiref
api_name:
- Player.CdromMediaChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.CdromMediaChange event

The **CdromMediaChange** event occurs when a CD or DVD is inserted into or ejected from a CD or DVD drive.

## Syntax


```JScript
Player.CdromMediaChange(
  CdromNum
)
```



## Parameters

<dl> <dt>

*CdromNum* 
</dt> <dd>

**Number** (**long**) specifying the index of the CD or DVD drive.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The index of the CD drive corresponds to the index of a **Cdrom** object in the **CdromCollection**.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cdrom Object**](cdrom-object.md)
</dt> <dt>

[**CdromCollection Object**](cdromcollection-object.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





