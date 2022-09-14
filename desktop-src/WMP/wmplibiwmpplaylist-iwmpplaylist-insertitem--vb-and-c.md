---
title: IWMPPlaylist insertItem method
description: The insertItem method inserts a media item at a specified location in a playlist.
ms.assetid: 6e472f0a-13df-41d9-8e6f-8430d87fe978
keywords:
- insertItem method Windows Media Player
- insertItem method Windows Media Player , IWMPPlaylist interface
- IWMPPlaylist interface Windows Media Player , insertItem method
topic_type:
- apiref
api_name:
- IWMPPlaylist.insertItem
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPPlaylist::insertItem method

The **insertItem** method inserts a media item at a specified location in a playlist.

## Syntax


```CSharp
public void insertItem(
  System.Int32 lIndex,
  IWMPMedia pIWMPMedia
);
```


```VB

Public Sub insertItem( _
  ByVal lIndex As System.Int32, _
  ByVal pIWMPMedia As IWMPMedia _
)
Implements IWMPPlaylist.insertItem
```





## Parameters

<dl> <dt>

*lIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the zero-based index at which the media item will be inserted in the playlist.

</dd> <dt>

*pIWMPMedia* \[in\]
</dt> <dd>

A **WMPLib.IWMPMedia** interface that represents the media item to be inserted.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

All media items after the inserted item will have their indexes increased by one.

Before calling this method, you must have full access to the library. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist.removeItem (VB and C#)**](wmplibiwmpplaylist-iwmpplaylist-removeitem--vb-and-c.md)
</dt> </dl>

 

 





