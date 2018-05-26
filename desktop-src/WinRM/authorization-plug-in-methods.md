---
title: Authorization Plug-in Methods
description: All authorization plug-in entry points have a callback mechanism to report the success or failure of the call. Some callback mechanisms are called multiple times until all of the results are reported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6d7c1c54-fab5-431b-b123-eee6fd4dfb92
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Authorization Plug-in Methods

All authorization plug-in entry points have a callback mechanism to report the success or failure of the call. Some callback mechanisms are called multiple times until all of the results are reported.

The following table provides an overview of the authorization callback methods.



| Method                                                                           | Description                                                          |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**WSManPluginAuthzOperationComplete**](/windows/win32/Wsman/nf-wsman-wsmanpluginauthzoperationcomplete?branch=master)   | Reports either a successful or failed user operation.                |
| [**WSManPluginAuthzQueryQuotaComplete**](/windows/win32/Wsman/nf-wsman-wsmanpluginauthzqueryquotacomplete?branch=master) | Reports quota details that are relevant for the specified user.      |
| [**WSManPluginAuthzUserComplete**](/windows/win32/Wsman/nf-wsman-wsmanpluginauthzusercomplete?branch=master)             | Reports either a successful or failed user connection authorization. |



 

 

 




