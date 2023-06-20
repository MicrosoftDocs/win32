---
title: sourceFilter Element
description: The sourceFilter element contains elements that select items from a library.
ms.assetid: c961990f-8c57-448d-b4dc-dcfe70300e5a
keywords:
- sourceFilter Element Windows Media Player
topic_type:
- apiref
api_name:
- sourceFilter Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# sourceFilter Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **sourceFilter** element contains elements that select items from a library.

``` syntax
<sourceFilter
    type = "string"
    id = "WPL_GUID"
    name = "string"
>
</sourceFilter>
```

## Attributes

<dl> <dt>

<span id="type"></span><span id="TYPE"></span>**type**
</dt> <dd>

The type of filter object. There are no predefined values for this attribute.

</dd> <dt>

<span id="id__required______________"></span><span id="ID__REQUIRED______________"></span>**id** (required) 
</dt> <dd>

The GUID that uniquely identifies the source filter object. The source filter object's methods are invoked to interpret the **fragment** elements contained in the **sourceFilter** element.



| Value                                  | Description                                              |
|----------------------------------------|----------------------------------------------------------|
| {4202947A-A563-4B05-A754-A1B4B5989849} | The GUID for the "Music in my library" source filter.    |
| {B2D9BDDC-8E49-444B-9BA4-193ABF9C7870} | The GUID for the "Video in my library" source filter.    |
| {CC823400-A8E4-4081-B073-D3B6D952FE69} | The GUID for the "Pictures in my library" source filter. |
| {E5415A66-7763-4BDE-B97F-5557CA73C303} | The GUID for the "TV shows in my library" source filter. |



 

</dd> <dt>

<span id="name__required______________"></span><span id="NAME__REQUIRED______________"></span>**name** (required) 
</dt> <dd>

The name of the filter object.



| Value                  | Description                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------|
| Music in my library    | A filter object that selects specified items from the set of music items in the user's library. |
| Video in my library    | A filter object that selects specified items from the set of video items in the user's library. |
| Pictures in my library | A filter object that selects specified items from the set of photo items in the user's library. |
| TV shows in my library | A filter object that selects specified items from the set of TV items in the user's library.    |



 

</dd> </dl>

## Parent/Child Elements



| Hierarchy | Elements                         |
|-----------|----------------------------------|
| Parent    | [querySet](queryset-element.md) |
| Child     | [fragment](fragment-element.md) |



 

## Remarks

The **sourceFilter** element selects items from the library without regard for the size of the result set. The **filter** element, on the other hand, limits the size of the result set.

## Examples


```
<sourceFilter 
    type = "smartFilterObject" 
    id = "{4202947A-A563-4B05-A754-A1B4B5989849}" 
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
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**filter Element**](filter-element.md)
</dt> <dt>

[**fragment Element**](fragment-element.md)
</dt> <dt>

[**querySet Element**](queryset-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





