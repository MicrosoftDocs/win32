---
title: UI Plug-in Options
description: UI Plug-in Options
ms.assetid: 3c188506-865c-4e0c-965d-1429eafd01ef
keywords:
- Windows Media Player plug-ins,options
- plug-ins,options
- user interface plug-ins,options
- UI plug-ins,options
- settings area plug-ins
- background plug-ins
- separate window plug-ins
- metadata area plug-ins
- display area plug-ins
ms.topic: article
ms.date: 05/31/2018
---

# UI Plug-in Options

Any of the five UI plug-in types can have a property page where the user can modify plug-in settings. This property page can be set to display automatically when a plug-in is loaded for the first time. It can also be accessed from the Plug-ins tab of the Options dialog box.

A UI plug-in can be set to load automatically after installation when Windows Media Player is started. If it is not started automatically, the user can load it by selecting it from the **Plug-ins** list on the **Tools** menu.

A display area plug-in can have multiple presets, which are different views that the plug-in can make available to the user. The user can change the preset by selecting a different entry from the **Visualizations and Views** list on the **View** menu, or by using the arrow buttons provided at the bottom of the **Now Playing** pane just above the status message and transport controls.

Background and separate window UI plug-ins can be programmed to accept a media item or playlist that the user sends to it. If a plug-in supports this feature, its name will appear on the **Send to** list available from the shortcut menu of the playlist control or the library.

A UI plug-in can be programmed to intercept keyboard shortcuts when it has the keyboard focus. Keyboard focus is required to prevent conflicts when multiple UI plug-ins that intercept the same keyboard shortcut are loaded. Although this prevents conflicts, it can also cause confusion to end users. For this reason, the use of keyboard shortcuts with UI plug-ins is not recommended. When they are used, however, they should not intercept any keyboard shortcuts that are used by Windows Media Player. For a complete list of keyboard shortcuts used by the Player, see Windows Media Player Help.

## Related topics

<dl> <dt>

[**UI Plug-in Overview**](ui-plug-in-overview.md)
</dt> </dl>

 

 




