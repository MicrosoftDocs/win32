---
Description: Client applications that call WMI interfaces can control the security levels of their processes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 790b4e40-9b92-464a-a774-dec0b75cedee
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Setting Client Application Process Security
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Client Application Process Security

Client applications that call WMI interfaces can control the security levels of their processes. All WMI applications access WMI through COM, and you can call the COM function [**CoInitializeSecurity**](https://msdn.microsoft.com/windows/desktop/e0933741-6b75-4ce1-aa63-6240e4a7130f) to set security for your processes. Applications that make asynchronous calls to WMI and applications that register as event consumers set security levels on the call into WMI.

If you do not make an explicit call to [**CoInitializeSecurity**](https://msdn.microsoft.com/windows/desktop/e0933741-6b75-4ce1-aa63-6240e4a7130f), COM calls it implicitly with values from the registry. However, the registry values may have lower settings for impersonation and authentication that do not provide the security required for WMI. For more information, see [Setting the Default Process Security Level Using C++](setting-the-default-process-security-level-using-c-.md).

Asynchronous access to WMI is not recommended. An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use semisynchronous or synchronous communication, or perform proper access checks in your client application. For more information, see [Calling a Method](calling-a-method.md).

Calls to any of the WMI proxies ([**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices), [**IEnumWbemClassObject**](/windows/desktop/api/Wbemcli/nn-wbemcli-ienumwbemclassobject),[**IWbemCallResult**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemcallresult), or [**IWbemRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemrefresher)) use an out-of-process pointer. For more information about the defaults and recommendations, see [Setting the Security on IWbemServices and Other Proxies](setting-the-security-on-iwbemservices-and-other-proxies.md).

The following procedure describes the steps you must perform to set the security for WMI on your application process.

**To set security for WMI on your application process**

1.  Determine the security levels required for the Windows operating systems on which your client application runs.
2.  Call the COM [**CoInitializeSecurity**](https://msdn.microsoft.com/windows/desktop/e0933741-6b75-4ce1-aa63-6240e4a7130f) function to set the default security for the process in which the client application runs. This declares how much security other applications require to access the process in which your application runs.
3.  If you need to change the security on an individual proxy, for example on another call to [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices), call [**CoSetProxyBlanket**](https://msdn.microsoft.com/windows/desktop/c2e5e681-8fa5-4b02-b59d-ba796eb0dccf).
4.  If you need to control remote hardware or a system object that requires more privilege, use the [**AdjustTokenPrivileges**](https://msdn.microsoft.com/library/windows/desktop/aa375202) function to enable the necessary privileges. Note that you cannot enable a privilege that the process does not already have assigned to it. For more information, see [Checking Access to Private Objects](https://msdn.microsoft.com/library/windows/desktop/aa376388).

For further information about setting the default process security level, see [Setting the Default Process Security Level Using C++](setting-the-default-process-security-level-using-c-.md) and [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

 

 



