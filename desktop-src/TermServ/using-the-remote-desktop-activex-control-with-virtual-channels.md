---
title: Using the Remote Desktop ActiveX control with virtual channels
description: If you have enabled a virtual channels application in your Remote Desktop Services deployment, you can make this application available to client computers.
ms.assetid: df537ffb-41dd-400e-8a49-9d8a10734eda
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Using the Remote Desktop ActiveX control with virtual channels

If you have enabled a virtual channels application in your Remote Desktop Services deployment, you can make this application available to client computers that access the Remote Desktop Session Host (RD Session Host) server by means of the Remote Desktop ActiveX control.

**To make a virtual channel application available**

1.  Deploy the server-side module of the application and make sure it is running on the RD Session Host server. In the connection page of the Remote Desktop Services web application running on your web server, access the **PluginDlls** property of the [**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md) interface to specify the name of your virtual channel DLL. If you have more than one plug-in, specify a comma-delimited list of DLL names. For instance, if your virtual channel plug-in is named "MyPlugin.dll", use the following code:

    ``` syntax
    MsRdpClient.AdvancedSettings.PluginDlls = "myplugin.dll"
    ```

    Use the following code if you have two virtual channel DLLs. In this example, the DLL file names are "MyPlugin.dll" and "Vdriver.dll":

    ``` syntax
    MsRdpClient.AdvancedSettings.PluginDlls = "myplugin.dll,Vdriver.dll"
    ```

    For security reasons, the **PluginDlls** property only accepts a named list of virtual channel DLLs. The control returns an error if any form of file system or UNC path is specified. In addition, the names of the DLLs must contain only alphanumeric characters.

2.  Ensure that the client-side module is installed in the %windir%\\system32 directory.

The virtual channel API does not allow for multiple instances of the same virtual channel DLL to be loaded within a single process. Because of this, if there are multiple instances of the Remote Desktop ActiveX control running within the same process, only the first instance of the control will be able to load the virtual channel DLL. If you are designing a virtual channel application that must support multiple instances within a single process, you must use the [Dynamic Virtual Channels](dynamic-virtual-channels.md) API to implement your virtual channel application.

> [!Note]  
> By default, the Remote Desktop ActiveX control loads virtual channel client DLLs from the %windir%\\system32 directory. It is possible for an administrator to change this default client plug-in DLL directory. To do so, edit the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Terminal Server Client**\\**vdllpath** registry key on the client computer. This directory path cannot be specified in the UNC format.

 

 

 




