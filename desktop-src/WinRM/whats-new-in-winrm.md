---
title: What's New in WinRM 2.0
description: New features are available in Windows Remote Management version 2.0. (WinRM 2.0).
ms.assetid: 402c179a-6dd7-4d75-9318-bb8194b5527d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# What's New in WinRM 2.0

New features are available in Windows Remote Management version 2.0. (WinRM 2.0)

WinRM 2.0 is included in Windows Server 2008 R2 and Windows 7.

You can also download WinRM 2.0 for Windows Server 2008 with Service Pack 2 (SP2) and Windows Vista with Service Pack 2 (SP2).

The following table lists the documentation for WinRM 2.0.




| Topic | Description | 
|-------|-------------|
| <a href="client-shell-api.md">WinRM Client Shell API</a><br /> | The WinRM Client Shell application programming interface (API) provides functionality to create and manage shells and shell operations, commands, and data streams on remote computers. <br /> | 
| <a href="winrm-plugin-api.md">WinRM Plugin API</a><br /> | The WinRM Plug-in API provides functionality that enables a user to write plug-ins by implementing certain APIs for supported <a href="windows-remote-management-glossary.md"><em>resource URIs</em></a> and operations.<br /> | 
| <a href="winrm-application-hosting.md">Infrastructure for Managing Hosted Services</a><br /> | WinRM 2.0 introduces a hosting framework. Two hosting models are supported. One is Internet Information Service (IIS)–based and the other is WinRM–service based. <br /> For more information about the host configuration, see the following topics:<br /><ul><li><a href="iis-host-plug-in-configuration.md">IIS Host Plug-in Configuration</a></li><li><a href="wsman-service-plug-in-configuration.md">WinRM Service Plug-in Configuration</a></li></ul> | 
| <a href="dmtf-association-traversal.md">DMTF Profile Discovery through Association Traversal</a><br /> | Association traversal enables a user to retrieve instances of Association classes by using a standard filtering mechanism.<br /> | 
| <a href="remote-shell-infrastructure-improvements.md">Remote Shell infrastructure improvements</a><br /> | This topic includes information about the remote infrastructure improvements for WinRM. <br /> | 
| <a href="multi-hop-support.md">Multi-hop Support</a><br /> | Functionality was added to WinRM 2.0 that supports delegating user credentials across multiple remote computers. <br /> The <a href="authentication-constants.md"><strong>Authentication Constants</strong></a> topic was updated to add the following constant: <strong>WSManFlagUseCredSsp</strong>.<br /> The following C++ API was added to provide multi-hop support: <a href="/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanex3"><strong>IWSManEx3</strong></a>.<br /> The following scripting API was added to provide multi-hop support: <a href="wsman-sessionflagusecredssp.md"><strong>WSMan.SessionFlagUseCredSsp</strong></a>.<br /> | 
| <a href="quotas.md">Quota Management for Remote Shells</a><br /> | This topic includes information about quota configuration for remote shell management.<br /> | 
| <a href="winrm-powershell-commandlets.md">Managed Reference for WS-Management PowerShell Commands</a><br /> | Users of WinRM 2.0 can use Windows PowerShell cmdlets for system management.<br /> | 




 

 

 





