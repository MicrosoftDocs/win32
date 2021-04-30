---
title: IWMPLibraryServices (VB and C ) interface (Wmp.h)
description: Provides methods to enumerate libraries.
ms.assetid: f2a72731-6e61-4f78-b0ca-ae907004eb7d
keywords:
- IWMPLibraryServices (VB and C ) interface Windows Media Player
- IWMPLibraryServices (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPLibraryServices (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPLibraryServices (VB and C#) interface

Provides methods to enumerate libraries.

## Members

The **IWMPLibraryServices (VB and C#)** interface has these types of members:

-   [Methods](#methods)

### Methods

The **IWMPLibraryServices (VB and C#)** interface has these methods.



| Method                                                                                               | Description                                                                                                        |
|:-----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**getCountByType**](wmplibiwmplibraryservices-iwmplibraryservices-getcountbytype--vb-and-c.md)     | Returns the count of available libraries of a specified type.<br/>                                           |
| [**getLibraryByType**](wmplibiwmplibraryservices-iwmplibraryservices-getlibrarybytype--vb-and-c.md) | Returns an **IWMPLibrary** interface that represents the library that has the specified type and index.<br/> |



 

Get an **IWMPLibraryServices** interface by casting the object returned from the **AxWindowsMediaPlayer.GetOcx** method.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
</dt> </dl>

 

 





