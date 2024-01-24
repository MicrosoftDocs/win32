---
title: UI Plug-in Overview
description: UI Plug-in Overview
ms.assetid: 8c4feb56-31c0-4f69-98dd-3c203941bb4c
keywords:
- Windows Media Player,plug-ins
- Windows Media Player,user interface plug-ins
- Windows Media Player plug-ins,user interface
- plug-ins,user interface
- user interface plug-ins,about
- UI plug-ins,about
- user interface plug-ins,types
- UI plug-ins,types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# UI Plug-in Overview

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

UI plug-ins can be installed, uninstalled, and configured using the Plug-ins tab of the Options dialog in Windows Media Player.

There are five types of UI plug-ins supported by Windows Media Player. Three of these types correspond to different areas of the **Now Playing** pane of the full mode of the player. The other two types are for plug-ins that display in a separate window and for plug-ins that have no display (except perhaps a property page).

UI plug-ins are unloaded when they are closed or disabled. UI plug-ins that appear in the **Now Playing** pane are also unloaded when the user chooses another plug-in of the same type or switches out of the **Now Playing** pane. When the user switches to skin mode, all plug-ins remain loaded, but are not displayed. If separate window or background plug-ins are running when Windows Media Player is closed, they will be automatically reloaded the next time the player is started.

The following sections provide general information about Windows Media Player UI plug-ins:

-   [Display Area Plug-ins (deprecated)](display-area-plug-ins--deprecated.md)
-   [Settings Area Plug-ins](settings-area-plug-ins.md)
-   [Metadata Area Plug-ins (deprecated)](metadata-area-plug-ins--deprecated.md)
-   [Separate Window Plug-ins](separate-window-plug-ins.md)
-   [Background Plug-ins](background-plug-ins.md)
-   [UI Plug-in Options](ui-plug-in-options.md)
-   [Displaying Modal User Interfaces](displaying-modal-user-interfaces.md)

## Related topics

<dl> <dt>

[**About User Interface Plug-ins**](about-user-interface-plug-ins.md)
</dt> </dl>

 

 




