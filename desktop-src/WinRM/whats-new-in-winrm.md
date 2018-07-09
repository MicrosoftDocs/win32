---
title: What's New in WinRM 2.0
description: New features are available in Windows Remote Management version 2.0. (WinRM 2.0).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 402c179a-6dd7-4d75-9318-bb8194b5527d
ms.prod: windows-server-dev
ms.technology: windows-remote-management
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
<td>[WinRM Client Shell API](client-shell-api.md)<br/></td>
<td>The WinRM Client Shell application programming interface (API) provides functionality to create and manage shells and shell operations, commands, and data streams on remote computers. <br/></td>
</tr>
<tr class="even">
<td>[WinRM Plugin API](winrm-plugin-api.md)<br/></td>
<td>The WinRM Plug-in API provides functionality that enables a user to write plug-ins by implementing certain APIs for supported [<em>resource URIs</em>](windows-remote-management-glossary.md) and operations.<br/></td>
</tr>
<tr class="odd">
<td>[Infrastructure for Managing Hosted Services](winrm-application-hosting.md)<br/></td>
<td>WinRM 2.0 introduces a hosting framework. Two hosting models are supported. One is Internet Information Service (IIS)–based and the other is WinRM–service based. <br/> For more information about the host configuration, see the following topics:<br/>
<ul>
<li>[IIS Host Plug-in Configuration](iis-host-plug-in-configuration.md)</li>
<li>[WinRM Service Plug-in Configuration](wsman-service-plug-in-configuration.md)</li>
</ul></td>
</tr>
<tr class="even">
<td>[DMTF Profile Discovery through Association Traversal](dmtf-association-traversal.md)<br/></td>
<td>Association traversal enables a user to retrieve instances of Association classes by using a standard filtering mechanism.<br/></td>
</tr>
<tr class="odd">
<td>[Remote Shell infrastructure improvements](remote-shell-infrastructure-improvements.md)<br/></td>
<td>This topic includes information about the remote infrastructure improvements for WinRM. <br/></td>
</tr>
<tr class="even">
<td>[Multi-hop Support](multi-hop-support.md)<br/></td>
<td>Functionality was added to WinRM 2.0 that supports delegating user credentials across multiple remote computers. <br/> The [<strong>Authentication Constants</strong>](authentication-constants.md) topic was updated to add the following constant: <strong>WSManFlagUseCredSsp</strong>.<br/> The following C++ API was added to provide multi-hop support: [<strong>IWSManEx3</strong>](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanex3).<br/> The following scripting API was added to provide multi-hop support: [<strong>WSMan.SessionFlagUseCredSsp</strong>](wsman-sessionflagusecredssp.md).<br/></td>
</tr>
<tr class="odd">
<td>[Quota Management for Remote Shells](quotas.md)<br/></td>
<td>This topic includes information about quota configuration for remote shell management.<br/></td>
</tr>
<tr class="even">
<td>[Managed Reference for WS-Management PowerShell Commands](winrm-powershell-commandlets.md)<br/></td>
<td>Users of WinRM 2.0 can use Windows PowerShell cmdlets for system management.<br/></td>
</tr>
</tbody>
</table>



 

 

 





