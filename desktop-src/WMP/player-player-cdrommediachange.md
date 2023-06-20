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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.CdromMediaChange event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



| Requirement | Value |
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

 

 





