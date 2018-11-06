---
title: Customizing the UI Plug-in
description: Customizing the UI Plug-in
ms.assetid: d961ed18-ba14-45af-90d3-b1e38dc53180
keywords:
- Windows Media Player plug-ins,customizing
- plug-ins,customizing
- user interface plug-ins,customizing
- UI plug-ins,customizing
ms.topic: article
ms.date: 05/31/2018
---

# Customizing the UI Plug-in

At this point, your project is ready for customization. You can modify the wizard-generated implementation of the **IWMPPluginUI** interface, you can add a user interface to the **CPluginWindow** class, and you can implement a property page in the **CPropertyDialog** class. If your plug-in is configured to listen to Windows Media Player events, the wizard will have generated default or empty implementations of all the necessary event handlers, which you also modify or create.

The type of plug-in and the features it supports are indicated by a value which is stored in the Windows registry. The wizard generates a file with a .rgs file name extension that contains the information to register the plug-in with. The "Capabilities" value in this file is the decimal equivalent of a Boolean OR of the plug-in type constants and plug-in flags defined in wmpplug.h. Although this value is determined by the options you select in the wizard, you must modify it if you want to create a plug-in with multiple presets or one that media items or playlists can be sent to.

As you modify and extend your plug-in code, you can build and register your DLL so that you can test your plug-in in Windows Media Player.

## Related topics

<dl> <dt>

[**Building a UI Plug-in**](building-a-ui-plug-in.md)
</dt> </dl>

 

 




