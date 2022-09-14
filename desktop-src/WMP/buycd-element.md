---
title: BuyCD Element
description: Note This section describes functionality designed for use by online stores. | BuyCD Element
ms.assetid: 01aaf20a-49ee-420b-a612-f09155390d4a
keywords:
- BuyCD Element Windows Media Player
topic_type:
- apiref
api_name:
- BuyCD Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BuyCD Element

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **BuyCD** element specifies the URLs for webpages that Windows Media Player displays when the user chooses to make a purchase.

``` syntax
<BuyCD
    MediaPlayerURL = "URL"
    MediaCenterURL = "URL"
    BrowserURL = "URL"
/>
```

## Attributes

<dl> <dt>

<span id="MediaPlayerURL__required_"></span><span id="mediaplayerurl__required_"></span><span id="MEDIAPLAYERURL__REQUIRED_"></span>**MediaPlayerURL** (required)
</dt> <dd>

URL for the webpage that the online store displays to offer a CD or DVD for purchase in Windows Media Player.

</dd> <dt>

<span id="MediaCenterURL"></span><span id="mediacenterurl"></span><span id="MEDIACENTERURL"></span>**MediaCenterURL**
</dt> <dd>

URL for the webpage the online store displays to offer a CD or DVD for purchase in Windows XP Media Center Edition 2004 Update.

</dd> <dt>

<span id="BrowserURL"></span><span id="browserurl"></span><span id="BROWSERURL"></span>**BrowserURL**
</dt> <dd>

URL for the webpage that the online store displays to offer a CD or DVD for purchase in a separate browser window. This URL is also used by Windows XP Service Pack 2 or later for the **Shop for music online** feature.

</dd> </dl>

## Parent/Child Elements



| Hierarchy       | Element         |
|-----------------|-----------------|
| Parent elements | **ServiceInfo** |
| Child elements  | None            |



 

## Remarks

When the user clicks a button or link in Windows Media Player to purchase a CD or DVD, the Player sends the URL request to ServiceTask1 with parameters attached using a question mark (?) query string separator. The following table details the parameters sent with the URL request. Others may be present for legacy compatibility purposes.



| Name         | Value                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Album*      | Value of the **WM/AlbumTitle** attribute for the media item.                                                                                                        |
| *Artist*     | Value of the **WM/AlbumArtist** attribute, if one exists, or else the value of the **Author** attribute for the media item.                                         |
| *geoid*      | Windows geographical location ID. The location ID is specified by the user in the **Location** area of the Regional and Language Options settings in Control Panel. |
| *locale*     | Windows Media Player locale ID.                                                                                                                                     |
| *Title*      | Value of the **Title** attribute for the media item.                                                                                                                |
| *UFID*       | Value of the **WM/UniqueFileIdentifier** attribute for the media item.                                                                                              |
| *userlocale* | Windows locale ID. The locale is specified by the user in the **Standards and Formats** area of the Regional and Language Options settings in Control Panel.        |
| *version*    | Windows Media Player version number using the following format: 10.0.x.xxxx or 11.0.x.xxxx.                                                                         |



 

Windows XP Media Center Edition 2004 provides users with a user interface designed to be viewed at a distance. You should create webpages for the *MediaCenterURL* parameter to be viewed on large displays.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 10 or later.<br/> |



## See also

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 





