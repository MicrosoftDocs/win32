---
title: IWMPMedia3 getAttributeCountByType method
description: The getAttributeCountByType method returns the number of attributes associated with the specified attribute type.
ms.assetid: d692635f-f9f1-4d8e-a9c5-9d7fa84f41bd
keywords:
- getAttributeCountByType method Windows Media Player
- getAttributeCountByType method Windows Media Player , IWMPMedia3 interface
- IWMPMedia3 interface Windows Media Player , getAttributeCountByType method
topic_type:
- apiref
api_name:
- IWMPMedia3.getAttributeCountByType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMedia3::getAttributeCountByType method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getAttributeCountByType** method returns the number of attributes associated with the specified attribute type.

## Syntax


```CSharp
public System.Int32 getAttributeCountByType(
  System.String bstrType,
  System.String bstrLanguage
);
```


```VB

Public Function getAttributeCountByType( _
  ByVal bstrType As System.String, _
  ByVal bstrLanguage As System.String _
) As System.Int32
Implements IWMPMedia3.getAttributeCountByType
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

</dd> </dl>

## Return value

A **System.Int32** that is the count of attributes that are associated with the type.

## Remarks

This method is used to discover the number of attributes corresponding to a particular attribute name for a given media item. Index numbers can then be passed to the **getItemInfoByType** method. This is useful, for example, when a media item has been categorized under multiple genres.

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

[**IWMPMedia3.getItemInfoByType (VB and C#)**](wmplibiwmpmedia3-iwmpmedia3-getiteminfobytype--vb-and-c.md)
</dt> </dl>

 

 





