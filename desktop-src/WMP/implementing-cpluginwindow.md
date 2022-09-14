---
title: Implementing CPluginWindow
description: Implementing CPluginWindow
ms.assetid: b22723ce-f373-43b1-a098-86a8dbcf485e
keywords:
- Windows Media Player plug-ins,CPluginWindow class
- plug-ins,CPluginWindow class
- user interface plug-ins,CPluginWindow class
- UI plug-ins,CPluginWindow class
- CPluginWindow class
- programming guide,user interface plug-ins
ms.topic: article
ms.date: 05/31/2018
---

# Implementing CPluginWindow

The CPluginWindow class provides the UI to the plug-in. In the case of the Search UI plug-in, this class contains the code for the **Search** button and the code that launches the search page when the button is clicked.

The wizard provides a basic implementation of CPluginWindow in the CPluginWindow.h header file. To keep things simple, the Search UI plug-in will modify this file directly, although extensive additions would normally be placed in a separate CPluginWindow.cpp file.

The following sections describe what you need to do to implement CPluginWindow:

-   [The Message Map](the-message-map.md)
-   [The Constructor](the-constructor.md)
-   [The OnPaint Method](the-onpaint-method.md)
-   [The OnCreate Method](the-oncreate-method.md)
-   [The OnSearch Method](the-onsearch-method.md)
-   [The LaunchPage Method](the-launchpage-method.md)

## Related topics

<dl> <dt>

[**User Interface Plug-ins Programming Guide**](user-interface-plug-ins-programming-guide.md)
</dt> </dl>

 

 




