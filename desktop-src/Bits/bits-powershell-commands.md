---
title: Managed Reference for BITS PowerShell Commands
description: Background Intelligent Transfer Service (BITS) 4.0 can use Windows PowerShell cmdlets to manage transfer jobs.
ms.assetid: 2c151dfe-4f89-41ea-a533-21ffcf0aa39e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managed Reference for BITS PowerShell Commands

Background Intelligent Transfer Service (BITS) 4.0 can use Windows PowerShell cmdlets to manage transfer jobs.

Windows PowerShell cmdlets for BITS provide much of the same functionality as the bitsadmin command-line utility. However, Windows PowerShell also does the following:

-   Automates BITS tasks in an extensible and management-oriented scripting language.
-   Provides a single tool for all job-related tasks.

> [!Note]  
> To use these commands, you must first import the BITS PowerShell module, using the `Import-Module Bits Transfer` command. For more information, see the following [TechNet article](http://technet.microsoft.com/magazine/ff382721.aspx).

 

For more information on using Windows Powershell, see [Windows PowerShell](http://go.microsoft.com/fwlink/p/?linkid=142509).

## BITS PowerShell Classes

**Namespace**: Microsoft.BackgroundIntelligentTransfer.Management

**Assembly**: System.Management.Automation

These BITS command classes are implemented by Windows PowerShell. These classes are included in this software development kit (SDK) for completeness only. The members of these classes cannot be used directly, nor should they be used to derive other classes.



| Class                           | Description                                                                                                                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AddBitsFileCommand**          | Adds one or more files to an existing BITS transfer job.<br/> See the [Add-BitsFile](http://go.microsoft.com/fwlink/p/?linkid=154641) cmdlet for detailed information about the parameters and for examples.<br/>                       |
| **ClearBitsTransferCommand**    | Cancels a BITS transfer job.<br/> See the [Clear-BitsTransfer]( http://go.microsoft.com/fwlink/p/?linkid=154642) cmdlet for detailed information about the parameters and for examples.<br/>                                          |
| **CompleteBitsTransferCommand** | Completes a BITS transfer job.<br/> See the [Complete-BitsTransfer]( http://go.microsoft.com/fwlink/p/?linkid=154644) cmdlet for detailed information about the parameters and for examples.<br/>                                     |
| **GetBitsTransferCommand**      | Retrieves the associated BitsJob object for an existing BITS transfer job.<br/> See the [Get-BitsTransfer](http://go.microsoft.com/fwlink/p/?linkid=154645) cmdlet for detailed information about the parameters and for examples.<br/> |
| **NewBitsTransferCommand**      | Creates a new BITS transfer job.<br/> See the [New-BitsTransfer](http://go.microsoft.com/fwlink/p/?linkid=154646) cmdlet for detailed information about the parameters and for examples.<br/>                                           |
| **ResumeBitsTransferCommand**   | Resumes a BITS transfer job.<br/> See the [Resume-BitsTransfer](http://go.microsoft.com/fwlink/p/?linkid=154647) cmdlet for detailed information about the parameters and for examples.<br/>                                            |
| **SetBitsTransferCommand**      | Modifies the properties of an existing BITS transfer job.<br/> See the [Set-BitsTransfer](http://go.microsoft.com/fwlink/p/?linkid=154648) cmdlet for detailed information about the parameters and for examples.<br/>                  |
| **SuspendBitsTransferCommand**  | Suspends a BITS transfer job.<br/> See the [Suspend-BitsTransfer](http://go.microsoft.com/fwlink/p/?linkid=154649) cmdlet for detailed information about the parameters and for examples.<br/>                                          |



 

 

 





