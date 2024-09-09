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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/MediaClassPrimaryID

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




