---
title: What's New in WinRM 2.0
description: New features are available in Windows Remote Management version 2.0. (WinRM 2.0).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 402c179a-6dd7-4d75-9318-bb8194b5527d
ms.tgt_platform: multiple
ms.author: windowssdkdev
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

You can also download WinRM 2.0 for Windows Server 2008 with Service Pack 2 (SP2) and Windows Vista with Service Pack 2 (SP2). For information about downloading WinRM 2.0, see [KB968929](http://go.microsoft.com/fwlink/p/?linkid=151321).

The following table lists the documentation for WinRM 2.0.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="client-shell-api">WinRM Client Shell API</a><br/></td>
<td>The WinRM Client Shell application programming interface (API) provides functionality to create and manage shells and shell operations, commands, and data streams on remote computers. <br/></td>
</tr>
<tr class="even">
<td><a href="winrm-plugin-api">WinRM Plugin API</a><br/></td>
<td>The WinRM Plug-in API provides functionality that enables a user to write plug-ins by implementing certain APIs for supported <a href="windows-remote-management-glossary"><em>resource URIs</em></a> and operations.<br/></td>
</tr>
<tr class="odd">
<td><a href="winrm-application-hosting">Infrastructure for Managing Hosted Services</a><br/></td>
<td>WinRM 2.0 introduces a hosting framework. Two hosting models are supported. One is Internet Information Service (IIS)–based and the other is WinRM–service based. <br/> For more information about the host configuration, see the following topics:<br/>
<ul>
<li><a href="iis-host-plug-in-configuration">IIS Host Plug-in Configuration</a></li>
<li><a href="wsman-service-plug-in-configuration">WinRM Service Plug-in Configuration</a></li>
</ul></td>
</tr>
<tr class="even">
<td><a href="dmtf-association-traversal">DMTF Profile Discovery through Association Traversal</a><br/></td>
<td>Association traversal enables a user to retrieve instances of Association classes by using a standard filtering mechanism.<br/></td>
</tr>
<tr class="odd">
<td><a href="remote-shell-infrastructure-improvements">Remote Shell infrastructure improvements</a><br/></td>
<td>This topic includes information about the remote infrastructure improvements for WinRM. <br/></td>
</tr>
<tr class="even">
<td><a href="multi-hop-support">Multi-hop Support</a><br/></td>
<td>Functionality was added to WinRM 2.0 that supports delegating user credentials across multiple remote computers. <br/> The <a href="authentication-constants"><strong>Authentication Constants</strong></a> topic was updated to add the following constant: <strong>WSManFlagUseCredSsp</strong>.<br/> The following C++ API was added to provide multi-hop support: <a href="/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanex3"><strong>IWSManEx3</strong></a>.<br/> The following scripting API was added to provide multi-hop support: <a href="wsman-sessionflagusecredssp"><strong>WSMan.SessionFlagUseCredSsp</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="quotas">Quota Management for Remote Shells</a><br/></td>
<td>This topic includes information about quota configuration for remote shell management.<br/></td>
</tr>
<tr class="even">
<td><a href="winrm-powershell-commandlets">Managed Reference for WS-Management PowerShell Commands</a><br/></td>
<td>Users of WinRM 2.0 can use Windows PowerShell cmdlets for system management.<br/></td>
</tr>
</tbody>
</table>



 

 

 





