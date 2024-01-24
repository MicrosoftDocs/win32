---
title: IWMPErrorItem (VB and C ) interface (Wmp.h)
description: Provides access to error information.
ms.assetid: 7f1571e1-4e3a-4f06-b9fa-9add34266537
keywords:
- IWMPErrorItem (VB and C ) interface Windows Media Player
- IWMPErrorItem (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPErrorItem (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPErrorItem (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides access to error information.

The **IWMPErrorItem** interface exposes the following properties.



| Property                                                                             | Description                                                                                |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [customUrl](wmplibiwmperroritem-iwmperroritem-customurl--vb-and-c.md)               | Gets the URL of a website that displays specific information about codec download failure. |
| [errorCode](wmplibiwmperroritem-iwmperroritem-errorcode--vb-and-c.md)               | Gets the current error code.                                                               |
| [errorContext](wmplibiwmperroritem-iwmperroritem-errorcontext--vb-and-c.md)         | Gets a value indicating the context of the error.                                          |
| [errorDescription](wmplibiwmperroritem-iwmperroritem-errordescription--vb-and-c.md) | Gets a description of the error.                                                           |
| [remedy](wmplibiwmperroritem-iwmperroritem-remedy--vb-and-c.md)                     | Reserved for future use.                                                                   |



 

Get an **IWMPErrorItem** interface using the following property.



| Interface                            | Property                                                                   |
|--------------------------------------|----------------------------------------------------------------------------|
| [IWMPError](iwmperror--vb-and-c.md) | [Item](iwmperror-item--vb-and-c.md) (in C# use the **get\_Item** method) |



 

## Members

The **IWMPErrorItem (VB and C#)** interface does not define any members.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPErrorItem2 Interface (VB and C#)**](iwmperroritem2--vb-and-c.md)
</dt> </dl>

 

 





