---
title: fragment Element
description: The fragment element specifies one condition of the query that selects items from the library. Conditions are specified by condition strings. A condition string typically has a name portion, a condition portion, and a value portion.
ms.assetid: 1575318f-8527-42ba-9c2f-9993a60987d7
keywords:
- fragment Element Windows Media Player
topic_type:
- apiref
api_name:
- fragment Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# fragment Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **fragment** element specifies one condition of the query that selects items from the library. Conditions are specified by condition strings. A condition string typically has a name portion, a condition portion, and a value portion.

``` syntax
<fragment
    name = "string"
>
</fragment>
```

## Attributes

<dl> <dt>

<span id="name__required______________"></span><span id="NAME__REQUIRED______________"></span>**name** (required) 
</dt> <dd>

A portion of a condition string. See Remarks.

</dd> </dl>

## Parent/Child Elements



| Hierarchy | Elements                                                               |
|-----------|------------------------------------------------------------------------|
| Parent    | [filter](filter-element.md), [sourceFilter](sourcefilter-element.md) |
| Child     | [argument](argument-element.md)                                       |



 

## Remarks

Certain condition strings have a metadata attribute portion, a condition portion, and a value portion. For example, in the condition string "Album Artist Is Joe", the metadata attribute portion is "Album Artist", the condition portion is "Is", and the value portion is "Joe".

Example:


```XML
<fragment name = "Album Artist">
    <argument name = "condition">Is</argument>
    <argument name = "value">Joe</argument>
</fragment>
```



For condition strings of this type, the following table shows the possible metadata attributes, possible conditions and possible values:



| Metadata attribute                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Possible conditions                                                                                             | Possible values                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ActorAlbum Artist<br/> Album Title<br/> Author<br/> Caption<br/> Channel<br/> Composer<br/> Conductor<br/> Content Provider<br/> Content Provider Genre<br/> Contributing Artist<br/> Copyright Text<br/> Director<br/> Episode<br/> File Type<br/> Genre<br/> Key<br/> Keywords<br/> Language<br/> Mood<br/> Parental Rating<br/> Period<br/> Producer<br/> Provider<br/> Publisher<br/> Series<br/> Station name<br/> Subgenre<br/> Subtitle<br/> Title<br/> Writer<br/> | EqualsDoes Not Equal<br/> Is<br/> Is Not<br/> Contains<br/> Does Not Contain<br/> | Any string value                                                                                                                                                                                                                                                                                                  |
| Bit Rate (In kilobytes per second.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | EqualsDoes Not Equal<br/> Is<br/> Is Not<br/> Contains<br/> Does Not Contain<br/> | 4864<br/> 96<br/> 128<br/> 160<br/> 192<br/> 256<br/> 300<br/> 500<br/> 750<br/> 1000<br/> 1500<br/> 3000<br/> 4500<br/> 6000<br/> 7500<br/>                                                                            |
| Secondary Media Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | EqualsDoes Not Equal<br/> Is<br/> Is Not<br/> Contains<br/> Does Not Contain<br/> | Audio: NewsAudio: Talk Show<br/> Audio: Audio Books<br/> Audio: Audio Spoken Word<br/> Video: News<br/> Video: Talk Show<br/> Video: Home Video<br/> Video: Movie / Film<br/> Video: TV show<br/> Video: Corporate Video<br/> Video: Music Video<br/> |
| File Size (in KB)Image height<br/> Image width<br/> Play Count : Afternoon Totals<br/> Play Count : Evening Totals<br/> Play Count : Morning Totals<br/> Play Count : Night Totals<br/> Play Count : Total Overall<br/> Play Count : Total Weekday<br/> Play Count : Total Weekend<br/>                                                                                                                                                                                                                                                                                                                  | Is Less ThanIs Greater Than<br/> Is<br/> Is Not<br/>                                          | Any number                                                                                                                                                                                                                                                                                                        |
| Broadcast timeDate Encoded<br/> Date Recorded<br/> Date taken<br/> Release Year<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Is BeforeIs After<br/> Is<br/> Is Not<br/>                                                    | YesterdayLast week<br/> Last month<br/> 6 months<br/> 1 year<br/> 2 years<br/> 5 years<br/> 2000s<br/> 1990s<br/> 1980s<br/> 1970s<br/> 1960s<br/> 1950s<br/> 1940s<br/>                                                            |
| Date Added                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Is BeforeIs After<br/> Is<br/> Is Not<br/>                                                    | YesterdayLast week<br/> Last month<br/> 6 months<br/> 1 year<br/> 2 years<br/> 5 years<br/>                                                                                                                                                                                   |
| Date Last Played                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Older ThanMore Recent Than<br/> Is<br/> Is Not<br/>                                           | YesterdayLast week<br/> Last month<br/> 6 months<br/> 1 year<br/> 2 years<br/> 5 years<br/>                                                                                                                                                                                   |
| Month taken                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Is BeforeIs More Recent Than<br/> Is<br/> Is Not<br/>                                         | 12<br/> 3<br/> 4<br/> 5<br/> 6<br/> 7<br/> 8<br/> 9<br/> 10<br/> 11<br/> 12<br/> 13<br/>                                                                                                                                                  |
| Year taken                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Is BeforeIs More Recent Than<br/> Is<br/> Is Not<br/>                                         | Any year                                                                                                                                                                                                                                                                                                          |
| Auto RatingMy Rating<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Is At LeastIs No More Than<br/> Is<br/> Is Not<br/>                                           | Unrated1 Star<br/> 2 Stars<br/> 3 Stars<br/> 4 Stars<br/> 5 Stars<br/>                                                                                                                                                                                                              |
| Custom Field \#1Custom Field \#2<br/> File Name<br/> Key Fields<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | ContainsDoes Not Contain<br/>                                                                             | Any string                                                                                                                                                                                                                                                                                                        |



 

Certain condition strings have a limiter portion, a number portion and a format portion. For example in the condition string "Limit Total Size To 3 Megabytes", the limiter portion is "Limit Total Size To", the number portion is "3" and the format portion is "Megabytes".

Example:


```XML
<fragment name = "Limit Total Size To">
  <argument name = "number">3</argument>
  <argument name = "format">Megabytes</argument>
</fragment>
```



For condition strings of this type the following table shows the possible limiters and formats.



| Limiter                 | Possible numbers | Possible formats                |
|-------------------------|------------------|---------------------------------|
| Limit Total Size To     | Any number       | Kilobytes, Megabytes, Gigabytes |
| Limit Total Duration To | Any number       | Seconds, Minutes, Hours, Days   |



 

Certain condition strings have a limiter portion and a number portion. For example in the condition string "Limit Number of Items to 25", the limiter portion is "Limit Number of Items" and the number portion is "25".

Example:


```XML
<fragment name = "Limit Number of Items">
    <argument name = "number">25</argument>
</fragment>
```



For condition strings of this type the following table shows the only possible limiter.



| Limiter               | Possible numbers |
|-----------------------|------------------|
| Limit Number Of Items | Any number       |



 

Certain condition strings have a protection portion and a condition portion. For example in the condition string "Protection Is present", the protection portion is "Protection" and the condition portion is "Is".

Example:


```XML
<fragment name = "Protection">
    <argument name = "condition">Is</argument>
</fragment>
```



For condition strings of this type the following table shows the possible conditions.



| Protection portion | Possible conditions             |
|--------------------|---------------------------------|
| Protection         | Is<br/> Is Not<br/> |



 

There is one type of **fragment** element that does not contain a condition string. If the name attribute of a **fragment** element is "Randomize Playback Order" the **fragment** element contains no **argument** elements. This **fragment** element instructs the player to play the list in random order.

Example:


```XML
<fragment name = "Randomize Playback Order">
</fragment>
```



Certain condition strings have a sort portion, a value portion and a condition portion. For example, in the condition string "Sort By Title Ascending order", the sort portion is "Sort By", the value portion is "Title", and the condition portion is "Ascending". Note that in this case the value portion is a metadata attribute.

Example:


```XML
<fragment name = "Sort By">
    <argument name = "value">Title</argument>
    <argument name = "condition">Ascending</argument>
</fragment>
```



For condition strings of this type the following table shows the possible values and conditions.



| Sort portion | Possible values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Possible conditions                              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| Sort By      | GenreTitle<br/> Date Added<br/> Auto Rating<br/> My Rating<br/> Play Count : Total Overall<br/> Play Count : Morning Totals<br/> Play Count : Afternoon Totals<br/> Play Count : Evening Totals<br/> Play Count : Night Totals<br/> Play Count : Total Weekday<br/> Play Count : Total Weekend<br/> Actor<br/> Subtitle<br/> Station name<br/> Channel<br/> Broadcast time<br/> Director<br/> Release Year<br/> Writer<br/> Producer<br/> Date Recorded<br/> Date Encoded<br/> Bit Rate<br/> Protection<br/> | AscendingDescending<br/> Random<br/> |



 

When you use a fragment element to sort a playlist, you must sort on a metadata attribute that applies to the type of media items you are sorting. For example, if you are sorting music items you can not sort on Actor. The following table shows which metadata attributes you can use to sort which media types.



| Media type  | Possible metadata attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Music       | GenreTitle<br/> Date Added<br/> Auto Rating<br/> My Rating<br/> Play Count : Total Overall<br/> Play Count : Morning Totals<br/> Play Count :Afternoon Totals<br/> Play Count :Evening Totals<br/> Play Count :Night Totals<br/> Play Count :Total Weekday<br/> Play Count : Total Weekend<br/>                                                                                                                                                                                                                                                                                            |
| Video or TV | GenreActor<br/> Subtitle<br/> Title<br/> Date Added<br/> Auto Rating<br/> Station name<br/> Channel<br/> Broadcast time<br/> Director<br/> Release Year<br/> Writer<br/> Producer<br/> Date Recorded<br/> Date Encoded<br/> Bit Rate<br/> My Rating<br/> Protection<br/> Play Count : Total Overall<br/> Play Count : Morning Totals<br/> Play Count : Afternoon Totals<br/> Play Count : Evening Totals<br/> Play Count : Night Totals<br/> Play Count : Total Weekday<br/> Play Count : Total Weekend<br/> |
| Radio       | TitleDate Added<br/> Bit Rate<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Photo       | Title                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Other       | GenreTitle<br/> Date Added<br/> Auto Rating<br/> My Rating<br/> Bit Rate<br/> Play Count : Total Overall<br/> Play Count : Morning Totals<br/> Play Count : Afternoon Totals<br/> Play Count : Evening Totals<br/> Play Count : Night Totals<br/> Play Count : Total Weekday<br/> Play Count : Total Weekend<br/>                                                                                                                                                                                                                                                                    |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**argument Element**](argument-element.md)
</dt> <dt>

[**filter Element**](filter-element.md)
</dt> <dt>

[**sourceFilter Element**](sourcefilter-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





