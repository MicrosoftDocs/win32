---
title: MetadataText Object
description: The MetadataText object provides a way to retrieve metadata for complex textual metadata attributes.
ms.assetid: 91d74b16-5a34-4ff3-9099-6590b12ed1cb
keywords:
- MetadataText Object Windows Media Player
topic_type:
- apiref
api_name:
- MetadataText Object
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MetadataText Object

The **MetadataText** object provides a way to retrieve metadata for complex textual metadata attributes.

The **MetadataText** object supports the following properties.



| Property                                    | Description                                   |
|---------------------------------------------|-----------------------------------------------|
| [description](metadatatext-description.md) | Retrieves a description of the metadata text. |
| [text](metadatatext-text.md)               | Retrieves the metadata text.                  |



 

The **MetadataText** object is accessed through the following method.



| Object                    | Method                                           |
|---------------------------|--------------------------------------------------|
| [Media](media-object.md) | [getItemInfoByType](media-getiteminfobytype.md) |



 

For purposes of illustration, *player*.*currentMedia*.**getItemInfoByType**(*name*, *language*, *index*) is used in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




