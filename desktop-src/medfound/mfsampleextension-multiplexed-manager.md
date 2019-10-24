---
Description: Provides an instance of IMFMuxStreamSampleManager which is used to access the collection of samples from the substreams of a multiplexed media source.
ms.assetid: 4FD8169D-FDDF-4C69-AD46-05B02B35028C
title: MFSampleExtension_MULTIPLEXED_MANAGER attribute
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_MULTIPLEXED\_MANAGER attribute

Provides an instance of [**IMFMuxStreamSampleManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreamsamplemanager) which is used to access the collection of samples from the substreams of a multiplexed media source.

## Data type

**[**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx)**

## Remarks

Pass this value into [**IMFAttributes::GetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getunknown) to get an instance of [**IMFMuxStreamSampleManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreamsamplemanager).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



 

 




