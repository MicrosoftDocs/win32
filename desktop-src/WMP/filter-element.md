---
title: filter Element
description: The filter element contains elements that limit the size of a playlist, duration of a playlist, or number of media items in a playlist.
ms.assetid: 880885f6-493f-466b-b5ad-ab9b569f4cc5
keywords:
- filter Element Windows Media Player
topic_type:
- apiref
api_name:
- filter Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# filter Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **filter** element contains elements that limit the size of a playlist, duration of a playlist, or number of media items in a playlist.

``` syntax
<filter
    type = "string"
    id = "WPL_GUID"
    name = "string"
>
</filter>
            
```

## Attributes

<dl> <dt>

<span id="type"></span><span id="TYPE"></span>**type**
</dt> <dd>

The type of filter object. There are no predefined values for this attribute.

</dd> <dt>

<span id="id__required______________"></span><span id="ID__REQUIRED______________"></span>**id** (required) 
</dt> <dd>

The GUID that uniquely identifies a filter object. The filter object's methods are invoked to interpret the **fragment** elements contained in the **filter** element.



| Value                                  | Description                                                                                                 |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------|
| {BC5E21B0-504C-46F6-82BF-FB975C911AD6} | The id for the "Microsoft Auto Playlist Filter -- Limits auto playlists by count, size or duration" filter. |



 

</dd> <dt>

<span id="name__required______________"></span><span id="NAME__REQUIRED______________"></span>**name** (required) 
</dt> <dd>

The name of the filter object.



| Value                                                                              | Description                                        |
|------------------------------------------------------------------------------------|----------------------------------------------------|
| Microsoft Auto Playlist Filter -- Limits auto playlists by count, size or duration | Limits auto playlists by count, size, or duration. |



 

</dd> </dl>

## Parent/Child Elements



| Hierarchy | Elements                                   |
|-----------|--------------------------------------------|
| Parent    | [smartPlaylist](smartplaylist-element.md) |
| Child     | [fragment](fragment-element.md)           |



 

## Remarks

The **filter** element does not add any media elements to a playlist; it simply removes or filters out content that was selected by the **sourceFilter** element.

## Examples


```XML
<filter 
    type = "smartFilterObject" 
    id = "{BC5E21B0-504C-46F6-82BF-FB975C911AD6}" 
    name = "Microsoft Auto Playlist Filter -- Limits auto playlists by count,size or duration">
        <fragment name = "Limit Number of Items">
            <argument name = "number">25</argument>
        </fragment>
</filter>
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**argument Element**](argument-element.md)
</dt> <dt>

[**fragment Element**](fragment-element.md)
</dt> <dt>

[**smartPlaylist Element**](smartplaylist-element.md)
</dt> <dt>

[**sourceFilter Element**](sourcefilter-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





