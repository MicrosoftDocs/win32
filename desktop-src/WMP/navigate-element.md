---
title: Navigate Element
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The Navigate element specifies a URL used by calls to External.NavigateTaskPaneURL.
ms.assetid: 3898e381-baf8-481a-90ee-d64e55b319a0
keywords:
- Navigate Element Windows Media Player
topic_type:
- apiref
api_name:
- Navigate Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Navigate Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **Navigate** element specifies a URL used by calls to **External.NavigateTaskPaneURL**.

``` syntax
<Navigate
    BaseURL = "URL"
/>
```

## Attributes



| Term                                                                                                                                             | Description                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BaseURL__required_"></span><span id="baseurl__required_"></span><span id="BASEURL__REQUIRED_"></span>**BaseURL** (required)<br/> | Fully qualified URL for the webpage to which to navigate. **NavigateTaskPaneURL** can append a query string to this URL.<br/> |



 

## Parent/Child Elements



| Hierarchy       | Element         |
|-----------------|-----------------|
| Parent elements | **ServiceInfo** |
| Child elements  | None            |



 

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

[**External.NavigateTaskPaneURL**](external-navigatetaskpaneurl.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 





