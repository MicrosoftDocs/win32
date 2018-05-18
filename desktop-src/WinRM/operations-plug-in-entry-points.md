---
title: Operations Plug-in Entry Points
description: Operations Plug-in Entry Points
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9a3ddc2b-9fde-4915-b0e8-0a5e79e73c00'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-remote-management'
ms.tgt_platform: multiple
---

# Operations Plug-in Entry Points

An operations plug-in needs to implement certain entry points depending on the capabilities that it wants to support.

A plug-in must register with the Windows Remote Management (WinRM) service, which contains the names of the plug-in DLL entry points. All operations have predefined DLL entry points that must be exposed if that operation is supported.

The following table provides an overview of the operations plug-in entry points in the WinRM Plug-in API.



| Function                                                                                 | Description                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_PLUGIN\_COMMAND**](wsman-plugin-command.md)                                   | Defines the command callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginCommand**](wsman-plugin-command.md).<br/> |
| [**WSMAN\_PLUGIN\_CONNECT**](wsman-plugin-connect.md)                                   | Defines the connect callback for a plug-in.<br/> The DLL entry point name for this method must be [**WSManPluginConnect**](wsman-plugin-connect.md).<br/>                                                                                                |
| [**WSMAN\_PLUGIN\_RECEIVE**](wsman-plugin-receive.md)                                   | Defines the receive callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginReceive**](wsman-plugin-receive.md).<br/> |
| [**WSMAN\_PLUGIN\_RELEASE\_COMMAND\_CONTEXT**](wsman-plugin-release-command-context.md) | Defines the release command callback for the plug-in.<br/> The DLL entry point name must be [**WSManPluginReleaseCommandContext**](wsman-plugin-release-command-context.md).<br/>                                                                        |
| [**WSMAN\_PLUGIN\_RELEASE\_SHELL\_CONTEXT**](wsman-plugin-release-shell-context.md)     | Defines the release shell callback for the plug-in.<br/> The DLL entry point name must be [**WSManPluginReleaseCommandContext**](wsman-plugin-release-command-context.md).<br/>                                                                          |
| [**WSMAN\_PLUGIN\_SEND**](wsman-plugin-send.md)                                         | Defines the send callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginSend**](wsman-plugin-send.md).<br/>          |
| [**WSMAN\_PLUGIN\_SHELL**](wsman-plugin-shell.md)                                       | Defines the shell callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginShell**](wsman-plugin-shell.md).<br/>       |
| [**WSMAN\_PLUGIN\_SHUTDOWN**](wsman-plugin-shutdown.md)                                 | Defines the shutdown callback for the plug-in.<br/> All WinRM plug-ins must implement this callback function.<br/> The DLL entry point name for this method must be [**WSManPluginShutdown**](wsman-plugin-shutdown.md).<br/>                      |
| [**WSMAN\_PLUGIN\_SIGNAL**](wsman-plugin-signal.md)                                     | Defines the signal callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginSignal**](wsman-plugin-signal.md).<br/>    |
| [**WSMAN\_PLUGIN\_STARTUP**](wsman-plugin-startup.md)                                   | Defines the startup callback for the plug-in.<br/> All WinRM plug-ins must implement this callback function.<br/> The DLL entry point name for this method must be [**WSManPluginStartup**](wsman-plugin-startup.md).<br/>                         |



 

 

 





