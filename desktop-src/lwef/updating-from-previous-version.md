---
title: Updating from Previous Version
description: Updating from Previous Version
ms.assetid: a3f0c0bb-8c12-4907-8e49-49b098449c38
ms.topic: article
ms.date: 05/31/2018
---

# Updating from Previous Version

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Applications built and compiled with the previous 1.5 version of Microsoft Agent should run without modification under the new 2.0 version. The [**Connected**](connected-property.md) property can no longer be set to **False**; certain properties of the SpeechInput object that have been replaced still exist, but no longer turn any values, and the server no longer fires the [**Restart**](https://www.bing.com/search?q=**Restart**) and [**Shutdown**](https://www.bing.com/search?q=**Shutdown**) events.

However, if you update your applications to use the Agent 2.0 control, you may have to modify your code. If you have installed the 2.0 version of Microsoft Agent and load a Visual Basic project use the earlier version of the Agent control, Visual Basic includes an option that will automatically display a message indicating that it detected a new version of the control. To ensure proper operation of your application, always choose to use the later version.

For other programming languages (such as Microsoft Office 97 VBA), to update the control, you may have to first remove the 1.5 Agent control and save your code. Then, quit the programming environment, restart the programming environment, reload your code and insert the new control. Avoid editing an Agent 2.0-enabled application in the same instance of the programming environment that you are editing an Agent 1.5-enabled application in. Some programming environments may not handle the differences between the two versions of controls.

You should be able to uninstall the Agent 1.5 release on your system after installing the Agent 2.0 release. However, if Agent 1.5 is installed over the 2.0 release, you may have to reinstall 2.0.

 

 




