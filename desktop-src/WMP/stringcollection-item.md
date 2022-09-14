---
title: StringCollection.item method
description: The item method retrieves the string at the specified index.
ms.assetid: '5f6afff2-3ecc-4b28-8c67-f859f5440d4f'
keywords:
- item method Windows Media Player
- item method Windows Media Player , StringCollection class
- StringCollection class Windows Media Player , item method
topic_type:
- apiref
api_name:
- StringCollection.item
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# StringCollection.item method

The **item** method retrieves the string at the specified index.

## Syntax


```JScript
strRetVal = StringCollection.item(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) containing the index.

</dd> </dl>

## Return value

This method returns a **String**.

## Remarks

The **StringCollection** object is used to retrieve the set of values available for an attribute. For example, the *MediaCollection*.**getAttributeStringCollection** method can be used to retrieve a **StringCollection** object representing all the values for the Genre attribute within the Audio media type. The **item** property can then be used to iterate through all of the possible values for the Genre attribute.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection.getAttributeStringCollection**](mediacollection-getattributestringcollection.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> <dt>

[**StringCollection Object**](stringcollection-object.md)
</dt> </dl>

 

 





