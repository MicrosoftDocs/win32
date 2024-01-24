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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPLibraryServices (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





