---
title: IWMPPlaylist.isIdentical (VB and C )
description: The isIdentical property (the get\_isIdentical method in C\ ) gets a value indicating whether the specified playlist is identical to the current playlist.
ms.assetid: 0e5520ee-3d41-4e36-98f4-7bc2ec45fcb8
keywords:
- IWMPPlaylist.isIdentical (VB and C ) Windows Media Player
topic_type:
- apiref
api_name:
- IWMPPlaylist.isIdentical (VB and C )
api_location:
- Interop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPPlaylist.isIdentical (VB and C#)

The **isIdentical** property (the **get\_isIdentical** method in C#) gets a value indicating whether the specified playlist is identical to the current playlist.


```
[Visual Basic]
ReadOnly Property isIdentical(
  pIWMPPlaylist As IWMPPlaylist
) As System.Boolean
```




```
[C#]
System.Boolean get_isIdentical (
  IWMPPlaylist pIWMPPlaylist
);
```



## Parameters

*pIWMPPlaylist*

A **WMPLib.IWMPPlaylist** Interface for the playlist that this method compares to the current playlist.

## Property Value

A **System.Boolean** that indicates whether the compared playlists are identical.

## Remarks

**IWMPPlaylist.isIdentical** is a property in Visual Basic that takes a parameter, while in C# it is referred to as the **IWMPPlaylist.get\_isIdentical** method.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> </dl>

 

 





