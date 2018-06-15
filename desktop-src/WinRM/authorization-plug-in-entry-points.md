---
title: Authorization Plug-in Entry Points
description: Authorization Plug-in Entry Points
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6cbfa79a-b57b-44b8-a421-d5e79c1b3757
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Authorization Plug-in Entry Points

Authorization plug-ins are configured only for an Internet Information Services (IIS) host process. Only one authorization plug-in can be configured per virtual directory.

All authorization plug-ins must support the following entry points:

-   [**WSManPluginStartup**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_startup)
-   [**WSManPluginShutdown**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_shutdown)
-   [**WSManPluginAuthzUser**](https://msdn.microsoft.com/en-us/library/Dd891168(v=VS.85).aspx)
-   [**WSManPluginAuthzOperation**](https://msdn.microsoft.com/en-us/library/Dd891165(v=VS.85).aspx)

The following entry point is optional:

-   [**WSManPluginAuthzQueryQuota**](https://msdn.microsoft.com/en-us/library/Dd891166(v=VS.85).aspx)

The following table provides an overview of the authorization plug-in entry points in the Windows Remote Management (WinRM) Plug-in API.



| Function                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_OPERATION**](https://msdn.microsoft.com/en-us/library/Dd891165(v=VS.85).aspx)              | Called to authorize a specific operation. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzOperation**](https://msdn.microsoft.com/en-us/library/Dd891165(v=VS.85).aspx).<br/>                                                                                                                                                                                                       |
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_QUERY\_QUOTA**](https://msdn.microsoft.com/en-us/library/Dd891165(v=VS.85).aspx)           | Called after a connection has been authorized to retrieve quota information for the user. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzQueryQuota**](https://msdn.microsoft.com/en-us/library/Dd891166(v=VS.85).aspx).<br/>                                                                                                                                                    |
| [**WSMAN\_PLUGIN\_ AUTHORIZE\_RELEASE\_CONTEXT**](https://msdn.microsoft.com/en-us/library/Dd891167(v=VS.85).aspx) | Called to release the context that a plug-in reports from either the [**WSManPluginAuthzUserComplete**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginauthzusercomplete) or [**WSManPluginAuthzOperationComplete**](/windows/desktop/api/Wsman/nf-wsman-wsmanpluginauthzoperationcomplete) methods. <br/> The DLL entry point name for this method must be [**WSManPluginAuthzReleaseContext**](https://msdn.microsoft.com/en-us/library/Dd891167(v=VS.85).aspx).<br/> |
| [**WSMAN\_PLUGIN\_AUTHORIZE\_USER**](https://msdn.microsoft.com/en-us/library/Dd891168(v=VS.85).aspx)                         | Called to determine whether the user is allowed to carry out a request. <br/> The dynamic-link library (DLL) entry point name for this method must be [**WSManPluginAuthzUser**](https://msdn.microsoft.com/en-us/library/Dd891168(v=VS.85).aspx).<br/>                                                                                                                                                            |



 

 

 





