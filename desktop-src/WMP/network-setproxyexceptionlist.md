---
title: Network.setProxyExceptionList method
description: The setProxyExceptionList method specifies the proxy exception list. | Network.setProxyExceptionList method
ms.assetid: 'c9eeb058-5ffb-4405-9bf2-776f120e2db4'
keywords:
- setProxyExceptionList method Windows Media Player
- setProxyExceptionList method Windows Media Player , Network class
- Network class Windows Media Player , setProxyExceptionList method
topic_type:
- apiref
api_name:
- Network.setProxyExceptionList
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Network.setProxyExceptionList method

The **setProxyExceptionList** method specifies the proxy exception list.

## Syntax


```JScript
Network.setProxyExceptionList(
  protocol,
  list
)
```



## Parameters

<dl> <dt>

*protocol* \[in\]
</dt> <dd>

**String** specifying the protocol name. For a list of supported protocols, see [Supported Protocols and File Types](supported-protocols-and-file-types.md).

</dd> <dt>

*list* \[in\]
</dt> <dd>

**String** specifying a semicolon-delimited list of hosts for which the proxy server is bypassed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This is a list of computers, domains, and/or addresses that will bypass the proxy server when the host portion of the target URL matches an entry in the list.

The \* character can be used as a wildcard for listing entries. For example, \*.com would match all hosts in the com domain, while 67.\* would match all hosts in the 67 class A subnet.

This method has no effect unless **getProxySettings** returns a value of 2 (use manual settings).

This method fails unless the calling application is running on the local computer or intranet.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *Network*.**setProxyExceptionList** to specify a list of hosts for which the proxy server is bypassed when using the MMS protocol. The new list is retrieved from an HTML TEXT element with ID = "XLIST". The **Player** object was created with ID = "Player".


```JScript
// Test whether proxy settings are manual.
if (Player.network.getProxySettings("MMS") == 2){

   // Store the user's new exception list.
   var proxyxlist = XLIST.value;

   // Set the exception list.
   Player.network.setProxyExceptionList("MMS", proxyxlist);
}

else

// Warn that the proxy settings must be set to 2.
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

 

 





