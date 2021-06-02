---
description: Connecting to WMI Remotely with PowerShell
ms.assetid: 9a06f0c3-2845-48aa-9988-79cc4607ce19
ms.tgt_platform: multiple
title: Connecting to WMI Remotely with PowerShell
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to WMI Remotely with PowerShell

Windows PowerShell provides a simple mechanism to connect to Windows Management Instrumentation (WMI) on a remote computer. Remote connections in WMI are affected by the [Windows Firewall](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754274(v=ws.11)), DCOM settings, and [User Account Control (UAC)](/previous-versions/aa905108(v=msdn.10)). For more information about configuring remote connections, see [Connecting to WMI Remotely Starting with Windows Vista](connecting-to-wmi-remotely-starting-with-vista.md).

The examples in this topic are based on the VBScripts from [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md). All of the examples in this topic use the [Get-WmiObject](/previous-versions//dd315295(v=technet.10)) cmdlet. For more information, see [Get-WmiObject](/previous-versions//dd315295(v=technet.10)).

## Windows PowerShell examples

When creating a connection to a remote computer, a user can specify the connection information such as the remote computer name, credentials, and the authentication level for the connection. The following examples illustrate how to connect to a remote computer by using different sets of credentials and how to access WMI information.

The following Windows PowerShell example shows setting the impersonation level:


```PowerShell

Get-WmiObject -Namespace "root\cimv2" -Class Win32_Process -Impersonation 3 -ComputerName Computer_B
```



In the preceding example, the user connects to a remote computer by using the same credentials (domain and user name) that they logged on with. The user also requested to use impersonation. Unlike the original VBScript example, a moniker string is not needed because the impersonation level is set by the "Impersonation" property. By default, the impersonation level is set to 3 (Impersonate).

The example lists all the instances of the [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) class that are running on remote computer.

> [!Note]  
> You should specify the WMI namespace to connect to on the remote computer because it is possible that the default namespace is not the same on different computers.

 

The following Windows PowerShell example shows how to connect to a remote computer with different credentials and to set the impersonation level to 3, which is Impersonate:


```PowerShell

$Computer = "atl-dc-01"

Get-WmiObject -Namespace "root\cimv2" -Class Win32_Process -Impersonation 3 -Credential `
FABRIKAM\administrator -ComputerName $Computer
```



In the preceding example, the computer name was assigned to the $Computer variable. The user connects to a remote computer by using specific credentials (domain and user name) and requests impersonation for the authentication level.

> [!Note]  
> The grave-accent character (\`) is used to indicate a line break. It is equivalent to the underscore character (\_) in VBScript.

 

The following Windows PowerShell example connects to a group of remote computers in the same domain by creating an array of remote computer names and then displaying names of the Plug and Play devices—instances of [**Win32\_PnPEntity**](/windows/desktop/CIMWin32Prov/win32-pnpentity)—on each computer:


```PowerShell
$ArrComputers = "Computer1", "Computer2", "Computer3"
foreach ($Computer in $ArrComputers) 
{
write-host ""
write-host "===================================="
write-host "Computer: $Computer"
write-host "===================================="

write-host "-----------------------------------"
write-host "Win32_PnPEntity instance"
write-host "-----------------------------------"

$ColItems = Get-WmiObject -Class Win32_PnPEntity -Namespace "root\cimv2" -Computer $Computer
$ColItems[0..47] | Format-List Name, Status
}
```



> [!Note]  
> To run the preceding Windows PowerShell script, you must be an administrator on the remote computers. Also, relating to the preceding example, note the following:

 

-   The computer names in the array must be enclosed in quotation marks because they are strings.
-   The objects returned by the [Get-WmiObject](/previous-versions//dd315295(v=technet.10)) are assigned to the $ColItems variable.
-   The range operator \[\] limited the list of Plug and Play devices to 48 instances. For more information, see [About\_Operators](/previous-versions//dd347588(v=technet.10)).
-   The "\|" is the pipeline character. The object returned by ColItems is sent to the [Format-List]( /previous-versions//dd347700(v=technet.10)) cmdlet.

The following Windows PowerShell example enables you to connect to a remote computer on a different domain. This example also displays the process names for instances of [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) on the remote computer.


```PowerShell
$Computer = "FullComputerName" 
$Domain = "DOMAIN"
$Credential = Get-Credential
$ColItems = Get-WmiObject -Class Win32_Process -Authority "ntlmdomain:$Domain" `
-Credential $Credential -Locale "MS_409" -Namespace "root\cimv2"  -ComputerName $Computer

foreach ($ObjItem in $colItems) 
{
write-host "Process Name:" $ObjItem.name
}
```



> [!Note]  
> To run the preceding Windows PowerShell script, you must be an administrator on the remote computer.

 

In the preceding example, the user connects to a remote computer on a different domain and specifies a preferred locale. The [Get-Credential](/previous-versions//dd315327(v=technet.10)) command requests the user's credentials and assigns the credentials to an object. The example also lists the names of instances of the [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) class that are running on the computer.

## Related topics

<dl> <dt>

[Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)
</dt> </dl>

 

 
