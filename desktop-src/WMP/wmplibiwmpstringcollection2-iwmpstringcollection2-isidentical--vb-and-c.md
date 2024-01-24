---
title: IWMPStringCollection2 isIdentical method
description: The isIdentical method returns a value indicating whether the object represented by the supplied interface is the same as the current one.
ms.assetid: 826e7fd8-88f8-4a2a-9ca0-82a500099272
keywords:
- isIdentical method Windows Media Player
- isIdentical method Windows Media Player , IWMPStringCollection2 interface
- IWMPStringCollection2 interface Windows Media Player , isIdentical method
topic_type:
- apiref
api_name:
- IWMPStringCollection2.isIdentical
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPStringCollection2::isIdentical method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isIdentical** method returns a value indicating whether the object represented by the supplied interface is the same as the current one.

## Syntax


```CSharp
public System.Boolean isIdentical(
  IWMPStringCollection2 pIWMPStringCollection2
);
```


```VB

Public Function isIdentical( _
  ByVal pIWMPStringCollection2 As IWMPStringCollection2 _
) As System.Boolean
Implements IWMPStringCollection2.isIdentical
```





## Parameters

<dl> <dt>

*pIWMPStringCollection2* \[in\]
</dt> <dd>

The **WMPLib.IWMPStringCollection2** interface that represents the object to compare with current one.

</dd> </dl>

## Return value

The **System.Boolean** that is the result of the comparison. A value of **true** indicates that the string collection objects are the same.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPStringCollection2 Interface (VB and C#)**](iwmpstringcollection2--vb-and-c.md)
</dt> </dl>

 

 





