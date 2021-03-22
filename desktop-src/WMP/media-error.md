---
title: Media.error
description: The error property retrieves an ErrorItem object if the media item has an error condition.
ms.assetid: cd572688-12f9-4615-8f22-9442d615a2b6
keywords:
- Media.error Windows Media Player
topic_type:
- apiref
api_name:
- Media.error
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Media.error

The **error** property retrieves an **ErrorItem** object if the media item has an error condition.

## Syntax

*player*.*currentMedia*.**error**

## Possible Values

This property is a read-only **ErrorItem** object.

## Remarks

If the media item cannot be played, this property retrieves an **ErrorItem** object that contains information about the problem encountered.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later.<br/>                           |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> </dl>

 

 





