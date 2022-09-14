---
title: Required Elements
description: Required Elements
ms.assetid: 6aabbdcc-f834-4908-b25a-1dfce038132a
keywords:
- Windows Media Player Mobile skins,elements
- skins,elements
- skin definition files,elements
- elements,skin definition files
- elements,Windows Media Player Mobile
ms.topic: article
ms.date: 05/31/2018
---

# Required Elements

You must provide the following elements in your skin definition file:

-   **Header.** The main skin definition file header is required. For header version information, see the table in the [Creating a Skin Definition File](creating-a-skin-definition-file.md) section.
-   **Description section.** The Description section is required when creating skins for Windows Media Player 9 Series for Windows Mobile. It must be the first section in the skin definition file, and it must specify valid values for Dimensions. Specifying a value for Orientation is optional.
-   **Bitmaps section.** The Bitmaps section is required. Additionally, the Bitmaps section must specify valid names for Background, Disabled, Pushed, Region, and Super image files.
-   **Image files.** You must provide Background, Disabled, Pushed, Region, and Super image files as part of your skin. If you are creating skins for Windows Media Player 10 Mobile or later, you do not need to include Region or Super image files.

If you create a skin with only images defined, the skin will be visible, but will not offer any meaningful functionality to the user. If you decide to create a skin without buttons, perhaps to prevent the user from skipping over certain content, be aware that it may still be possible to map functionality to the hardware buttons on the device.

Thumb files are required and your trackbars cannot be used without thumbs.

## Related topics

<dl> <dt>

[**Skin Definition File**](skin-definition-file-mobile.md)
</dt> </dl>

 

 




