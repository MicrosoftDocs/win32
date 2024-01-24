---
title: IWMPMediaCollection2 getByAttributeAndMediaType method
description: The getByAttributeAndMediaType method returns an IWMPPlaylist interface that provides access to media items that have a specified attribute and media type.
ms.assetid: dce9cef4-1d12-4bee-a75d-42274556c5bc
keywords:
- getByAttributeAndMediaType method Windows Media Player
- getByAttributeAndMediaType method Windows Media Player , IWMPMediaCollection2 interface
- IWMPMediaCollection2 interface Windows Media Player , getByAttributeAndMediaType method
topic_type:
- apiref
api_name:
- IWMPMediaCollection2.getByAttributeAndMediaType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMediaCollection2::getByAttributeAndMediaType method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `getByAttributeAndMediaType` method returns an **IWMPPlaylist** interface that provides access to media items that have a specified attribute and media type.

## Syntax


```CSharp
public IWMPPlaylist getByAttributeAndMediaType(
  System.String bstrAttribute,
  System.String bstrValue,
  System.String bstrMediaType
);
```


```VB

Public Function getByAttributeAndMediaType( _
  ByVal bstrAttribute As System.String, _
  ByVal bstrValue As System.String, _
  ByVal bstrMediaType As System.String _
) As IWMPPlaylist
Implements IWMPMediaCollection2.getByAttributeAndMediaType
```





## Parameters

<dl> <dt>

*bstrAttribute* \[in\]
</dt> <dd>

The **System.String** that is the specified attribute.

</dd> <dt>

*bstrValue* \[in\]
</dt> <dd>

The **System.String** that is the specified value for the attribute that is specified in *bstrAttribute*.

</dd> <dt>

*bstrMediaType* \[in\]
</dt> <dd>

The **System.String** that is the specified media type.

</dd> </dl>

## Return value

A **WMPLib.IWMPPlaylist** interface for the retrieved playlist.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMediaCollection2 Interface (VB and C#)**](iwmpmediacollection2--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> </dl>

 

 





