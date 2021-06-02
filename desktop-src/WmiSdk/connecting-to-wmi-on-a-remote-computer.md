---
description: Describes how scripts, applications, and providers can establish connections to WMI on remote computers to obtain data or control hardware and software.
ms.assetid: 16b00ee3-f721-4912-9e8e-2fdbc897a813
ms.tgt_platform: multiple
title: Connecting to WMI on a Remote Computer
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to WMI on a Remote Computer

WMI can be used to manage and access WMI data on remote computers. Remote connections in WMI are affected by the [Windows Firewall](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754274(v=ws.11)) and DCOM settings. [User Account Control (UAC)](/previous-versions/aa905108(v=msdn.10)) may also require changes to some settings. However, once your have your settings correct, the call to a remote system is very similar to a local WMI call. You may choose to make it more complex however, by using different credentials, alternate authentication protocols, and other security features.

## Configuring a Computer for a Remote Connection

Before you can access a remote system with WMI, you may need to check some security settings to confirm that you have access. Specifically:

-   Windows contains a number of security features that may block access to scripts on remote systems. As such, you may need to modify your system's Active Directory and Windows Firewall settings before making a WMI call. For more information, see [Setting up a Remote WMI Connection](connecting-to-wmi-remotely-starting-with-vista.md) and [Troubleshooting a Remote WMI Connection](troubleshooting-a-remote-wmi-connection.md).

-   The correct DCOM settings must be enabled for a remote connection to work. Changing DCOM settings can allow low rights users access to a computer for a remote connection. For more information, see [Securing a Remote WMI Connection](securing-a-remote-wmi-connection.md).

In addition, there may be some circumstances in which you may wish to run WMI though a fixed port. To do this, you will also need to change your settings. For more information, see [Setting Up a Fixed Port for WMI](setting-up-a-fixed-port-for-wmi.md).

## Connecting to a Remote Computer

At its heart, connecting to a remote system with WMI consists of making sure that you have the appropriate permissions to access the system, and that your connection is properly configured. Once you have those two elements, the connection itself is relatively simple. For example, if you are using your default security credentials, you can access WMI on a remote system using the following code:

<dl> <dt>

<span id="Connecting_to_WMI_Remotely_with_PowerShell"></span><span id="connecting_to_wmi_remotely_with_powershell"></span><span id="CONNECTING_TO_WMI_REMOTELY_WITH_POWERSHELL"></span>[Connecting to WMI Remotely with PowerShell](connecting-to-wmi-on-a-remote-computer-by-using-powershell.md)
</dt> <dd>

Use the *-ComputerName* parameter common to most WMI cmdlets, such as [Get-WmiObject](/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1&preserve-view=true).


```PowerShell
$strComputer = "Computer_B"
$colSettings = Get-WmiObject Win32_OperatingSystem -ComputerName $strComputer
```



</dd> <dt>

<span id="Connecting_to_WMI_Remotely_with_VBScript"></span><span id="connecting_to_wmi_remotely_with_vbscript"></span><span id="CONNECTING_TO_WMI_REMOTELY_WITH_VBSCRIPT"></span>[Connecting to WMI Remotely with VBScript](connecting-to-wmi-remotely-with-vbscript.md)
</dt> <dd>

Use a moniker that contains the name of the remote system in the call to [**GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject).


```VB
strComputer = "Computer_B"
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colSettings = objWMIService.ExecQuery("Select * from Win32_OperatingSystem")
```



</dd> <dt>

<span id="Connecting_to_WMI_Remotely_with_C_"></span><span id="connecting_to_wmi_remotely_with_c_"></span><span id="CONNECTING_TO_WMI_REMOTELY_WITH_C_"></span>[Connecting to WMI Remotely with C#](connecting-to-wmi-remotely-with-c-.md)
</dt> <dd>

For the current version of the WMI managed interface ([Microsoft.Management.Infrastructure](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832958(v=vs.85))), use the [CimSession](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832509(v=vs.85)) object to represent a connection to a remote host.


```CSharp
using Microsoft.Management.Infrastructure;
...
string Namespace = @"root\cimv2";
string OSQuery = "SELECT * FROM Win32_OperatingSystem";
CimSession mySession = CimSession.Create("Computer_B");
IEnumerable<CimInstance> queryInstance = mySession.QueryInstances(Namespace, "WQL", OSQuery);
```



</dd> <dt>

<span id="Connecting_to_WMI_Remotely_with_C_"></span><span id="connecting_to_wmi_remotely_with_c_"></span><span id="CONNECTING_TO_WMI_REMOTELY_WITH_C_"></span>[Connecting to WMI Remotely with C#](connecting-to-wmi-remotely-with-c-.md)
</dt> <dd>

For the v1 version of the WMI managed interface ([System.Management](/dotnet/api/system.management)), use the [ManagementScope](/dotnet/api/system.management.managementscope) object to represent a connection to a remote host.


```CSharp
using System.Management;
...
ManagementScope scope = new ManagementScope("\\\\Computer_B\\root\\cimv2");
scope.Connect();
ObjectQuery query = new ObjectQuery("SELECT * FROM Win32_OperatingSystem");
ManagementObjectSearcher searcher = new ManagementObjectSearcher(scope, query);
```



</dd> <dt>

<span id="Example__Getting_WMI_Data_from_a_Remote_Computer__C___"></span><span id="example__getting_wmi_data_from_a_remote_computer__c___"></span><span id="EXAMPLE__GETTING_WMI_DATA_FROM_A_REMOTE_COMPUTER__C___"></span>[Example: Getting WMI Data from a Remote Computer (C++)](example--getting-wmi-data-from-a-remote-computer.md)
</dt> <dd>

Use the [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver) method to specify the name of the remote computer in the *strNetworkResource* parameter.


```CSharp
    hres = pLoc->ConnectServer(
        _bstr_t(L"\\\\COMPUTER_B\\root\\cimv2"),
        _bstr_t(useToken?NULL:pszName),    // User name
        _bstr_t(useToken?NULL:pszPwd),     // User password
        NULL,                              // Locale             
        NULL,                              // Security flags
        _bstr_t(useNTLM?NULL:pszAuthority),// Authority        
        NULL,                              // Context object 
        &pSvc                              // IWbemServices proxy
        );
```



</dd> </dl>

The previous code samples are arguably the most basic remote connection you can perform with WMI. Specifically, the samples assume the following:

-   You are an administrator on the remote machine. Due to [User Account Control](/previous-versions/aa905108(v=msdn.10)), the account on the remote system must be a domain account in the Administrators group. For more information, see User Account Control and WMI.
-   The password on your current local machine is not blank. This is essentially a Windows security requirement that you must have logged onto your system with a password.
-   Both your local and remote computers are within the same domain. If you need to cross domain boundaries, you would need to supply additional information or use a slightly different programming model.
-   You are using your own account to access the remote machine. If you were trying to access a different account, you would need to supply additional credentials. (Note that trying to access WMI locally with credentials different than your current account is not permitted.)
-   Both computers are running IPv6. WMI supports connections to computers running IPv6. However, both your local machine and "Computer\_B" must be running IPv6. Either computer may be running IPv4 also. For more information, see [IPv6 and IPv4 Support in WMI](ipv6-and-ipv4-support-in-wmi.md).
-   Your script does not need to delegate - that is, it does not need to access additional remote computers through the targeted remote computer. For more information, see [Delegating with WMI](connecting-to-a-3rd-computer-delegation.md).
-   You are trying to make a specific call, rather than creating a remote process. For more information, see [Creating Processes Remotely using WMI](creating-processes-remotely.md).

With those restrictions in mind, a remote WMI call is very similar to a local WMI call - the only difference being that you must specify the name of the remote system. However, you may choose to change many of those features: using different credentials, or routing your call through a 3rd party computer, or accessing a different domain.

 

 
