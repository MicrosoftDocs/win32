---
description: The following topics describe symbol files and the functionality provided by the DbgHelp functions.
ms.assetid: 1bae2f0a-94a4-4152-bccc-b4deb1291a09
title: About DbgHelp
ms.topic: article
ms.date: 05/31/2018
---

# About DbgHelp

The following topics describe symbol files and the functionality provided by the [DbgHelp functions](dbghelp-functions.md).

-   [DbgHelp Versions](dbghelp-versions.md)
-   [Symbol Files](symbol-files.md)
-   [Symbol Handling](symbol-handling.md)
-   [Symbol Servers and Symbol Stores](symbol-servers-and-symbol-stores.md)
-   [Minidump Files](minidump-files.md)
-   [Source Server](source-server-and-source-indexing.md)
-   [Updated Platform Support](updated-platform-support.md)

Note that all [DbgHelp functions](dbghelp-functions.md) are single threaded. Therefore, calls from more than one thread to this function will likely result in unexpected behavior or memory corruption. To avoid this, you must synchronize all concurrent calls from more than one thread to this function.

 

 



