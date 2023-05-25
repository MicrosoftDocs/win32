---
title: MediaCollection.createQuery method
description: The createQuery method creates a new Query object.
ms.assetid: f6360717-ea36-456c-8f3d-683ab6df012e
keywords:
- createQuery method Windows Media Player
- createQuery method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , createQuery method
topic_type:
- apiref
api_name:
- MediaCollection.createQuery
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MediaCollection.createQuery method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **createQuery** method creates a new **Query** object.

## Syntax


```JScript
retVal = MediaCollection.createQuery()
```



## Parameters

This method has no parameters.

## Return value

This method returns a new, empty **Query** object.

## Remarks

Creating a new **Query** object is the first step toward creating a compound query.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Query Object**](query-object.md)
</dt> </dl>

 

 





