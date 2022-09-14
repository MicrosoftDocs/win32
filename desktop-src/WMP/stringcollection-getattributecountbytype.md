---
title: StringCollection.getAttributeCountByType method
description: The getAttributeCountByType method retrieves the number of attributes associated with the specified StringCollection item index, attribute name, and language.
ms.assetid: 3671b7b7-d6d4-4049-8710-d0f34c740b1e
keywords:
- getAttributeCountByType method Windows Media Player
- getAttributeCountByType method Windows Media Player , StringCollection class
- StringCollection class Windows Media Player , getAttributeCountByType method
topic_type:
- apiref
api_name:
- StringCollection.getAttributeCountByType
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# StringCollection.getAttributeCountByType method

The **getAttributeCountByType** method retrieves the number of attributes associated with the specified **StringCollection** item index, attribute name, and language.

## Syntax


```JScript
retVal = StringCollection.getAttributeCountByType(
  index,
  name,
  language
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) specifying the zero-based index of the **StringCollection** item from which to get the attribute.

</dd> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the name of the attribute.

</dd> <dt>

*language* \[in\]
</dt> <dd>

**String** containing the language. If the value is set to null or the empty string (""), the current locale string is used. Otherwise, the value must be a valid RFC 1766 language string such as "en-us".

</dd> </dl>

## Return value

This method returns a **Number** (**long**).

## Remarks

This method is used to determine the number of attributes corresponding to a particular attribute name for a particular **StringCollection** item. Index numbers can then be passed to the fourth parameter of the **StringCollection.getItemInfoByType** method.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**StringCollection Object**](stringcollection-object.md)
</dt> </dl>

 

 





