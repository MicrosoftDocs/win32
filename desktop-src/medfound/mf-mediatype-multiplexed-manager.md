---
Description: Provides an instance of IMFMuxStreamMediaTypeManager which can be used to get the media types of the substreams of a multiplexed media source as well as control the combination of substreams that are multiplexed by the source.
ms.assetid: 5C36956D-336A-4956-8793-D86DC792E906
title: MF\_MEDIATYPE\_MULTIPLEXED\_MANAGER attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MEDIATYPE\_MULTIPLEXED\_MANAGER attribute

Provides an instance of [**IMFMuxStreamMediaTypeManager**](/windows/win32/mfobjects/nn-mfobjects-imfmuxstreammediatypemanager?branch=master) which can be used to get the media types of the substreams of a multiplexed media source as well as control the combination of substreams that are multiplexed by the source.

## Data type

**[**IUnknown**](com.iunknown)**

## Remarks

Pass this value into [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master) to get an instance of [**IMFMuxStreamMediaTypeManager**](/windows/win32/mfobjects/nn-mfobjects-imfmuxstreammediatypemanager?branch=master).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



 

 




