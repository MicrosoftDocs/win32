---
description: You can use Win32\_Process.Create to execute a script or application on a remote computer. However, for security reasons, the process cannot be interactive. When Win32\_Process.Create is called on the local computer, the process can be interactive.
ms.assetid: 11fea8b1-7d05-4f44-9103-ea804a1d4b38
ms.tgt_platform: multiple
title: Creating Processes Remotely using WMI
ms.topic: article
ms.date: 05/31/2018
---

# Creating Processes Remotely using WMI

You can use [**Win32\_Process.Create**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process) to execute a script or application on a remote computer. However, for security reasons, the process cannot be interactive. When **Win32\_Process.Create** is called on the local computer, the process can be interactive.

> [!WARNING]
> This topic describes the general procedure for creating a remote process with WMI. If you are simply looking to run a script on a remote system, see [Connecting to WMI Remotely Starting with Windows Vista](connecting-to-wmi-remotely-starting-with-vista.md), or [Connecting to WMI on a Remote Computer by Using Windows PowerShell](connecting-to-wmi-on-a-remote-computer-by-using-powershell.md). For more general information on remoting with PowerShell, see [Running Remote Commands](/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.2).

 

The remote process has no user interface but it is listed in the **Task Manager**. A process created locally can run under any account if the account has the **Execute Method** permission for the root\\cimv2 namespace. A process created remotely can run under any account if the account has the **Execute Method** and **Remote Enable** permissions for root\\cimv2. The **Execute Method** and **Remote Enable** permissions are set in WMI Control in the Control Panel. For more information, see [Setting Namespace Security with the WMI Control](setting-namespace-security-with-the-wmi-control.md).

You can use [**Win32\_ScheduledJob.Create**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-scheduledjob) to create an interactive process remotely. But processes started by **Win32\_ScheduledJob.Create** run under the LocalSystem account that can confer too much privilege.

## Related topics

<dl> <dt>

[Securing a Remote WMI Connection](securing-a-remote-wmi-connection.md)
</dt> <dt>

[Connecting to a 3rd Computer-Delegation](connecting-to-a-3rd-computer-delegation.md)
</dt> </dl>

 

 
