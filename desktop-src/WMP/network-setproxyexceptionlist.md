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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.setProxyExceptionList method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> </dl>

 

 





