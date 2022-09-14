---
title: Player.URL
description: The URL property specifies or retrieves the name of the media item to play.
ms.assetid: 74987ffd-c625-4d30-9f5f-5170119158f9
keywords:
- Player.URL Windows Media Player
topic_type:
- apiref
api_name:
- Player.URL
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.URL

The **URL** property specifies or retrieves the name of the media item to play.

## Syntax

*player* .**URL**

## Possible Values

This property is a read/write **String** with no default value.

## Remarks

This property can only be set to a URL in a security zone that is the same or is less restrictive than the security zone of the calling program or webpage.

Applications that open media items from behind a firewall will have better performance if the address is specified using the domain name server (DNS) name instead of the IP address.

Do not call this method from event handler code. Calling *Player*.**URL** from an event handler may yield unexpected results.

## Examples

The following example creates an HTML TEXT input element and an HTML BUTTON input element. The TEXT element allows the user to type a path to specify a digital media file to play. The BUTTON element executes JScript that opens the file and starts Windows Media Player. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an INPUT control to get a file path from the user. -->
<INPUT Type = "TEXT" ID = "inputURL">

<!-- Create a BUTTON control to execute the script. -->
<INPUT  Type = "BUTTON"  ID = "openMedia"  VALUE = "Open Media"
    onClick = "
        /* Specify the URL obtained from user input. */
        Player.URL = inputURL.value;

        /* Start the Player. */
        Player.controls.play();
">

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





