---
title: InfoCenter Element
description: Note This section describes functionality designed for use by online stores. | InfoCenter Element
ms.assetid: 1a9cc513-5dd1-46d8-9409-16413695b4c8
keywords:
- InfoCenter Element Windows Media Player
topic_type:
- apiref
api_name:
- InfoCenter Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# InfoCenter Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **InfoCenter** element specifies the URL of the webpage that Windows Media Player displays in the Info Center View feature of **Now Playing** when the online store is active.

``` syntax
<InfoCenter
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

The user controls when Info Center View is active.

To retrieve information about the currently playing media item, you must embed an instance of Windows Media Player control in your webpage and use the Player object model.

The following table details the parameters sent with the URL request. Others may be present for legacy compatibility purposes.



| Name         | Value                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *geoid*      | Windows geographical location ID. The location ID is specified by the user in the **Location** area of the Regional and Language Options settings in Control Panel. |
| *locale*     | Windows Media Player locale ID.                                                                                                                                     |
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

 

 





