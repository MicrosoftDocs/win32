---
title: Network.setProxyPort method
description: The setProxyPort method specifies the proxy port to use. | Network.setProxyPort method
ms.assetid: '09cfce4a-191c-4596-b678-15d9328d5c53'
keywords:
- setProxyPort method Windows Media Player
- setProxyPort method Windows Media Player , Network class
- Network class Windows Media Player , setProxyPort method
topic_type:
- apiref
api_name:
- Network.setProxyPort
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Network.setProxyPort method

The **setProxyPort** method specifies the proxy port to use.

## Syntax


```JScript
Network.setProxyPort(
  protocol,
  port
)
```



## Parameters

<dl> <dt>

*protocol* \[in\]
</dt> <dd>

**String** specifying the protocol name. For a list of supported protocols, see [Supported Protocols and File Types](supported-protocols-and-file-types.md).

</dd> <dt>

*port* \[in\]
</dt> <dd>

**Number** (**long**) specifying the proxy port to use.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method has no effect unless **getProxySettings** returns a value of 2 (use manual settings).

This method fails unless the calling application is running on the local computer or intranet.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *Network*.**setProxyPort** to specify the Windows Media Player proxy port number for the MMS protocol. The port number is retrieved from an HTML INPUT element with ID = "PORT". The **Player** object was created with ID = "Player".


```JScript
// Test whether proxy settings are manual.
if (Player.network.getProxySettings("MMS") == 2){

   // Store the port number specified by the user.
   var portnumber = PORT.value;

   // Set the port number for the MMS protocol.
   Player.network.setProxyPort("MMS", portnumber);
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

 

 





