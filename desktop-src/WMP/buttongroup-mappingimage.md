---
title: BUTTONGROUP.mappingImage
description: The mappingImage attribute specifies or retrieves the name of the image representing the button map of the BUTTONGROUP.
ms.assetid: bfea52d1-0e7f-4f77-a212-d34e356a4d85
keywords:
- BUTTONGROUP.mappingImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.mappingImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONGROUP.mappingImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **mappingImage** attribute specifies or retrieves the name of the image representing the button map of the **BUTTONGROUP**.

``` syntax
        elementID.mappingImage
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

This is a mandatory attribute that must be specified.

The mapping image should be the same dimensions as the main **image**. It is a map of the clickable areas of the main image. Construct the map by filling each clickable area with a different color.

When defining each **BUTTONELEMENT**, designate its color from the map using the **mappingColor** attribute. For example, if you have a stop-sign-shaped button graphic in the main image, you can create a map with the area of the sign colored red. The **BUTTONELEMENT** attribute must then be specified as red to make the stop-sign image clickable.

The supported image formats are BMP, JPG, PNG, and GIF (not including animated GIFs). Because JPGs are lossy and therefore subject to unexpected color change, they are not recommended for mapping images.

## Examples

The following illustration is an example of a **mappingImage** and the visible image it corresponds to. These images are part of the skin in the Tiny folder included with the SDK.

![sample mapping image](images/absam01m.png)![sample background image](images/absam01f.png)

See the *BUTTONELEMENT*.[mappingColor](buttonelement-mappingcolor.md) attribute for a code sample illustrating the use of this attribute.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONELEMENT.mappingColor**](buttonelement-mappingcolor.md)
</dt> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> <dt>

[**BUTTONGROUP.image**](buttongroup-image.md)
</dt> <dt>

[**BUTTONGROUP.transparencyColor**](buttongroup-transparencycolor.md)
</dt> </dl>

 

 





