---
description: You can debug custom actions that are based on dynamic-link libraries by using Debugging Tools for Windows. It is not possible to use dynamic debugging with custom actions based on executable files or scripts.
ms.assetid: 4241a27a-c127-4c65-96a2-1d655b343eba
title: Debugging Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Custom Actions

You can debug custom actions that are based on [dynamic-link libraries](dynamic-link-libraries.md) by using [Debugging Tools for Windows](https://www.microsoft.com/?ref=go). It is not possible to use dynamic debugging with custom actions based on [executable files](executable-files.md) or [scripts](scripts.md).

The techniques described in this section can help you debug Windows Installer custom actions. See the Driver Development Tools section of the Windows Driver Kit (WDK) for information about [Debugging Tools for Windows](https://www.microsoft.com/?ref=go).

Windows Installer uses the MsiBreak environment variable to determine which custom action is to be debugged. If you have access to the custom action's source code, you may be able to use debugging without MsiBreak. To start debugging without MsiBreak, put a temporary message box at the beginning of the action's code. When the message box appears during the installation, attach the debugger to the process owning the message box. You can then set any necessary breakpoints and dismiss the message box to resume execution. It is not possible to debug the earlier portions of the custom action by this method.

To use the MsiBreak environment variable to debug the custom action, set MsiBreak to the custom action's name in the [CustomAction table](customaction-table.md). MsiBreak can be either a system or a user environment variable. If the variable is set as a system variable, a restart of the system may be needed when the value is changed to detect the new value.

To use the MsiBreak environment variable to debug an embedded user interface, set the value of MsiBreak to MsiEmbeddedUI.

Windows Installer only checks the MsiBreak environment variable if the user is an Administrator. The installer ignores the value of MsiBreak if the user is not an Administrator, even if this is a [*managed application*](m-gly.md).

If you are debugging a custom action that runs with elevated (system) privileges in the execution sequence, attach the debugger to the Windows Installer service. When debugging a custom action that runs with impersonated privileges in the execution sequence, the system prompts with a dialog box that indicates which process should be debugged. The user is prompted with a dialog box indicating which process to debug. For more information about elevated custom actions, see [Custom Action Security](custom-action-security.md).

Once the debugger has been attached to the correct process, the installer triggers a debugger breakpoint immediately before calling the entry point of the DLL. At the breakpoint, your DLL is already loaded into the process and the entry point address determined. If your custom action DLL could not be loaded or the custom action entry point did not exist, no breakpoint is triggered. Because the breakpoint is triggered before calling the DLL function, once the breakpoint has been triggered you should use your debugger to step forward until your custom action entry point is called. Alternately, you can set a breakpoint anywhere in your custom action and resume normal execution.

The Windows Installer executes DLLs not stored in the [Binary table](binary-table.md) directly from the DLL location. The installer does not know the original name of a DLL stored in the Binary table and runs the DLL custom action under a temporary file name. The form of the temporary file name is MSI?????.TMP. On Windows XP, this temporary file is stored in a secure location, commonly &lt;WindowFolder&gt;\\Installer.

Note that many DLLs created for debugging contain the name and path of the corresponding PDB file as part of the DLL itself. When debugging this type of DLL on a system where the PDB can be found at the location stored in the DLL, symbols may be loaded automatically by the debugger tool. In situations where the PDB cannot be found at the stored location, where the debugger does not support loading symbols from the stored location, or where the DLL was not built with debugging information, you may need to place your symbol files in the folder with the temporary DLL file.

The installer adds debugging information for custom action scripts to the installation log file.

``` syntax
There is a problem with this Windows Installer package. A script 
required for this install to complete could not be run. Contact your 
support personnel or package vendor.  {Custom action [2] script error 
[3], [4]: [5] Line [6], Column [7], [8] }
```

 

 



