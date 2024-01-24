---
title: querySet Element
description: The querySet element contains elements that define which media items will be selected from the library.
ms.assetid: 18b5a509-a56b-4fd1-812f-60b8efd5136b
keywords:
- querySet Element Windows Media Player
topic_type:
- apiref
api_name:
- querySet Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# querySet Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **querySet** element contains elements that define which media items will be selected from the library.

``` syntax
<querySet>
</querySet>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy | Elements                                   |
|-----------|--------------------------------------------|
| Parent    | [smartPlaylist](smartplaylist-element.md) |
| Child     | [sourceFilter](sourcefilter-element.md)   |



 

## Remarks

The **querySet** element specifies which media items should be selected from the library, without regard for the size of the result set. The **filter** element, on the other hand, limits the size of the result set.

## Examples


```
<querySet>
    <sourceFilter 
        type = "smartFilterObject" 
        id = "{4202947A-A563-4B05-A754-A1B4B5989849}"
        name = "Windows Media Local Music Library Filter">
            <fragment name = "Genre">
                <argument name = "Condition">Equals</argument>
                <argument name = "Value">Rock</argument>
            </fragment>
            <fragment name = "Artist">
                <argument name = "Condition">Does Not Equal</argument>
                <argument name = "Value">Brenda Diaz</argument>
            </fragment>
    </sourceFilter>
</querySet>
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

[**smartPlaylist Element**](smartplaylist-element.md)
</dt> <dt>

[**sourceFilter Element**](sourcefilter-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





