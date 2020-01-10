---
title: WM/MediaClassPrimaryID
description: The WM/MediaClassPrimaryID attribute contains the GUID of the primary media class.
ms.assetid: 1d01e273-e6ec-49f1-90af-5c2ae171b199
keywords:
- WM/MediaClassPrimaryID windows Media Format
topic_type:
- apiref
api_name:
- WM/MediaClassPrimaryID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/MediaClassPrimaryID

The **WM/MediaClassPrimaryID** attribute contains the GUID of the primary media class.

## Global Constant

g\_wszWMMediaClassPrimaryID

## Data Type

**WMT\_TYPE\_GUID**

## Remarks

This attribute should be set to one of the values in the following table.



| Primary class GUID                     | Description                                                  |
|----------------------------------------|--------------------------------------------------------------|
| "D1607DBC-E323-4BE2-86A1-48A42A28441E" | Use for music files. Do not use for audio that is not music. |
| "DB9830BD-3AB3-4FAB-8A37-1A995F7FF74B" | Use for video files.                                         |
| "01CD0F29-DA4E-4157-897B-6275D50C4F11" | Use for audio files that are not music.                      |
| "FCF24A76-9A57-4036-990D-E35DD8B244E1" | Use for files that are neither audio or video.               |



 

When you specify a primary class identifier, you should also set a secondary class identifier to clarify the type of content in the file.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> <dt>

[**WM/MediaClassSecondaryID**](wm-mediasecondaryid.md)
</dt> </dl>

 

 




