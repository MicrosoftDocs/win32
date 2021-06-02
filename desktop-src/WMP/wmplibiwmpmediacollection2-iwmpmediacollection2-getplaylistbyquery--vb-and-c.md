---
title: IWMPMediaCollection2 getPlaylistByQuery method
description: The getPlaylistByQuery method returns an IWMPPlaylist interface that provides access to media items that match the query conditions.
ms.assetid: ebbb631f-1faa-4c89-8c1d-cc2b128126b8
keywords:
- getPlaylistByQuery method Windows Media Player
- getPlaylistByQuery method Windows Media Player , IWMPMediaCollection2 interface
- IWMPMediaCollection2 interface Windows Media Player , getPlaylistByQuery method
topic_type:
- apiref
api_name:
- IWMPMediaCollection2.getPlaylistByQuery
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMediaCollection2::getPlaylistByQuery method

The `getPlaylistByQuery` method returns an **IWMPPlaylist** interface that provides access to media items that match the query conditions.

## Syntax


```CSharp
public IWMPPlaylist getPlaylistByQuery(
  IWMPQuery pQuery,
  System.String bstrMediaType,
  System.String bstrSortAttribute,
  System.Boolean fSortAscending
);
```


```VB

Public Function getPlaylistByQuery( _
  ByVal pQuery As IWMPQuery, _
  ByVal bstrMediaType As System.String, _
  ByVal bstrSortAttribute As System.String, _
  ByVal fSortAscending As System.Boolean _
) As IWMPPlaylist
Implements IWMPMediaCollection2.getPlaylistByQuery
```





## Parameters

<dl> <dt>

*pQuery* \[in\]
</dt> <dd>

The **WMPLib.IWMPQuery** interface that represents the query.

</dd> <dt>

*bstrMediaType* \[in\]
</dt> <dd>

The **System.String** that is the media type. Must contain one of the following values: "audio", "video", "photo", "playlist", or "other".

</dd> <dt>

*bstrSortAttribute* \[in\]
</dt> <dd>

The **System.String** that is the attribute name used for sorting. A zero-length string ("") means no sorting is applied.

</dd> <dt>

*fSortAscending* \[in\]
</dt> <dd>

The **System.Boolean** value that indicates whether the playlist must be sorted in ascending order.

</dd> </dl>

## Return value

A **WMPLib.IWMPPlaylist** interface for the retrieved playlist.

## Remarks

Compound queries using **IWMPQuery** are not case sensitive.

When the compound query specified by the *pQuery* parameter contains a condition built on the **MediaType** attribute, that condition is ignored. The value for the *bstrMediaType* parameter is always used. For example, if the compound query contains the condition "MediaType Equals audio" and the value for the *bstrMediaType* parameter is "video", the resulting playlist will contain only video items.

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
</dt> <dt>

[**IWMPQuery Interface (VB and C#)**](iwmpquery--vb-and-c.md)
</dt> <dt>

[**MediaType Attribute**](mediatype-attribute.md)
</dt> </dl>

 

 





