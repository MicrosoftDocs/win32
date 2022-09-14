---
title: Authorization Plug-in Methods
description: All authorization plug-in entry points have a callback mechanism to report the success or failure of the call. Some callback mechanisms are called multiple times until all of the results are reported.
ms.assetid: 6d7c1c54-fab5-431b-b123-eee6fd4dfb92
ms.tgt_platform: multiple
ms.topic: reference
ms.date: 05/31/2018
---

# Authorization Plug-in Methods

All authorization plug-in entry points have a callback mechanism to report the success or failure of the call. Some callback mechanisms are called multiple times until all of the results are reported.

The following table provides an overview of the authorization callback methods.



| Method                                                                           | Description                                                          |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**WSManPluginAuthzOperationComplete**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginauthzoperationcomplete)   | Reports either a successful or failed user operation.                |
| [**WSManPluginAuthzQueryQuotaComplete**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginauthzqueryquotacomplete) | Reports quota details that are relevant for the specified user.      |
| [**WSManPluginAuthzUserComplete**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginauthzusercomplete)             | Reports either a successful or failed user connection authorization. |



 

 

 




