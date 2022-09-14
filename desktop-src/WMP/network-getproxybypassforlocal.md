---
title: Network.getProxyBypassForLocal method
description: The getProxyBypassForLocal method retrieves a value indicating whether the proxy server is bypassed if the origin server is on a local network.
ms.assetid: 'e5217d56-da22-4424-94b0-400369410b47'
keywords:
- getProxyBypassForLocal method Windows Media Player
- getProxyBypassForLocal method Windows Media Player , Network class
- Network class Windows Media Player , getProxyBypassForLocal method
topic_type:
- apiref
api_name:
- Network.getProxyBypassForLocal
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Network.getProxyBypassForLocal method

The **getProxyBypassForLocal** method retrieves a value indicating whether the proxy server is bypassed if the origin server is on a local network.

## Syntax


```JScript
bRetVal = Network.getProxyBypassForLocal(
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

This method returns a **Boolean** indicating whether the proxy server is bypassed. The value returned is meaningful only when **getProxySettings** returns a value of two (use manual settings).

## Remarks

This method fails unless the calling application is running on the local computer or intranet.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *Network*.**getProxyBypassForLocal** to display whether Windows Media Player is set to bypass the proxy server for local addresses. The **Player** object was created with ID = "Player".


```JScript
// Test whether the HTTP proxy settings are manual.
if (Player.network.getProxySettings("HTTP") == 2)

   // Get the proxy bypass for local value for HTTP.
   var proxyBypassForLocalHTTP = Player.network.getProxyBypassForLocal("HTTP");

// Test whether the MMS proxy settings are manual.
if (Player.network.getProxySettings("MMS") == 2)

   // Get the proxy bypass for local value for MMS.
   var proxyBypassForLocalMMS = Player.network.getProxyBypassForLocal("MMS");

// Display the proxy bypass for local values in the browser client area.
// Unavailable proxy bypass for local values will display as "undefined".
document.write("The current HTTP proxy bypass for local value: " + proxyBypassForLocalHTTP);
document.write("<BR>");
document.write("The current MMS proxy bypass for local value: " + proxyBypassForLocalMMS);

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

 

 





