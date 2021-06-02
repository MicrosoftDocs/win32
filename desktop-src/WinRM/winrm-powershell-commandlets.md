---
title: Managed Reference for WinRM Windows PowerShell Command Classes
description: Windows Remote Management 2.0 (WinRM) can use Windows PowerShell cmdlets for system management. Windows PowerShell cmdlets enable an administrator to configure WinRM and to get data or manage resources.
ms.assetid: 1ecdd41e-7257-483a-9a20-ae817f5f5ebe
ms.tgt_platform: multiple
keywords:
- ConnectWSManCommand
- DisableWSManCredSSPCommand
- DisconnectWSManCommand
- EnableWSManCredSSPCommand
- GetWSManCredSSPCommand
- GetWSManInstanceCommand
- InvokeWSManActionCommand
- NewWSManInstanceCommand
- NewWSManSessionOptionCommand
- RemoveWSManInstanceCommand
- SetWSManInstanceCommand
- SetWSManQuickConfigCommand
- TestWSManCommand
- SessionOption
- AuthenticationMechanism
- ProxyAccessType
- ProxyAuthentication
ms.topic: article
ms.date: 05/31/2018
---

# Managed Reference for WinRM Windows PowerShell Command Classes

Windows Remote Management 2.0 (WinRM) can use Windows PowerShell cmdlets for system management. Windows PowerShell cmdlets enable an administrator to configure WinRM and to get data or manage resources.

Windows PowerShell cmdlets for WinRM provide the same functionality as the winrm command line utility. However, Windows PowerShell also does the following:

-   Automates WinRM tasks in an extensible and management-oriented scripting language.
-   Provides a single tool for all management tasks.

See [Windows PowerShell](https://msdn.microsoft.com/library/dd835506(v=vs.85).aspx) for more information.

## WS-Management Windows PowerShell Classes

**Namespace**: Microsoft.WsMan.Management

**Assembly**: System.Management.Automation

The following WinRM command classes are implemented by Windows PowerShell. These classes are included in this software development kit (SDK) for completeness only. The members of these classes cannot be used directly nor should they be used to derive other classes.



| Class                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ConnectWSManCommand          | Connects to the WinRM service on a remote computer. <br/> See the [Connect-WSMan](/powershell/module/Microsoft.WsMan.Management/Connect-WSMan?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                                              |
| DisableWSManCredSSPCommand   | Disables CredSSP authentication on a client.<br/> See the [Disable-WSManCredSSP](/powershell/module/Microsoft.WsMan.Management/Disable-WSManCredSSP?view=powershell-5.1&preserve-view=true) cmdlet for detailed information about the parameters and for examples.<br/>                                                                                                                                                                                                                                                                                                                                           |
| DisconnectWSManCommand       | Disconnects from the WinRM service on a remote computer. <br/> See the [Disconnect-WSMan](/powershell/module/Microsoft.WsMan.Management/Disconnect-WSMan?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                                      |
| EnableWSManCredSSPCommand    | Enables CredSSP authentication on the client.<br/> See the [Enable-WSManCredSSP](/powershell/module/Microsoft.WsMan.Management/Enable-WSManCredSSP?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                                               |
| GetWSManCredSSPCommand       | Gets the CredSSP-related configuration for the client.<br/> See the [Get-WSManCredSSP](/powershell/module/Microsoft.WsMan.Management/Get-WSManCredSSP?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                                         |
| GetWSManInstanceCommand      | Displays management information for a resource instance specified by a Resource URI.<br/> See the [Get-WSManInstance](/powershell/module/Microsoft.WsMan.Management/Get-WSManInstance?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                          |
| InvokeWSManActionCommand     | Invokes an action on the target object specified by the Resource URI and selectors. <br/> See the [Invoke-WSManAction](/powershell/module/Microsoft.WsMan.Management/Invoke-WSManAction?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                         |
| NewWSManInstanceCommand      | Creates a new instance of a management resource. <br/> See the [New-WSManInstance](/powershell/module/Microsoft.WsMan.Management/New-WSManInstance?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                                             |
| NewWSManSessionOptionCommand | Creates a WinRM Session option hash table to use as input parameters for the following WSMan cmdlets: [Get-WSManInstance](/powershell/module/Microsoft.WsMan.Management/Get-WSManInstance?view=powershell-5.1&preserve-view=true), [Set-WSManInstance](/powershell/module/Microsoft.WsMan.Management/Set-WSManInstance?view=powershell-5.1&preserve-view=true), [Invoke-WSManAction](/powershell/module/Microsoft.WsMan.Management/Invoke-WSManAction?view=powershell-5.1&preserve-view=true), and [Connect-WSMan](/powershell/module/Microsoft.WsMan.Management/Connect-WSMan?view=powershell-5.1&preserve-view=true). <br/> See the [New-WSManSessionOption](/powershell/module/Microsoft.WsMan.Management/New-WSManSessionOption?view=powershell-5.1&preserve-view=true) for examples and detailed information about the parameters.<br/> |
| RemoveWSManInstanceCommand   | Deletes a management resource instance. <br/> See the [Remove-WSManInstance](/powershell/module/Microsoft.WsMan.Management/Remove-WSManInstance?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                                                   |
| SetWSManInstanceCommand      | Modifies management information related to a resource. <br/> See the [Set-WSManInstance](/powershell/module/Microsoft.WsMan.Management/Set-WSManInstance?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                                       |
| SetWSManQuickConfigCommand   | Configures the local computer for remote management. <br/> See the [Set-WSManQuickConfig](/powershell/module/Microsoft.WsMan.Management/Set-WSManQuickConfig?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                                      |
| TestWSManCommand             | Tests whether the WinRM service is running on a local or remote computer. <br/> See the [Test-WSMan]( /powershell/module/microsoft.wsman.management/test-wsman?view=powershell-7&preserve-view=true) cmdlet for examples and detailed information about the parameters.<br/>                                                                                                                                                                                                                                                                                                                        |
| SessionOption                | Defines a set of extended options for the WS-Management session.<br/> See the [Connect-WSMan](/powershell/module/Microsoft.WsMan.Management/Connect-WSMan?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the possible values.<br/>                                                                                                                                                                                                                                                                                                                             |



 

## WS-Management Windows PowerShell Enumerations

The following enumerations are implemented by Windows PowerShell. These enumerations are included in this software development kit (SDK) for completeness only.



| Enumeration             | Description                                                                                                                                                                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AuthenticationMechanism | Specifies the authentication mechanism to be used at the server. <br/> See the [Connect-WSMan](/powershell/module/Microsoft.WsMan.Management/Connect-WSMan?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the possible values.<br/>      |
| ProxyAccessType         | Specifies the mechanism by which the proxy server is located.<br/> See the [New-WSManSessionOption](/powershell/module/Microsoft.WsMan.Management/New-WSManSessionOption?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the possible values.<br/> |
| ProxyAuthentication     | Specifies the authentication method to use at the proxy.<br/> See the [New-WSManSessionOption](/powershell/module/Microsoft.WsMan.Management/New-WSManSessionOption?view=powershell-5.1&preserve-view=true) cmdlet for examples and detailed information about the possible values.<br/>      |



 

 

