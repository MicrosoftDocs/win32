---
title: Settings.mute
description: The mute property specifies and retrieves a value indicating whether audio is muted.
ms.assetid: d6d4b46d-5631-4af7-bd99-21674f067121
keywords:
- Settings.mute Windows Media Player
topic_type:
- apiref
api_name:
- Settings.mute
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Settings.mute

The **mute** property specifies and retrieves a value indicating whether audio is muted.

## Syntax

player.settings.mute

## Possible Values

This property is a read/write **Boolean**.



| Value | Description                  |
|-------|------------------------------|
| true  | Audio is muted.              |
| false | Default. Audio is not muted. |



 

## Examples

The following example creates an HTML CHECKBOX element that allows the user to mute and un-mute audio. The **Player** object was created with ID = "Player".


```
<!-- Create an HTML CHECKBOX control. -->
<INPUT  TYPE = "CHECKBOX"  ID = MUTE  
             onClick = "
                        /* Use the CHECKBOX state to set 
                           the mute property. */
                        Player.settings.mute = MUTE.checked;
">
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





