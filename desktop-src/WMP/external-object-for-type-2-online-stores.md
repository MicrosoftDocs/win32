---
title: External Object for Type 2 Online Stores
description: External Object for Type 2 Online Stores
ms.assetid: d12e7480-39ec-4d32-9cf9-5555d0f92d80
keywords:
- Windows Media Player online stores,external objects
- online stores,external objects
- type 2 online stores,external objects
- external objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External Object for Type 2 Online Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **External** object can provide functionality to webpages that are provided by a type 2 online store and hosted in Windows Media Player.

The **External** object exposes the following properties.



| Property                                                        | Description                                                                               |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [appColorButtonHighlight](external-appcolorbuttonhighlight.md) | Retrieves the current button highlight color for the Windows Media Player user interface. |
| [appColorButtonHoverFace](external-appcolorbuttonhoverface.md) | Retrieves the current button hover color for the Windows Media Player user interface.     |
| [appColorButtonShadow](external-appcolorbuttonshadow.md)       | Retrieves the current button shadow color for the Windows Media Player user interface.    |
| [appColorDark](external-appcolordark.md)                       | Retrieves the current dark shaded color of the Windows Media Player user interface.       |
| [appColorLight](external-appcolorlight.md)                     | Retrieves the current light shaded color of the Windows Media Player user interface.      |
| [appColorMedium](external-appcolormedium.md)                   | Retrieves the current medium shaded color of the Windows Media Player user interface.     |
| [DownloadManager](external-downloadmanager.md)                 | Retrieves the **DownloadManager** object.                                                 |
| [SelectedTaskPane](external-selectedtaskpane.md)               | Specifies or retrieves the currently selected task pane.                                  |
| [version](external-version.md)                                 | Retrieves the current version of Windows Media Player.                                    |



 

The **External** object exposes the following methods.



| Method                                                  | Description                                                                          |
|---------------------------------------------------------|--------------------------------------------------------------------------------------|
| [NavigateTaskPaneURL](external-navigatetaskpaneurl.md) | Opens a webpage in the specified task pane, and changes focus to the specified pane. |
| [playMedia (deprecated)](external-playmedia.md)        | Specifies the URL of a digital media item to play.                                   |



 

The **External** object exposes the following event.



| Event                                             | Description                                                               |
|---------------------------------------------------|---------------------------------------------------------------------------|
| [OnColorChange](external-oncolorchange-event.md) | Occurs when the color of the Windows Media Player user interface changes. |



 

## Related topics

<dl> <dt>

[**Reference for Type 2 Online Stores**](reference-for-type-2-online-stores.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 




