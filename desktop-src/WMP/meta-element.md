---
title: meta Element
description: The meta element specifies metadata that applies to the entire playlist.
ms.assetid: 7248e1d9-ebd1-48cb-9019-89a35eac27ae
keywords:
- meta Element Windows Media Player
topic_type:
- apiref
api_name:
- meta Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# meta Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **meta** element specifies metadata that applies to the entire playlist.

``` syntax
<meta
    name = "string"
    content = "string"
/>
```

## Attributes



| Term                                                                       | Description                                                                                                                       |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <span id="name"></span><span id="NAME"></span>**name**<br/>          | The name of an item of metadata.<br/>                                                                                       |
| <span id="content"></span><span id="CONTENT"></span>**content**<br/> | The value of an item of metadata. For example, if the name attribute is "Genre" the content attribute could be "Rock".<br/> |



 

## Parent/Child Elements



| Hierarchy | Elements                 |
|-----------|--------------------------|
| Parent    | [head](head-element.md) |
| Child     | None                     |



 

## Remarks

The creator of a Windows Media Playlist can set the name attribute of a meta element to any string. The following list shows some typical name attributes that are found in Windows Media Playlists created by Windows Media Player and other Microsoft components.

-   Author
-   Category
-   Genre
-   UserName
-   UserRating
-   Generator

## Examples


```
<head>
    <meta name = "Author" content = "Frank Lee"/>
    <meta name = "Category" content = "Classic"/>
    <meta name = "Genre" content = "Rock"/>
</head>
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**head Element**](head-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





