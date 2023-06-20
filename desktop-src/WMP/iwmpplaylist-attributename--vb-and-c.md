---
title: IWMPPlaylist.attributeName (VB and C )
description: The attributeName property (the get\_attributeName method in C\ ) gets the name of a playlist attribute specified by an index.
ms.assetid: bb436657-5156-437e-af58-6497ad3b311b
keywords:
- IWMPPlaylist.attributeName (VB and C ) Windows Media Player
topic_type:
- apiref
api_name:
- IWMPPlaylist.attributeName (VB and C )
api_location:
- Interop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPPlaylist.attributeName (VB and C#)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **attributeName** property (the **get\_attributeName** method in C#) gets the name of a playlist attribute specified by an index.


```
[Visual Basic]
ReadOnly Property attributeName(
  lIndex As System.Int32
) As System.String
```




```
[C#]
System.String get_attributeName(
  System.Int32 lIndex
);
```



## Parameters

*lIndex*

A **System.Int32** that is the index of the playlist attribute.

## Return Value

A **System.String** that is the name of the playlist attribute.

## Remarks

**IWMPPlaylist.attributeName** is a read-only property in Visual Basic that takes a parameter, while in C# it is referred to as the **IWMPPlaylist.get\_attributeName** method.

The number of attributes associated with a playlist is returned by the **IWMPPlaylist.attributeCount** property.

The name returned by this property can be supplied to the **setItemInfo** or **getItemInfo** methods to specify or retrieve a value for the named attribute.

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

For more information about attributes supported by Windows Media Player, see the [Attribute Reference](attribute-reference.md).

## Examples

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
</dt> <dt>

[**IWMPPlaylist.attributeCount (VB and C#)**](wmplibiwmpplaylist-iwmpplaylist-attributecount--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist.getItemInfo (VB and C#)**](wmplibiwmpplaylist-iwmpplaylist-getiteminfo--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist.setItemInfo (VB and C#)**](wmplibiwmpplaylist-iwmpplaylist-setiteminfo--vb-and-c.md)
</dt> </dl>

 

 





