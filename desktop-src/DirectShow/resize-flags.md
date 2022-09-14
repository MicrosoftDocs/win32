---
description: These flags specify how a video source is rendered if its size does not match the output dimensions.
ms.assetid: f740b732-ba05-4fda-aafb-ed04bc3efd33
title: Resize Flags (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RESIZEF_STRETCH
- RESIZEF_CROP
- RESIZEF_PRESERVEASPECTRATIO
- RESIZEF_PRESERVEASPECTRATIO_NOLETTERBOX
api_type: 
- HeaderDef
api_location: 
- Qedit.h
---

# Resize Flags

\[Deprecated. This API may be removed from future releases of Windows.\]

These flags specify how a video source is rendered if its size does not match the output dimensions.



| Constant/value                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                        |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RESIZEF_STRETCH"></span><span id="resizef_stretch"></span><dl> <dt>**RESIZEF\_STRETCH**</dt> <dt>0</dt> </dl>                                                                          | The image is stretched to fit the target frame size in both dimensions, without preserving the aspect ratio.<br/>                                                                                                            |
| <span id="RESIZEF_CROP"></span><span id="resizef_crop"></span><dl> <dt>**RESIZEF\_CROP**</dt> <dt>1</dt> </dl>                                                                                   | The image is not resized. If the image is smaller than the target frame, the surrounding area is black. If the image is larger than the target frame, the image is cropped.<br/>                                             |
| <span id="RESIZEF_PRESERVEASPECTRATIO"></span><span id="resizef_preserveaspectratio"></span><dl> <dt>**RESIZEF\_PRESERVEASPECTRATIO**</dt> <dt>2</dt> </dl>                                      | The image is resized to fit the target frame along one dimension, while preserving the aspect ratio. If the ratio of width to height in the image does not match the ratio in the target frame, it creates a letterbox.<br/> |
| <span id="RESIZEF_PRESERVEASPECTRATIO_NOLETTERBOX"></span><span id="resizef_preserveaspectratio_noletterbox"></span><dl> <dt>**RESIZEF\_PRESERVEASPECTRATIO\_NOLETTERBOX**</dt> <dt>3</dt> </dl> | The image is resized to fill the entire target frame while preserving the aspect ratio. Rather than create a letterbox, this mode crops the image, either along the sides or across the top and bottom.<br/>                 |



## Remarks

The following images show the effects of these flags.

![resize flags](images/stretch14.png)

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineSrc::GetStretchMode**](iamtimelinesrc-getstretchmode.md)
</dt> <dt>

[**IAMTimelineSrc::SetStretchMode**](iamtimelinesrc-setstretchmode.md)
</dt> </dl>

 

 




