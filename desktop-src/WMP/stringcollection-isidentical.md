---
title: StringCollection.isIdentical method
description: The isIdentical method retrieves a value indicating whether the supplied object is the same as the current one. | StringCollection.isIdentical method
ms.assetid: 5f2aabbe-e6c7-4aa2-a30d-30178a4ba3db
keywords:
- isIdentical method Windows Media Player
- isIdentical method Windows Media Player , StringCollection class
- StringCollection class Windows Media Player , isIdentical method
topic_type:
- apiref
api_name:
- StringCollection.isIdentical
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# StringCollection.isIdentical method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isIdentical** method retrieves a value indicating whether the supplied object is the same as the current one.

## Syntax


```JScript
bRetVal = StringCollection.isIdentical(
  stringCollection
)
```



## Parameters

<dl> <dt>

*stringCollection* \[in\]
</dt> <dd>

**StringCollection** object to compare with the current one.

</dd> </dl>

## Return value

This method returns a **Boolean**.

## Remarks

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

 

 





