---
title: Super Files
description: Super Files
ms.assetid: a5005d1a-4b87-482d-914e-3184a2c93267
keywords:
- Windows Media Player Mobile skins,art files
- skins,art files
- files for skins,art
- art files for skins,Super files files
- Windows Media Player Mobile skins,Super files files
- skins,Super files
- Super files in skins
ms.topic: article
ms.date: 05/31/2018
---

# Super Files

Super files are used to store the Disabled images for trackbars. Because the main trackbar image is displayed in the Background file, and the user taps on the thumb image, not the trackbar image, only the Disabled image is needed for trackbars. It is stored in the file defined by Super in the Bitmaps section of the skin definition file. A Super file can also store the Pushed and Disabled images for other buttons such as Mute, which is not required to be a hit-type button.

> [!Note]  
> Super art files are not used in skins for Windows Media Player 10 Mobile or later because the disabled images for seek trackbars are located in the seekthumb file.

 

The following image is a typical Super file.

![super file](images/cesdksup.png)

This stores the disabled images for the trackbars and the mute button. These images are offset as defined by the Bitmaps section.

The background area of the disabled trackbar image exactly matches the corresponding area in the Background file. This is important, because the entire rectangle defined for the disabled trackbar image will replace the matching area in the Background file. This ensures that the disabled trackbar image blends seamlessly into the background image.

## Related topics

<dl> <dt>

[**Art Files**](art-files-mobile.md)
</dt> </dl>

 

 




