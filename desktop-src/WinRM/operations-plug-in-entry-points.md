---
title: Operations Plug-in Entry Points
description: Operations Plug-in Entry Points
ms.assetid: 9a3ddc2b-9fde-4915-b0e8-0a5e79e73c00
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Operations Plug-in Entry Points

An operations plug-in needs to implement certain entry points depending on the capabilities that it wants to support.

A plug-in must register with the Windows Remote Management (WinRM) service, which contains the names of the plug-in DLL entry points. All operations have predefined DLL entry points that must be exposed if that operation is supported.

The following table provides an overview of the operations plug-in entry points in the WinRM Plug-in API.



| Function                                                                                 | Description                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_PLUGIN\_COMMAND**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_command)                                   | Defines the command callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginCommand**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_command).<br/> |
| [**WSMAN\_PLUGIN\_CONNECT**](/windows/desktop/api/WsMan/nc-wsman-wsman_plugin_connect)                                   | Defines the connect callback for a plug-in.<br/> The DLL entry point name for this method must be [**WSManPluginConnect**](/windows/desktop/api/WsMan/nc-wsman-wsman_plugin_connect).<br/>                                                                                                |
| [**WSMAN\_PLUGIN\_RECEIVE**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_receive)                                   | Defines the receive callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginReceive**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_receive).<br/> |
| [**WSMAN\_PLUGIN\_RELEASE\_COMMAND\_CONTEXT**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_release_command_context) | Defines the release command callback for the plug-in.<br/> The DLL entry point name must be [**WSManPluginReleaseCommandContext**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_release_command_context).<br/>                                                                        |
| [**WSMAN\_PLUGIN\_RELEASE\_SHELL\_CONTEXT**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_release_shell_context)     | Defines the release shell callback for the plug-in.<br/> The DLL entry point name must be [**WSManPluginReleaseCommandContext**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_release_command_context).<br/>                                                                          |
| [**WSMAN\_PLUGIN\_SEND**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_send)                                         | Defines the send callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginSend**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_send).<br/>          |
| [**WSMAN\_PLUGIN\_SHELL**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_shell)                                       | Defines the shell callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginShell**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_shell).<br/>       |
| [**WSMAN\_PLUGIN\_SHUTDOWN**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_shutdown)                                 | Defines the shutdown callback for the plug-in.<br/> All WinRM plug-ins must implement this callback function.<br/> The DLL entry point name for this method must be [**WSManPluginShutdown**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_shutdown).<br/>                      |
| [**WSMAN\_PLUGIN\_SIGNAL**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_signal)                                     | Defines the signal callback for a plug-in.<br/> All WinRM plug-ins that support shell capabilities need to implement this callback.<br/> The DLL entry point name for this method must be [**WSManPluginSignal**](/windows/win32/api/wsman/nc-wsman-wsman_plugin_signal).<br/>    |
| [**WSMAN\_PLUGIN\_STARTUP**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_startup)                                   | Defines the startup callback for the plug-in.<br/> All WinRM plug-ins must implement this callback function.<br/> The DLL entry point name for this method must be [**WSManPluginStartup**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_startup).<br/>                         |



 

 

