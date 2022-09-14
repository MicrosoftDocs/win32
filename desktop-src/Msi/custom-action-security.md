---
description: The installer runs custom actions with user privileges by default in order to limit the access of custom actions to the system.
ms.assetid: 62a3d103-a786-4727-b757-3a8229c8a53f
title: Custom Action Security
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Security

The installer runs custom actions with user privileges by default in order to limit the access of custom actions to the system. The installer may run custom actions with elevated privileges if a managed application is being installed or if the system policy has been specified for elevated privileges.

You should use the [**MsiHiddenProperties**](msihiddenproperties.md) property and **msidbCustomActionTypeHideTarget** to prevent logging of sensitive information used by the custom action. For more information about **msidbCustomActionTypeHideTarget** see [Custom Action Hidden Target Option](custom-action-hidden-target-option.md).

Clear the CustomActionData property after setting it to ensure that sensitive data is no longer available. Example code below is a snippet used by an immediate DLL custom action that is setting up data for use by a deferred custom action called "MyDeferredCA":


```C++
#include <windows.h>
#include <Msiquery.h>
#pragma comment(lib, "msi.lib")

UINT __stdcall MyImmediateCA(MSIHANDLE hInstall)
{
    // set up information for deferred custom action called MyDeferredCA
    const TCHAR szValue[] = TEXT("data");
    UINT uiStat = ERROR_INSTALL_FAILURE;
    if (ERROR_SUCCESS == MsiSetProperty(hInstall, TEXT("MyDeferredCA"), szValue))
    {
        uiStat = MsiDoAction(hInstall, TEXT("MyDeferredCA"));

        // clear CustomActionData property
        if (ERROR_SUCCESS != MsiSetProperty(hInstall, TEXT("MyDeferredCA"), TEXT("")))
            return ERROR_INSTALL_FAILURE;
    }

    return (uiStat == ERROR_SUCCESS) ? uiStat : ERROR_INSTALL_FAILURE;    
}
```



Note that only [deferred execution custom actions](deferred-execution-custom-actions.md) can use the **msidbCustomActionTypeNoImpersonate** attribute. For more information see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

If the **msidbCustomActionTypeNoImpersonate** bit is not set for a custom action, the installer runs the custom action with user-level privileges. For more information, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

If the **msidbCustomActionTypeNoImpersonate** bit is set and a managed application is being installed with administrator permission, the installer may run the custom action with elevated privileges. However, if a user attempts to install the managed application without administrator permission, the installer runs the application with user level privileges regardless of whether **msidbCustomActionTypeNoImpersonate** is set.

Note that a custom action may run with system privileges even when the **msidbCustomActionTypeNoImpersonate** bit is not set. This occurs if an administrator installs the application for all users on a server running the Terminal Server role service using Windows 2000 and the action is not marked with **msidbCustomActionTypeTSAware**. A custom action may also run with system privileges if the installation is invoked when there is no user context. For example, if there is no currently logged-on user during an installation invoked by Windows 2000 Application Deployment.

When creating your own custom actions, you should always author the custom action using secure methods. For more information, see [Guidelines for Securing Custom Actions](guidelines-for-securing-custom-actions.md).

 

 



