---
title: IWMPStringCollection (VB and C ) interface (Wmp.h)
description: Provides a property and a method for accessing a collection of strings by index number.The IWMPStringCollection interface exposes the following property.
ms.assetid: 03d163f9-40a5-4aff-b36e-b9c6a1d11905
keywords:
- IWMPStringCollection (VB and C ) interface Windows Media Player
- IWMPStringCollection (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPStringCollection (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPStringCollection (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides a property and a method for accessing a collection of strings by index number.

The **IWMPStringCollection** interface exposes the following property.

## Members

The **IWMPStringCollection (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPStringCollection (VB and C#)** interface has these methods.



| Method                                                                         | Description                                           |
|:-------------------------------------------------------------------------------|:------------------------------------------------------|
| [**Item**](wmplibiwmpstringcollection-iwmpstringcollection-item--vb-and-c.md) | Returns the string at the specified index.<br/> |



 

### Properties

The **IWMPStringCollection (VB and C#)** interface has these properties.



| Property                                                                                    | Access type          | Description                                                   |
|:--------------------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------|
| [**count**](wmplibiwmpstringcollection-iwmpstringcollection-count--vb-and-c.md)<br/> | Read-only<br/> | Gets the number of items in the string collection.<br/> |



 

Get an **IWMPStringCollection** interface by using the following methods.



| Object                                                   | Property                                                                                 |
|----------------------------------------------------------|------------------------------------------------------------------------------------------|
| [IWMPMediaCollection](iwmpmediacollection--vb-and-c.md) | [**getAttributeStringCollection**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmediacollection-getattributestringcollection) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPStringCollection2 Interface (VB and C#)**](iwmpstringcollection2--vb-and-c.md)
</dt> </dl>

 

 





