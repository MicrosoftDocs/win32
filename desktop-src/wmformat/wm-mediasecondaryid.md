---
title: WM/MediaClassSecondaryID
description: The WM/MediaClassSecondaryID attribute contains the GUID of the secondary media class.
ms.assetid: 3d1429bc-f168-4b25-9d26-c1c28b852160
keywords:
- WM/MediaClassSecondaryID windows Media Format
topic_type:
- apiref
api_name:
- WM/MediaClassSecondaryID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/MediaClassSecondaryID

The **WM/MediaClassSecondaryID** attribute contains the GUID of the secondary media class.

## Global Constant

g\_wszWMMediaClassSecondaryID

## Data Type

**WMT\_TYPE\_GUID**

## Remarks

This attribute should be set to one of the values in the following table.



| Secondary class GUID                   | Description                                                                                                                                                                             |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "E0236BEB-C281-4EDE-A36D-7AF76A3D45B5" | Use for audio book files.                                                                                                                                                               |
| "3A172A13-2BD9-4831-835B-114F6A95943F" | Use for audio files that contain spoken word, but are not audio books. For example, stand-up comedy routines.                                                                           |
| "6677DB9B-E5A0-4063-A1AD-ACEB52840CF1" | Use for audio files related to news.                                                                                                                                                    |
| "1B824A67-3F80-4E3E-9CDE-F7361B0F5F1B" | Use for audio files with talk show content.                                                                                                                                             |
| "1FE2E091-4E1E-40CE-B22D-348C732E0B10" | Use for video files related to news.                                                                                                                                                    |
| "D6DE1D88-C77C-4593-BFBC-9C61E8C373E3" | Use for video files containing Web-based shows, short films, movie trailers, and so on. This is the general identifier for video entertainment that does not fit into another category. |
| "00033368-5009-4AC3-A820-5D2D09A4E7C1" | Use for audio files containing sound clips from games.                                                                                                                                  |
| "F24FF731-96FC-4D0F-A2F5-5A3483682B1A" | Use for audio files containing complete songs from game sound tracks. If only part of a song is encoded in the file, use the identifier for game sound clips instead.                   |
| "E3E689E2-BA8C-4330-96DF-A0EEEFFA6876" | Use for video files containing music videos.                                                                                                                                            |
| "B76628F4-300D-443D-9CB5-01C285109DAF" | Use for video files containing general home video.                                                                                                                                      |
| "A9B87FC9-BD47-4BF0-AC4F-655B89F7D868" | Use for video files containing feature films.                                                                                                                                           |
| "BA7F258A-62F7-47A9-B21F-4651C42A000E" | Use for video files containing television shows. For Web-based shows, use the more generic identifier.                                                                                  |
| "44051B5B-B103-4B5C-92AB-93060A9463F0" | Use for video files containing corporate video. For example, recorded meetings or training videos.                                                                                      |
| "0B710218-8C0C-475E-AF73-4C41C0C8F8CE" | Use for video files containing home video made from photographs.                                                                                                                        |



 

When specifying a secondary class identifier, the file should also contain a primary class identifier attribute.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> <dt>

[**WM/MediaClassPrimaryID**](wm-mediaprimaryid.md)
</dt> </dl>

 

 




