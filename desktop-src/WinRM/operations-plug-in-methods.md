---
title: Operations Plug-in Methods
description: Operations Plug-in Methods
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '81fe751f-51fd-4da6-b44a-0af9007eea9a'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-remote-management'
ms.tgt_platform: multiple
---

# Operations Plug-in Methods

All operations plug-in entry points have a callback mechanism to report the success or failure of the call. Some callback mechanisms are called multiple times, until all of the results are reported.

The following table provides an overview of the operations callback methods.



| Method                                                                         | Description                                                                                                                                          |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSManPluginFreeRequestDetails**](wsmanpluginfreerequestdetails.md)         | Releases memory that is allocated for the [**WSMAN\_PLUGIN\_REQUEST**](wsman-plugin-request.md) structure.                                          |
| [**WSManPluginGetOperationParameters**](wsmanplugingetoperationparameters.md) | Gets operational information, such as time-outs and data restrictions that are associated with an operation.                                         |
| [**WSManPluginOperationComplete**](wsmanpluginoperationcomplete.md)           | Records the completion of an operation.                                                                                                              |
| [**WSManPluginReceiveResult**](wsmanpluginreceiveresult.md)                   | Reports results to Windows Remote Management (WinRM) plug-ins.                                                                                       |
| [**WSManPluginReportContext**](wsmanpluginreportcontext.md)                   | Reports the shell and command context back to the WinRM infrastructure so that further operations can be performed against the shell and/or command. |



 

 

 




