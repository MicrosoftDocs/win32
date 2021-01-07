---
description: Applications can manage an activation context by directly calling the activation context functions.
ms.assetid: 606147a8-435d-43d4-8fb5-79d2d1a8d870
title: Using the Activation Context API
ms.topic: article
ms.date: 05/31/2018
---

# Using the Activation Context API

Applications can manage an [activation context](activation-contexts.md) by directly calling the activation context functions. Activation contexts are data structures in memory. The system can use the information in the activation context to redirect an application to load a particular DLL version, COM object instance, or custom window version. For more information, see [Activation Context Reference](activation-context-reference.md).

The application programming interface (API) can be used to manage the activation context and create version-named objects with [manifests](manifests.md). The following two scenarios illustrate how an application can manage an activation context by directly calling the activation context functions. In most cases however, the activation context is managed by the system. Application developers and assembly providers do not commonly need to make calls to the stack to manage the activation context.

-   Processes and applications that implement indirection or dispatch layers.

    For example, a user managing activation contexts in the event loop. Each time the window is accessed, such as by moving the mouse over the window, [**ActivateActCtx**](/windows/desktop/api/Winbase/nf-winbase-activateactctx) is called, which activates the current activation context for the resource, as shown in the following code fragment.

    <dl> HANDLE hActCtx;  
    CreateWindow();  
    ...  
    GetCurrentActCtx(&ActCtx);  
    ...  
    ReleaseActCtx(&ActCtx);  
    </dl>

    In the following code fragment, the API function activates the appropriate activation contexts before calling [**CallWindowProc**](/windows/win32/api/winuser/nf-winuser-callwindowproca). When **CallWindowProc** is called, it uses this context to pass a message to Windows. When all resource operations have completed, the function will deactivate the context.

    <dl> ULONG\_PTR ulpCookie;  
    HANDLE hActCtx;  
    if(ActivateActCtx(hActCtx, &ulpCookie))  
    {  
    ...  
    CallWindowProc(...);  
    ...  
    DeactivateActCtx(0, ulpCookie);  
    }  
    </dl>

-   Delegator dispatch layer.

    This scenario applies to managers that manage multiple entities with a common API layer, such as a driver manager. Although it has not yet been implemented, an example of this would be the ODBC driver.

    In this scenario, the middle layer becomes capable of processing assembly bindings. To get the version-specific binding driver, publishers must provide a manifest and specify dependencies on specific components in that manifest. The base application does not dynamically bind to the components; at run time, the driver manager manages the calls. When the ODBC driver is called based on the connect string it loads the appropriate driver. It then creates the activation context using the information in the assembly manifest file.

    Without the manifest, the default action for the driver is to use the same context as that specified by the application—in this example, version 2 of MSVCRT. Since a manifest does exist, a separate activation context is established. When the ODBC driver runs, it binds to version 1 of the MSVCRT assembly.

    Each time the driver manager calls the dispatch layer—for example, to get the next set of data—it uses the appropriate assemblies based on the activation context. The following code fragment illustrates this.

    <dl> HANDLE hActCtx;  
    ULONG\_PTR ulpCookie;  
    ACTCTX ActCtxToCreate = {...};  
    hActCtx = CreateActCtx(&ActCtxToCreate);  
    ...;  
    if (ActivateActCtx(hActCtx, &ulpCookie))  
    {  
    ...  
    ConnectDb(...);  
    DeactivateActCtx(0, ulpCookie);  
    }  
    ...  
    ReleaseActCtx(hActCtx);  
    </dl>

 

 
