---
title: Remote Shell Infrastructure Improvements
description: Windows Remote Management version 2.0 (WinRM 2.0) offers many remote shell infrastructure improvements.
ms.assetid: b22693ba-fa43-44bb-9b2d-0c64fad6e3cc
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Shell Infrastructure Improvements

Windows Remote Management version 2.0 (WinRM 2.0) offers many remote shell infrastructure improvements. The following topics describe these improvements in detail:

-   [Multi-Hop Support](multi-hop-support.md)
-   [Quota Management for Remote Shells](quotas.md)

One of the improvements to the WinRM remote shell infrastructure is the addition of a more robust shell manager that maintains user-specific shell information. WinRM users can create shells on remote computers to run commands or scripts. In addition, users can create multiple shells on a computer. Users and administrators both need the ability to manage shells. Users can enumerate, get, and delete the shells that they have created. Administrators can enumerate over all active shells and retrieve details about specific shells on a local or remote host. Administrators can also delete any active shells on a local or remote host.

When a user or administrator enumerates the active shells, the following information can be returned by the WinRM service.

<dl> <dt>

<span id="ShellId"></span><span id="shellid"></span><span id="SHELLID"></span>ShellId
</dt> <dd>

Specifies the unique identifier for the shell.

</dd> <dt>

<span id="Environment_variables"></span><span id="environment_variables"></span><span id="ENVIRONMENT_VARIABLES"></span>Environment variables
</dt> <dd>

Specifies any environment variables set by the user.

</dd> <dt>

<span id="WorkingDirectory"></span><span id="workingdirectory"></span><span id="WORKINGDIRECTORY"></span>WorkingDirectory
</dt> <dd>

Specifies the starting directory for the shell.

</dd> <dt>

<span id="ResourceURI"></span><span id="resourceuri"></span><span id="RESOURCEURI"></span>ResourceURI
</dt> <dd>

Specifies the resource URI for the shell operation. The resource URI can be used to retrieve plug-in configuration that is specific to the shell instance.

</dd> <dt>

<span id="IdleTimeout"></span><span id="idletimeout"></span><span id="IDLETIMEOUT"></span>IdleTimeout
</dt> <dd>

Specifies the maximum duration, in milliseconds, that the shell will stay open without any request.

</dd> <dt>

<span id="InputStreams"></span><span id="inputstreams"></span><span id="INPUTSTREAMS"></span>InputStreams
</dt> <dd>

Specifies the input streams for the shell.

</dd> <dt>

<span id="OutputStreams"></span><span id="outputstreams"></span><span id="OUTPUTSTREAMS"></span>OutputStreams
</dt> <dd>

Specifies the output streams for the shell.

</dd> <dt>

<span id="Shell_creation_time"></span><span id="shell_creation_time"></span><span id="SHELL_CREATION_TIME"></span>Shell creation time
</dt> <dd>

Specifies the creation timestamp for the shell.

</dd> <dt>

<span id="IdleTime"></span><span id="idletime"></span><span id="IDLETIME"></span>IdleTime
</dt> <dd>

Specifies the duration, in milliseconds, that the shell has been idle.

</dd> <dt>

<span id="UserId"></span><span id="userid"></span><span id="USERID"></span>UserId
</dt> <dd>

Specifies the user ID.

</dd> <dt>

<span id="Hostname_or_IP_address"></span><span id="hostname_or_ip_address"></span><span id="HOSTNAME_OR_IP_ADDRESS"></span>Hostname or IP address
</dt> <dd>

Specifies either the host name or IP address of the computer that created the shell.

</dd> <dt>

<span id="Shell_memory_usage"></span><span id="shell_memory_usage"></span><span id="SHELL_MEMORY_USAGE"></span>Shell memory usage
</dt> <dd>

Specifies the amount of memory that has been used by the shell.

</dd> <dt>

<span id="Number_of_processes"></span><span id="number_of_processes"></span><span id="NUMBER_OF_PROCESSES"></span>Number of processes
</dt> <dd>

Specifies the number of processes that have been created by the shell.

</dd> </dl>

## Enumerating a Shell on a Local Host

The following command demonstrates how to use the winrm utility to enumerate shells on a WinRM client: **winrm enumerate shell**.

The following text-based example displays the output for shell enumeration:

``` syntax
Shell
    ShellId = 0A6E6A01-8AB2-4037-86CC-BFC826A1244E
    ResourceUri = http://schemas.microsoft.com/wbem/wsman/1/windows/shell/cmd
    Owner = FABRIKAM\myAccount
    ClientIP = ::1
    IdleTimeOut = PT180.000S
    InputStreams = stdin
    OutputStreams = stdout stderr
    ShellRunTime = P0DT0H0M36S
    ShellInactivity = P0DT0H0M35S

Shell
    ShellId = EE3F11CE-FB3C-4C4E-B113-6F4D643C97D8
    ResourceUri = http://schemas.microsoft.com/powershell/Microsoft.PowerShell
    Owner = FABRIKAM\myAccount
    ClientIP = ::1
    IdleTimeOut = PT180.000S
    InputStreams = stdin pr
    OutputStreams = stdout
    ShellRunTime = P0DT0H1M46S
    ShellInactivity = P0DT0H0M45S
    MemoryUsed = 48MB
    ChildProcesses = 0

Shell
    ShellId = 8FD7F2C4-A434-4D58-A7E8-46F8BF202D0B
    ResourceUri = http://schemas.microsoft.com/powershell/Microsoft.PowerShell
    Owner = FABRIKAM\myAccount
    ClientIP = ::1
    IdleTimeOut = PT180.000S
    InputStreams = stdin pr
    OutputStreams = stdout
    ShellRunTime = P0DT0H1M47S
    ShellInactivity = P0DT0H0M47S
    MemoryUsed = 48MB
    ChildProcesses = 0
```

For more information, see the online help provided by running the following command: **winrm enumerate -?**.

## Retrieving Information About a Specific Shell

An administrator or user can also use the ShellId identifier to retrieve information about the shell. The following command demonstrates how to use the winrm utility to get information about a specific shell: **winrm get shell?ShellId=0A6E6A01-8AB2-4037-86CC-BFC826A1244E**.

The following text-based example displays the output for shell information:

``` syntax
Shell
    ShellId = 0A6E6A01-8AB2-4037-86CC-BFC826A1244E
    ResourceUri = http://schemas.microsoft.com/wbem/wsman/1/windows/shell/cmd
    Owner = FABRIKAM\myAccount
    ClientIP = ::1
    IdleTimeOut = PT180.000S
    InputStreams = stdin
    OutputStreams = stdout stderr
    ShellRunTime = P0DT0H0M36S
    ShellInactivity = P0DT0H0M35S
```

For more information, see the online help provided by the following command: **winrm get -?**.

## Related topics

<dl> <dt>

[Multi-Hop Support](multi-hop-support.md)
</dt> <dt>

[Quota Management for Remote Shells](quotas.md)
</dt> <dt>

[Managed Reference for WS-Management PowerShell Commands](winrm-powershell-commandlets.md)
</dt> </dl>

 

 




