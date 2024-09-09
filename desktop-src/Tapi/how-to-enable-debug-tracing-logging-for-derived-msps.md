---
description: The following procedure describes how to enable debug tracing and logging.
ms.assetid: 52381397-df75-4d81-a048-f0ed408ac6b8
title: How to Enable Debug Tracing/Logging for Derived MSPs
ms.topic: article
ms.date: 05/31/2018
---

# How to Enable Debug Tracing/Logging for Derived MSPs

First, make sure that the implementation of the derived MSP has followed the guidelines in the previous section with regard to debug tracing (defining the preprocessor symbol MSPLOG, registering for tracing during DllMain, and using the LOG macro for tracing). Find out what name the MSP uses when registering for tracing (this should usually be the DLL's name; it is referred to below as "&lt;dll name&gt;"). To enable tracing, use a registry editor ("Regedit.exe" or "Regedt32.exe") to locate the key "HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Tracing" and do the following. Note that all of the values mentioned below, except the EnableDebuggerTracing value, should be created automatically after running your MSP for the first time.

-   To enable tracing to user and kernel mode debuggers, set the **DWORD** value &lt;dll name&gt;\\EnableDebuggerTracing to 1. Optionally, use the **DWORD** value &lt;dll name&gt;\ConsoleTracing Mask to enable or disable various levels of trace output (the default is 0xFFFF0000, which enables all trace levels).
-   To enable tracing to a file, set the **DWORD** value &lt;dll name&gt;\\EnableFileTracing to 1. Optionally, use the string value &lt;dll name&gt;\\FileDirectory to adjust the location of the log file. Optionally, use the **DWORD** value &lt;dll name&gt;\\FileTracingMask to enable or disable various levels of trace output (the default is 0xFFFF0000, which enables all trace levels).
-   To enable tracing to a separate console window, separated by DLL, set the **DWORD** value EnableConsoleTracing to 1, AND ALSO set the **DWORD** value &lt;dll name&gt;\\EnableConsoleTracing to 1. Optionally, use the **DWORD** value &lt;dll name&gt;\\ConsoleTracing Mask to enable or disable various levels of trace output (the default is 0xFFFF0000, which enables all trace levels).

 

 



