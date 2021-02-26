---
title: Network.setProxyName method
description: The setProxyName method specifies the name of the proxy server to use. | Network.setProxyName method
ms.assetid: 'dbcb2a00-4387-42af-8055-61d78d021ec7'
keywords:
- setProxyName method Windows Media Player
- setProxyName method Windows Media Player , Network class
- Network class Windows Media Player , setProxyName method
topic_type:
- apiref
api_name:
- Network.setProxyName
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Network.setProxyName method

The **setProxyName** method specifies the name of the proxy server to use.

## Syntax


```JScript
Network.setProxyName(
  protocol,
  name
)
```



## Parameters

<dl> <dt>

*protocol* \[in\]
</dt> <dd>

**String** specifying the protocol name. For a list of supported protocols, see [Supported Protocols and File Types](supported-protocols-and-file-types.md).

</dd> <dt>

*name* \[in\]
</dt> <dd>

**String** specifying the name of the proxy server to use.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method has no effect unless **getProxySettings** returns a value of 2 (use manual settings).

This method fails unless the calling application is running on the local computer or intranet.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *Network*.**setProxyName** to specify the name of the Windows Media Player proxy server for the MMS protocol. The new name is retrieved from an HTML TEXT element with ID = "NAME". The **Player** object was created with ID = "Player".


```JScript
// Test whether proxy settings are manual.
if (Player.network.getProxySettings("MMS") == 2){

   // Store the new proxy server name specified by the user.
   var proxyname = NAME.value;

   // Set the proxy server name.
   Player.network.setProxyName("MMS", proxyname);
}

else

// Warn that proxy settings must be set to 2.
alert("Proxy settings must be manual!");

```



## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> </dl>

 

 





