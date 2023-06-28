---
title: THEME Element
description: THEME Element
ms.assetid: fe7e793e-1774-412c-aed2-721ed2cf1bb3
keywords:
- Windows Media Player skins,THEME element
- skins,THEME element
- THEME element
- reference for skins,THEME element
- elements,THEME
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# THEME Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **THEME** element is the parent-level element of a skin, and contains one or more **VIEW** elements, which in turn contain all other elements within a skin. Within script code, the **THEME** element is accessed through the **theme** global attribute rather than through a name specified by an **id** attribute, which is not supported by the **THEME** element.

The **THEME** element supports the following attributes.



| Attribute                                | Description                                                                                                                     |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [author](theme-author.md)               | Specifies or retrieves the name of the author of the skin.                                                                      |
| [authorVersion](theme-authorversion.md) | Specifies or retrieves the version number of the skin as assigned by the author.                                                |
| [copyright](theme-copyright.md)         | Specifies or retrieves the copyright string for the skin.                                                                       |
| [currentViewID](theme-currentviewid.md) | Specifies or retrieves the currently displayed **VIEW**.                                                                        |
| [title](theme-title.md)                 | Specifies or retrieves the title of the skin.                                                                                   |
| [version](theme-version.md)             | Specifies or retrieves the Windows Media Player version number for which the skin was authored. Can only be set at design time. |



 

The **THEME** element supports the following methods.



| Method                                         | Description                                                                                                     |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [closeView](theme-closeview.md)               | Closes an open **VIEW**.                                                                                        |
| [loadPreference](theme-loadpreference.md)     | Loads a preference from the registry.                                                                           |
| [logString](theme-logstring.md)               | Logs a user-defined string to the error file, if logging is enabled.                                            |
| [openDialog](theme-opendialog.md)             | Opens a file dialog box.                                                                                        |
| [openView](theme-openview.md)                 | Opens a **VIEW** in a new window.                                                                               |
| [openViewRelative](theme-openviewrelative.md) | Opens a **VIEW** in a new window at a specified initial position relative to the upper-left corner of the skin. |
| [playSound](theme-playsound.md)               | Plays the specified sound file.                                                                                 |
| [savePreference](theme-savepreference.md)     | Saves a preference in the registry.                                                                             |
| [showErrorDialog](theme-showerrordialog.md)   | Displays the standard error dialog box.                                                                         |



 

The **THEME** element does not support event handlers.

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




