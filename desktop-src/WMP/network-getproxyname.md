---
title: Network.getProxyName method
description: The getProxyName method retrieves the name of the proxy server being used.
ms.assetid: '273b1f7d-84b7-4e50-9f80-9fd1978e7528'
keywords:
- getProxyName method Windows Media Player
- getProxyName method Windows Media Player , Network class
- Network class Windows Media Player , getProxyName method
topic_type:
- apiref
api_name:
- Network.getProxyName
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.getProxyName method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getProxyName** method retrieves the name of the proxy server being used.

## Syntax


```JScript
strRetVal = Network.getProxyName(
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

This method returns a **String** containing the name of the proxy server being used. The value returned is meaningful only when **getProxySettings** returns a value of 2 (use manual settings).

## Remarks

This method fails unless the calling application is running on the local computer or intranet.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *Network*.**getProxyName** to display the Windows Media Player proxy server names for the HTTP and MMS protocols. The **Player** object was created with ID = "Player".


```JScript
// Test whether the HTTP proxy settings are manual.
if (Player.network.getProxySettings("HTTP") == 2)

   // Get the proxy server name for HTTP.
   var proxyNameHTTP = Player.network.getProxyName("HTTP");

// Test whether the MMS proxy settings are manual.
if (Player.network.getProxySettings("MMS") == 2)

   // Get the proxy server name for MMS.
   var proxyNameMMS = Player.network.getProxyName("MMS");

// Display the proxy server names in the browser client area.
// Unavailable proxy server names will display as "undefined".
document.write("The current HTTP proxy server name is: " + proxyNameHTTP);
document.write("<BR>");
document.write("The current MMS proxy server name is: " + proxyNameMMS);

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> <dt>

[**Network.getProxySettings**](network-getproxysettings.md)
</dt> </dl>

 

 





