---
title: NetShell Initialization Procedure
description: NetShell loads all previously installed DLLs upon startup. New DLLs can be installed using the add helper NetShell command.
ms.assetid: 1e9f8d74-3ef3-4ebd-aa9e-8e4131956084
keywords:
- helper NetSh , implementing, initialization
- initialization NetSh
- NetShell NetSh , tasks, initializing
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NetShell Initialization Procedure

NetShell loads all previously installed DLLs upon startup. New DLLs can be installed using the **add helper** NetShell command.

NetShell calls a helper's exposed [**InitHelperDll**](/previous-versions/windows/desktop/api/Netsh/nc-netsh-ns_dll_init_fn) function upon loading the helper's DLL. Within the [**InitHelperDll**](/previous-versions/windows/desktop/api/Netsh/nc-netsh-ns_dll_init_fn) routine, helpers must call the [**RegisterHelper**](/previous-versions/windows/desktop/api/Netsh/nf-netsh-registerhelper) function, but must not call the [**RegisterContext**](/previous-versions/windows/desktop/api/Netsh/nf-netsh-registercontext) function.

The following is an example of an [**InitHelperDll**](/previous-versions/windows/desktop/api/Netsh/nc-netsh-ns_dll_init_fn) function for a "Sample" context:

``` syntax
DWORD WINAPI InitHelperDll(
  DWORD     dwNetshVersion,
  PVOID     pReserved 
)
{
    DWORD dwErr;
    NS_HELPER_ATTRIBUTES attMyAttributes;

    // Register helper. One option is to register a single helper that
    // registers a context for each protocol supported. Alternatively 
    // we could register a different helper for each protocol, where 
    // each helper registers a single context. There's only a 
    // difference if we expect sub-helpers. Since a sub-helper 
    // registers with a parent helper, not a parent context, it is 
    // valid in every context its parent helper registers.

    // Attributes of this helper
    ZeroMemory(&attMyAttributes, sizeof(attMyAttributes));
    attMyAttributes.guidHelper      = g_MyGuid; // GUID of this helper
    attMyAttributes.dwVersion       = SAMPLE_HELPER_VERSION;
    attMyAttributes.pfnStart        = SampleStartHelper;
    attMyAttributes.pfnStop         = NULL;

    dwErr = RegisterHelper(&g_ParentGuid, // GUID of parent helper
                           &attMyAttributes);

    return dwErr;
}
```

After all helper DLLs are initialized, NetShell starts helpers by calling [**NS\_HELPER\_START\_FN**](/previous-versions/windows/desktop/api/Netsh/nc-netsh-ns_helper_start_fn) (the Start function) registered in the [**NS\_CONTEXT\_ATTRIBUTES**](/previous-versions/windows/desktop/api/Netsh/ns-netsh-_ns_context_attributes) structure passed in the *pChildAttributes* parameter of the [**RegisterHelper**](/previous-versions/windows/desktop/api/Netsh/nf-netsh-registerhelper) function call.

Once all helper DLLs are initialized, NetShell starts helpers by calling their exposed [**NS\_HELPER\_START\_FN**](/previous-versions/windows/desktop/api/Netsh/nc-netsh-ns_helper_start_fn) (**start** function) function call, registered in the [**NS\_CONTEXT\_ATTRIBUTES**](/previous-versions/windows/desktop/api/Netsh/ns-netsh-_ns_context_attributes) structure passed in the *pChildAttributes* parameter of the [**RegisterHelper**](/previous-versions/windows/desktop/api/Netsh/nf-netsh-registerhelper) function call. NetShell guarantees that a helper's **start** function will only be called after its parent helper has been started.

In its **start** function routine, a helper should register each of its top-level contexts using the [**RegisterContext**](/previous-versions/windows/desktop/api/Netsh/nf-netsh-registercontext) function supported by its parent helper.

The following is a sample **start** function for a top-level helper for a fictional "Sample" context.

``` syntax
DWORD WINAPI SampleStartHelper(
    CONST GUID *pguidParent,
    DWORD       dwVersion
)
{
    DWORD dwErr;
    //
    // The type of the following variable will depend
    // on the helper we're registering under.  If we're
    // registering directly under NetSh, then the type is
    // NS_CONTEXT_ATTRIBUTES.
    //
    NS_CONTEXT_ATTRIBUTES attMyAttributes;

    ZeroMemory(&attMyAttributes, sizeof(attMyAttributes));

    // Fill in all my attributes
    attMyAttributes.pwszContext   = L"sample";
    attMyAttributes.guidHelper    = g_MyGuid;
    attMyAttributes.dwVersion     = 1;
    attMyAttributes.dwFlags       = 0;
    attMyAttributes.pfnCommitFn   = SampleCommit;
    attMyAttributes.pfnDumpFn     = SampleDump;
    attMyAttributes.pfnConnectFn  = SampleConnect;
    attMyAttributes.ulNumTopCmds  = g_ulNumSampleTopCmds;
    attMyAttributes.pTopCmds      = (CMD_ENTRY (*)[])&g_SampleTopCmds;
    attMyAttributes.ulNumGroups   = g_ulNumSampleCmdGroups;
    attMyAttributes.pCmdGroups    = (CMD_GROUP_ENTRY (*)[])&g_SampleCmdGroups;

    dwErr = RegisterContext(&attMyAttributes);

    return dwErr;
}
```

The differentiating factors between a DLL, helper, and context are the following:

-   A DLL constitutes a single DLL file.
-   A helper has an associated GUID.
-   A context has a textual name.

> [!Note]  
> It is recommended that you have a single helper in each DLL, perhaps registering multiple contexts.

 

When the [**RegisterContext**](/previous-versions/windows/desktop/api/Netsh/nf-netsh-registercontext) function is called, NetShell stores a copy of the top commands and command groups passed therein. If commands can change dynamically, the helper should store the **RegisterContext** pointer for later use, and may pass in zero top commands and zero groups in its exported [**NS\_HELPER\_START\_FN**](/previous-versions/windows/desktop/api/Netsh/nc-netsh-ns_helper_start_fn) function (**start** function). If the commands may have changed since the previous **RegisterContext** call, the helper, in its exposed [**NS\_CONTEXT\_CONNECT\_FN**](/previous-versions/windows/desktop/api/Netsh/nc-netsh-ns_context_connect_fn) (Connect function) routine, should call the **RegisterContext** function again with a current set of commands.

 

 




