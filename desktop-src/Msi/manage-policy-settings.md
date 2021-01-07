---
description: The VBScript file WiPolicy.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample shows how script can be used to manage system policy. Policy can be configured by an administrator using the Group Policy Editor (GPE).
ms.assetid: 17cfed46-503f-4124-9f0e-1655fda153d0
title: Manage Policy Settings
ms.topic: article
ms.date: 05/31/2018
---

# Manage Policy Settings

The VBScript file WiPolicy.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script can be used to manage [system policy](system-policy.md). Policy can be configured by an administrator using the Group Policy Editor (GPE).

This sample demonstrates the Windows Installer policies.

Using this sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiPolicy.vbs \[policy\]\[value\]**

If no arguments are specified on the command line, the sample returns the current policy settings. Specify the policy to be set by using the following identifier codes. Specify the new value for the policy. To return the current value of a policy, specify an empty string "" for the value.



| CODE | Description                                                                                                                                  |
|------|----------------------------------------------------------------------------------------------------------------------------------------------|
| LM   | Logging modes. For more information, see [Logging](logging.md) .                                                                            |
| DO   | Debug modes. For more information, see [Debug](debug.md).                                                                                   |
| DI   | Disable Windows Installer mode. For more information, see [DisableMsi](disablemsi.md).                                                      |
| WT   | Wait timeout in seconds in case of no activity. **HKLM**\\**SoftWare**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**\\**Timeout** |
| DB   | Disable user browsing of source locations. For more information, see [DisableBrowse](disablebrowse.md).                                     |
| DP   | Disable patching. For more information, see [DisablePatch](disablepatch.md).                                                                |
| UC   | Public properties sent to install service. For more information, see [EnableUserControl](enableusercontrol.md).                             |
| SS   | Installer safe for scripting from browser. For more information, see [SafeForScripting](safeforscripting.md).                               |
| EM   | System privileges (HKLM). For more information, see [AlwaysInstallElevated](alwaysinstallelevated.md).                                      |
| EU   | System privileges (HKCU). For more information, see [AlwaysInstallElevated](alwaysinstallelevated.md).                                      |
| DR   | Disable rollback policy. For more information, see [DisableRollback](disablerollback.md).                                                   |
| TS   | Locate transforms at root of source image. For more information, see [TransformsAtSource policy](transformsatsource-policy.md).             |
| TP   | Pin secure tranforms in client-side-cache. For more information, see [TransformsSecure policy](transformssecure-policy.md).                 |
| SO   | Search order of source types. For more information, see [SearchOrder](searchorder.md).                                                      |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



