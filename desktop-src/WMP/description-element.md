---
title: Description Element
description: Note This section describes functionality designed for use by online stores. | Description Element
ms.assetid: 4d9ff447-e5a4-46b1-b599-87202077abfb
keywords:
- Description Element Windows Media Player
topic_type:
- apiref
api_name:
- Description Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Description Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **Description** element specifies a marketing description of the online store that is displayed during the user's first experience with an installation of Windows Media Player.

``` syntax
<Description>
    text string
</Description>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy       | Element         |
|-----------------|-----------------|
| Parent elements | **ServiceInfo** |
| Child elements  | None            |



 

## Remarks

The length of the description must be less than or equal to 255 characters.

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------|
| Version<br/> | Windows Media Player 11.<br/> |



## See also

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 





