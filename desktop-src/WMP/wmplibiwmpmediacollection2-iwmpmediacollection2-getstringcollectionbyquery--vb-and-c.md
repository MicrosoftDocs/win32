---
title: IWMPMediaCollection2 getStringCollectionByQuery method
description: The getStringCollectionByQuery method returns an IWMPStringCollection interface that provides access to the set of all string values for a specified attribute that match the query conditions.
ms.assetid: 2d3b29af-0b6c-4405-8334-9a47a30ff6de
keywords:
- getStringCollectionByQuery method Windows Media Player
- getStringCollectionByQuery method Windows Media Player , IWMPMediaCollection2 interface
- IWMPMediaCollection2 interface Windows Media Player , getStringCollectionByQuery method
topic_type:
- apiref
api_name:
- IWMPMediaCollection2.getStringCollectionByQuery
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMediaCollection2::getStringCollectionByQuery method

The `getStringCollectionByQuery` method returns an **IWMPStringCollection** interface that provides access to the set of all string values for a specified attribute that match the query conditions.

## Syntax


```CSharp
public IWMPStringCollection getStringCollectionByQuery(
  System.String bstrAttribute,
  IWMPQuery pQuery,
  System.String bstrMediaType,
  System.String bstrSortAttribute,
  System.Boolean fSortAscending
);
```


```VB

Public Function getStringCollectionByQuery( _
  ByVal bstrAttribute As System.String, _
  ByVal pQuery As IWMPQuery, _
  ByVal bstrMediaType As System.String, _
  ByVal bstrSortAttribute As System.String, _
  ByVal fSortAscending As System.Boolean _
) As IWMPStringCollection
Implements IWMPMediaCollection2.getStringCollectionByQuery
```





## Parameters

<dl> <dt>

*bstrAttribute* \[in\]
</dt> <dd>

The **System.String** that is the attribute name.

</dd> <dt>

*pQuery* \[in\]
</dt> <dd>

The **WMPLib.IWMPQuery** interface that is the query that defines the conditions used to retrieve the string collection.

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

The **System.Boolean** value that indicates whether the set of string values must be sorted in ascending order.

</dd> </dl>

## Return value

A **WMPLib.IWMPStringCollection** interface for the retrieved set of string values.

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

[**IWMPQuery Interface (VB and C#)**](iwmpquery--vb-and-c.md)
</dt> <dt>

[**IWMPStringCollection Interface (VB and C#)**](iwmpstringcollection--vb-and-c.md)
</dt> <dt>

[**MediaType Attribute**](mediatype-attribute.md)
</dt> </dl>

 

 





