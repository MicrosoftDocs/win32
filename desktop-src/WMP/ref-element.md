---
title: REF Element
description: The REF element specifies a URL for digital media content.
ms.assetid: '0ba11a1e-3802-4156-83ca-f1bae1eb366c'
keywords:
- REF Element Windows Media Player
topic_type:
- apiref
api_name:
- REF Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# REF Element

The **REF** element specifies a URL for digital media content.

``` syntax
<REF
   HREF = "URL"
>
</REF>
```

## Attributes

**HREF** (required)

URL to any piece of media content supported by Windows Media Player.

## Parent/Child Elements



| Hierarchy       | Elements                                                                         |
|-----------------|----------------------------------------------------------------------------------|
| Parent elements | **ENTRY**                                                                        |
| Child elements  | **DURATION**, **ENDMARKER**, **PREVIEWDURATION**, **STARTMARKER**, **STARTTIME** |



 

## Remarks

This element specifies a URL for a piece of media content. The URL can point to any media type supported, using any protocol supported by Windows Media Player.

The media types supported include still images such as .gif and .jpg images and Flash files with an .swf file name extension. These media types are useful for including advertising content within a playlist. With image files and Flash files that play in a loop, you must also specify the amount of time to display the media item by including a **DURATION** element within the **REF** element. If you want an image to continue displaying while the next entry in the playlist is buffered, include a **PARAM** element within the **ENTRY** element, set its **name** attribute to ShowWhileBuffering, and set its **value** attribute to true.

To reference content on a CD or a DVD that allows it, the wmpcd and wmpdvd protocols are provided. For example, setting the **HREF** attribute to "wmpdvd://f/5/3" will play chapter 3 of title 5 on a DVD, but only if the DVD has been authored to allow it.

Applications that open digital media from behind a firewall will have better performance when opening the media items if the address is specified using the domain name server (DNS) name instead of the IP address.

The most common use of this element is for URL rollover. If Windows Media Player is unable to open a piece of media defined in a **REF** element, it tries the URL in the next **REF** element. Once Windows Media Player opens media content from a URL defined within the scope of one **ENTRY** element, it ignores subsequent **REF** tags within that **ENTRY** element. After the piece of content is done playing, Windows Media Player moves on to the next **ENTRY** element, if any.

-   **Important** Once Windows Media Player establishes a connection to a referenced piece of content, it ignores all other **REF** elements in that **ENTRY**, whether the connection terminates normally or abnormally.

If the media item referenced is an image file, the **DURATION** element must be used to specify the display time for the image.

**Note**

Attempting to play Flash media that includes sound with the first frame may yield unexpected results. You should author Flash content to play sound starting no earlier than the second frame.

## Examples


```XML
<ASX VERSION="3.0">
   <ENTRY>
   <TITLE>Example Clip</TITLE>
      <REF HREF="mms://example.microsoft.com/selection1.asf" />
      <REF HREF="mms://sample.microsoft.com/mirror/selection1.asf" />
   </ENTRY>
</ASX>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Supported Protocols and File Types**](supported-protocols-and-file-types.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





