---
title: IWMPPlaylist getItemInfo method
description: The getItemInfo method returns the value of a playlist attribute specified by name.
ms.assetid: 62e882d6-66bb-450c-9700-b99d30dd42fa
keywords:
- getItemInfo method Windows Media Player
- getItemInfo method Windows Media Player , IWMPPlaylist interface
- IWMPPlaylist interface Windows Media Player , getItemInfo method
topic_type:
- apiref
api_name:
- IWMPPlaylist.getItemInfo
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPPlaylist::getItemInfo method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getItemInfo** method returns the value of a playlist attribute specified by name.

## Syntax


```CSharp
public System.String getItemInfo(
  System.String bstrName
);
```


```VB

Public Function getItemInfo( _
  ByVal bstrName As System.String _
) As System.String
Implements IWMPPlaylist.getItemInfo
```





## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

A **System.String** that is the name of the playlist attribute.

</dd> </dl>

## Return value

A **System.String** that is the value of the playlist attribute.

## Remarks

Before using this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

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

[**IWMPPlaylist.setItemInfo (VB and C#)**](wmplibiwmpplaylist-iwmpplaylist-setiteminfo--vb-and-c.md)
</dt> </dl>

 

 





