---
title: argument Element
description: The argument element contains one portion of a condition string.
ms.assetid: 7e4744ce-e9e2-4a70-a2cc-d33ae1ad2f99
keywords:
- argument Element Windows Media Player
topic_type:
- apiref
api_name:
- argument Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# argument Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **argument** element contains one portion of a condition string. A condition string typically has a condition portion and a value portion. For example, in the condition string "Artist Equals Joe", the condition portion is "Equals" and the value portion is "Joe".

``` syntax
<argument
   name = "string"
>
   string
</argument>
        
```

## Attributes

**name** (required)

The name of one portion of the condition string.

## Parent/Child Elements



| Hierarchy | Elements                         |
|-----------|----------------------------------|
| Parent    | [fragment](fragment-element.md) |
| Child     | None                             |



 

## Remarks

When the **name** attribute of a **fragment** element is a media item characteristic such as Album Artist, or Genre, the **fragment** element must contain two **argument** elements: one that specifies a condition and another that specifies a value. The following table shows two possible values for the **name** attribute and how **argument** elements are used to specify conditions and values.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Attribute value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Condition</td>
<td>The content of the <strong>argument</strong> element is the condition portion of a condition string. For example, in the condition string &quot;Artist Equals Joe&quot;, the condition portion is &quot;Equals&quot;. The condition portion of a condition string must be one of the following: Equals, Does Not Equal, Contains, Does Not Contain, Is Less Than, Is Greater Than, Is, Is Not, Is Before, Is Later Than, Is More Recent Than, Above, Below, Ascending, Descending, Random, Is At Least, Is No More Than.</td>
</tr>
<tr class="even">
<td>Value</td>
<td>The content of the <strong>argument</strong> element is the value portion of a condition string. For example, in the condition string &quot;Artist Equals Joe&quot;, the value portion is &quot;Joe&quot;.Example:<br/>
<pre data-space="preserve"><code>\&lt;fragment name = &quot;Artist&quot;&gt;
  &lt;argument name = &quot;Condition&quot;>Equals&lt;/argument&gt;
  &lt;argument name = &quot;Value&quot;>Joe&lt;/argument&gt;
&lt;/fragment&gt;</code></pre></td>
</tr>
</tbody>
</table>



 

When the **name** attribute of a **fragment** element is "Limit Total Size To" or "Limit Total Duration To", the **fragment** element must contain two **argument** elements: one that specifies a format and one that specifies a number. The following table shows two possible values for the **name** attribute and how **argument** elements are used to limit the size or duration of a playlist.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Attribute value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Format</td>
<td>When the <strong>name</strong> attribute of the <strong>fragment</strong> element is &quot;Limit Total Size To&quot;, the content of the <strong>argument</strong> element must be one of the following: Kilobytes, Megabytes, or Gigabytes.When the <strong>name</strong> attribute of the <strong>fragment</strong> element is &quot;Limit Total Duration To&quot;, the content of the <strong>argument</strong> element must be one of the following: Seconds, Minutes, Hours, or Days.<br/></td>
</tr>
<tr class="even">
<td>Number</td>
<td>The content of the <strong>argument</strong> element is a number that limits the size or duration of the playlist.Examples:<br/>
<pre data-space="preserve"><code>\&lt;fragment name = &quot;Limit Total Size To&quot;&gt;
  &lt;argument name = &quot;Format&quot;>Megabytes&lt;/argument&gt;
  &lt;argument name = &quot;Number&quot;>5&lt;/argument&gt;
&lt;/fragment&gt;

\<fragment name = &quot;Limit Total Duration To&quot;>
  &lt;argument name = &quot;Format&quot;>Minutes&lt;/argument&gt;
  &lt;argument name = &quot;Number&quot;>20&lt;/argument&gt;
&lt;/fragment&gt;</code></pre></td>
</tr>
</tbody>
</table>



 

When the **name** attribute of a **fragment** element is "Limit Number of Items", the **fragment** element must contain one **argument** element that specifies the number of items. The following table shows how to use the Number value of the **name** attribute.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Attribute value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Number</td>
<td>The content of the <strong>argument</strong> element is a number that limits the number of items in a playlist.Example:<br/>
<pre data-space="preserve"><code>\&lt;fragment name = &quot;Limit Number of Items&quot;&gt;
  &lt;argument name = &quot;Number&quot;&gt;15&lt;/argument&gt;
&lt;/fragment&gt;</code></pre></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**fragment Element**](fragment-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





