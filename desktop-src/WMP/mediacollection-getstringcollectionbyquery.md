---
title: MediaCollection.getStringCollectionByQuery method
description: The getStringCollectionByQuery method retrieves a StringCollection object containing all strings that match the query conditions.
ms.assetid: 17442151-7eb1-4256-ac5f-142b11645216
keywords:
- getStringCollectionByQuery method Windows Media Player
- getStringCollectionByQuery method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , getStringCollectionByQuery method
topic_type:
- apiref
api_name:
- MediaCollection.getStringCollectionByQuery
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MediaCollection.getStringCollectionByQuery method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getStringCollectionByQuery** method retrieves a **StringCollection** object containing all strings that match the query conditions.

## Syntax


```JScript
retVal = MediaCollection.getStringCollectionByQuery(
  attribute,
  query,
  mediaType,
  sortAttribute,
  sortAscending
)
```



## Parameters

<dl> <dt>

*attribute* \[in\]
</dt> <dd>

**String** containing the attribute name.

</dd> <dt>

*query* \[in\]
</dt> <dd>

**Query** object.

</dd> <dt>

*mediaType* \[in\]
</dt> <dd>

**String** containing the media type. Must contain one of the following values: "audio", "video", "photo", "playlist", or "other".

</dd> <dt>

*sortAttribute* \[in\]
</dt> <dd>

**String** containing the attribute name used for sorting. An empty string ("") means no sorting is applied.

</dd> <dt>

*sortAscending* \[in\]
</dt> <dd>

**Boolean**, true indicating that the **StringCollection** must be sorted in ascending order.

</dd> </dl>

## Return value

This method returns a **StringCollection** object.

## Remarks

Compound queries using **Query** are not case sensitive.

When the compound query specified by the *query* parameter contains a condition built on the **MediaType** attribute, that condition is ignored. The value for the *mediaType* parameter is always used. For example, if the compound query contains the condition "MediaType Equals audio" and the value for the *mediaType* parameter is "video", the resulting playlist will contain only video items.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**MediaType Attribute**](mediatype-attribute.md)
</dt> <dt>

[**Query Object**](query-object.md)
</dt> </dl>

 

 





