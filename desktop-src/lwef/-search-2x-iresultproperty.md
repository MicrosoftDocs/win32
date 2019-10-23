---
title: IResultProperty interface
description: Exposes result properties.
ms.assetid: 58d8c516-47c6-4cae-b46c-5127baf3054d
keywords:
- IResultProperty interface Legacy Windows Environment Features
- IResultProperty interface Legacy Windows Environment Features , described
topic_type:
- apiref
api_name:
- IResultProperty
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultProperty interface

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

Exposes result properties.

## Members

The **IResultProperty** interface inherits from the [**IUnknown**](https://docs.microsoft.com/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IResultProperty** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IResultProperty** interface has these methods.



| Method                                                    | Description                 |
|:----------------------------------------------------------|:----------------------------|
| [**GoBack**](-search-2x-iresultproperty-goback.md)       | Not implemented.<br/> |
| [**GoForward**](-search-2x-iresultproperty-goforward.md) | Not implemented.<br/> |



 

### Properties

The **IResultProperty** interface has these properties.



| Property                                                                   | Access type          | Description                                           |
|:---------------------------------------------------------------------------|:---------------------|:------------------------------------------------------|
| [**DataType**](-search-2x-iresultproperty-datatype.md)<br/>         | Read-only<br/> | A properties data type. <br/>                   |
| [**DisplayName**](-search-2x-iresultproperty-displayname.md)<br/>   | Read-only<br/> | Localized display name of the property. <br/>   |
| [**DisplayState**](-search-2x-iresultproperty-displaystate.md)<br/> | Read-only<br/> | Visability of the property. <br/>               |
| [**Hint**](-search-2x-iresultproperty-hint.md)<br/>                 | Read-only<br/> | Special value used to aid data retrieval. <br/> |
| [**IndexColumn**](-search-2x-iresultproperty-indexcolumn.md)<br/>   | Read-only<br/> | Properties column name in the index. <br/>      |
| [**UID**](-search-2x-iresultproperty-uid.md)<br/>                   | Read-only<br/> | Unique identifier for the property. <br/>       |



 

## Remarks

These are the items return properties.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>                                               |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





