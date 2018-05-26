---
title: Operations Plug-in Entry Points
description: Operations Plug-in Entry Points
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9a3ddc2b-9fde-4915-b0e8-0a5e79e73c00
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Operations Plug-in Entry Points

An operations plug-in needs to implement certain entry points depending on the capabilities that it wants to support.

A plug-in must register with the Windows Remote Management (WinRM) service, which contains the names of the plug-in DLL entry points. All operations have predefined DLL entry points that must be exposed if that operation is supported.

The following table provides an overview of the operations plug-in entry points in the WinRM Plug-in API.



| Function                                                                                 | Description                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_PLUGIN\_COMMAND**](/windows/win32/Wsman/nc-wsman-wsman_plugin_command?branch=master)                                   | Defines the command callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginCommand**](/windows/win32/Wsman/nc-wsman-wsman_plugin_command?branch=master).<br/> |
| [**WSMAN\_PLUGIN\_CONNECT**](/windows/win32/WsMan/nc-wsman-wsman_plugin_connect?branch=master)                                   | Defines the connect callback for a plug-in.<br/> The DLL entry point name for this method must be [**WSManPluginConnect**](/windows/win32/WsMan/nc-wsman-wsman_plugin_connect?branch=master).<br/>                                                                                                |
| [**WSMAN\_PLUGIN\_RECEIVE**](/windows/win32/Wsman/nc-wsman-wsman_plugin_receive?branch=master)                                   | Defines the receive callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginReceive**](/windows/win32/Wsman/nc-wsman-wsman_plugin_receive?branch=master).<br/> |
| [**WSMAN\_PLUGIN\_RELEASE\_COMMAND\_CONTEXT**](/windows/win32/Wsman/nc-wsman-wsman_plugin_release_command_context?branch=master) | Defines the release command callback for the plug-in.<br/> The DLL entry point name must be [**WSManPluginReleaseCommandContext**](/windows/win32/Wsman/nc-wsman-wsman_plugin_release_command_context?branch=master).<br/>                                                                        |
| [**WSMAN\_PLUGIN\_RELEASE\_SHELL\_CONTEXT**](/windows/win32/Wsman/nc-wsman-wsman_plugin_release_shell_context?branch=master)     | Defines the release shell callback for the plug-in.<br/> The DLL entry point name must be [**WSManPluginReleaseCommandContext**](/windows/win32/Wsman/nc-wsman-wsman_plugin_release_command_context?branch=master).<br/>                                                                          |
| [**WSMAN\_PLUGIN\_SEND**](/windows/win32/Wsman/nc-wsman-wsman_plugin_send?branch=master)                                         | Defines the send callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginSend**](/windows/win32/Wsman/nc-wsman-wsman_plugin_send?branch=master).<br/>          |
| [**WSMAN\_PLUGIN\_SHELL**](/windows/win32/Wsman/nc-wsman-wsman_plugin_shell?branch=master)                                       | Defines the shell callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginShell**](/windows/win32/Wsman/nc-wsman-wsman_plugin_shell?branch=master).<br/>       |
| [**WSMAN\_PLUGIN\_SHUTDOWN**](/windows/win32/Wsman/nc-wsman-wsman_plugin_shutdown?branch=master)                                 | Defines the shutdown callback for the plug-in.<br/> All WinRM plug-ins must implement this callback function.<br/> The DLL entry point name for this method must be [**WSManPluginShutdown**](/windows/win32/Wsman/nc-wsman-wsman_plugin_shutdown?branch=master).<br/>                      |
| [**WSMAN\_PLUGIN\_SIGNAL**](/windows/win32/Wsman/nc-wsman-wsman_plugin_signal?branch=master)                                     | Defines the signal callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginSignal**](/windows/win32/Wsman/nc-wsman-wsman_plugin_signal?branch=master).<br/>    |
| [**WSMAN\_PLUGIN\_STARTUP**](/windows/win32/Wsman/nc-wsman-wsman_plugin_startup?branch=master)                                   | Defines the startup callback for the plug-in.<br/> All WinRM plug-ins must implement this callback function.<br/> The DLL entry point name for this method must be [**WSManPluginStartup**](/windows/win32/Wsman/nc-wsman-wsman_plugin_startup?branch=master).<br/>                         |



 

 

 





