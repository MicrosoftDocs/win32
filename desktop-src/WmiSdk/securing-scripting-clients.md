---
description: Scripts and Visual Basic applications must set DCOM security, especially for remote access, and may also need to enable privileges.
ms.assetid: 4816914d-a1cf-47d8-af20-2b22c53042d6
ms.tgt_platform: multiple
title: Securing Scripting Clients
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Securing Scripting Clients

Scripts and Visual Basic applications must set DCOM security, especially for remote access, and may also need to enable privileges.

## Default Access Permissions

WMI access differs between local and remote computers. For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

The following are the default access permissions by account:

-   Everyone, LocalService, NetworkService

    Permission to read or write data and to run [*provider methods*](gloss-p.md) on the local computer. These accounts cannot create new classes or install new providers.

-   Administrator accounts

    Full control on local computer. When connecting to a remote computer, the account must be a local administrator on the remote computer also.

## Securing a Scripting Client

WMI scripting and Visual Basic applications must set DCOM security levels appropriately for the operating systems they are targeting. For more information, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

When connecting to a remote computer, you may need to change the service (NTLM or Kerberos) that handles authentication. For more information, see [Setting the Authentication Service Using VBScript](setting-the-authentication-service-using-vbscript.md).

Access to some WMI classes or data may require a privilege that is not enabled. For example, you must include the Security privilege when connecting to the [**Win32\_NTEventlogFile**](/previous-versions/windows/desktop/legacy/aa394225(v=vs.85)) class. For more information, see [Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md).

If you are accessing WMI from an Active Server Page (ASP), then some IIS configuration is required. For more information, see [Configuring IIS 5.0 and Later for WMI ASP Scripting](configuring-iis-5-for-wmi-asp-scripting.md).

You may be trying to connect to a namespace which requires an encrypted connection, in other words, one that requires an authentication level of pktPrivacy. For more information, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

 

 
