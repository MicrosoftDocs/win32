---
description: Provides an instance of IMFMuxStreamMediaTypeManager which can be used to get the media types of the substreams of a multiplexed media source as well as control the combination of substreams that are multiplexed by the source.
ms.assetid: 5C36956D-336A-4956-8793-D86DC792E906
title: MF_MEDIATYPE_MULTIPLEXED_MANAGER attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MEDIATYPE\_MULTIPLEXED\_MANAGER attribute

Provides an instance of [**IMFMuxStreamMediaTypeManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreammediatypemanager) which can be used to get the media types of the substreams of a multiplexed media source as well as control the combination of substreams that are multiplexed by the source.

## Data type

**[**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown)**

## Remarks

Pass this value into [**IMFAttributes::GetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getunknown) to get an instance of [**IMFMuxStreamMediaTypeManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreammediatypemanager).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



 

 
