---
title: IWMPStringCollection2 getItemInfobyType method
description: The getItemInfoByType method returns the value corresponding to the specified string collection item index, name, language, and attribute index.
ms.assetid: 51035fed-51ce-4cd2-a936-4c99802128f2
keywords:
- getItemInfobyType method Windows Media Player
- getItemInfobyType method Windows Media Player , IWMPStringCollection2 interface
- IWMPStringCollection2 interface Windows Media Player , getItemInfobyType method
topic_type:
- apiref
api_name:
- IWMPStringCollection2.getItemInfobyType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPStringCollection2::getItemInfobyType method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getItemInfoByType** method returns the value corresponding to the specified string collection item index, name, language, and attribute index.

## Syntax


```CSharp
public System.Object getItemInfobyType(
  System.Int32 lCollectionIndex,
  System.String bstrType,
  System.String bstrLanguage,
  System.Int32 lAttributeIndex
);
```


```VB

Public Function getItemInfobyType( _
  ByVal lCollectionIndex As System.Int32, _
  ByVal bstrType As System.String, _
  ByVal bstrLanguage As System.String, _
  ByVal lAttributeIndex As System.Int32 _
) As System.Object
Implements IWMPStringCollection2.getItemInfobyType
```





## Parameters

<dl> <dt>

*lCollectionIndex* \[in\]
</dt> <dd>

The **System.Int32** that is the zero-based index of the string collection item from which to get the attribute.

</dd> <dt>

*bstrType* \[in\]
</dt> <dd>

The **System.String** that is the attribute name.

</dd> <dt>

*bstrLanguage* \[in\]
</dt> <dd>

The **System.String** that indicates the language. If the value is set to null or to a zero-length string (""), the current locale string is used. Otherwise, the value must be a valid RFC 1766 language string such as "en-us".

</dd> <dt>

*lAttributeIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the zero-based index of the attribute.

</dd> </dl>

## Return value

A **System.Object** that is the string collection item.

## Remarks

This method supports attributes with multiple values and attributes with complex values. The **getItemInfo** method does not support attributes with multiple values or attributes with complex values.

By passing the value "ChildList" in the *bstrType* parameter, you can retrieve a new string collection that contains the children of one of the items in the parent string collection. For instance, if the parent collection contains a list of AlbumIDs, you can use this method to obtain a child string collection that contains all the tracks for one of the albums. This approach is faster and more efficient than calling the **IWMPMediaCollection2.getStringCollectionByQuery** method twice; once to get a collection of AlbumIDs, and a second time to get a collection of tracks for a particular AlbumID. To use ChildList in the way just described, the parent string collection must be obtained from a media collection through **IWMPLibraryServices**, and not by using the **AxWindowsMediaPlayer.mediaCollection** property.

When using ChildList, pass the value "ChildList" in the *bstrType* parameter, and the value 0 in the *lAttributeIndex* parameter. You can then cast the object that is returned to an **IWMPStringCollection2** interface to access the child list.

To use this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AlbumID Attribute**](albumid-attribute.md)
</dt> <dt>

[**IWMPLibraryServices Interface (VB and C#)**](iwmplibraryservices--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection2.getStringCollectionByQuery (VB and C#)**](wmplibiwmpmediacollection2-iwmpmediacollection2-getstringcollectionbyquery--vb-and-c.md)
</dt> <dt>

[**IWMPStringCollection2 Interface**](iwmpstringcollection2--vb-and-c.md)
</dt> <dt>

[**IWMPStringCollection2.getItemInfo (VB and C#)**](wmplibiwmpstringcollection2-iwmpstringcollection2-getiteminfo--vb-and-c.md)
</dt> </dl>

 

 





