---
title: IWMPCdrom (VB and C ) interface (Wmp.h)
description: Provides a way to access a CD or DVD in its drive.The IWMPCdrom interface exposes the following properties.
ms.assetid: 2748e64b-b9b7-489a-a6b5-21154aabd312
keywords:
- IWMPCdrom (VB and C ) interface Windows Media Player
- IWMPCdrom (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPCdrom (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdrom (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides a way to access a CD or DVD in its drive.

The **IWMPCdrom** interface exposes the following properties.

## Members

The **IWMPCdrom (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPCdrom (VB and C#)** interface has these methods.



| Method                                                     | Description                                     |
|:-----------------------------------------------------------|:------------------------------------------------|
| [**eject**](wmplibiwmpcdrom-iwmpcdrom-eject--vb-and-c.md) | Ejects the CD or DVD from the drive.<br/> |



 

### Properties

The **IWMPCdrom (VB and C#)** interface has these properties.



| Property                                                                                | Access type          | Description                                                                                                                                  |
|:----------------------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| [**driveSpecifier**](wmplibiwmpcdrom-iwmpcdrom-drivespecifier--vb-and-c.md)<br/> | Read-only<br/> | Gets the CD or DVD drive letter.<br/>                                                                                                  |
| [**Playlist**](wmplibiwmpcdrom-iwmpcdrom-playlist--vb-and-c.md)<br/>             | Read-only<br/> | Gets an [**IWMPPlaylist**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylist) interface representing the tracks on a CD or the root-level title entries for a DVD.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> </dl>

 

 





