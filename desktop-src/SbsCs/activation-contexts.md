---
description: Activation contexts are data structures in memory containing information that the system can use to redirect an application to load a particular DLL version, COM object instance, or custom window version.
ms.assetid: 5416f8c0-d99b-4a5d-a689-a47bd0cf1a88
title: Activation Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Activation Contexts

[*Activation contexts*](a-sbscs-gly.md) are data structures in memory containing information that the system can use to redirect an application to load a particular DLL version, COM object instance, or custom window version. One section of the activation context may contain DLL redirection information which is used by the DLL loader; another section may contain COM server information. The activation context functions use, create, activate, and deactivate activation contexts. The activation functions can redirect the binding of an application to version-named objects that specify particular DLL versions, window classes, COM servers, type libraries, and interfaces. For more information about the activation context functions and structures, see the [Activation Context Reference](activation-context-reference.md).

Beginning with Windows XP, activation context functions enable Windows to use information in [manifests](manifests.md) to create version-named objects. If an application creates a process by calling [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa), Windows checks for the existence of an [application manifest](application-manifests.md). If a manifest exists, Windows uses the information in the manifest to populate the activation context. Because manifests describe an application's dependence on [side-by-side assembly](about-side-by-side-assemblies-.md) versions, objects specified without versions in the manifest are mapped to version-named objects. For example, the manifest may describe DLLs, files, window classes, COM servers, type libraries, and interfaces.

When a global object is created within the activation context, the system automatically gives the object a version-specific name by consulting the manifest. When the application executes and requests a named object, it gets the version-named object. This enables multiple versions of a code module to run on the system at the same time without interfering with each other. For example, [Windows Shell](/previous-versions/windows/desktop/legacy/bb776778(v=vs.85)) uses a manifest to describe a dependence on version 6.0 of COMCTL32 and to create versions of window classes.

If an application creates a resource by calling [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa), the process specifies a class name to that function. The call to [**GetCurrentActCtx**](/windows/desktop/api/Winbase/nf-winbase-getcurrentactctx) gets the current activation context and checks to see if a mapping exists for the given class name. If a mapping exists, it will use that version of the calling process to resolve the mapping and provide the version-specific class name. Windows creates a window with the window procedure, styles, and other attributes associated with that class name and version.

The activation context is managed by the system in most cases. Application developers and assembly providers do not commonly need to make calls to the stack. Applications can manage an activation context by directly calling the activation context. For more information, see [Using the Activation Context API](using-the-activation-context-api.md).

 

 
