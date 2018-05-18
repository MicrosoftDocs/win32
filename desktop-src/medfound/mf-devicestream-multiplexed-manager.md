---
Description: 'Provides an instance of IMFMuxStreamAttributesManager which manages the IMFAttributes describing the substreams of a multiplexed media source.'
ms.assetid: '0149BD8B-8C9D-47FD-9EC1-BEBEE73BC73E'
title: 'MF\_DEVICESTREAM\_MULTIPLEXED\_MANAGER attribute'
---

# MF\_DEVICESTREAM\_MULTIPLEXED\_MANAGER attribute

Provides an instance of [**IMFMuxStreamAttributesManager**](imfmuxstreamattributesmanager.md) which manages the [**IMFAttributes**](imfattributes.md) describing the substreams of a multiplexed media source.

## Data type

**[**IUnknown**](com.iunknown)**

## Remarks

Pass this value into [**IMFAttributes::GetUnknown**](imfattributes-getunknown.md) to determine if the media source provides multiplexed streams and, if so, get an instance of [**IMFMuxStreamAttributesManager**](imfmuxstreamattributesmanager.md).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



 

 




