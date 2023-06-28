---
title: StringCollection.getItemInfo method
description: The getItemInfo method retrieves the string corresponding to the specified StringCollection item index and name.
ms.assetid: a031b91e-9d3b-47ac-bc5b-c111d5e3bc12
keywords:
- getItemInfo method Windows Media Player
- getItemInfo method Windows Media Player , StringCollection class
- StringCollection class Windows Media Player , getItemInfo method
topic_type:
- apiref
api_name:
- StringCollection.getItemInfo
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# StringCollection.getItemInfo method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getItemInfo** method retrieves the string corresponding to the specified **StringCollection** item index and name.

## Syntax


```JScript
strRetVal = StringCollection.getItemInfo(
  index,
  name
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

**String** containing the attribute name.

</dd> </dl>

## Return value

This method returns a **String** representing the value of the specified attribute. For attributes whose underlying value is **Boolean**, it returns the string "true" or "false".

## Remarks

To retrieve attributes with multiple values and attributes with complex values, use the **getItemInfoByType** method.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**StringCollection.getItemInfoByType**](stringcollection-getiteminfobytype.md)
</dt> <dt>

[**StringCollection Object**](stringcollection-object.md)
</dt> </dl>

 

 





