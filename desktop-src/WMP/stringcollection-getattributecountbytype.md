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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# StringCollection.getAttributeCountByType method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





