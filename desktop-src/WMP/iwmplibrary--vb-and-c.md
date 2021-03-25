---
title: IWMPLibrary (VB and C ) interface (Wmp.h)
description: Represents a library.The IWMPLibrary interface exposes the following properties.
ms.assetid: 956b2da1-5f01-48d6-8faa-e360c225afda
keywords:
- IWMPLibrary (VB and C ) interface Windows Media Player
- IWMPLibrary (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPLibrary (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPLibrary (VB and C#) interface

Represents a library.

The **IWMPLibrary** interface exposes the following properties.

## Members

The **IWMPLibrary (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPLibrary (VB and C#)** interface has these methods.



| Method                                                                     | Description                                                                                           |
|:---------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**isIdentical**](wmplibiwmplibrary-iwmplibrary-isidentical--vb-and-c.md) | Returns a value that indicates whether the supplied object is the same as the current one.<br/> |



 

### Properties

The **IWMPLibrary (VB and C#)** interface has these properties.



| Property                                                                                      | Access type          | Description                                                                   |
|:----------------------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------|
| [**mediaCollection**](wmplibiwmplibrary-iwmplibrary-mediacollection--vb-and-c.md)<br/> | Read-only<br/> | Gets an **IWMPMediaCollection** interface for the current library.<br/> |
| [**name**](wmplibiwmplibrary-iwmplibrary-name--vb-and-c.md)<br/>                       | Read-only<br/> | Gets the display name of the current library.<br/>                      |
| [**type**](wmplibiwmplibrary-iwmplibrary-type--vb-and-c.md)<br/>                       | Read-only<br/> | Gets a value that indicates the library type.<br/>                      |



 

Get an **IWMPLibrary** interface by using the following method.



| Object                                                   | Property                                                         |
|----------------------------------------------------------|------------------------------------------------------------------|
| [IWMPLibraryServices](iwmplibraryservices--vb-and-c.md) | [**getLibraryByType**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibraryservices-getlibrarybytype) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPLibraryServices.getLibraryByType (VB and C#)**](wmplibiwmplibraryservices-iwmplibraryservices-getlibrarybytype--vb-and-c.md)
</dt> </dl>

 

 





