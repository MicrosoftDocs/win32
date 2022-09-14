---
title: DownloadStatus Element (Msfeeds.h)
description: Note This section describes functionality designed for use by online stores. | DownloadStatus Element (Msfeeds.h)
ms.assetid: 08d9719a-390d-454a-935e-27812c0f3599
keywords:
- DownloadStatus Element Windows Media Player
topic_type:
- apiref
api_name:
- DownloadStatus Element
api_location:
- msfeeds.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DownloadStatus Element

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **DownloadStatus** element specifies a URL the Windows Media Player displays as a link to enable users to view download status.

``` syntax
<DownloadStatus
    URL = "URL"
/>
```

## Attributes

<dl> <dt>

<span id="URL"></span><span id="url"></span>URL
</dt> <dd>

URL for the webpage that the online store displays to show download status to the user.

</dd> </dl>

## Parent/Child Elements



| Hierarchy       | Element         |
|-----------------|-----------------|
| Parent elements | **ServiceInfo** |
| Child elements  | None            |



 

## Remarks

Windows Media Player displays a message to users when a download is in progress. If the current active services defines a download status URL, the user can click the message text. When the user clicks the message, the Player navigates to the URL specified by the **DownloadStatus** element so the current active store can provide details about downloads in progress.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/>                                          |
| Header<br/>  | <dl> <dt>Msfeeds.h</dt> </dl> |



## See also

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 





