---
title: Network.bufferingTime
description: The bufferingTime property specifies or retrieves the amount of time in milliseconds allocated for buffering incoming data before playing begins.
ms.assetid: b52b7f44-6be1-4299-94da-c37d758795af
keywords:
- Network.bufferingTime Windows Media Player
topic_type:
- apiref
api_name:
- Network.bufferingTime
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.bufferingTime

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **bufferingTime** property specifies or retrieves the amount of time in milliseconds allocated for buffering incoming data before playing begins.

## Syntax

*player*.*network*.**bufferingTime**

## Possible Values

This property is a read/write **Number** (**long**) ranging from zero to 60,000 with a default value of 5,000.

## Examples

The following JScript example uses *Network*.**bufferingTime** to specify the number of seconds allocated for buffering incoming data. The information is retrieved from an HTML TEXT INPUT element created with ID = "bufText". The **Player** object was created with ID = "Player".


```JScript
<!-- Create a BUTTON element to change the bufferingTime value. -->
<INPUT TYPE = "BUTTON" NAME = "bufTime" ID = "bufTime" 
       VALUE = "Change Buffer Time"

    onClick = "
       /* Test whether the user entered a valid value. */
       if (bufText.value >= 0 & bufText.value <= 60) 
           Player.network.bufferingTime = bufText.value * 1000;
       else
           alert('Buffering time must be between 0 and 60.');
">

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> </dl>

 

 





