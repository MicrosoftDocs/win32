---
description: When making calls outside of the calling process or to a remote WMI service, WMI uses the distributed version of the Component Object Model (DCOM).
ms.assetid: 261b4f18-5de5-4e06-a887-f5afd9c45511
ms.tgt_platform: multiple
title: Setting Authentication in WMI
ms.topic: article
ms.date: 05/31/2018
---

# Setting Authentication in WMI

When making calls outside of the calling process or to a remote WMI service, WMI uses the distributed version of the Component Object Model (DCOM). Out-of-process and remote calls are made through proxies, which require authentication of the credentials of the calling process.

You set the authentication level when connecting to a computer and WMI namespace. To connect to WMI, call [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver) in C++. In scripting or Visual Basic, you connect to WMI using SWbemLocator.ConnectServer or through the [moniker](constructing-a-moniker-string.md) string. DCOM security and WMI both require certain authentication levels when connecting between computers. The required level differs according to which operating system you are connecting. For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

WMI normally runs in a shared service host and shares the same authentication as other processes in the host. To run the WMI process with a different level of authentication, run WMI with the [**winmgmt**](winmgmt.md) command with the **/standalonehost** switch and set the authentication level for WMI generally. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md).

For more information and code examples of how to set authentication for WMI connections, see [Setting the Authentication Service using VBScript](setting-the-authentication-service-using-vbscript.md) and [Setting Authentication Using C++](setting-authentication-using-c-.md). These topics also contain tables that list the authentication constants for C++ and scripting.

## Using Proxies in WMI

To set authentication for a proxy, call the [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) function. For more information and a code example, see [Setting the Security on IWbemServices and Other Proxies](setting-the-security-on-iwbemservices-and-other-proxies.md).

The following [COM API for WMI](com-api-for-wmi.md) objects use proxies directly in C++ or C# to call out of process or to a remote WMI service:

-   [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices)
-   [**IEnumWbemClassObject**](/windows/desktop/api/Wbemcli/nn-wbemcli-ienumwbemclassobject)
-   [**IWbemCallResult**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemcallresult)
-   [**IWbemRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemrefresher)

The scripting objects, such as [**SWbemObject**](swbemobject.md), [**SWbemServices**](swbemservices.md), and [**SWbemRefresher**](swbemrefresher.md) do not use proxies directly. Instead, the scripting objects represent a wrapper or layer that calls into the [COM API for WMI](com-api-for-wmi.md) objects listed above. For more information and a code example of setting authentication in scripting, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

 

 
