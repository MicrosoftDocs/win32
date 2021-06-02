---
title: IPropertyFilterCollection interface (WdsSharedIDL.h)
description: Exposes properties of the returned collection based on the query submitted.
ms.assetid: 9ed4217f-54b0-4d69-bf44-2547320a9681
keywords:
- IPropertyFilterCollection interface Legacy Windows Environment Features
- IPropertyFilterCollection interface Legacy Windows Environment Features , described
topic_type:
- apiref
api_name:
- IPropertyFilterCollection
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IPropertyFilterCollection interface

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Exposes properties of the returned collection based on the query submitted.

## Members

The **IPropertyFilterCollection** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPropertyFilterCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IPropertyFilterCollection** interface has these properties.



| Property                                                                         | Access type           | Description                                                  |
|:---------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------|
| [**AddItem**](-search-2x-ipropertyfiltercollection-additem.md)<br/>       | Read-only<br/>  | Adds a new filter to the collection. <br/>             |
| [**clear**](-search-2x-ipropertyfiltercollection-clear.md)<br/>           | Write-only<br/> | Clears the collection. <br/>                           |
| [**Count**](-search-2x-ipropertyfiltercollection-count.md)<br/>           | Read-only<br/>  | Number of filters in the collection. <br/>             |
| [**GetITem**](-search-2x-ipropertyfiltercollection-getitem.md)<br/>       | Read/write<br/> | Returns a specific filter within the collection. <br/> |
| [**RemoveItem**](-search-2x-ipropertyfiltercollection-removeitem.md)<br/> | Write-only<br/> | Removes a specific filter to the collection. <br/>     |



 

## Remarks

These properties are used to filter collection returned by the query.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>                                               |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

