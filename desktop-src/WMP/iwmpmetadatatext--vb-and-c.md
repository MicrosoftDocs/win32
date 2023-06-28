---
title: IWMPMetadataText (VB and C ) interface (Wmp.h)
description: Provides properties for getting information about complex textual metadata attributes.
ms.assetid: c0f300d2-6ddb-470b-849d-771d3719bb97
keywords:
- IWMPMetadataText (VB and C ) interface Windows Media Player
- IWMPMetadataText (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPMetadataText (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMetadataText (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides properties for getting information about complex textual metadata attributes.

The **IWMPMetadataText** interface exposes the following properties.



| Property                                                                         | Description                              |
|----------------------------------------------------------------------------------|------------------------------------------|
| [Description](wmplibiwmpmetadatatext-iwmpmetadatatext-description--vb-and-c.md) | Gets a description of the metadata text. |
| [text](wmplibiwmpmetadatatext-iwmpmetadatatext-text--vb-and-c.md)               | Gets the metadata text.                  |



 

Get an **IWMPMetadataText** interface by passing in an attribute name such as **WM/UserWebURL** to the following method and casting the object that is returned.



| Interface                              | Property                                                                         |
|----------------------------------------|----------------------------------------------------------------------------------|
| [IWMPMedia3](iwmpmedia3--vb-and-c.md) | [getItemInfoByType](wmplibiwmpmedia3-iwmpmedia3-getiteminfobytype--vb-and-c.md) |



 

## Members

The **IWMPMetadataText (VB and C#)** interface does not define any members.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> </dl>

 

 





