---
Description: Provides an instance of IMFMuxStreamAttributesManager which manages the IMFAttributes describing the substreams of a multiplexed media source.
ms.assetid: 0149BD8B-8C9D-47FD-9EC1-BEBEE73BC73E
title: MF\_DEVICESTREAM\_MULTIPLEXED\_MANAGER attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_DEVICESTREAM\_MULTIPLEXED\_MANAGER attribute

Provides an instance of [**IMFMuxStreamAttributesManager**](/windows/win32/mfobjects/nn-mfobjects-imfmuxstreamattributesmanager?branch=master) which manages the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) describing the substreams of a multiplexed media source.

## Data type

**[**IUnknown**](com.iunknown)**

## Remarks

Pass this value into [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master) to determine if the media source provides multiplexed streams and, if so, get an instance of [**IMFMuxStreamAttributesManager**](/windows/win32/mfobjects/nn-mfobjects-imfmuxstreamattributesmanager?branch=master).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



 

 




