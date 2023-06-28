---
title: PLAYLIST.itemMedia
description: The itemMedia attribute retrieves the Media object corresponding to the given index in the PLAYLIST element.
ms.assetid: 38085798-7986-432f-8c88-de886bfc2ac5
keywords:
- PLAYLIST.itemMedia Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.itemMedia
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.itemMedia

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **itemMedia** attribute retrieves the **Media** object corresponding to the given index in the **PLAYLIST** element.

``` syntax
        elementID.itemMedia(index)
```

## Possible Values

This attribute is a read-only **Media** object.

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number**(**long**) containing the index of a playlist item.

</dd> </dl>

## Remarks

The **itemMedia** property will return media objects that are expanded in the **PLAYLIST** element. For example, if there is a playlist that contains three media clips that is not expanded in the **PLAYLIST** element, **itemMedia**(0) will return the playlist as the media object. If the playlist is expanded, **itemMedia**(0) will return the first media clip in the playlist.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





