---
title: StringCollection Object
description: The StringCollection object provides a way to manipulate a collection of strings.
ms.assetid: 7d1210fa-9ea5-45cc-89f7-46731413f806
keywords:
- StringCollection Object Windows Media Player
topic_type:
- apiref
api_name:
- StringCollection Object
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StringCollection Object

The **StringCollection** object provides a way to manipulate a collection of strings.

The **StringCollection** object supports the following property.



| Property                            | Description                                             |
|-------------------------------------|---------------------------------------------------------|
| [count](stringcollection-count.md) | Retrieves the number of items in the string collection. |



 

The **StringCollection** object supports the following methods.



| Method                                                                  | Description                                                                                                                     |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [getAttributeCountByType](stringcollection-getattributecountbytype.md) | Retrieves the number of attributes associated with the specified **StringCollection** item index, attribute name, and language. |
| [getItemInfo](stringcollection-getiteminfo.md)                         | Retrieves the string corresponding to the specified **StringCollection** item index and name.                                   |
| [getItemInfoByType](stringcollection-getiteminfobytype.md)             | Retrieves the string corresponding to the specified **StringCollection** item index, name, language, and attribute index.       |
| [isIdentical](stringcollection-isidentical.md)                         | Retrieves a value indicating whether the supplied object is the same as the current one.                                        |
| [item](stringcollection-item.md)                                       | Retrieves the string at the specified index.                                                                                    |



 

The **StringCollection** object is accessed through the following method.



| Object                                        | Method                                                                           |
|-----------------------------------------------|----------------------------------------------------------------------------------|
| [MediaCollection](mediacollection-object.md) | [getAttributeStringCollection](mediacollection-getattributestringcollection.md) |



 

For purposes of illustration, *player*.*mediaCollection*.**getAttributeStringCollection**(*attribute*, *mediaType*) is used in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




