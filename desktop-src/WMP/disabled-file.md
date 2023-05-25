---
title: Disabled File
description: Disabled File
ms.assetid: '8b3339f6-a5d5-4501-826c-6ce33bfbf0cb'
keywords:
- Windows Media Player Mobile skins,art files
- skins,art files
- files for skins,art
- art files for skins,Disabled files
- Windows Media Player Mobile skins,Disabled files
- skins,Disabled files
- Disabled files in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Disabled File

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Disabled file contains the images that will be displayed when a particular button function cannot be used or a button state is off. For example, if an empty playlist is defined, the **Next** and **Prev** buttons will be displayed, and they should be displayed using a disabled image. Also, for toggle buttons, the Disabled image is used to indicate that the state is off.

The following image is a typical Disabled file.

![disabled file](images/cesdkdis.png)

This stores the images for hit-type buttons that are disabled. The images are similar to the Background file, but the colors are lighter. Using the offset defined in the Bitmaps section of the skin definition file, the button images line up with the Background file image.

Notice that the background of the button image exactly matches the corresponding area in the Background file. This is important, because when a hit-type button is unavailable, the entire rectangle defined for the disabled image will replace the matching area in the Background file. Keep the graphic consistent with the background image to ensure that only the parts of the button that you want to appear different will actually change.

## Related topics

<dl> <dt>

[**Art Files**](art-files-mobile.md)
</dt> </dl>

 

 




