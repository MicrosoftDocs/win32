---
title: IWMPMedia getItemInfoByAtom method
description: The getItemInfoByAtom method returns the value of the attribute with the specified index number.
ms.assetid: d9a4b737-add1-4bbd-8e03-e58f45d65a62
keywords:
- getItemInfoByAtom method Windows Media Player
- getItemInfoByAtom method Windows Media Player , IWMPMedia interface
- IWMPMedia interface Windows Media Player , getItemInfoByAtom method
topic_type:
- apiref
api_name:
- IWMPMedia.getItemInfoByAtom
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMedia::getItemInfoByAtom method

The **getItemInfoByAtom** method returns the value of the attribute with the specified index number.

## Syntax


```CSharp
public System.String getItemInfoByAtom(
  System.Int32 lAtom
);
```


```VB

Public Function getItemInfoByAtom( _
  ByVal lAtom As System.Int32 _
) As System.String
Implements IWMPMedia.getItemInfoByAtom
```





## Parameters

<dl> <dt>

*lAtom* \[in\]
</dt> <dd>

A **System.Int32** that specifies the index at which the requested attribute resides within the set of available attributes.

</dd> </dl>

## Return value

A **System.String** that is the value of the attribute.

## Remarks

This method can be used to retrieve metadata for a specific media item by using an attribute index number. The **attributeCount** property can be used to determine the number of attributes available for the media item.

The **getMediaAtom** method of the **IWMPMediaCollection** interface can also be used to retrieve the index of a particular attribute. This technique is generally more efficient than the **getItemInfo** or **getItemInfoByType** methods when working with large playlists.

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

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

[**IWMPMedia.attributeCount (VB and C#)**](wmplibiwmpmedia-iwmpmedia-attributecount--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.getItemInfo (VB and C#)**](wmplibiwmpmedia-iwmpmedia-getiteminfo--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.setItemInfo (VB and C#)**](wmplibiwmpmedia-iwmpmedia-setiteminfo--vb-and-c.md)
</dt> <dt>

[**IWMPMedia3.getItemInfoByType (VB and C#)**](wmplibiwmpmedia3-iwmpmedia3-getiteminfobytype--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection.getMediaAtom (VB and C#)**](wmplibiwmpmediacollection-iwmpmediacollection-getmediaatom--vb-and-c.md)
</dt> </dl>

 

 





