---
Description: Managed Reference for WMI Windows PowerShell Command Classes
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 30e77956-8428-4259-9218-b93f143fd987
ms.tgt_platform: multiple
title: Managed Reference for WMI Windows PowerShell Command Classes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managed Reference for WMI Windows PowerShell Command Classes

Windows PowerShell implements Windows Management Instrumentation (WMI) functionality through a set of cmdlets. You can use these cmdlets to complete the end-to-end tasks that are necessary to manage local and remote computers.

See [Windows PowerShell](http://go.microsoft.com/fwlink/p/?linkid=142509) for more information.

## WMI PowerShell Classes

**Namespace**: Microsoft.PowerShell.Commands

**Assembly**: Microsoft.PowerShell.Commands.Management

**DLL**: Microsoft.PowerShell.Commands.Management.dll

These WMI command classes are implemented by Windows PowerShell. These classes are included in this software development kit (SDK) for completeness only. The members of these classes cannot be used directly, nor should they be used to derive other classes.



| Class                   | Description                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GetWmiObjectCommand     | Gets instances of WMI classes or information about the available classes.<br/> See the [Get-WmiObject](http://go.microsoft.com/fwlink/p/?linkid=153476) cmdlet for examples and detailed information about the parameters.<br/> |
| InvokeWmiMethod         | Calls WMI methods.<br/> See the [Invoke-WmiMethod](http://go.microsoft.com/fwlink/p/?linkid=154182) cmdlet for examples and detailed information about the parameters.<br/>                                                     |
| RegisterWmiEventCommand | Subscribes to a WMI event.<br/> See the [Register-WmiEvent](http://go.microsoft.com/fwlink/p/?linkid=154183) cmdlet for examples and detailed information about the parameters.<br/>                                            |
| RemoveWmiObject         | Deletes an instance of an existing WMI class.<br/> See the [Remove-WmiObject](http://go.microsoft.com/fwlink/p/?linkid=154184) cmdlet for examples and detailed information about the parameters.<br/>                          |
| SetWmiInstance          | Creates or updates an instance of an existing WMI class.<br/> See the [Set-WmiInstance](http://go.microsoft.com/fwlink/p/?linkid=154185) cmdlet for examples and detailed information about the parameters.<br/>                |



 

 

 




