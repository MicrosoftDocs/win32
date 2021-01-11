---
description: The AnyPath data type is a text string containing either a full path or a relative path.
ms.assetid: fe8a4d2a-1960-40af-a0e4-4d65accdd388
title: AnyPath
ms.topic: article
ms.date: 05/31/2018
---

# AnyPath

The AnyPath data type is a text string containing either a full path or a relative path. When specifying a relative path, you can include a long file name with the short file name by separating the short and long names with a vertical bar (\|). Note that you cannot specify multiple levels of a directory or fully qualified paths in this way. The path may contain properties enclosed within square brackets (\[ \]).

Examples of valid AnyPath data:

-   \\\\server\\share\\temp
-   c:\\temp
-   \\temp
-   projec~1\|Project Status

Examples of invalid AnyPath data:

-   c:\\temp\\projec~1\|c:\\temp one\\Project Status
-   \\temp\\projec~1\|\\temp one\\Project Status

 

 



