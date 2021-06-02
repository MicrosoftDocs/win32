---
description: While in C++ you can set the security on the entire process by calling CoInitializeSecurity before connecting to WMI through IWbemLocator::ConnectServer.
ms.assetid: 83c04a96-3829-4c07-91a7-06e5b75b2c12
ms.tgt_platform: multiple
title: Setting the Security on IWbemServices and Other Proxies
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Security on IWbemServices and Other Proxies

While in C++ you can set the security on the entire process by calling [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) before connecting to WMI through [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver). You can also change the authentication level, impersonation level, or the authentication service in a call that obtains a pointer to a WMI proxy, such as [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) or [**IWbemCallResult**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemcallresult). Calling [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) also allows you to change the authentication service (Kerberos, NTLM, or negotiate).

Scripts and Visual Basic applications only set security on proxies indirectly through calls to [**SWbemServices**](swbemservices.md) and other automation objects. For more information about setting and changing authentication and impersonation in script, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

Changing security levels or services is primarily a concern when connecting to WMI on a remote computer that is running a different operating system. For more information, see [Connecting Between Different Operating Systems](/windows/desktop/WmiSdk/troubleshooting-a-remote-wmi-connection).

A client application connects to a WMI proxy using an identity. An identity is a data object that consists of a user name, password, and authority settings. For a WMI client application, the call to the [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver) interface creates the initial identity. The [**ConnectServer**](swbemlocator-connectserver.md) method takes the identity in a set of three parameters, which you can set to **NULL** to indicate the current user. You can also specify a non-**NULL** parameter to indicate a specific user and domain. If the call is successful, **ConnectServer** returns a pointer through which you can access a variety of remote processes, such as a WMI service or the Windows operating system directly.

Like many COM interfaces, [**ConnectServer**](swbemlocator-connectserver.md) returns a pointer to a proxy. A proxy is a data object that represents a remote process, such as WMI or a remote provider. COM uses a proxy to allow developers access to remote data as though the data were local.

The following WMI interfaces use proxies:

-   [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) ([**SWbemServices**](swbemservices.md) scripting object)
-   [**IEnumWbemClassObject**](/windows/desktop/api/Wbemcli/nn-wbemcli-ienumwbemclassobject)
-   [**IWbemCallResult**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemcallresult)
-   [**IWbemRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemrefresher) ([**SWbemRefresher**](swbemrefresher.md) scripting object)

    The WMI Refresher is a special case because it is passed an [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) pointer, whose security settings must be properly set. For more information about using refresher objects, see [Accessing Performance Data in C++](accessing-performance-data-in-c--.md).

After you receive a pointer to a remote process, you can do one of two things. If you know what the process does, you can choose to set the security on the pointer and access the process normally. This is the case with most pointers to a WMI service. For more information, see [Setting the Security Levels on a WMI Connection](setting-the-security-levels-on-a-wmi-connection.md). Alternately, you need to access a different COM interface on the proxy, such as [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release), through a call to the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface on the proxy.

## Defaults and Recommendations

The distributed version of the Component Object Model (DCOM) negotiates the default authentication service (Kerberos, NTLM, or Negotiate), and you cannot specify the default authentication service using [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity). Specifying **RPC\_C\_AUTHN\_DEFAULT** in the authentication service parameter of [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) allows DCOM to select the appropriate service. For remote connections the default service is Negotiate, which is the recommended service for applications functioning in both Kerberos and non-Kerberos domains. For local connections, the default authentication service is NT LAN Manager (NTLM).

The following code example shows the default authentication service being used.


```C++
// The pWbemServices variable is of type IWbemServices*

HRESULT hr = CoSetProxyBlanket(
     pWbemServices,                //Proxy
     RPC_C_AUTHN_DEFAULT,          //Authentication service 
     RPC_C_AUTHZ_DEFAULT,          //Authorization service 
     COLE_DEFAULT_PRINCIPAL,       //Server principal name used 
                                       // by authentication service
     RPC_C_AUTHN_LEVEL_DEFAULT,    //Authentication level
     RPC_C_IMP_LEVEL_IMPERSONATE,  //Impersonation level
     COLE_DEFAULT_AUTHINFO,       //Client identity
     EOAC_DEFAULT                  //Capability flags
     );
```



The code example in this topic requires the following reference and \#include statements.


```C++
#define _WIN32_DCOM
#include <wbemidl.h>
#include <comdef.h>

#pragma comment(lib, "wbemuuid.lib")
```



For scripting, it is recommended that you use the defaults that DCOM selects for remote calls. On the local machine you cannot specify an authentication service for calls to WMI. For more information, see [Setting the Authentication Service Using VBScript](setting-the-authentication-service-using-vbscript.md) and [Constructing a Moniker String](constructing-a-moniker-string.md).

 

 
