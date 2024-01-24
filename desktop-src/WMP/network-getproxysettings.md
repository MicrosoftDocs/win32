---
title: Network.getProxySettings method
description: The getProxySettings method retrieves the proxy setting for a given protocol.
ms.assetid: 'a7b21eab-93e1-458b-aab0-60fd298cce44'
keywords:
- getProxySettings method Windows Media Player
- getProxySettings method Windows Media Player , Network class
- Network class Windows Media Player , getProxySettings method
topic_type:
- apiref
api_name:
- Network.getProxySettings
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.getProxySettings method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getProxySettings** method retrieves the proxy setting for a given protocol.

## Syntax


```JScript
retVal = Network.getProxySettings(
  protocol
)
```



## Parameters

<dl> <dt>

*protocol* \[in\]
</dt> <dd>

**String** specifying the protocol name. For a list of supported protocols, see [Supported Protocols and File Types](supported-protocols-and-file-types.md).

</dd> </dl>

## Return value

This method returns a **Number** (**long**) containing one of the following values.



| Value | Description                                                                      |
|-------|----------------------------------------------------------------------------------|
| 0     | A proxy server is not being used.                                                |
| 1     | The proxy settings for the current browser are being used (only valid for HTTP). |
| 2     | The manually specified proxy settings are being used.                            |
| 3     | The proxy settings are being auto-detected.                                      |



 

## Remarks

This method fails unless the calling application is running on the local computer or intranet.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *Network*.**getProxySettings** to display a message, which gives information about the current proxy settings of the Player, in the browser window. The **Player** object was created with ID = "Player".


```JScript
// Retrieve a number representing the current proxy settings.
var proxySetting = Player.network.getProxySettings("MMS");

// Display the message the corresponds to the current settings.
switch(proxySetting){

   case 0:
     document.write("A proxy server is not being used");
     break;

   case 1: 
     document.write("The proxy settings for the current browser are being used.");
     break;

   case 2:
     document.write("The manually specified proxy settings are being used.");
     break;

case 3:
     document.write("The proxy settings are being auto-detected.");
     break;

   default:
     document.write("Unable to determine proxy setting, try again.");
}

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

 

 





