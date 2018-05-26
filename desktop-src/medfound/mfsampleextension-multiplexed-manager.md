---
Description: Provides an instance of IMFMuxStreamSampleManager which is used to access the collection of samples from the substreams of a multiplexed media source.
ms.assetid: 4FD8169D-FDDF-4C69-AD46-05B02B35028C
title: MFSampleExtension\_MULTIPLEXED\_MANAGER attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_MULTIPLEXED\_MANAGER attribute

Provides an instance of [**IMFMuxStreamSampleManager**](/windows/win32/mfobjects/nn-mfobjects-imfmuxstreamsamplemanager?branch=master) which is used to access the collection of samples from the substreams of a multiplexed media source.

## Data type

**[**IUnknown**](com.iunknown)**

## Remarks

Pass this value into [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master) to get an instance of [**IMFMuxStreamSampleManager**](/windows/win32/mfobjects/nn-mfobjects-imfmuxstreamsamplemanager?branch=master).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



 

 




