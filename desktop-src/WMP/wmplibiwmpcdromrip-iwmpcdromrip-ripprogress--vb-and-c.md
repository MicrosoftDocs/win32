---
title: IWMPCdromRip ripProgress property
description: The ripProgress property gets the CD ripping progress as percent complete.
ms.assetid: 00d4f074-a16d-4c5f-930f-4411b90303f1
keywords:
- ripProgress property Windows Media Player
- ripProgress property Windows Media Player , IWMPCdromRip interface
- IWMPCdromRip interface Windows Media Player , ripProgress property
topic_type:
- apiref
api_name:
- IWMPCdromRip.ripProgress
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromRip::ripProgress property

The **ripProgress** property gets the CD ripping progress as percent complete.

## Syntax


```CSharp
public System.Int32 ripProgress {get; set;}
```


```VB

Public ReadOnly Property ripProgress As System.Int32
```





## Property value

A **System.Int32** that is the progress value. Progress values range from 0 to 100.

## Remarks

The progress value represents the completed percentage of the entire ripping process. To determine the progress of a specific track, use [IWMPMedia.getItemInfo](wmplibiwmpplaylist-iwmpplaylist-getiteminfo--vb-and-c.md) with **RipProgress** as the attribute name. To get the index of the track currently being ripped, call IWMPPlaylist.getItemInfo with "CurrentRipTrackIndex" as the attribute name.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromRip Interface (VB and C#)**](iwmpcdromrip--vb-and-c.md)
</dt> <dt>

[**Ripping a CD**](ripping-a-cd.md)
</dt> </dl>

 

 





