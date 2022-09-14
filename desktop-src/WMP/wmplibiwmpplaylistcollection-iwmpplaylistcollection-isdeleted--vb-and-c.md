---
title: IWMPPlaylistCollection isDeleted method
description: The isDeleted method returns a value indicating whether the specified playlist is in the deleted items folder.
ms.assetid: 02bc4b9f-6149-4fe2-8417-6484b22f2d74
keywords:
- isDeleted method Windows Media Player
- isDeleted method Windows Media Player , IWMPPlaylistCollection interface
- IWMPPlaylistCollection interface Windows Media Player , isDeleted method
topic_type:
- apiref
api_name:
- IWMPPlaylistCollection.isDeleted
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPPlaylistCollection::isDeleted method

The **isDeleted** method returns a value indicating whether the specified playlist is in the deleted items folder.

## Syntax


```CSharp
public System.Boolean isDeleted(
  IWMPPlaylist pItem
);
```


```VB

Public Function isDeleted( _
  ByVal pItem As IWMPPlaylist _
) As System.Boolean
Implements IWMPPlaylistCollection.isDeleted
```





## Parameters

<dl> <dt>

*pItem* \[in\]
</dt> <dd>

A **WMPLib.IWMPPlaylist** interface for the queried playlist.

</dd> </dl>

## Return value

A **System.Boolean** that specifies whether the playlist was deleted.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later.<br/>                                                                     |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection Interface (VB and C#)**](iwmpplaylistcollection--vb-and-c.md)
</dt> </dl>

 

 





