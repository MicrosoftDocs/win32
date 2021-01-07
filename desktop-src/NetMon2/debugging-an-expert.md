---
description: Use the following procedure to debug experts written in Microsoft Visual C++.
ms.assetid: 7356fcae-3cfe-4a5b-86dd-bebee859fa19
title: Debugging an Expert
ms.topic: article
ms.date: 05/31/2018
---

# Debugging an Expert

Use the following procedure to debug experts written in Microsoft Visual C++.

**Debugging an Expert**

1.  Install the expert (DLL file) and the program database file (.pdb) generated when you compiled the expert in the correct location. For further details, see [Installing an Expert to Network Monitor 2.1](installing-an-expert-to-network-monitor-2-1.md).
2.  Start Microsoft Visual C++.
3.  From the **File** menu, click **Open** and select the name of your expert DLL.
4.  After Microsoft Visual C++ loads, click the **Project** menu and then click **Settings**.
5.  Click **Debug**. Under **Executable for debug session**, type the full path of Netmon.exe, for example:

    ``` syntax
    C:\Program files\Netmon2\Netmon.exe
    ```

6.  Set the breakpoints in your code.

 

 



