---
title: Bitmap Type
description: Bitmap Type
ms.assetid: 208df4b9-d1be-49ff-bc0b-2e000608e9c7
keywords:
- Windows Media Player Mobile skins,bitmaps
- skins,bitmaps
- reference for skins,bitmaps
- bitmaps in skins,types
- bitmaps in skins,values
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Bitmap Type

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table shows the values that are valid for the bitmap type. Only the Background type is required; others are optional and relate to different possible uses of images.



| Value       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Background  | Required. The image upon which all button images are superimposed. The base background image dimensions include the full width and height of the screen. This is also the file where images for the natural states of buttons and trackbars are displayed. (Pushed and disabled buttons are not part of this image.)                                                                                                                                                                                                                                                                                           |
| Disabled    | Required. Indicates that pushing the button will have no effect. Defines an image that is displayed when specific player functionality is unavailable to the user. You must supply a Coordinates value to indicate the top-left corner position of this image relative to the Background image.                                                                                                                                                                                                                                                                                                                |
| Pushed      | Required. Defines an image that is displayed when the user pushes a button. Use Pushed to give visual feedback to the user when he taps on a button. You must supply a Coordinates value to indicate the top-left corner position of this image relative to the Background image.                                                                                                                                                                                                                                                                                                                              |
| Region      | Defines images that use colored regions to represent the tap-response area for the hit-type buttons: PushHit, ToggleHit, 2PushHit. If you are using the hit-type buttons, you must supply a Region image. This image file uses specific Windows Palette colors for each control. The colors are defined by numbers representing the value of red, green, and blue for the region. This image is never seen by the user. You must also supply a Coordinates value to indicate the top-left corner position of this image relative to the Background image.                                                      |
| SeekThumb   | Defines an image that you will use in conjunction with a trackbar to indicate the current position in the media item. For example, if a song is half finished playing, the SeekThumb image is displayed in the middle of the trackbar. By tapping and dragging the SeekThumb image, the user can restart the media item at any position, which is called *seeking*. The image of the trackbar itself is defined in the Background image. The SeekThumb image is not included in the Bitmaps section of the skin definition file, but is specified as part of the trackbar definition in the TrackBars section. |
| Super       | Defines the Disabled image for a trackbar. It can also contain alternate images for the mute button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VolumeThumb | Defines an image to use in conjunction with a trackbar to indicate the volume position. By tapping and dragging the VolumeThumb image, the user can change the volume level. The image of the trackbar itself is defined in the Background image. The VolumeThumb image is not included in the Bitmaps section of the skin definition file, but is specified as part of the trackbar definition in the TrackBars section.                                                                                                                                                                                      |



 

> [!Note]  
> Region and Super bitmap types are deprecated in skins for Windows Media Player 10 Mobile or later.

 

Note that the file name and the file type are not necessarily the same. You can call the Pushed file anything you like, but it is still referred to in other places as Pushed. For example, in the Buttons section, you will have an item such as:


```C++
Pushed @ 50,60

```



This refers to the type of the file, not the file name.

## Related topics

<dl> <dt>

[**Bitmaps**](bitmaps.md)
</dt> </dl>

 

 




