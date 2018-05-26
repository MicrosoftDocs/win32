---
Description: The Kerberos authentication service specifies the server principal name to ensure the identity of the computer to which it is connecting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3d58db28-2e69-4e27-9f27-61529abbf750
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Specifying the Server Principal Name
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Specifying the Server Principal Name

The Kerberos authentication service specifies the server principal name to ensure the identity of the computer to which it is connecting. Specify the server principal name in the call to the scripting method [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) by giving the name of the remote computer. In C++, specify the server principal name in the *pServerPrincName* parameter when calling [**CoSetProxyBlanket**](_com_cosetproxyblanket) for the proxy. For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

This parameter is required for Kerberos to support mutual authentication. However, using the default server principal name does not allow mutual authentication. Clients for which mutual authentication is critical, must specify a server principal name that matches the server identity that the WMI service is using. For more information about setting proxy security and a C++ example showing how to set the server principal name, see [Setting the Security on IWbemServices and Other Proxies](setting-the-security-on-iwbemservices-and-other-proxies.md).

For more information about setting the server principal name in script and Visual Basic, see [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) and [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

Unlike most security protocols for Windows Management Instrumentation (WMI) and Component Object Model (COM), you cannot set the server principal in a call to [**CoInitializeSecurity**](_com_coinitializesecurity). However, you can set the server principal with the *bstrAuthority* parameter for [**IWbemLocator::ConnectServer**](/windows/win32/Wbemcli/nf-wbemcli-iwbemlocator-connectserver?branch=master), or the *pServerPrincName* parameter for [**CoSetProxyBlanket**](_com_cosetproxyblanket).

The code example in this topic requires the following \#include statement to correctly compile.


```C++
#include <wbemidl.h>
```



The following code example shows how to set the server principal name with [**ConnectServer**](/windows/win32/Wbemcli/nf-wbemcli-iwbemlocator-connectserver?branch=master).


```C++
IWbemServices* g_pNameSpace = NULL;

// Namespace to which to connect
BSTR  bstrNameSpace = 
SysAllocString( L"\\\\MyMachine\\root\default" );

// The bstrAuthority string contains the server
// principal name MyDomain\\MyMachine
// and the authentication service, which is Kerberos.
BSTR  bstrAuthority = 
SysAllocString( L"kerberos:MyDomain\\MyMachine"  );

HRESULT hr = NULL;
IWbemLocator* pWbemLocator = 0;

  hr = pWbemLocator->ConnectServer(
          bstrNameSpace,  // NameSpace name
          NULL,           // User name
          NULL,           // Password
          NULL,           // Locale
          0L,             // Security flags
          bstrAuthority,  // Authority, server principal name
          NULL,           // WBEM context
          &amp;g_pNameSpace   // Namespace
          );

  // Free memory resources.
  g_pNameSpace->Release();
  SysFreeString(bstrNameSpace);
  SysFreeString(bstrAuthority);
```



## Related topics

<dl> <dt>

[Setting the Authentication Service Using VBScript](setting-the-authentication-service-using-vbscript.md)
</dt> <dt>

[Setting Authentication Using C++](setting-authentication-using-c-.md)
</dt> <dt>

[Setting the Security on IWbemServices and Other Proxies](setting-the-security-on-iwbemservices-and-other-proxies.md)
</dt> </dl>

 

 



