---
title: Art Files
description: Art Files
ms.assetid: 93893610-de8d-4b9a-b23d-75ddb3e1e557
keywords:
- Windows Media Player skins,art files
- skins,art files
- files for skins,art
- art files for skins,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Art Files

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must create one or more art files for your skin. Without art, the user will have nothing to look at. You could create an invisible skin, but no one would see it! And even then, you would still have to create art files to hold your invisible images, because the skin definition file requires art files for specific elements.

There are three uses for art in skins: primary images, mapping images, and alternate images.

## Primary Images

You must create a primary image for your skin. This is what the users will see when they install your skin. The primary image is composed of one or more images that are created by specific skin controls.

If you have more than one control, you must specify the z-order, which defines which controls are displayed in front of other controls. Each **View** element will have a background image that you can add other element images to, allowing you to create a primary composite image.

You also may have secondary images, such as a sliding tray, that do not display when your skin first appears, but that show up when the user takes some action. These follow the same rules as primary images, in that they are created with a set of controls.

## Mapping Images

One of the most powerful features of Windows Media Player skins is that you can use image mapping to trigger events for your skin. Image maps are files that contain special images. The images in an image map file, however, are not meant to be viewed by the user, but are used by Windows Media Player to take action when the user clicks on your skin.

Different controls need different kinds of image maps. For example, if you color part of an image map a specific red value, and the user clicks on the corresponding area of your primary image, a button will fire an event. Color is used to define which events are triggered by clicking in a particular area of the skin.

## Alternate Images

You can also set up alternate images to display when a user does something. For example, you can create an alternate image of a button that will be displayed only when the mouse hovers over the button. This is a good way to let users know what they can do, and also allows for a highly discoverable user interface. By using ToolTips and hover images carefully, you can create unusual user interfaces that still give the user feedback about what options are available.

The following sections provide more information about art files:

-   [Primary Images](primary-images.md)
-   [Mapping Images](mapping-images.md)
-   [Alternate Images](alternate-images.md)
-   [Art File Formats](art-file-formats.md)
-   [Simple Art Example](simple-art-example.md)

## Related topics

<dl> <dt>

[**Skin Files**](skin-files.md)
</dt> </dl>

 

 




