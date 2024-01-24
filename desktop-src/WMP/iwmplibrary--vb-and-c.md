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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPLibrary (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





