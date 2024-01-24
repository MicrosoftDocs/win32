---
title: About the Metadata
description: About the Metadata
ms.assetid: bdb35606-7861-4f97-aae5-4f7f3ed48106
keywords:
- Windows Media Player,metadata
- metadata,about
- metadata,attributes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Metadata

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player 10 or later attempts to synchronize the following metadata attributes.



| Player attribute | WMDM global constant  | Description                                                                                                 | Required version                  |
|------------------|-----------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------|
| AlbumArtist      | g\_wszWMDMAlbumArtist | Null-terminated **string** containing the name of the primary artist for the album.                         | Windows Media Player 11 or later. |
| Album            | g\_wszWMDMAlbumTitle  | Null-terminated **string** containing the title of the album on which the content was originally released.  | Windows Media Player 11 or later. |
| Author           | g\_wszWMDMAuthor      | Null-terminated **string** containing the name of the media artist or actor associated with the content.    | Windows Media Player 11 or later. |
| BuyNow           | g\_wszWMDMBuyNow      | **Boolean** indicating whether the user has chosen to purchase the content.                                 | Windows Media Player 10 or later. |
| WM/Genre         | g\_wszWMDMGenre       | Null-terminated **string** containing the genre of the content.                                             | Windows Media Player 11 or later. |
| UserPlayCount    | g\_wszWMDMPlayCount   | **DWORD** containing the number of times the user has played the digital media file.                        | Windows Media Player 10 or later. |
| ReleaseDate      | g\_wszWMDMYear        | The date of the original release of the item.                                                               | Windows Media Player 11 or later. |
| Title            | g\_wszWMDMTitle       | Null-terminated **string** containing the title.                                                            | Windows Media Player 11 or later. |
| WM/TrackNumber   | g\_wszWMDMTrack       | **DWORD** containing the track number of the item on the album on which it was originally released.         | Windows Media Player 11 or later. |
| UserRating       | g\_wszWMDMUserRating  | **DWORD** containing a value that represents the star rating the user specified for the digital media file. | Windows Media Player 10 or later. |



 

## Related topics

<dl> <dt>

[**Device Extensions for Accelerated Metadata Transfer**](device-extensions-for-accelerated-metadata-transfer.md)
</dt> </dl>

 

 




