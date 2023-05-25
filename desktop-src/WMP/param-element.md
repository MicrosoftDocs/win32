---
title: PARAM Element (WMP SDK)
description: The PARAM element defines a custom parameter associated with a playlist or an element of a playlist.
ms.assetid: d905a42a-ac89-4c99-94ca-b3b7060ebbdc
keywords:
- PARAM Element Windows Media Player
topic_type:
- apiref
api_name:
- PARAM Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PARAM Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PARAM** element defines a custom parameter associated with a playlist or an element of a playlist.

``` syntax
<PARAM
   NAME = "parameter name"
   VALUE = "parameter value"
/>
```

## Parameters

A parameter can also be associated with the show rather than an individual clip, by placing this element directly after the **ASX** tag. These items are referenced by their names and an index value beginning with zero.

> [!Note]  
> This **ASX** element is only available for Windows Media Player version 6.01 and later. The standard installation of Microsoft Internet Explorer 5 includes a compatible version of Windows Media Player.

 

## Attributes

**NAME**

Name used to access the parameter value. The name can be any valid string. The following strings have already been defined.



| String                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AllowShuffle                    | The **VALUE** attribute specifies whether the metafile playlist allows the Windows Media Player shuffle feature to play the entries in random order. The **VALUE** attribute can be set to "Yes" or "No". The default value is "No".                                                                                                                                                                                                                                                                                                                                                                  |
| CanPause                        | The **VALUE** attribute specifies whether the user can pause playback. The **VALUE** attribute can be set to "Yes" or "No". The default value is "Yes".                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| CanSeek                         | The **VALUE** attribute specifies whether the user can change the current playback position by using the seek bar, fast forward, or fast reverse. The **VALUE** attribute can be set to "Yes" or "No". The default value is "Yes".                                                                                                                                                                                                                                                                                                                                                                    |
| CanSkipBack                     | The **VALUE** attribute specifies whether the user can skip backward to the previous playlist item by clicking **Previous**. The **VALUE** attribute can be set to "Yes" or "No". The default value is "Yes".                                                                                                                                                                                                                                                                                                                                                                                         |
| CanSkipForward                  | The **VALUE** attribute specifies whether the user can skip forward to the next playlist item by clicking **Next**. The **VALUE** attribute can be set to "Yes" or "No". The default value is "Yes".                                                                                                                                                                                                                                                                                                                                                                                                  |
| CPRadioID                       | The **VALUE** attribute specifies the ID of a radio feed provided by a type 1 online store. That is, the **VALUE** attribute must be equal to the RadioID field of one of the radio feeds in the online store's catalog. The parent element is the **ASX** element.                                                                                                                                                                                                                                                                                                                                   |
| Encoding                        | The **VALUE** attribute is set to "utf-8" to indicate that the metafile is a Unicode (UTF-8) encoded file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| HtmlFlink                       | The **VALUE** attribute is a string provided by a type 1 online store. Windows Media Player passes the string to the [IWMPContentPartner::GetItemInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getiteminfo) method, which is implemented by the online store's plug-in. The **GetItemInfo** method returns the URL of the webpage to display in the **Now Playing** pane of the Player. The webpage has access to all of the methods that the **External** object exposes to type 1 stores. For a list of those methods, see [External Object for Type 1 Online Stores](external-object-for-type-1-online-stores.md). |
| HTMLView                        | The **VALUE** attribute specifies a URL that displays in the **Now Playing** pane of the full mode Player for the duration of the playlist or the current entry depending on whether the parent element is the **ASX** element or an **ENTRY** element. HTMLView is not supported for the Windows Media Player control.                                                                                                                                                                                                                                                                               |
| Log:*FieldName*\[:*NameSpace*\] | The **VALUE** attribute specifies the value that the indicated log field will be set to. The :*NameSpace* portion of the **NAME** attribute is optional.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Prebuffer                       | The **VALUE** attribute specifies whether the next playlist entry begins buffering before the end of the current entry, which enables a seamless transition. The **VALUE** attribute can be set to "true" or "false".                                                                                                                                                                                                                                                                                                                                                                                 |
| ShowWhileBuffering              | The **VALUE** attribute specifies whether an image file referenced by the current **ENTRY** element continues to display past its specified duration time while the next playlist entry is buffered. The **VALUE** attribute can be set to "true" or "false".                                                                                                                                                                                                                                                                                                                                         |



 

**VALUE**

Value associated with this parameter. It can be either a numeric or string value.

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ASX**, **ENTRY** |
| Child elements  | None               |



 

## Remarks

This element allows users to place additional information about each clip inside the **ENTRY** element that contains it. To retrieve metadata information specified in the playlist **ENTRY**, use the *Media*.**getItemInfo** method. The *Media*.**getItemInfo** method retrieves the value of the **VALUE** attribute, given the name of the parameter. Previous versions of Windows Media Player retrieve metadata information specified in the playlist **ENTRY**, using the **GetMediaParameter** method given the name of the parameter and an index number for the entry.

A parameter can also be associated with the show rather than an individual clip, by placing this element directly after the **ASX** tag. These items are referenced by their names and an index value beginning with zero.

**Note**

This **ASX** element is only available for Windows Media Player version 6.01 and later. The standard installation of Microsoft Internet Explorer 5 includes a compatible version of Windows Media Player.

## Examples


```XML
<ASX VERSION="3.0">
   <TITLE>Example Media Player Show</TITLE>
   <PARAM NAME="Director" VALUE="Jane D." />
   
   <ENTRY>
      <TITLE>Example Clip</TITLE>
      <REF HREF="https://sample.microsoft.com/media.asf" />
      <PARAM NAME="Location" VALUE="North America" />
      <PARAM NAME="Release Date" VALUE="March 1998" />
   </ENTRY>
   
   <ENTRY>
      <TITLE>Another Clip</TITLE>
      <REF HREF="https://sample.microsoft.com/more_media.asf" />
      <PARAM NAME="Location" VALUE="Japan">
      <PARAM NAME="Release Date" VALUE="December 1996" />
   </ENTRY>
</ASX>

```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later, Windows Media Player 9 Series or later is required for the predefined NAME attributes, Windows Media Player 10 or later is required for the predefined names CanPause, CanSeek, CanSkipBack, and CanSkipForward<br/> |



## See also

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**Logging Stream Data**](logging-stream-data.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





