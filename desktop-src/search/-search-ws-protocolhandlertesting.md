---
title: Debugging protocol handlers
description: Understanding how protocol handlers are launched is integral to testing and debugging your protocol handler implementations.
ms.assetid: 33c99620-7381-4719-9fc6-4c8284481411
ms.topic: how-to
ms.date: 05/31/2018
---

# Debugging protocol handlers

Understanding how protocol handlers are launched is integral to testing and debugging your protocol handler implementations.

This topic is organized as follows:

-   [About Debugging Protocol Handlers](#about-debugging-protocol-handlers)
-   [Setting Up Debugging](#setting-up-debugging)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## About debugging protocol handlers

The SearchIndexer process (searchindexer.exe) launches one copy of the SearchProtocolHost process (SearchProtocolHost.exe) in the system context and another copy in the user context. Then, the protocol handlers are loaded in the SearchProtocolHost process as needed. They are not unloaded until the search service is stopped. The same instance of a protocol handler is reused any number of times while the service is running.

The SearchIndexer and SearchProtocolHost processes communicate frequently during indexing. If you pause or stop the SearchProtocolHost process to debug, the SearchIndexer will launch a new SearchProtocolHost process, invalidating your debugging session. Also, if you attach your debugger directly to the SearchProtocolHost process, you can break handle-inheritance from searchindexer.exe to searchprotocolhost.exe, and the two processes will be unable to communicate.

To avoid these problems, you need to notify the search service that you are debugging, and you need to attach the debugger to the SearchIndexer process with instructions to debug child processes, as described next.

## Setting up debugging

Follow these steps to set up debugging for your protocol handler.

1.  Notify the search service that you are debugging by setting the DebugFilters value to 1 in the registry:

    ```
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft
       Windows Search
          Gathering Manager
             DebugFilters = 1
    ```

2.  Attach a debugger using the Image File Execution Options registry key:

    ```
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
       Image File Execution Options
          SearchIndexer.exe
             Debugger = <path to debugger> <debugger options> 
    ```

    The options for a sample debugger are described in the following table.

    **Example using the ntsd debugger**   *Debugger = C:\\debuggers\\ntsd.exe -odGx -c: "sxe ld mydll.dll;g"*<br/>

3.  Restart searchindexer.exe under the debugger using compmgmt.msc, services.msc, or a command window with commands similar to the following:
    ```
    net stop wsearch
    <copy new DLLs for debugging>
    net start wsearch
    ```

To distinguish between a SearchProtocolHost process running in the system context and one running in the user context, you can review the environment strings. With ntsd.exe, for example, you can use extension command **!peb** to display a formatted view of the information in the process environment block (PEB).

## Additional resources

* For information on creating handlers, see [Registering Shell Extensions](../shell/reg-shell-exts.md).

## Related topics

**Conceptual**

* <a href="-search-3x-wds-phaddins.md">Developing Protocol Handlers</a>
* <a href="-search-3x-wds-extidx-prot-implementing.md">Understanding Protocol Handlers</a>
* <a href="-search-3x-wds-notifyingofchanges.md">Notifying the Index of Changes</a>
* <a href="-search-3x-wds-ph-ui-extensions.md">Adding Icons and Context Menus</a>
* <a href="-search-3x-wds-ph-ui-samplecode.md">Code Sample: Shell Extensions for Protocol Handlers</a>
* <a href="-search-3x-wds-ph-search-connector.md">Creating a Search Connector for a Protocol Handler</a>
* <a href="-search-3x-wds-ph-install-registration.md">Installing and Registering Protocol Handlers</a>
