---
title: Quota Management for Remote Shells
description: Quota management allows users to manage system resources more efficiently.
ms.assetid: 6651a500-a95a-45a1-b46a-27b2e9b36a1c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Quota Management for Remote Shells

Quota management allows users to manage system resources more efficiently. Windows Remote Management (WinRM) has added a specific set of quotas that provide a better quality of service, help prevent denial of service issues, and allocate server resources to concurrent users. The WinRM quota set is based on the quota infrastructure that is implemented for the Internet Information Services (IIS) service.

Implementing quotas will help to prevent performance degradation and denial of service issues by doing the following:

-   Limiting the number of shells and shell processes that a user can create
-   Limiting the maximum number of concurrent users
-   Managing the amount of memory that is allocated to a shell
-   Setting a time-out for shells that are inactive

## Quota Settings

The following quotas need to be enforced for remote shell management. These quotas can be configured through the winrm utility or through Group Policy settings. Settings configured by a Group Policy supersede the quotas set by the winrm utility. For more information about setting Group Policies for WinRM, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md).

<dl> <dt>

<span id="IdleTimeout"></span><span id="idletimeout"></span><span id="IDLETIMEOUT"></span>IdleTimeout
</dt> <dd>

The maximum time in milliseconds before an inactive remote shell is deleted. The default is 180000 milliseconds. The minimum time is 1000 milliseconds.

</dd> <dt>

<span id="MaxProcessesPerShell"></span><span id="maxprocessespershell"></span><span id="MAXPROCESSESPERSHELL"></span>MaxProcessesPerShell
</dt> <dd>

The maximum number of processes allowed per shell, including the shell's child processes. The default is 25.

</dd> <dt>

<span id="MaxMemoryPerShellMB"></span><span id="maxmemorypershellmb"></span><span id="MAXMEMORYPERSHELLMB"></span>MaxMemoryPerShellMB
</dt> <dd>

The maximum amount of memory allocated per shell, including the shell's child processes. The default is 1024 MB.

> [!Note]  
> The behavior is unsupported if the MaxMemoryPerShellMB is set to a value that is less than the default.

 

</dd> <dt>

<span id="MaxShellsPerUser"></span><span id="maxshellsperuser"></span><span id="MAXSHELLSPERUSER"></span>MaxShellsPerUser
</dt> <dd>

The maximum number of shells per user. The default is 30.

</dd> <dt>

<span id="MaxConcurrentUsers"></span><span id="maxconcurrentusers"></span><span id="MAXCONCURRENTUSERS"></span>MaxConcurrentUsers
</dt> <dd>

The maximum number of concurrent users who can open shells. The default is 10.

</dd> </dl>

## Deprecated Quotas

WinRM 2.0 sets the MaxShellRunTime quota to read-only. Changing the value for this quota will have no effect on the remote shells.

## Retrieving Quota Configuration Information

To check the quota configuration settings, type **winrm get winrm/config**.

The following snippet is a text-based example of a WinRM configuration with the default quota settings.

``` syntax
Config

          ...         

          Winrs

                   AllowRemoteShellAccess = true

                   IdleTimeout = 7200000

                   MaxConcurrentUsers = 10

                   MaxProcessesPerShell = 25

                   MaxMemoryPerShellMB = 1024

                   MaxShellsPerUser = 30
```

## Configuring Shell Quotas

Quotas can be set through a Group Policy setting or manually. For more information about specific configuration settings, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md).

**To set a quota with Group Policy**

1.  Open a Command Prompt window as an administrator.
2.  At the Command Prompt, type **gpedit.msc**. The **Group Policy Object Editor** window opens.
3.  Find the **Windows Remote Management** and **Windows Remote Shell** Group Policy Objects (GPO) under **Computer Configuration\\Administrative Templates\\Windows Components**.
4.  On the **Extended** tab, select a setting to see a description. Double click a setting to edit it.

**To set a quota manually**

1.  Open a Command Prompt window as an administrator.
2.  At the Command Prompt, type **winrm set winrm/config/winrs '@{***&lt;Quota&gt;***="***&lt;Value&gt;***"}'**

For example, to increase the maximum number of shells per user from 5 to 7, type **winrm set winrm/config/winrs '@{MaxShellsPerUser="7"}'**.

 

 




