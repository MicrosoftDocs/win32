---
description: The stretchmode attribute specifies how to stretch an image that does not match the output dimensions.
ms.assetid: 9a26bb8b-2b1c-424a-ae30-e175c60c76a1
title: stretchmode Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# stretchmode Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `stretchmode` attribute specifies how to stretch an image that does not match the output dimensions.

## Possible Values

Must have one of the following values.

-   "stretch": The image is stretched to fit the output frame size without preserving aspect ratio. (Default)
-   "crop": The image is cropped to fit the output frame size.
-   "preserveaspectratio": The original aspect ratio is preserved, with a black letterbox along the shorter dimension.
-   "preserveaspectrationoletterbox": The image is resized to fill the entire target frame while preserving the aspect ratio.

## Applies To

[**clip**](clip-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineSrc::SetStretchMode**](iamtimelinesrc-setstretchmode.md)
</dt> </dl>

 

 



