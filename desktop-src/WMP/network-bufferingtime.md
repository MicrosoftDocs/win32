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
ms.date: 05/31/2018
---

# Network.bufferingTime

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

 

 





