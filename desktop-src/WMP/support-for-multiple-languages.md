---
title: Support for Multiple Languages
description: Support for Multiple Languages
ms.assetid: f46efb7f-73d1-4f64-aa44-cb50170a2245
keywords:
- Windows Media metafile playlists,support for multiple languages
- metafile playlists,support for multiple languages
- playlists,support for multiple languages
- Windows Media metafile playlists,multiple language support
- metafile playlists,multiple language support
- playlists,multiple language support
- Windows Media metafile playlists,language support
- metafile playlists,language support
- playlists,language support
- support for multiple languages
- multiple language support
- language support
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Support for Multiple Languages

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player 9 Series or later supports Windows Media metafiles created using the Unicode character set. This allows you to include multilingual metadata in your metafile playlist. The following rules govern the use of multilingual metadata in Windows Media metafiles:

-   Characters must be encoded using the UTF-8 encoding scheme.
-   The metafile playlist must include the following **PARAM** at the playlist level:
    ```XML
    <PARAM  NAME = "Encoding"  VALUE = "utf-8">
    
    ```

    

-   Only Windows Media Player 9 Series or later supports this functionality.
-   If the metafile playlist is not saved with UTF-8 encoding and the correct **PARAM** element, it will be parsed using the default system locale code page of the user's computer.

## Related topics

<dl> <dt>

[**PARAM Element**](param-element.md)
</dt> <dt>

[**Windows Media Metafiles Overview**](windows-media-metafiles-overview.md)
</dt> </dl>

 

 




