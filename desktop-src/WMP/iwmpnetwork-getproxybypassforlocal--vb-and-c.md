---
title: IWMPNetwork getProxyBypassForLocal method
description: The getProxyBypassForLocal method returns a value indicating whether the proxy server is bypassed if the origin server is on a local network.
ms.assetid: 150a05f3-6979-4a88-a617-472f07d38807
keywords:
- getProxyBypassForLocal method Windows Media Player
- getProxyBypassForLocal method Windows Media Player , IWMPNetwork interface
- IWMPNetwork interface Windows Media Player , getProxyBypassForLocal method
topic_type:
- apiref
api_name:
- IWMPNetwork.getProxyBypassForLocal
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPNetwork::getProxyBypassForLocal method

The **getProxyBypassForLocal** method returns a value indicating whether the proxy server is bypassed if the origin server is on a local network.

## Syntax


```CSharp
public System.Boolean getProxyBypassForLocal(
  System.String bstrProtocol
);
```


```VB

Public Function getProxyBypassForLocal( _
  ByVal bstrProtocol As System.String _
) As System.Boolean
Implements IWMPNetwork.getProxyBypassForLocal
```





## Parameters

<dl> <dt>

*bstrProtocol* 
</dt> <dd>

A **System.String** that is the protocol name.

</dd> </dl>

## Return value

A **System.Boolean** value that indicates whether the proxy server is bypassed. The value is meaningful only when **IWMPNetwork.getProxySettings** returns a value of 2 (use manual settings).

## Remarks

This method fails unless the calling application is running on the local computer or intranet.

## Examples

The following code example uses **getProxyBypassForLocal** to display whether Windows Media Player is set to bypass the proxy server for local addresses. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```VB
' Boolean values to hold the results of calls to getProxyBypassForLocal. 
Dim proxyBypassForLocalHTTP As Boolean = False
Dim proxyBypassForLocalMMS As Boolean = False

' Test whether the HTTP proxy settings are manual.
If (player.network.getProxySettings("HTTP") = 2) Then

    proxyBypassForLocalHTTP = player.network.getProxyBypassForLocal("HTTP")

End If

' Test whether the MMS proxy settings are manual.
If (player.network.getProxySettings("MMS") = 2) Then

    proxyBypassForLocalMMS = player.network.getProxyBypassForLocal("MMS")

End If

' Store the proxy bypass for local values in a string array and display them
' using a multi-line text box. Unavailable proxy bypass for local values will display
' as "undefined".
proxyInfo(0) = ("The current HTTP proxy bypass for local value: " + proxyBypassForLocalHTTP.ToString())
proxyInfo(1) = ("The current MMS proxy bypass for local value: " + proxyBypassForLocalMMS.ToString())
proxyBypassText.Lines = proxyInfo
```


```CSharp

// Boolean values to hold the results of calls to getProxyBypassForLocal. 
bool proxyBypassForLocalHTTP = false;
bool proxyBypassForLocalMMS = false;

// Test whether the HTTP proxy settings are manual.
if (player.network.getProxySettings(&quot;HTTP&quot;) == 2)
{
    proxyBypassForLocalHTTP = player.network.getProxyBypassForLocal(&quot;HTTP&quot;);
}

// Test whether the MMS proxy settings are manual.
if (player.network.getProxySettings(&quot;MMS&quot;) == 2)
{
   proxyBypassForLocalMMS = player.network.getProxyBypassForLocal(&quot;MMS&quot;);
}

// Store the proxy bypass for local values in a string array and display them
// using a multi-line text box. Unavailable proxy bypass for local values will display
// as &quot;undefined&quot;.
proxyInfo[0] = (&quot;The current HTTP proxy bypass for local value: &quot; + proxyBypassForLocalHTTP.ToString());
proxyInfo[1] = (&quot;The current MMS proxy bypass for local value: &quot; + proxyBypassForLocalMMS.ToString());
proxyBypassText.Lines = proxyInfo;
```





## Requirements



| Requirement | Value |
|----------------------|-----------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                             |
| Namespace<br/> | **WMPLib**<br/>                                                                         |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll</dt> </dl> |



## See also

<dl> <dt>

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> <dt>

[**IWMPNetwork.getProxySettings (VB and C#)**](wmplibiwmpnetwork-iwmpnetwork-getproxysettings--vb-and-c.md)
</dt> <dt>

[**IWMPNetwork.setProxyBypassForLocal (VB and C#)**](wmplibiwmpnetwork-iwmpnetwork-setproxybypassforlocal--vb-and-c.md)
</dt> </dl>

 

 





