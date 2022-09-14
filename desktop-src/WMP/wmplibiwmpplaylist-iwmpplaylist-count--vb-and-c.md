---
title: IWMPPlaylist count property
description: The count property gets the number of media items in a playlist.
ms.assetid: dbff3c86-2d42-4d47-a5cb-b8199efac728
keywords:
- count property Windows Media Player
- count property Windows Media Player , IWMPPlaylist interface
- IWMPPlaylist interface Windows Media Player , count property
topic_type:
- apiref
api_name:
- IWMPPlaylist.count
- IWMPPlaylist.get_count
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPPlaylist::count property

The **count** property gets the number of media items in a playlist.

This property is read-only.

## Syntax


```CSharp
public System.Int32 count {get;}
```


```VB

Public ReadOnly Property count As System.Int32
```





## Property value

A **System.Int32** that is the number of media items in the playlist.

## Remarks

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

See the [attributeCount](wmplibiwmpplaylist-iwmpplaylist-attributecount--vb-and-c.md) property for example code that uses this property.

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

 

 





