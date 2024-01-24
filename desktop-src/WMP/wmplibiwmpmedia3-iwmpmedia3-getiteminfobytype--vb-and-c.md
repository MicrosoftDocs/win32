---
title: IWMPMedia3 getItemInfoByType method
description: The getItemInfoByType method returns the value of the attribute corresponding to the specified attribute type and index.
ms.assetid: e4cf14b4-3c59-485f-a573-734a0076647b
keywords:
- getItemInfoByType method Windows Media Player
- getItemInfoByType method Windows Media Player , IWMPMedia3 interface
- IWMPMedia3 interface Windows Media Player , getItemInfoByType method
topic_type:
- apiref
api_name:
- IWMPMedia3.getItemInfoByType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMedia3::getItemInfoByType method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getItemInfoByType** method returns the value of the attribute corresponding to the specified attribute type and index.

## Syntax


```CSharp
public System.Object getItemInfoByType(
  System.String bstrType,
  System.String bstrLanguage,
  System.Int32 lIndex
);
```


```VB

Public Function getItemInfoByType( _
  ByVal bstrType As System.String, _
  ByVal bstrLanguage As System.String, _
  ByVal lIndex As System.Int32 _
) As System.Object
Implements IWMPMedia3.getItemInfoByType
```





## Parameters

<dl> <dt>

*bstrType* \[in\]
</dt> <dd>

A **System.String** that is the attribute type.

</dd> <dt>

*bstrLanguage* \[in\]
</dt> <dd>

A **System.String** that is the language. If the value is set to null or a zero-length string (""), the current locale string is used. Otherwise, the value must be a valid RFC 1766 language string such as "en-us".

</dd> <dt>

*lIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the attribute index.

</dd> </dl>

## Return value

A **System.Object** that is the value of the attribute. The type to cast this object to depends on the type of the attribute.

## Remarks

This method returns the metadata for an individual digital media item or a media item that is part of a playlist.

This method supports attributes with multiple values and attributes with complex values. The **getItemInfo** method does not support attributes with multiple values and attributes with complex values.

The **attributeCount** property gets the number of attribute names available for a given media item. Index numbers can then be used with the **getAttributeName** method to determine the name of each available attribute. Individual attribute names can be passed to the *name* parameter of **getItemInfoByType**.

The **getAttributeCountByType** method returns the number of attributes that correspond to a particular attribute name for a given media item. Index numbers can then be passed to the *index* parameter of **getItemInfoByType**. This is useful when a media item has been categorized under multiple genres, for example.

If the media item came from a library that was retrieved by calling [IWMPLibrary.mediaCollection](wmplibiwmplibrary-iwmplibrary-mediacollection--vb-and-c.md), the set of available attributes will differ from those which can be queried from the local library retrieved by calling [AxWindowsMediaPlayer.mediaCollection](axwmplib-axwindowsmediaplayer-mediacollection--vb-and-c.md). For example, the attributes available from the local library retrieved by using **IWMPLibrary** will be a subset of the attributes available from the local library retrieved by using **AxWindowsMediaPlayer**. The set of attributes available from other sources (remote libraries, portable devices, or CDs is defined by the other sources.

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMedia3 Interface (VB and C#)**](iwmpmedia3--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.attributeCount (VB and C#)**](wmplibiwmpmedia-iwmpmedia-attributecount--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.getAttributeName (VB and C#)**](wmplibiwmpmedia-iwmpmedia-getattributename--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.getItemInfo (VB and C#)**](wmplibiwmpmedia-iwmpmedia-getiteminfo--vb-and-c.md)
</dt> <dt>

[**IWMPMedia3.getAttributeCountByType (VB and C#)**](wmplibiwmpmedia3-iwmpmedia3-getattributecountbytype--vb-and-c.md)
</dt> </dl>

 

 





