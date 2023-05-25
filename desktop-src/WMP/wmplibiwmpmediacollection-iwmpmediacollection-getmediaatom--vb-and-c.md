---
title: IWMPMediaCollection getMediaAtom method
description: The getMediaAtom method returns the index of a specified attribute within the set of available attributes.
ms.assetid: 01e3d073-677b-4939-96d3-63ae96eaa25d
keywords:
- getMediaAtom method Windows Media Player
- getMediaAtom method Windows Media Player , IWMPMediaCollection interface
- IWMPMediaCollection interface Windows Media Player , getMediaAtom method
topic_type:
- apiref
api_name:
- IWMPMediaCollection.getMediaAtom
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMediaCollection::getMediaAtom method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `getMediaAtom` method returns the index of a specified attribute within the set of available attributes.

## Syntax


```CSharp
public System.Int32 getMediaAtom(
  System.String bstrItemName
);
```


```VB

Public Function getMediaAtom( _
  ByVal bstrItemName As System.String _
) As System.Int32
Implements IWMPMediaCollection.getMediaAtom
```





## Parameters

<dl> <dt>

*bstrItemName* \[in\]
</dt> <dd>

The **System.String** that is the name of the item for which the index should be retrieved.

</dd> </dl>

## Return value

The **System.Int32** that is the index.

## Remarks

The index number retrieved with this method can be passed to the **IWMPMedia.getItemInfoByAtom** to access attribute values. This technique is generally more efficient when working with large playlists than accessing an attribute value by name through **IWMPMedia.getItemInfo**.

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMedia.getItemInfo (VB and C#)**](wmplibiwmpmedia-iwmpmedia-getiteminfo--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.getItemInfoByAtom (VB and C#)**](wmplibiwmpmedia-iwmpmedia-getiteminfobyatom--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> </dl>

 

 





