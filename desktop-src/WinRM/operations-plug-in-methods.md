---
title: Operations Plug-in Methods
description: Operations Plug-in Methods
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 81fe751f-51fd-4da6-b44a-0af9007eea9a
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Operations Plug-in Methods

All operations plug-in entry points have a callback mechanism to report the success or failure of the call. Some callback mechanisms are called multiple times, until all of the results are reported.

The following table provides an overview of the operations callback methods.



| Method                                                                         | Description                                                                                                                                          |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSManPluginFreeRequestDetails**](/windows/win32/Wsman/nf-wsman-wsmanpluginfreerequestdetails?branch=master)         | Releases memory that is allocated for the [**WSMAN\_PLUGIN\_REQUEST**](/windows/win32/Wsman/ns-wsman-_wsman_plugin_request?branch=master) structure.                                          |
| [**WSManPluginGetOperationParameters**](/windows/win32/Wsman/nf-wsman-wsmanplugingetoperationparameters?branch=master) | Gets operational information, such as time-outs and data restrictions that are associated with an operation.                                         |
| [**WSManPluginOperationComplete**](/windows/win32/Wsman/nf-wsman-wsmanpluginoperationcomplete?branch=master)           | Records the completion of an operation.                                                                                                              |
| [**WSManPluginReceiveResult**](/windows/win32/Wsman/nf-wsman-wsmanpluginreceiveresult?branch=master)                   | Reports results to Windows Remote Management (WinRM) plug-ins.                                                                                       |
| [**WSManPluginReportContext**](/windows/win32/Wsman/nf-wsman-wsmanpluginreportcontext?branch=master)                   | Reports the shell and command context back to the WinRM infrastructure so that further operations can be performed against the shell and/or command. |



 

 

 




