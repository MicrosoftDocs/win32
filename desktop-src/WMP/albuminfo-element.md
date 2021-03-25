---
title: AlbumInfo Element
description: The AlbumInfo element specifies the URL for the webpage that Windows Media Player displays when the user chooses to view more information about a particular media item.
ms.assetid: c872e95a-3723-4ce8-8d61-e2bc9e12c785
keywords:
- AlbumInfo Element Windows Media Player
topic_type:
- apiref
api_name:
- AlbumInfo Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AlbumInfo Element

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **AlbumInfo** element specifies the URL for the webpage that Windows Media Player displays when the user chooses to view more information about a particular media item.

``` syntax
<AlbumInfo
   URL = "URL"
/>
      
```

## Attributes

<dl> <dt>

<span id="URL__required_"></span><span id="url__required_"></span><span id="URL__REQUIRED_"></span>**URL** (required)
</dt> <dd>

URL for the webpage that Windows Media Player displays.

</dd> </dl>

## Parent/Child Elements



| Hierarchy       | Element         |
|-----------------|-----------------|
| Parent elements | **ServiceInfo** |
| Child elements  | None            |



 

## Remarks

When the user clicks a button in Windows Media Player to view additional information about a particular media item, the Player sends the URL request with parameters attached using a question mark (?) query string separator. The following table details the parameters sent with the URL request. Others may be present for legacy compatibility purposes.



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

 

 





