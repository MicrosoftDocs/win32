---
description: Managed Reference for WMI Windows PowerShell Command Classes
ms.assetid: 30e77956-8428-4259-9218-b93f143fd987
ms.tgt_platform: multiple
title: Managed Reference for WMI Windows PowerShell Command Classes
ms.topic: article
ms.date: 05/31/2018
---

# Managed Reference for WMI Windows PowerShell Command Classes

Windows PowerShell implements Windows Management Instrumentation (WMI) functionality through a set of cmdlets. You can use these cmdlets to complete the end-to-end tasks that are necessary to manage local and remote computers.

See [Windows PowerShell](https://msdn.microsoft.com/library/dd835506(v=vs.85).aspx) for more information.

## WMI PowerShell Classes

**Namespace**: Microsoft.PowerShell.Commands

**Assembly**: Microsoft.PowerShell.Commands.Management

**DLL**: Microsoft.PowerShell.Commands.Management.dll

These WMI command classes are implemented by Windows PowerShell. These classes are included in this software development kit (SDK) for completeness only. The members of these classes cannot be used directly, nor should they be used to derive other classes.



| Class                   | Description                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GetWmiObjectCommand     | Gets instances of WMI classes or information about the available classes.<br/> See the [Get-WmiObject](/previous-versions//dd315295(v=technet.10)) cmdlet for examples and detailed information about the parameters.<br/> |
| InvokeWmiMethod         | Calls WMI methods.<br/> See the [Invoke-WmiMethod](/previous-versions//dd315300(v=technet.10)) cmdlet for examples and detailed information about the parameters.<br/>                                                     |
| RegisterWmiEventCommand | Subscribes to a WMI event.<br/> See the [Register-WmiEvent](/previous-versions//dd315242(v=technet.10)) cmdlet for examples and detailed information about the parameters.<br/>                                            |
| RemoveWmiObject         | Deletes an instance of an existing WMI class.<br/> See the [Remove-WmiObject](/previous-versions//dd347605(v=technet.10)) cmdlet for examples and detailed information about the parameters.<br/>                          |
| SetWmiInstance          | Creates or updates an instance of an existing WMI class.<br/> See the [Set-WmiInstance](/previous-versions//dd315391(v=technet.10)) cmdlet for examples and detailed information about the parameters.<br/>                |



 

 

