---
title: Authorization Plug-in Entry Points
description: Authorization Plug-in Entry Points
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6cbfa79a-b57b-44b8-a421-d5e79c1b3757'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-remote-management'
ms.tgt_platform: multiple
---

# Authorization Plug-in Entry Points

Authorization plug-ins are configured only for an Internet Information Services (IIS) host process. Only one authorization plug-in can be configured per virtual directory.

All authorization plug-ins must support the following entry points:

-   [**WSManPluginStartup**](wsman-plugin-startup.md)
-   [**WSManPluginShutdown**](wsman-plugin-shutdown.md)
-   [**WSManPluginAuthzUser**](wsman-plugin-authorize-user.md)
-   [**WSManPluginAuthzOperation**](wsman-plugin-authorize-operation.md)

The following entry point is optional:

-   [**WSManPluginAuthzQueryQuota**](wsman-plugin-authorize-query-quota.md)

The following table provides an overview of the authorization plug-in entry points in the Windows Remote Management (WinRM) Plug-in API.



| Function                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_OPERATION**](wsman-plugin-authorize-operation.md)              | Called to authorize a specific operation. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzOperation**](wsman-plugin-authorize-operation.md).<br/>                                                                                                                                                                                                       |
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_QUERY\_QUOTA**](wsman-plugin-authorize-operation.md)           | Called after a connection has been authorized to retrieve quota information for the user. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzQueryQuota**](wsman-plugin-authorize-query-quota.md).<br/>                                                                                                                                                    |
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_RELEASE\_CONTEXT**](wsman-plugin-authorize-release-context.md) | Called to release the context that a plug-in reports from either the [**WSManPluginAuthzUserComplete**](wsmanpluginauthzusercomplete.md) or [**WSManPluginAuthzOperationComplete**](wsmanpluginauthzoperationcomplete.md) methods. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzReleaseContext**](wsman-plugin-authorize-release-context.md).<br/> |
| [**WSMAN\_PLUGIN\_AUTHORIZE\_USER**](wsman-plugin-authorize-user.md)                         | Called to determine whether the user is allowed to carry out a request. <br/> The dynamic-link library (DLL) entry point name for this method must be [**WSManPluginAuthzUser**](wsman-plugin-authorize-user.md).<br/>                                                                                                                                                            |



 

 

 





