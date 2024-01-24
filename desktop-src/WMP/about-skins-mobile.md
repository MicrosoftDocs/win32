---
title: About Skins (Mobile)
description: Learn about skins for mobile players. A skin is a customized user interface to Windows Media Player.
ms.assetid: 105c11ce-705b-4a0c-8982-d0f9dd9ae3ac
keywords:
- Windows Media Player Mobile,skins
- Windows Media Player Mobile skins,about
- Windows Media Player Mobile skins,creating
- skins,Windows Media Player Mobile
- creating skins,Windows Media Player Mobile
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Skins (Mobile)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A skin is a customized user interface to Windows Media Player. You can create your own buttons to start and stop playback of digital media, add sliders to change volume and playback position in the media item, and provide the user with text information such as the name of a song. Best of all, you can add your own artwork or use existing art to create a unique appearance for your skin.

The basic steps in creating a skin are:

1.  **Design** your user interface. Decide which buttons, text boxes, and trackbars you want to provide to the user so that they can control the functions you chose in step 1. You may want to sketch out your ideas to see how they fit on the image size you will be working with.
2.  **Create** the art you want to show the user. This will consist of several images that show the background images, other images you may want to display, and mapping images if you use region buttons.
3.  **Write** the skin definition file that will link together the digital media functions, user interface, and images. You must follow certain rules for entering the text data into the file, but you can look at the default skin as a guide.

You do not need to follow these steps in the order given, but a good design will come from being aware of all the possibilities and taking care of all the details.

The following sections provide detailed information about skins.



| Section                                                                                    | Description                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Compatibility](about-compatibility.md)                                             | Lists the different versions of Windows Media Player Mobile, the hardware requirements, availability of Windows Media Player, and the skin features introduced for each version of the software. |
| [Windows Media Player Mobile Functionality](windows-media-player-mobile-functionality.md) | Describes the features your skin can support.                                                                                                                                                    |
| [User Interface Elements](user-interface-elements.md)                                     | Describes the user interface elements you can create for your skin, such as buttons, trackbars, and video displays.                                                                              |
| [Art Files](art-files-mobile.md)                                                          | Describes the art files you create for your skin.                                                                                                                                                |
| [Skin Definition File](skin-definition-file-mobile.md)                                    | Describes the file you must create to describe your skin.                                                                                                                                        |



 

## Related topics

<dl> <dt>

[**Windows Media Player Mobile Skins**](windows-media-player-mobile-skins.md)
</dt> </dl>

 

 




