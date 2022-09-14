---
title: Operations Plug-in Methods
description: Operations Plug-in Methods
ms.assetid: 81fe751f-51fd-4da6-b44a-0af9007eea9a
ms.tgt_platform: multiple
ms.topic: reference
ms.date: 05/31/2018
---

# Operations Plug-in Methods

All operations plug-in entry points have a callback mechanism to report the success or failure of the call. Some callback mechanisms are called multiple times, until all of the results are reported.

The following table provides an overview of the operations callback methods.



| Method                                                                         | Description                                                                                                                                          |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSManPluginFreeRequestDetails**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginfreerequestdetails)         | Releases memory that is allocated for the [**WSMAN\_PLUGIN\_REQUEST**](/windows/desktop/api/Wsman/ns-wsman-wsman_plugin_request) structure.                                          |
| [**WSManPluginGetOperationParameters**](/windows/desktop/api/Wsman/nf-wsman-wsmanplugingetoperationparameters) | Gets operational information, such as time-outs and data restrictions that are associated with an operation.                                         |
| [**WSManPluginOperationComplete**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginoperationcomplete)           | Records the completion of an operation.                                                                                                              |
| [**WSManPluginReceiveResult**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginreceiveresult)                   | Reports results to Windows Remote Management (WinRM) plug-ins.                                                                                       |
| [**WSManPluginReportContext**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginreportcontext)                   | Reports the shell and command context back to the WinRM infrastructure so that further operations can be performed against the shell and/or command. |



 

 

 




