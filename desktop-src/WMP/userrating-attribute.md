---
title: UserRating Attribute
description: The UserRating attribute is the rating specified by the user in the library.
ms.assetid: 33df5316-1506-4ecb-b729-c2d66b878825
keywords:
- UserRating Attribute Windows Media Player
topic_type:
- apiref
api_name:
- UserRating
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# UserRating Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **UserRating** attribute is the rating specified by the user in the library.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Photo Items](photo-item-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Video Items](video-item-attributes.md)

## Remarks

User ratings are represented by integer values, as described in the following table. When specifying a value, use one of the values from the Writing value column. When retrieving values, you can use the ranges in the Reading values column to determine the number of stars.



| Rating  | Writing value | Reading values |
|---------|---------------|----------------|
| Unrated | 0             | 0              |
| 1 star  | 1             | 1 to 12        |
| 2 stars | 25            | 13 to 37       |
| 3 stars | 50            | 38 to 62       |
| 4 stars | 75            | 63 to 86       |
| 5 stars | 99            | 87 to 99       |



 

This attribute is stored only in the library.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later (The photo item is supported only in Windows Media Player 10 or later)<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





