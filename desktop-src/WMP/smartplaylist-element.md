---
title: smartPlaylist Element
description: The smartPlaylist element contains the dynamically defined portion of a playlist.
ms.assetid: 05912849-7475-4eb9-a7bd-00f20b80b1cf
keywords:
- smartPlaylist Element Windows Media Player
topic_type:
- apiref
api_name:
- smartPlaylist Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# smartPlaylist Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **smartPlaylist** element contains the dynamically defined portion of a playlist.

``` syntax
<smartPlaylist
    version = "number"
>
</smartPlaylist>
```

## Attributes



| Term                                                                                                                                   | Description                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <span id="version__required______________"></span><span id="VERSION__REQUIRED______________"></span>**version** (required) <br/> | The decimal number representing the version number of the smart playlist schema. Set to 1.0.0.0.<br/> |



 

## Parent/Child Elements



| Hierarchy | Elements                                                       |
|-----------|----------------------------------------------------------------|
| Parent    | [seq](seq-element.md)                                         |
| Child     | [querySet](queryset-element.md), [filter](filter-element.md) |



 

## Remarks

A **smartPlaylist** element typically contains a **querySet** element and can also contain a **filter** element.

## Examples


```
<smartPlaylist version = "1.0.0.0">
    <querySet>
        <sourceFilter 
            type = "smartFilterObject"
            id = "12345678-1234-3333-abCD-123ABCdefGHI"
            name = "Music in my library">
                <fragment name = "Genre">
                    <argument name = "condition">Is</argument>
                    <argument name = "value">Rock</argument>
                </fragment>
                <fragment name = "Album Artist">
                    <argument name = "condition">Is Not</argument>
                    <argument name = "value">Brenda Diaz</argument>
                </fragment>
        </sourceFilter>
    </querySet>
    <filter>
    </filter>
</smartPlaylist>
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**argument Element**](argument-element.md)
</dt> <dt>

[**filter Element**](filter-element.md)
</dt> <dt>

[**fragment Element**](fragment-element.md)
</dt> <dt>

[**querySet Element**](queryset-element.md)
</dt> <dt>

[**seq Element**](seq-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





