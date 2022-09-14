---
title: Network.setProxyBypassForLocal method
description: The setProxyBypassForLocal method specifies a value indicating whether the proxy server is bypassed if the origin server is on a local network.
ms.assetid: '3023a561-f3b7-45c8-a432-baadd795aaa6'
keywords:
- setProxyBypassForLocal method Windows Media Player
- setProxyBypassForLocal method Windows Media Player , Network class
- Network class Windows Media Player , setProxyBypassForLocal method
topic_type:
- apiref
api_name:
- Network.setProxyBypassForLocal
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Network.setProxyBypassForLocal method

The **setProxyBypassForLocal** method specifies a value indicating whether the proxy server is bypassed if the origin server is on a local network.

## Syntax


```JScript
Network.setProxyBypassForLocal(
  protocol,
  bypass
)
```



## Parameters

<dl> <dt>

*protocol* \[in\]
</dt> <dd>

**String** specifying the protocol name. For a list of supported protocols, see [Supported Protocols and File Types](supported-protocols-and-file-types.md).

</dd> <dt>

*bypass* \[in\]
</dt> <dd>

**Boolean** specifying whether the proxy server is bypassed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method has no effect unless **getProxySettings** returns a value of 2 (use manual settings).

This method fails unless the calling application is running on the local computer or intranet.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *Network*.**setProxyBypassForLocal** to specify whether the Windows Media Player proxy server is bypassed, when using the MMS protocol, if the origin server is on a local network. The **Player** object was created with ID = "Player".


```JScript
// Test whether the proxy settings are manual.
if (Player.network.getProxySettings("MMS") == 2){

   // Prompt the user for a setting. Store the response in a variable.
   var proxybypass = confirm("Bypass proxy server for local addresses? \n OK = Yes \n Cancel = No");

   // Set the proxy bypass value using the user input.
   Player.network.setProxyBypassForLocal("MMS", proxybypass);
}

else

// Warn that proxy settings must be set to 2.
alert("Proxy settings must be manual!");

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

 

 





