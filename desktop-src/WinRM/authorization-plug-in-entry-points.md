---
title: Authorization Plug-in Entry Points
description: Authorization Plug-in Entry Points
ms.assetid: 6cbfa79a-b57b-44b8-a421-d5e79c1b3757
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Authorization Plug-in Entry Points

Authorization plug-ins are configured only for an Internet Information Services (IIS) host process. Only one authorization plug-in can be configured per virtual directory.

All authorization plug-ins must support the following entry points:

-   [**WSManPluginStartup**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_startup)
-   [**WSManPluginShutdown**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_shutdown)
-   [**WSManPluginAuthzUser**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_user)
-   [**WSManPluginAuthzOperation**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_operation)

The following entry point is optional:

-   [**WSManPluginAuthzQueryQuota**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_query_quota)

The following table provides an overview of the authorization plug-in entry points in the Windows Remote Management (WinRM) Plug-in API.



| Function                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_OPERATION**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_operation)              | Called to authorize a specific operation. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzOperation**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_operation).<br/>                                                                                                                                                                                                       |
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_QUERY\_QUOTA**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_operation)           | Called after a connection has been authorized to retrieve quota information for the user. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzQueryQuota**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_query_quota).<br/>                                                                                                                                                    |
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_RELEASE\_CONTEXT**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_release_context) | Called to release the context that a plug-in reports from either the [**WSManPluginAuthzUserComplete**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginauthzusercomplete) or [**WSManPluginAuthzOperationComplete**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginauthzoperationcomplete) methods. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzReleaseContext**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_release_context).<br/> |
| [**WSMAN\_PLUGIN\_AUTHORIZE\_USER**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_user)                         | Called to determine whether the user is allowed to carry out a request. <br/> The dynamic-link library (DLL) entry point name for this method must be [**WSManPluginAuthzUser**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_authorize_user).<br/>                                                                                                                                                            |



 

 

