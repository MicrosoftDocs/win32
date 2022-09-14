---
title: Debugging an Active Directory Extension
description: The Microsoft Active Directory directory service property sheet, context menu, and object creation wizard extensions documented in this topic are implemented as COM in-proc servers.
ms.assetid: 8c280084-fd2f-4d34-a119-d4e925a68a5c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Debugging an Active Directory Extension

The Microsoft Active Directory directory service property sheet, context menu, and object creation wizard extensions documented in this topic are implemented as COM in-proc servers. That is, each extension is a DLL that runs in the context of the host process. To debug the extension, it is necessary to associate the extension with an application and run the application in a debugger.

## Debugging Active Directory Extensions Displayed in the Windows Shell

Active Directory extensions displayed in the Windows shell are loaded in the context of the Explorer.exe process. These extensions can be debugged like a standard shell extension. For more information about debugging shell extensions, see [Debugging with the Shell](/previous-versions/windows/desktop/legacy/cc144064(v=vs.85)).

## Debugging Active Directory Extensions Displayed in the Active Directory MMC Snap-Ins

Active Directory extensions displayed in the Active Directory administrative MMC snap-ins are loaded in the context of the Microsoft Management Console. To debug an extension, locate Mmc.exe on the local system and set the debugger to use this as the application for debugging. On most systems, Mmc.exe is located in the Windows system directory, for example, C:\\WINNT\\System32. Depending on the debugger, you may or may not have to set the extension DLL to also be loaded by the debugger. Many debuggers also allow you to attach the debugger to a running MMC process. For more information, see your debugger User's Guide.

It can be convenient to have MMC automatically load a specific snap-in. To do this, set the application arguments to the path and file name of an MSC file. This can either be a system-installed MSC file or one you create. An MSC file can be created by following these steps.

1.  Run Mmc.exe.
2.  Load the desired snap-in by selecting **File** - **Add/Remove Snap-in...** in the MMC menu and select the desired snap-in.
3.  Save the MSC file by selecting **File** - **Save As...** in the MMC menu.

If you do not set a start-up MSC file, you must manually load the desired snap-in when you run the application in the debugger.

When the host application is run in the debugger, the debugger may display a warning message stating that the application being run does not contain any debug symbols. This is expected and can safely be ignored because you are actually debugging the DLL, not the host application.

In most cases, the extension will not be called until the user performs some action that causes the extension to be loaded and initialized. For example, if you are debugging a context menu extension displayed for user objects, the extension will not load until the first time the context menu for a user object is displayed.

You should now be able to set breakpoints and view debug output. If the extension does not appear to load, set a breakpoint in the extension's [**DllGetClassObject**](/windows/win32/api/combaseapi/nf-combaseapi-dllgetclassobject) function. If **DllGetClassObject** is not called, the extension is probably not registered correctly.

When the debug is complete, exit MMC and the debugger should unload normally.

 

 